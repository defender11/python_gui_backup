from tkinter import *
from tkinter import ttk

from lib.frames.BaseFrame import BaseFrame


class FrameCenter(BaseFrame):
    def init(self):
        self.window.grid()
        self.label()

    def label(self):
        Label(self.window, text='FrameCenter').grid(row=1, column=0)
