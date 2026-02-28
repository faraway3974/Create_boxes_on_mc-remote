from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)

mc.postToChat("Hello, World! This API can create boxes!")

sX = 0 # 起点
sY = 0
sZ = 0
lX = 10 # 辺の長さ
lY = 10
lZ = 10
Block = block.DIAMOND_BLOCK