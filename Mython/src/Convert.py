import mcpi.minecraft as minecraft
import mcpi.block as Block
import math
import os

def Convert(x1, y1, z1, x2, y2, z2):
    mc = minecraft.Minecraft.create()

    xhigh = max(x1, x2)
    xlow = min(x1, x2)
    yhigh = max(y1, y2)
    ylow = min(y1, y2)
    zhigh = max(z1, z2)
    zlow = min(z1, z2)

    array = []
 
    for x in range(xhigh - xlow + 1):
        for y in range(yhigh - ylow + 1):
            for z in range(zhigh - zlow + 1):
                blockType = mc.getBlockWithData(xlow + x, ylow + y, zlow + z)  
                print(xlow + x, ylow + y, zlow + z, blockType)
                block = 5

                # http://www.stuffaboutcode.com/p/minecraft-api-reference.html 
                if blockType == Block.Block(3, 0):
                    block = 1
                elif blockType == Block.Block(17, 0):
                    block = 2
                elif blockType == Block.Block(35, 14):
                    block = 4
                elif blockType == Block.Block(35, 11):
                    block = 5
                elif blockType == Block.Block(57, 0):
                    block = 6
                elif blockType == Block.Block(45, 0):
                    block = 7
                elif blockType == Block.Block(5, 0):
                    block = 8
                elif blockType == Block.Block(1, 0):
                    block = 9
                elif blockType == Block.Block(17, 2):
                    block = 12   
                elif blockType == Block.Block(80, 7):
                    block = 15  
                elif blockType == Block.Block(79, 0):
                    block = 16  
                elif blockType == Block.Block(35, 4):
                    block = 17
                elif blockType == Block.AIR:
                    block = 0

                array.append(block)


    tempX = xhigh - xlow
    tempY = yhigh - ylow
    tempZ = xhigh - xlow

    array.reverse()

    textData  = "var map = " + str(array) + ";\n"
    textData += "var i = 0\n"
    textData += "\n"
    textData += "for(x = 0; x < " + str(tempX + 1) + "; x++) {\n"
    textData += "  for(y = 0; y < " + str(tempY + 1) + "; y++) {\n"
    textData += "    for(z = 0; z < " + str(tempZ + 1) + "; z++) {\n"
    textData += "      cube(x, z, y, map[i]);\n" + "      i++;\n"
    textData += "    }\n"
    textData += "  }\n"
    textData += "}\n"

    curDir = os.path.dirname(os.path.realpath(__file__))
    fullDir = curDir + '\output'
    if not os.path.isdir(fullDir):
        os.mkdir(fullDir)
    with open(curDir + "\output\convert.txt", 'wt') as file:
        file.write(textData)
