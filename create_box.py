import math
from mc_remote.minecraft import Minecraft
from param_mc_remote import block


class CreateBox:
    def __init__(self, sx=10, sy=63, sz=10, lx=3, ly=3, lz=3, rx=0, ry=0, rz=0, block=block.DIAMOND_BLOCK):
        self.sx, self.sy, self.sz = sx, sy, sz
        self.lx, self.ly, self.lz = lx, ly, lz
        self.rx, self.ry, self.rz = rx, ry, rz
        self.block = block

    def _rot_x(self, y, z, rad):
        return y * math.cos(rad) - z * math.sin(rad), y* math.sin(rad) + z * math.cos(rad)

    def _rot_y(self, x, z, rad):
        return x * math.cos(rad) + z * math.sin(rad), -x * math.sin(rad) + z * math.cos(rad)

    def _rot_z(self, x, y, rad):
        return x * math.cos(rad) -y * math.sin(rad), x * math.sin(rad) + y * math.cos(rad)

    def _rotate(self, x, y, z):
        rad_x, rad_y, rad_z = math.radians(self.rx), math.radians(self.ry), math.radians(self.rz)
        y, z = self._rot_x(y, z, rad_x)
        x, z = self._rot_y(x, z, rad_y)
        x, y = self._rot_z(x, y, rad_z)
        return x, y, z

    def _inverse_rotate(self, x, y, z):
        rad_x, rad_y, rad_z = math.radians(self.rx), math.radians(self.ry), math.radians(self.rz)
        x, y = self._rot_z(x, y, -rad_z)
        x, z = self._rot_y(x, z, -rad_y)
        y, z = self._rot_x(y, z, -rad_x)
        return x, y, z

    def create_box(self, mc, hollow=False):
        mc.postToChat("Hello, World! This API can create boxes!")

        corners = [(x, y, z)
                   for x in (0, self.lx)
                   for y in (0, self.ly)
                   for z in (0, self.lz)]
        rotated_corners = [self._rotate(x, y, z) for x, y, z in corners]

        min_x = math.floor(min(p[0] for p in rotated_corners))
        max_x = math.ceil(max(p[0] for p in rotated_corners))
        min_y = math.floor(min(p[1] for p in rotated_corners))
        max_y = math.ceil(max(p[1] for p in rotated_corners))
        min_z = math.floor(min(p[2] for p in rotated_corners))
        max_z = math.ceil(max(p[2] for p in rotated_corners))

        for dx in range(min_x, max_x + 1):
            for dy in range(min_y, max_y + 1):
                for dz in range(min_z, max_z + 1):
                    lx_, ly_, lz_ = self._inverse_rotate(dx + 0.5, dy + 0.5, dz + 0.5)
                    if not (0 <= lx_ < self.lx and 0 <= ly_ < self.ly and 0 <= lz_ < self.lz):
                        continue

                    if hollow:
                        on_surface = (lx_ < 1 or lx_ > self.lx - 1 or
                                      ly_ < 1 or ly_ > self.ly - 1 or
                                      lz_ < 1 or lz_ > self.lz -1)
                        if not on_surface:
                            continue

                    mc.setBlock(self.sx + dx, self.sy + dy, self.sz + dz, self.block)
