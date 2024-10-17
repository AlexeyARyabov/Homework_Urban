from PIL import Image

with Image.open("06.jpg") as im:
    print(im.format, im.size, im.mode)
    width, height = im.size
    width_out = int(width * 0.5)
    height_out = int(height * 0.5)
    out = im.resize((width_out, height_out))
    out = out.convert('L')
    out.save('out_im.gif')
