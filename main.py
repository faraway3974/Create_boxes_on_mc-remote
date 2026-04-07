from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import block
from createbox import CreateBox

Box1 = CreateBox(10, 63, 10, 3, 3, 3, block.DIAMOND_BLOCK)
Box1.create_box()