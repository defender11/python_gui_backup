from tkinter import *

from modules import config
from lib.frames.FrameTop import FrameTop
from lib.frames.FrameCenter import FrameCenter
from lib.frames.FrameBottom import FrameBottom


class Application:
    def __init__(self, window: Tk, app_config):
        self.window = window

        frame_top = FrameTop(window, app_config['frames']['FrameTop']).init()
        frame_center = FrameCenter(window, app_config['frames']['FrameCenter']).init()
        frame_bottom = FrameBottom(window, app_config['frames']['FrameBottom']).init()

    def run(self):
        self.window.mainloop()


# Application run
# -------

def app():
    window = Tk()
    app_config = config.get('app_config')
    Application(window, app_config).run()


app()
