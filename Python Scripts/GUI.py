# by Roll&Rock
# example used per link below
# https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python


import config
#import importlib
import sys
import os
from tkinter import filedialog
from tkinter import *


class MyWindow:

    def __init__(self, win):
        # folder location will be passed to config.py for other scripts to pick it up
        root = Tk()  # pointing root to Tk() to use it as Tk() in program.
        root.withdraw()  # Hides small tkinter window.
        root.attributes('-topmost', True)

        self.lbl1 = Label(win, text='Target FWHM ')
        self.lbl1.place(x=100, y=55)
        self.t1 = Entry(bd=4)
        self.t1.place(x=200, y=50)

        self.btn1 = Button(win, text='Start: DeepSkyStackerSNS')
        self.btn2 = Button(win, text='Start: DeepSkyStackerSNS_Filter')
        self.btn3 = Button(win, text='Start: SirilSNS')
        self.b1 = Button(win, text='Start: DeepSkyStackerSNS', command=self.ds)
        self.b1.place(x=550, y=50)
        self.b2 = Button(win, text='Start: DeepSkyStackerSNS_Filter', command=self.dsf)
        self.b2.place(x=550, y=100)
        self.b3 = Button(win, text="Start: SirilSNS", command=self.siril)
        self.b3.place(x=550, y=150)

    def ds(self):
        config.v = float(self.t1.get())  ## Store current entry value in shared module
        config.open_file = filedialog.askdirectory()  # saving Folder address as "open_file" variable to config.py
        import DeepSkyStackerSNS
        #DeepSkyStackerSNS.main()

    def dsf(self):
        config.v = float(self.t1.get())  ## Store current entry value in shared module
        config.open_file = filedialog.askdirectory()  # saving Folder address as "open_file" variable to config.py
        import DeepSkyStackerSNS_Filter
        #DeepSkyStackerSNS_Filter.main()

    def siril(self):
        import config
        config.v = float(self.t1.get())  ## Store current entry value in shared module
        config.open_file = filedialog.askdirectory()  # saving Folder address as "open_file" variable to config.py
        try:
            del sys.modules["SirilSNS"]
            from SirilSNS import main
        except:
            from SirilSNS import main



# main window settings
window = Tk()
mywin = MyWindow(window)
window.title('Batmobile Garage')
window.geometry("800x250+10+10")

# centering window - does not work on Windows
#window.eval('tk::PlaceWindow %s center' % window.winfo_pathname(window.winfo_id()))
window.mainloop()
