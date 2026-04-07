from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)

class CreateBox:
    def __init__(self, sx=10, sy=63, sz=10, lx=3, ly=3, lz=3, block=block.DIAMOND_BLOCK):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.lx = lx
        self.ly = ly
        self.lz = lz
        self.block = block

    def create_box(self):
        mc.postToChat("Hello, World! This API can create boxes!")
        mc.setBlocks(self.sx, self.sy, self.sz, self.sx + self.lx -1, self.sy + self.ly -1, self.sz + self.lz -1, self.block)
