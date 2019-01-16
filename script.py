from PIL import Image


img = Image.open("0.jpeg")
img = img.convert('L')


print(img.getpixel((1,1)))

width, height = img.size


string = ''
for i in range(width):
    for j in range(height):
        pixel = img.getpixel((j,i))
        if 0 < pixel < 63.75:
            char = 'm'
        elif 63.75 < pixel < 127.5:
            char = 'v'
        elif 127.5 < pixel < 191.25:
            char = '*'
        else :
            char = ' '
        string += char
    string += '\n'

with open("photo.txt", "w") as f :
    f.write(string)
