from cairosvg import svg2png

from PIL import Image
import numpy as np

from icecream import ic

from img_util import ImgUtil as Iu

if __name__ == '__main__':
    # s = open("assets/wave 1.svg", "rb").read()
    # ic(s)
    #
    # svg2png(bytestring=s, parent_width=4000, parent_height=4000, write_to="output.png")
    # ImgUtil.svg2png('assets/wave 1.svg')

    im = Image.open('wave 1.png')

    # data = np.array(im)   # "data" is a height x width x 4 numpy array
    # red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
    #
    # # Replace white with red... (leaves alpha values alone...)
    # white_areas = (red == 0) & (blue == 0) & (green == 0)
    # data[..., :-1][white_areas.T] = (255, 0, 0) # Transpose back needed
    #
    # im2 = Image.fromarray(data)
    # im2.show()

    THEME = (255, 161, 70)
    c = Iu.lightness(THEME, 0.25)
    ic(c)

    im = Iu.refill_color(im, (0, 0, 0), c)
    # im.putalpha(127)
    # im.show()

    im = Iu.sweep_alpha(im, 0.75)


