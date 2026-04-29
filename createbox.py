from mc_remote.minecraft import Minecraft
from param_mc_remote import block

class CreateBox:
    def __init__(self, sx=10, sy=63, sz=10, lx=3, ly=3, lz=3, block=block.DIAMOND_BLOCK):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.lx = lx
        self.ly = ly
        self.lz = lz
        self.block = block

    def create_box(self, mc):
        mc.postToChat("Hello, World! This API can create boxes!")
        mc.setBlocks(self.sx, self.sy, self.sz, self.sx + self.lx -1, self.sy + self.ly -1, self.sz + self.lz -1, self.block)
