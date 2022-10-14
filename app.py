import tkinter
from tkinter import *

from modules import config


class Application:
    def __init__(self, window: Tk, app_config):
        self.window = window
        window.columnconfigure(0, weight=3)
        # config the root window
        # window.geometry('300x200')
        # window.resizable(False, False)
        window.title('DB BACKUP Widget')

        frame_log = LogFrame(window)
        frame_log.set('test')
        frame_main = MainFrame(window, frame_log)

    def run(self):
        self.window.mainloop()


class MainFrame:
    def __init__(self, window, frame_log):
        self.window = window
        self.name = self.__class__
        self.LogFrame = frame_log
        self.label()
        self.window.grid()

    def label(self):
        Label(self.window, text='DB LIST: ').grid(row=0, column=0)
        Entry(self.window).grid(row=0, column=1)
        self.LogFrame.set('test 321', True, True)


class LogFrame:
    def __init__(self, window):
        self.window = window
        self.entry_text = tkinter.StringVar()

        self.entry = Entry(
            self.window,
            textvariable=self.entry_text
        )

        self.entry.grid(row=1, columnspan=2, sticky='wens')

    def set(self, new_text, append=False, is_new_row=False):
        text = new_text
        if append:
            text = self.entry.get()
            if is_new_row:
                text = text + '\n'

            text = text + new_text

        self.entry_text.set(text)


# Application run
# -------

def app():
    window = Tk()
    app_config = config.get('app_config')
    Application(window, app_config).run()


app()
