import sys
from PIL import Image

MetaData = 10

def Encrypt(Img,data):
    pixels = Img.load() 
    width, height = Img.size
    DataSize = len(data)

    pixs = []
    NewPixs = []
    for i in range(width):
        for j in range(height):
            pixs.append(pixels[i,j])


    dd = DataSize
    i = 0
    while(i<MetaData):
        nw = pixs[i][2] & (~0 << 1)
        x = dd%2
        nw = nw | x
        #print(nw & 1)
        NewPixs.append((pixs[i][0],pixs[i][1],nw))
        dd = dd/2
        i = i+1
    k = 0
    #print(NewPixs)
    while(k<DataSize):
        cc = 0
        dd = ord(data[k])
        while(cc<8):
            nw = pixs[i][2] & (~0 << 1)
            x = dd%2
            nw = nw | x
            NewPixs.append((pixs[i][0],pixs[i][1],nw))
            dd = dd/2
            i = i+1
            cc = cc+1
        k = k+1

    while(i<len(pixs)):
        NewPixs.append(pixs[i])
        i = i+1

    NewImg = Image.new("RGB",Img.size,"blue")
    pix = NewImg.load()
    
    k = 0
    for i in range(width):
        for j in range(height):
            pix[i,j] = NewPixs[k]
            k = k+1
    #NewImg.show()
    return NewImg

pth = raw_input("Enter Path to Encrypt Image : ")
data = raw_input("Enter Data to Encrypt : ")
Img = Image.open(pth)

NewImg= Encrypt(Img,data)
idx = pth.rfind('.')
NewPth = pth[:idx]+"-Enc"+".png"


pix = []
x = NewImg.load()
width, height = NewImg.size

for i in range(width):
    for j in range(height):
        pix.append(x[i,j])
#for i in range(10):
#    print(pix[i][2])

    
NewImg.save(NewPth)
print("Created : " + NewPth)
