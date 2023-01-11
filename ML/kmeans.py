# -*- coding: utf-8 -*-

import urllib.request
import io
from PIL import Image
import random
import sys
#URL = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/109547da-8cce-413f-a249-0fdc507ea45d/d48opvm-0a7817f6-42a7-4d16-aeeb-f147c4910706.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvMTA5NTQ3ZGEtOGNjZS00MTNmLWEyNDktMGZkYzUwN2VhNDVkXC9kNDhvcHZtLTBhNzgxN2Y2LTQyYTctNGQxNi1hZWViLWYxNDdjNDkxMDcwNi5qcGcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.UqY9qleiTOcgO3v90RskHTZRwxEORPhudnMbPGil8b4'
#URL = "https://i.pinimg.com/originals/95/2a/04/952a04ea85a8d1b0134516c52198745e.jpg"
URL = sys.argv[1]

f = io.BytesIO(urllib.request.urlopen(URL).read()) # Download the picture at the url as a file object
kSize = int(sys.argv[2])
# You can also use this on a local file; just put the local filename in quotes in place of f.
#img.show() # Send the image to your OS to be displayed as a temporary file
# =============================================================================
# print(img.size) # A tuple. Note: width first THEN height. PIL goes [x, y] with y counting from the top of the frame.
# pix = img.load() # Pix is a pixel manipulation object; we can assign pixel values and img will change as we do so.
# print(pix[2,5]) # Access the color at a specific location; note [x, y] NOT [row, column].
# pix[2,5] = (255, 255, 255) # Set the pixel to white. Note this is called on “pix”, but it modifies “img”.
# img.show() # Now, you should see a single white pixel near the upper left corner
# img.save("my_image.png") # Save the resulting image. Alter your filename as necessary.
# =============================================================================

img = Image.open(f)
pix= img.load()

width = img.size[0]
height = img.size[1]

dictK = {}
for i in range(0,kSize):
    x = random.randint(0,width-10)
    y = random.randint(0,height-10)
    t = pix[x,y]
    if t not in dictK:
        dictK[t]= []

for i in range(0,width):
    for j in range(0,height):
        point = pix[i,j]
        
        closest = (0,0,0) 
        dist = 100000000
        for k in dictK:
            temp = ((k[0]-point[0])**2 + (k[1]-point[1])**2 + (k[2]-point[2])**2)**0.5
            if temp < dist:
                dist = temp
                closest = k
        tuple1 = (i,j)
        dictK[closest].append(tuple1)
       
newDictK = {}
times = 1
while True:
    #print(times)
    times += 1
    newDictK = {}
    count = 0
    for k in dictK:
        red = 0
        green = 0
        blue = 0
        for s in dictK[k]:
            r = pix[s[0],s[1]]
            red += r[0]
            green += r[1]
            blue += r[2]
        red = int(red / len(dictK[k]))
        green = int(green / len(dictK[k]))
        blue = int(blue / len(dictK[k]))

        if red == k[0] and green == k[1] and blue == k[2]:
            count += 1
        tuple1 = (red,green,blue)
        newDictK[tuple1] = []
        #print(str(k) + "  " + str(tuple1))

    if count == kSize:
        break
    #print(count)
    for i in range(0,width):
        for j in range(0,height):
            point = pix[i,j]
        
            closest = (0,0,0) 
            dist = 100000000
            for k in newDictK:
                temp = ((k[0]-point[0])**2 + (k[1]-point[1])**2 + (k[2]-point[2])**2)**0.5
                if temp < dist:
                    dist = temp
                    closest = k
            tuple1 = (i,j)
            newDictK[closest].append(tuple1)
    dictK = newDictK

for k in dictK:
    for s in dictK[k]:
        x = s[0]
        y = s[1]
        pix[x,y] = k

img.save("kmeansout.png")
            
# =============================================================================
#NAIVE ALGORITHM
# =============================================================================
# img27 = Image.open(f)
# img8 = Image.open(f) 
# width = img27.size[0]
# height = img27.size[1]
# 
# pix27 = img27.load()
# pix8 = img8.load()
# 
# for i in range(0,width):
#     for j in range(0,height):
#         red27 = pix27[i,j][0]
#         green27 = pix27[i,j][1]
#         blue27 = pix27[i,j][2]
#         if red27 < 255//3:
#             red27 = 0
#         elif red27 > 255*2//3:
#             red27 = 255
#         else:
#             red27 = 127
#             
#         if green27 < 255//3:
#             green27 = 0
#         elif green27 > 255*2//3:
#             green27 = 255
#         else:
#             green27 = 127
#             
#         if blue27 < 255//3:
#             blue27 = 0
#         elif blue27 > 255*2//3:
#             blue27 = 255
#         else:
#             blue27 = 127
#             
#         pix27[i,j] = (red27,green27,blue27)
#         
#         red8 = pix8[i,j][0]
#         green8 = pix8[i,j][1]
#         blue8 = pix8[i,j][2]
#         if red8 < 128:
#             red8 = 0
#         else:
#             red8 = 255
# 
#         if green8 < 128:
#             green8 = 0
#         else:
#             green8 = 255
#             
#         if blue8 < 128:
#             blue8 = 0
#         else:
#             blue8 = 255
#             
#         pix8[i,j] = (red8,green8,blue8)
# 
# img27.save("Naive_27.png")
# img8.save("Naive_8.png")
# =============================================================================






