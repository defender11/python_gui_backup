from tkinter import *
from tkinter import ttk

from lib.frames.BaseFrame import BaseFrame


class FrameBottom(BaseFrame):
    def init(self):
        self.window.grid()
        self.label()

    def label(self):
        Label(self.window, text='FrameBottom').grid(row=2, column=0)
