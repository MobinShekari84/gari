import pygame

POSSIBLE_TILE_LOCS = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
NON_PASSABLE_TILES = ['stone', 'grass']

class tileMap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tiles = {}
        for i in range(10):
            self.tiles[str(i + 3) + ";10"] = {'type': 'grass', 'pos': (i + 3, 10), 'variant': 1}
            self.tiles["10;" + str(i + 2)] = {'type': 'stone', 'pos': (10, i + 2), 'variant': 1}

    def render(self, surf):
        for tile in self.tiles.values():
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))

    def get_tile(self, pos):
        tile = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        near_tiles = []
        for loc in POSSIBLE_TILE_LOCS:
            if (str(tile[0] + loc[0]) + ";" + str(tile[1] + loc[1])) in self.tiles:
                near_tiles.append(self.tiles[str(tile[0] + loc[0]) + ";" + str(tile[1] + loc[1])])
        return near_tiles

    def get_non_passable_tiles(self, pos):
        near_tiles = self.get_tile(pos)
        non_passable = []
        for tile in near_tiles:
            if tile['type'] in NON_PASSABLE_TILES:
                non_passable.append(self.get_rect_tiles(tile))
        return non_passable
    
    def get_rect_tiles(self, tile):
        return pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size)
    