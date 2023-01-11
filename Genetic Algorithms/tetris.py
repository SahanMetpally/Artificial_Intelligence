# -*- coding: utf-8 -*-
import sys

orientations = [([(0,0),(0,1),(0,2),(0,3)],4),
                ([(0,0),(1,0),(2,0),(3,0)],1),
                ([(0,0),(0,1),(1,0),(1,1)],2),
                ([(0,0),(-1,1),(0,1),(0,2)],3),
                ([(0,0),(1,0),(1,1),(2,0)],2),
                ([(0,0),(0,1),(0,2),(1,1)],3),
                ([(0,0),(-1,1),(0,1),(1,1)],2),
                ([(0,0),(0,1),(-1,1),(-1,2)],3),
                ([(0,0),(1,0),(1,1),(2,1)],2),
                ([(0,0),(0,1),(1,1),(1,2)],3),
                ([(0,0),(-1,1),(0,1),(1,0)],2),
                ([(0,0),(1,0),(1,1),(1,2)],3),
                ([(0,0),(0,1),(1,0),(2,0)],2),
                ([(0,0),(0,1),(0,2),(1,2)],3),
                ([(0,0),(0,1),(-1,1),(-2,1)],2),
                ([(0,0),(0,1),(0,2),(-1,2)],3),
                ([(0,0),(1,0),(2,0),(2,1)],2),
                ([(0,0),(0,1),(0,2),(1,0)],3),
                ([(0,0),(0,1),(1,1),(2,1)],2)
                ]

#inputB = "          #         #         #      #  #      #  #      #  #     ##  #     ##  #     ## ##     ## #####  ########  ######### ######### ######### ######### ########## #### # # # # ##### ###   ########"
inputB = sys.argv[1]

WIDTH = 10
HEIGHT = 20

# =============================================================================
# board = [[0]*WIDTH]*HEIGHT
# 
# for i in range(0,HEIGHT):
#     for j in range(0,WIDTH):
#         ind = i*WIDTH + j
#         print(inputB[ind], end='')
#         board[i][j] = inputB[ind]
#     print()
# =============================================================================

answers = []

for t in orientations:
    piece = t[0]
    wid = t[1]
    one = piece[0]
    two= piece[1]
    three = piece[2]
    four = piece[3]
    for i in range(0,WIDTH-wid+1):
        place = 0
        fit = False
        for j in range(0,HEIGHT):
            point1 = j*WIDTH+i
            point2 = point1 + two[0]*WIDTH + two[1]
            point3 = point1 + three[0]*WIDTH + three[1]
            point4 = point1 + four[0]*WIDTH + four[1]
            
            if(point1 >= 0 and point1 < 200 and point2 >= 0 and point2 < 200 and point3 >= 0 and point3 < 200 and point4 >= 0 and point4 < 200):
                if(inputB[point1] == " " and inputB[point2] == " " and inputB[point3] == " " and inputB[point4] == " "):
                    place = j
                    fit = True
                else:
                    break

        point1 = place*WIDTH+i
        point2 = point1 + two[0]*WIDTH + two[1]
        point3 = point1 + three[0]*WIDTH + three[1]
        point4 = point1 + four[0]*WIDTH + four[1]
        if not fit:
            answers.append("GAME OVER")
        else:  
            tempList = list(inputB)
            tempList[point1] = "#"
            tempList[point2] = "#"
            tempList[point3] = "#"
            tempList[point4] = "#"
            temp = "".join(tempList)
            
            for row in range(0,HEIGHT):
                rowFill = True
                for col in range(0,WIDTH):
                    pos = row*WIDTH + col
                    if tempList[pos] == " ":
                        rowFill = False
                        break
                if rowFill:
                    pos = row*WIDTH
                    pos2 = row*WIDTH+9
                    temp = "          " + temp[0:pos] + temp[pos2+1:]
            answers.append(temp)
final = ""
for s in answers:
    final += s + "\n"

output = open("tetrisout.txt", "w")
print(final, file=output)
output.close()















