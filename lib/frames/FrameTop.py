from tkinter import *

from lib.frames.BaseFrame import BaseFrame


class FrameTop(BaseFrame):
    def init(self):
        self.window.grid()
        self.label()

    def label(self):
        print(self.config)
        Label(self.window, text='FrameTop').grid(row=0, column=0)
