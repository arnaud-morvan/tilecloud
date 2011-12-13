from tilecloud import BoundingPyramid, Tile, TileStore



class BoundingPyramidTileStore(TileStore):
    """All tiles in a bounding box"""

    def __init__(self, bounding_pyramid=None):
        self.bounding_pyramid = bounding_pyramid or BoundingPyramid()

    def list(self):
        for tilecoord in self.bounding_pyramid:
            yield Tile(tilecoord)

    def put_one(self, tile):
        self.bounding_pyramid.add(tile.tilecoord)
        return tile