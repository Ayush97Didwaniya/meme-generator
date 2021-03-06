"""to generate meme by writting text over image."""
from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine():
    """Class to generate Meme's."""

    def __init__(self, out_path):
        """Create instance object with output path."""
        self.outPath = out_path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme With writting text on Image.

        Arguments:
            img -- the file location for the input image.
            text -- text of quote to add on Image to generate meme.
            author -- author of quote.
            width -- The pixel width value. Default=500px.
        Returns:
            str -- the file path to the output image.
        """
        img = Image.open(img_path)
        if width is not None:
            ratio = width/float(img.width)
            height = int(ratio*float(img.height))
            img = img.resize((width, height))

        img = img.convert('RGB')
        message = text + ' - ' + author
        if text is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            draw.text((10, 30), message, font=font, fill='white')

        outputfile = f'/{random.randint(0,100000000)}.jpg'
        filePath = self.outPath + outputfile
        try:
            img.save(filePath)
        except ValueError:
            print(ValueError)
        return filePath
