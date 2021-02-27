from PIL import Image, ImageDraw, ImageFont


class MemeMaker():
    def __init__(self, path):
        pass

    def make_meme(img, body, author, width=500px) -> str:
        """Create a meme With writting text on Image.

        Arguments:
            in_path {str} -- the file location for the input image.
            out_path {str} -- the desired location for the output image.
            crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-
                            tuple.      Default=None.
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """
        img = Image.open(in_path)
        if crop is not None:
            img = img.crop(crop)

        if width is not None:
            ratio = width/float(img.width)
            height = int(ratio*float(img.height))
            img = img.resize((width, height))

        if message is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            draw.text((10, 30), message, font=font, fill='white')

        img.save(out_path)
        return out_path
