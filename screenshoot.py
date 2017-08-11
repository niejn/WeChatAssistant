from time import time
import os
import itchat
import platform


def GetImagePath():
    if not os.path.exists("./ScreenShoot/"):
        os.mkdir("./ScreenShoot/")
    return "./ScreenShoot/"


def SC():
    im_path = GetImagePath()
    im_name = "{}{}.{}".format(im_path, str(time()), "png")

    im = None
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        from PIL import ImageGrab
        im = ImageGrab.grab()
    elif platform.system() == 'Linux':
        import pyscreenshot as ImageGrab
        im = ImageGrab.grab()

    if im is not None:
        im.save(im_name)

    itchat.send("@img@{}".format(im_name), toUserName="filehelper")
    os.remove(im_name)
