from PIL import Image, ImageDraw, ImageFont
import string


class ImageMaker:
    def __init__(self, input_path):
        self.input_path = input_path

    @staticmethod
    def generate_inputs(raw_path):
        info = {}

        image_dim = raw_path.split('/')
        if len(image_dim) == 1 or image_dim[1] == '':
            im_dim = [image_dim[0], image_dim[0]]

        im_dim = [int(integer) for integer in im_dim]
        info["image_dim"] = im_dim

        # Default text on image will be same as the image_dim
        # TODO: What about the text passed?
        text = " x ".join((str(integer) for integer in im_dim))

        info["text"] = text

        try:
            bg = image_dim[2]
            hex_tuple = tuple(x for x in string.hexdigits)
            if bg.startswith(hex_tuple):
                for char in bg:
                    if not char in hex_tuple:
                        raise IndexError
                if not len(bg) in (3, 6):
                    raise IndexError
            else:
                raise IndexError
        except IndexError:
            bg = "dddddd"
        finally:
            bg = "#" + bg

        info["bg"] = bg

        return info

    def make_image(self):
        info = ImageMaker.generate_inputs(self.input_path)
        image_dim = info['image_dim']
        text = info['text']
        bg = info['bg']

        # Draws the new image, with image_dim and bg color specified
        img = Image.new("RGB", image_dim, bg)
        # sets size of font to be 10 times smaller than height of image
        font = ImageFont.truetype(
            "assets/fonts/Roboto-Light.ttf", image_dim[1]//10)
        draw = ImageDraw.Draw(img)
        text_dim = draw.textsize(text, font=font)
        # Centers the text on the image
        text_location = tuple((x - y) // 2 for x,
                              y in zip(image_dim, text_dim))
        draw.text(text_location, text, font=font, fill="#aaaaaa")

        return img
