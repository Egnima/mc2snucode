import mcpi.minecraft as minecraft
import mcpi.block as block
import mc2snucode
import cmd
import math

class Commands(cmd.Cmd):
    mc = minecraft.Minecraft.create()

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">> "
        self.intro = ""

    def do_exit(self, args):
        # exit 
        return -1

    def do_convert(self, args):
        mc2snucode.Convert(self.startPos.x, self.startPos.y, self.startPos.z,
            self.endPos.x, self.endPos.y, self.endPos.z)
            

    def do_setPos1(self, args):
        self.startPos = self.mc.player.getTilePos()
        # self.startPos = minecraft.Vec3(681, 4, 79)
        print(str(self.startPos))
        
    def do_setPos2(self, args):
        self.endPos = self.mc.player.getTilePos()
        # self.endPos = minecraft.Vec3(679, 4, 81)
        print(str(self.endPos))
                     

    def do_EOF(self, line):
        return True


if __name__ == "__main__":
    Commands().cmdloop()