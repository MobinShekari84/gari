import pygame

class physicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.gravity = (0, 0.1)
        self.collision = {"left": False, "right": False, "top": False, "bottom": False}

    def update(self, near_tiles, movement = (0, 0)):
        self.collision = {"left": False, "right": False, "top": False, "bottom": False}
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        self.pos[0] += frame_movement[0]
        player_rect = self.get_rect()
        for tile in near_tiles:
            if player_rect.colliderect(tile):
                if frame_movement[0] > 0:
                    player_rect.right = tile.left
                    self.collision["right"] = True
                elif frame_movement[0] < 0:
                    player_rect.left = tile.right
                    self.collision["left"] = True
                self.pos[0] = player_rect.x

        self.pos[1] += frame_movement[1]
        player_rect = self.get_rect()
        for tile in near_tiles:
            if player_rect.colliderect(tile):
                if frame_movement[1] > 0:
                    player_rect.bottom = tile.top
                    self.collision["bottom"] = True
                elif frame_movement[1] < 0:
                    player_rect.top = tile.bottom
                    self.collision["top"] = True
                self.pos[1] = player_rect.y

        self.velocity[0] = min(5, self.velocity[0] + self.gravity[0])
        self.velocity[1] = min(5, self.velocity[1] + self.gravity[1])
        
        if self.collision["bottom"] or self.collision["top"]:
            self.velocity[1] = 0
        if self.collision["left"] or self.collision["right"]:   
            self.velocity[0] = 0

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)

    def get_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])