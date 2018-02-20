import mcpi.minecraft as minecraft
import mcpi.block as block
import math

def Convert(x1, y1, z1, x2, y2, z2):
    mc = minecraft.Minecraft.create()
    file = open("convert.txt", 'w')

    xhigh = max(x1, x2)
    xlow = min(x1, x2)
    yhigh = max(y1, y2)
    ylow = min(y1, y2)
    zhigh = max(z1, z2)
    zlow = min(z1, z2)

    array = []
 
    # blocks = []
    for x in range(xhigh - xlow + 1):
        # blocks.append([])
        for y in range(yhigh - ylow + 1):
            # blocks[x].append([])
            for z in range(zhigh - zlow + 1):
                # blocks[x][y].append([])
                block = mc.getBlock(xlow + x, ylow + y, zlow + z)        
                print(xlow + x, ylow + y, zlow + z, block)
                array.append(block)
                rawTextData = str(xlow + x) + "," + str(ylow + y) + "," + str(zlow + z) + "," + str(block) + "\n"
                # blocks[x][y][z] = block


    tempX = xhigh - xlow
    tempY = yhigh - ylow
    tempZ = xhigh - xlow



    textData = "var map = " + str(array) + ";\n" + "var i = 0\n" + "\n" + "for(x = 0; x < " + str(tempX + 1) + "; x++) {\n" + "  for(y = 0; y < " + str(tempY + 1) + "; y++) {\n" + "    for(z = 0; z < " + str(tempZ + 1) + "; z++) {\n" +  "      cube(x+5, z+5, y+5, map[i]);\n" + "      i++;\n" + "    }\n" + "  }\n" + "}\n"

    file.write(textData)
    file.close()
    # return blocks
