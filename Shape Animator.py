from tkinter import *
from PIL import Image, ImageTk, ImageGrab, ImageDraw
import time
import numpy as np
import pygame
from pygame.locals import QUIT


class Error(Exception):
    """Exception"""
    pass


class FrameError(Error):
    """An Error Occured While Trying to Animate."""
    pass

class Animate:
    def __init__(self, master, mainFrame: str, fps: int, maxFrames: int):
        self.master = master
        self.mainFrame = mainFrame
        self.fps = fps
        self.maxFrames = maxFrames

    
    def _update(self):
        pass
# class Animation:
#     """
#     Used to animate
#     """

#     def __init__(self, master, mainFrame: Canvas, fps=int and None, maxFrames=int and None):
#         self.master = master
#         self.mainFrame = mainFrame
#         if fps == None:
#             pass
#         else:
#             self.fps = fps
#         if maxFrames == None:
#             self.maxFrames = 1
#         else:
#             self.maxFrames = maxFrames
#         self.frames = {}
#         self.count = 0

#     def update(self, frame):
#         """Update the frames."""
#         self.frames.update({f'frame_{self.count}':frame})
#         self.count += 1

#     def create_frame(self, frame):
#         if len(self.frames) > self.maxFrames:
#             raise FrameError(
#                 """Frames Exceeds Maximum Frame Limit"""
#             )
#         else:
#             self.update(frame)
    
#     def play(self):
#         self.mainFrame.delete(self.frames[list(self.frames.keys())[0]])
#         del self.frames[list(self.frames.keys())[0]]
#         self.master.after(35, self.play)

# def click(event):
#     global image1
#     image1 = Image.new('RGB', (root.winfo_screenwidth(),
#                                root.winfo_screenheight()), 'white')
#     draw = ImageDraw.Draw(image1)
#     def activate_paint(e):
#         global lastx, lasty
#         frame.bind('<B1-Motion>', paint)
#         lastx, lasty = e.x, e.y
#     def paint(e):
#         global lastx, lasty
#         x, y = e.x, e.y
#         frame_ = frame.create_line((lastx, lasty, x, y), width=2)
#         #  --- PIL
#         draw.line((lastx, lasty, x, y), fill='black', width=1)
#         lastx, lasty = x, y
#     frame.bind('<1>', activate_paint)

# def clicked():
#     animation.create_frame(image1)

# def new():
#     frame.delete('all')

root = Tk()
root.state('zoomed')
root.config(bg='#0d0c0c')
root.title('Shape Animator')
root.iconphoto(False, ImageTk.PhotoImage(file='ShapeEditorLogo.png'))
frame = Canvas(root, height=root.winfo_screenheight(), width=root.winfo_screenwidth(), bg='white')
frame.pack()
animation = Animation(root, frame, maxFrames=1000)
menubar = Menu(root, tearoff=0)
View = Menu(menubar, tearoff=0)
View.add_command(label='Add Frame', command=clicked)
View.add_command(label='New Frame', command=new)
menubar.add_cascade(label='Frame', menu=View)
root.config(menu = menubar)
root.bind('<Button-1>', click)
root.mainloop()
