from mc_remote.minecraft import Minecraft
from param_mc_remote import block

class createBox:
    def __init__(self, sx=10, sy=63, sz=10, lx=3, ly=3, lz=3, block=block.DIAMOND_BLOCK):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.lx = lx
        self.ly = ly
        self.lz = lz
        self.block = block

    def createBox(self, mc):
        x = 0
        y = 0
        z = 0
        mc.postToChat("Hello, World! This API can create boxes!")
        for x in range(self.lx):
            for y in range(self.ly):
                for z in range(self.lz):
                    mc.setBlock(self.sx + x, self.sy + y, self.sz + z, self.block)
                    z += 1
                y += 1
            x += 1
