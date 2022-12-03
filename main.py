from PIL import Image

def encryptFormula(colors:tuple,x,y)->tuple:
    colors = [*colors]
    colors[0] = (colors[0] + x*y+1) % 256
    colors[1] = (colors[1] + x*y+1) % 256
    colors[2] = (colors[2] + x*y+1) % 256
    return (colors[0],colors[1],colors[2])

def colorPaletteSwap(image,xBound:int,yBound:int):
    for x in range(xBound):
        for y in range(yBound):
            image[x,y] = encryptFormula(image[x,y],x,y)
    return image


def main():
    preImage = Image.open(r"mountains.jpg")
    xBound,yBound = preImage.size
    encryptedImage = colorPaletteSwap(preImage.load(),xBound,yBound)
    preImage.save("encryptedImage.png")
    preImage.show()
    


if __name__ == "__main__":
    main()