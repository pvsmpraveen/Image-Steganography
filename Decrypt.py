import sys
from PIL import Image
def Decrypt(Img,MetaData):
    
    pix = Img.load() 
    width, height = Img.size
    dLen = 0
    
    i = 0
    tw = 0
    pixs = []
    for i in range(width):
        for j in range(height):
            pixs.append(pix[i,j])

    i = 0
    tw= 1
    while(i<MetaData):
        nw = pixs[i][2] & 1
        #print(nw)
        dLen = dLen + tw*(pixs[i][2] & 1)
        tw = tw*2
        i = i+1

    d = []
    while(len(d)<dLen):
        k = 0
        ch = 0
        tw = 1
        while(k<8):
            ch = ch + tw*(pixs[i][2] & 1)
            tw = tw*2
            i = i+1
            k = k+1
        d.append(chr(ch))
        
    print("--Data--\n"+"".join(d))
        
pth = raw_input("Enter Path to Decrypt Image : ")
Meta = int(raw_input("Enter Secret Key : "))

Img = Image.open(pth)
Decrypt(Img,Meta)

cmt = """
pix = []
x = Img.load()
width, height = Img.size

for i in range(width):
    for j in range(height):
        pix.append(x[i,j])
for i in range(10):
    print(pix[i][2])
"""
