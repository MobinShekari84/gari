import pygame
from scripts.entities import physicsEntity
from scripts.utils import load_image, load_images
from scripts.tilemap import tileMap

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 900))
        self.display = pygame.Surface((400, 300))
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.display.set_caption("Ninga Game")
        self.movement = [False, False]
        self.assets = {
            'player' : load_image('entities/player.png'),
            'decor' : load_images('tiles/decor'),
            'grass' : load_images('tiles/grass'),
            'large_decor' : load_images('tiles/large_decor'),
            'stone' : load_images('tiles/stone')
        }
        self.tile_map = tileMap(self)
        self.player = physicsEntity(self, 'player', (50, 50), (8, 15))

    def run(self):
        while self.running:
            self.display.fill((14, 219, 248))
            self.player.update(self.tile_map.get_non_passable_tiles(self.player.pos) ,(self.movement[1] - self.movement[0], 0))
            self.tile_map.render(self.display)
            self.player.render(self.display)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_SPACE:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60) # Limit to 60 frames per second
        pygame.quit()

game = Game()
if __name__ == "__main__":
    game.run()