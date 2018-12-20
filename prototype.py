from PIL import Image, ImageDraw, ImageFont

# image_dim of the image, will later be taken from url
image_dim = (800, 600)

# Default text on image will be same as the image_dim
text = " x ".join([str(integer) for integer in image_dim])

# Draws the new image, with image_dim and bg color specified
img = Image.new("RGB", image_dim, "#dddddd")

# sets size of font to be 10 times smaller than height of image
font = ImageFont.truetype("assets/fonts/Roboto-Light.ttf", image_dim[1]//10)

draw = ImageDraw.Draw(img)
text_dim = draw.textsize(text, font=font)

# Centers the text on the image
text_location = [(x - y) // 2 for x, y in zip(image_dim, text_dim)]

draw.text(text_location, text, font=font, fill="#aaaaaa")

img.save('build/demo.png')
