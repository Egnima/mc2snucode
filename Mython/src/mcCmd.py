import mcpi.minecraft as minecraft
import mcpi.block as block
import Convert
import mcTurtle
import cmd

class Commands(cmd.Cmd):
    mc = minecraft.Minecraft.create()

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">> "
        self.intro = ""

    def do_exit(self, args):
        # exit 
        return -1
                     
    def do_EOF(self, line):
        return True

    # convert mcMaps to turtlecraft(snu) Commands

    def do_convert(self, args):
        Convert.Convert(self.startPos.x, self.startPos.y, self.startPos.z,
            self.endPos.x, self.endPos.y, self.endPos.z)
            
    def do_setPos1(self, args):
        self.startPos = self.mc.player.getTilePos()
        print(str(self.startPos))
        
    def do_setPos2(self, args):
        self.endPos = self.mc.player.getTilePos()
        print(str(self.endPos))

    # mcTurtle Commands

    def do_start(self, args):
        self.peter = mcTurtle.MinecraftTurtle(self.mc, self.mc.player.getPos())
        self.do_setTPos("setTPos")
        print(self.mc.player.getPos())

    def do_setTPos(self, args):
        "set the turtle's position"
        temp = self.mc.player.getPos()
        self.peter.setposition(temp.x, temp.y, temp.z)    

    # Moves------------------------------------------

    def do_up(self, num):
        "pitch up by a number(int) of degrees"
        try:    
            self.peter.up(int(num))
        except Exception as ex:
            print("Error", ex)


    def do_down(self, num):
        "pitch down by a number(int) of degrees"  
        try:
            self.peter.down(int(num))
        except Exception as ex:
            print("Error", ex)

    def do_right(self, num):
        "rotate right by a number(int) of degrees"
        try:
            self.peter.right(int(num))
        except Exception as ex:
            print("Error", ex)

    def do_left(self, num):
        "rotate left by a number(int) of degrees"
        try:
            self.peter.left(int(num))
        except Exception as ex:
            print("Error", ex)

    def do_forward(self, num):
        "go forward by a number of blocks"
        try:
            self.peter.forward(int(num))
        except Exception as ex:
            print("Error", ex)

    def do_backward(self, num):
        "go backward by a number of blocks"
        try:
            self.peter.backward(int(num))
        except Exception as ex:
            print("Error", ex)

    def do_setSpeed(self, speed):
        "set Turtle's speed"
        try:
            self.peter.speed(int(speed))
        except Exception as ex:
            print("Error", ex)

    def do_home(self, args):
        try:
            self.peter.home()
        except Exception as ex:
            print("Error", ex)

    # Pens-----------------------------------------

    def do_penUp(self, args):
        try:
            self.peter.penup()
        except Exception as ex:
            print("Error", ex)

    def do_penDown(self, args):
        try:
            self.peter.pendown()
        except Exception as ex:
            print("Error", ex)

    def do_isDown(self, args):
        try:
            print(self.peter.isdown())
        except Exception as ex:
            print("Error", ex)

    def do_penBlock(self, num):
        try:
            self.peter.penblock(block.Block(int(num)))
        except Exception as ex:
            print("Error", ex)

if __name__ == "__main__":
    Commands().cmdloop()