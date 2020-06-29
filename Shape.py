from tkinter import *
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw, ImageFilter, ImageGrab, ImageTk
import sys
import time
import tkinter as tk

LAYERS_DICT = {}
RECYCLED = {}
Circles = {}
OUTLINES = {}
X3_CIRCLES = {}
SAVED = False
count = 0
marks = 0
root = Tk()
root.state('zoomed')
root.config(bg='#0d0c0c')
root.iconphoto(False, ImageTk.PhotoImage(
    file="C:/Users/DrewM/OneDrive/Documents/Code/ShapeEditorLogo.png"))


def Exit():
    global SAVED
    warn = messagebox.askyesnocancel(
        'WARNING', 'Are you sure you want to exit without saving?')
    if warn == True:
        sys.exit()
    elif warn == False:
        Save_Canvas()
    elif warn == None:
        pass


def start_pos(event):
    global x1, y1
    if 'OUTLINE' in OUTLINES:
        LAYERS_DICT['canvas'].delete(OUTLINES['OUTLINE'])
    if 'CIRCLE1' in Circles:
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE1'])
    x1 = event.x
    y1 = event.y
    circle1 = LAYERS_DICT['canvas'].create_oval(
        x1, y1, x1+5, y1+5, fill='black')
    if 'CIRCLE2' in Circles:
        out = LAYERS_DICT['canvas'].create_rectangle(
            x1, y1, x2, y2, outline='black', dash=(3, 100))
        OUTLINES.update({'OUTLINE': out})
    Circles.update({'CIRCLE1': circle1})
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def end_pos(event):
    global x2, y2
    if 'OUTLINE' in OUTLINES:
        LAYERS_DICT['canvas'].delete(OUTLINES['OUTLINE'])
    if 'CIRCLE2' in Circles:
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE2'])
    x2 = event.x
    y2 = event.y
    circle2 = LAYERS_DICT['canvas'].create_oval(
        x2, y2, x2+5, y2+5, fill='black')
    if 'CIRCLE1' in Circles:
        out = LAYERS_DICT['canvas'].create_rectangle(
            x1, y1, x2, y2, outline='black', dash=(3, 100))
        OUTLINES.update({'OUTLINE': out})
    Circles.update({'CIRCLE2': circle2})
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def escape(event):
    try:
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE1'])
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE2'])
        LAYERS_DICT['canvas'].delete(OUTLINES['OUTLINE'])
    except KeyError:
        pass
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def Arc():
    global count
    if 'canvas' in LAYERS_DICT:
        canvas = LAYERS_DICT['canvas']
    else:
        canvas = Canvas(root, height=root.winfo_screenheight(),
                        width=root.winfo_screenwidth(), background='white')
        LAYERS_DICT.update({'canvas': canvas})
        canvas.grid(row=13, column=0)
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')

    def fill_area(event):
        global count
        color = colorchooser.askcolor()
        arc = canvas.create_arc(
            x1, y1, x2, y2, fill=color[1], outline=color[1], style=ARC)
        LAYERS_DICT.update({f'arc{count}': arc})
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE1'])
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE2'])
        LAYERS_DICT['canvas'].delete(OUTLINES['OUTLINE'])
        del Circles['CIRCLE1']
        del Circles['CIRCLE2']
        if SAVED == False:
            root.title('Shape Editor • Unsaved')
        else:
            root.title(f'Shape Editor • {str(root.filename)} •')
    canvas.bind("<Button-1>", start_pos)
    canvas.bind("<Button-3>", end_pos)
    canvas.bind("<Escape>", escape)
    root.bind("<Return>", fill_area)


def make_Text():
    global count
    if 'canvas' in LAYERS_DICT:
        canvas = LAYERS_DICT['canvas']
    else:
        canvas = Canvas(root, height=root.winfo_screenheight(),
                        width=root.winfo_screenwidth(), background='white')
        LAYERS_DICT.update({'canvas': canvas})
        canvas.grid(row=13, column=0)
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')
    entry_root = Tk()
    entry_root.title('Text')
    e = Entry(entry_root, borderwidth=5)
    e2 = Entry(entry_root, borderwidth=5)
    e2.insert(0, "Font Size")
    e.insert(0, "Text")
    e.grid(row=0, column=0)
    e2.grid(row=1, column=0)

    def fill_area(event):
        global count
        current = e.get()
        text = canvas.create_text(
            x1, y1, text=current, font=("Helvetica", e2.get()))
        count += 1
        LAYERS_DICT.update({f'text{count}': text})
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE1'])
        LAYERS_DICT['canvas'].delete(OUTLINES['OUTLINE'])
        del Circles['CIRCLE1']
        del Circles['CIRCLE2']
        if SAVED == False:
            root.title('Shape Editor • Unsaved')
        else:
            root.title(f'Shape Editor • {str(root.filename)} •')
    canvas.bind("<Button-1>", start_pos)
    canvas.bind("<Escape>", escape)
    root.bind("<Return>", fill_area)


def make_Line():
    global count
    if 'canvas' in LAYERS_DICT:
        canvas = LAYERS_DICT['canvas']
    else:
        canvas = Canvas(root, height=root.winfo_screenheight(),
                        width=root.winfo_screenwidth(), background='white')
        LAYERS_DICT.update({'canvas': canvas})
        canvas.grid(row=13, column=1)
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')

    def fill_area(event):
        global count
        color = colorchooser.askcolor()
        line = canvas.create_line(x1, y1, x2, y2, fill=color[1])
        count += 1
        LAYERS_DICT.update({f'line{count}': line})
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE1'])
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE2'])
        LAYERS_DICT['canvas'].delete(OUTLINES['OUTLINE'])
        del Circles['CIRCLE1']
        del Circles['CIRCLE2']
        if SAVED == False:
            root.title('Shape Editor • Unsaved')
        else:
            root.title(f'Shape Editor • {str(root.filename)} •')
    canvas.bind("<Button-1>", start_pos)
    canvas.bind("<Button-3>", end_pos)
    canvas.bind("<Escape>", escape)
    root.bind("<Return>", fill_area)


def make_Square():
    global count
    if 'canvas' in LAYERS_DICT:
        canvas = LAYERS_DICT['canvas']
    else:
        canvas = Canvas(root, height=root.winfo_screenheight(),
                        width=root.winfo_screenwidth(), background='white')
        LAYERS_DICT.update({'canvas': canvas})
        canvas.grid(row=13, column=1)
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')

    def fill_area(event):
        global count
        color = colorchooser.askcolor()
        rect = canvas.create_rectangle(
            x1, y1, x2, y2, fill=color[1], outline=color[1])
        count += 1
        LAYERS_DICT.update({f'rect{count}': rect})
        
        LAYERS_DICT['canvas'].delete(OUTLINES['OUTLINE'])
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE1'])
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE2'])
        del Circles['CIRCLE1']
        del Circles['CIRCLE2']
        if SAVED == False:
            root.title('Shape Editor • Unsaved')
        else:
            root.title(f'Shape Editor • {str(root.filename)} •')
    canvas.bind("<Button-1>", start_pos)
    canvas.bind("<Button-3>", end_pos)
    canvas.bind("<Escape>", escape)
    root.bind("<Return>", fill_area)


def make_Circle():
    global count
    if 'canvas' in LAYERS_DICT:
        canvas = LAYERS_DICT['canvas']
    else:
        canvas = Canvas(root, height=root.winfo_screenheight(),
                        width=root.winfo_screenwidth(), background='white')
        LAYERS_DICT.update({'canvas': canvas})
        canvas.grid(row=13, column=1)
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')

    def fill_area(event):
        global count
        color = colorchooser.askcolor()
        circle = canvas.create_oval(
            x1, y1, x2, y2, fill=color[1], outline=color[1])
        count += 1
        LAYERS_DICT.update({f'circ{count}': circle})
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE1'])
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE2'])
        del Circles['CIRCLE1']
        del Circles['CIRCLE2']
        LAYERS_DICT['canvas'].delete(OUTLINES['OUTLINE'])
        if SAVED == False:
            root.title('Shape Editor • Unsaved')
        else:
            root.title(f'Shape Editor • {str(root.filename)} •')
    canvas.bind("<Button-1>", start_pos)
    canvas.bind("<Button-3>", end_pos)
    canvas.bind("<Escape>", escape)
    root.bind("<Return>", fill_area)


def make_Triangle():
    global count
    if 'canvas' in LAYERS_DICT:
        canvas = LAYERS_DICT['canvas']
    else:
        canvas = Canvas(root, height=root.winfo_screenheight(),
                        width=root.winfo_screenwidth(), background='white')
        LAYERS_DICT.update({'canvas': canvas})
        canvas.grid(row=13, column=1)
    tri_root = Tk()
    label1 = Label(tri_root, text="Choose the first point of the Triangle: ")
    en1 = Entry(tri_root, borderwidth=5)
    label2 = Label(tri_root, text="Choose the second point of the Triangle: ")
    e2 = Entry(tri_root, borderwidth=5)
    label3 = Label(tri_root, text="Choose the third point of the Triangle: ")
    e3 = Entry(tri_root, borderwidth=5)
    label4 = Label(tri_root, text="Choose the fourth point of the Triangle: ")
    e4 = Entry(tri_root, borderwidth=5)
    label5 = Label(tri_root, text="Choose the fifth point of the Triangle: ")
    e5 = Entry(tri_root, borderwidth=5)
    label6 = Label(tri_root, text="Choose the sixth point of the Triangle: ")
    e6 = Entry(tri_root, borderwidth=5)
    label7 = Label(tri_root, text="Choose the seventh point of the Triangle: ")
    e7 = Entry(tri_root, borderwidth=5)
    label8 = Label(tri_root, text="Choose the eighth point of the Triangle: ")
    e8 = Entry(tri_root, borderwidth=5)
    label9 = Label(tri_root, text="Choose the ninth point of the Triangle: ")
    e9 = Entry(tri_root, borderwidth=5)
    label10 = Label(tri_root, text="Choose the tenth point of the Triangle: ")
    e10 = Entry(tri_root, borderwidth=5)
    label11 = Label(
        tri_root, text="Choose the eleventh point of the Triangle: ")
    e11 = Entry(tri_root, borderwidth=5)
    label12 = Label(tri_root, text="Choose the twelth point of the Triangle: ")
    e12 = Entry(tri_root, borderwidth=5)
    label13 = Label(
        tri_root, text="Always delete after you have entered in your numbers!")
    color = Entry(tri_root, borderwidth=5)
    en1.insert(0, "x1")
    e2.insert(0, "y1")
    e3.insert(0, "x2")
    e4.insert(0, "y2")
    e5.insert(0, "x1")
    e6.insert(0, "y1")
    e7.insert(0, "x2")
    e8.insert(0, "y2")
    e9.insert(0, "x1")
    e10.insert(0, "y1")
    e11.insert(0, "x2")
    e12.insert(0, "y2")
    color.insert(0, "Color")
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')

    def submit2():
        global count
        if 'canvas' in LAYERS_DICT:
            canvas = LAYERS_DICT['canvas']
        else:
            canvas = Canvas(root, height=root.winfo_screenheight(
            ), width=root.winfo_screenwidth(), background='white')
            LAYERS_DICT.update({'canvas': canvas})
            canvas.grid(row=13, column=1)
        current = en1.get()
        current2 = e2.get()
        current3 = e3.get()
        current4 = e4.get()
        current5 = e5.get()
        current6 = e6.get()
        current7 = e7.get()
        current8 = e8.get()
        current9 = e9.get()
        current10 = e10.get()
        current11 = e11.get()
        current12 = e12.get()
        colour = color.get()
        T = canvas.create_line(current, current2, current3, current4, current5, current6,
                               current7, current8, current9, current10, current11, current12, fill=colour)
        count += 1
        LAYERS_DICT.update({f'Triangle{count}': T})
        en1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e9.delete(0, END)
        e10.delete(0, END)
        e11.delete(0, END)
        e12.delete(0, END)
        if SAVED == False:
            root.title('Shape Editor • Unsaved')
        else:
            root.title(f'Shape Editor • {str(root.filename)} •')

    def Delete():
        label1.destroy()
        en1.destroy()
        label2.destroy()
        e2.destroy()
        label3.destroy()
        e3.destroy()
        label4.destroy()
        e4.destroy()
        label5.destroy()
        e5.destroy()
        label6.destroy()
        e6.destroy()
        label7.destroy()
        label8.destroy()
        label9.destroy()
        label10.destroy()
        label11.destroy()
        label12.destroy()
        e7.destroy()
        e8.destroy()
        e9.destroy()
        e10.destroy()
        e11.destroy()
        e12.destroy()
        but2.destroy()
        color.destroy()
        delete_button.destroy()
        label13.destroy()
        tri_root.destroy()
    but2 = Button(tri_root, text="Submit", command=submit2)
    delete_button = Button(tri_root, text="Delete", command=Delete)
    label13.grid(row=13, column=0)
    label1.grid(row=0, column=0)
    en1.grid(row=0, column=1)
    label2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    label3.grid(row=2, column=0)
    e3.grid(row=2, column=1)
    label4.grid(row=3, column=0)
    e4.grid(row=3, column=1)
    label5.grid(row=4, column=0)
    e5.grid(row=4, column=1)
    label6.grid(row=5, column=0)
    e6.grid(row=5, column=1)
    label7.grid(row=6, column=0)
    e7.grid(row=6, column=1)
    label8.grid(row=7, column=0)
    e8.grid(row=7, column=1)
    label9.grid(row=8, column=0)
    e9.grid(row=8, column=1)
    label10.grid(row=9, column=0)
    e10.grid(row=9, column=1)
    label11.grid(row=10, column=0)
    e11.grid(row=10, column=1)
    label12.grid(row=11, column=0)
    e12.grid(row=11, column=1)
    color.grid(row=12, column=0)
    but2.grid(row=12, column=1)
    delete_button.grid(row=12, column=2)


def delete_all():
    global LAYERS_DICT
    LAYERS_DICT['canvas'].destroy()
    LAYERS_DICT = {}
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def clear_canvas():
    global LAYERS_DICT
    LAYERS_DICT['canvas'].delete("all")
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def shortcut(event):
    make_Square()


def shortcut2(event):
    make_Circle()


def shortcut3(event):
    make_Triangle()


def shortcut4(event):
    delete_all()


def shortcut5(event):
    make_Line()


def shortcut6(event):
    Open_Image()


def shortcut7(event):
    Save_Canvas()


def shortcut8(event):
    grab_clipboard()


def shortcut9(event):
    clear_canvas()


def shortcut10(event):
    New_Canvas()


def shortcut11(event):
    Arc()


def shortcut12(event):
    make_Text()


def shortcut13(event):
    undo()


def shortcut14(event):
    save_as()


def Free_Draw():
    global image1
    image1 = Image.new('RGB', (root.winfo_screenwidth(),
                               root.winfo_screenheight()), 'white')
    draw = ImageDraw.Draw(image1)

    def activate_paint(e):
        global lastx, lasty
        LAYERS_DICT['canvas'].bind('<B1-Motion>', paint)
        lastx, lasty = e.x, e.y

    def paint(e):
        global lastx, lasty, count
        x, y = e.x, e.y
        mark = LAYERS_DICT['canvas'].create_line((lastx, lasty, x, y), width=2)
        #  --- PIL
        draw.line((lastx, lasty, x, y), fill='black', width=1)
        LAYERS_DICT.update({f'mark{count}': mark})
        count += 1
        lastx, lasty = x, y
    LAYERS_DICT['canvas'].bind('<1>', activate_paint)
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def smile():
    part1 = LAYERS_DICT['canvas'].create_oval(0, 0, 500, 500, fill='yellow')
    part2 = LAYERS_DICT['canvas'].create_oval(373, 94, 403, 127, fill='black')
    part3 = LAYERS_DICT['canvas'].create_oval(117, 94, 147, 127, fill='black')
    part4 = LAYERS_DICT['canvas'].create_line(111, 270, 211, 362, fill='black')
    part5 = LAYERS_DICT['canvas'].create_line(211, 362, 345, 362, fill='black')
    part6 = LAYERS_DICT['canvas'].create_line(345, 362, 448, 270, fill='black')
    LAYERS_DICT.update({'smile': [part1, part2, part3, part4, part5, part6]})
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def New_Canvas():
    global canvas
    canvas = Canvas(root, height=root.winfo_screenheight(),
                    width=root.winfo_screenwidth(), background='white')
    LAYERS_DICT.update({'canvas': canvas})
    canvas.grid(row=13, column=1)
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def ground():
    g = canvas.create_rectangle(
        0, 370, root.winfo_screenwidth(), root.winfo_screenheight(), fill='green')
    LAYERS_DICT.update({'ground': g})
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def erase():
    def eraser(event):
        LAYERS_DICT['canvas'].delete('all')
    LAYERS_DICT['canvas'].bind('<Button-1>', eraser)
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def coords_find():
    global can
    coords = Tk()
    coords.title('Coordinate Finder')
    can = Canvas(coords, height=500, width=500)
    can.configure(background='black')
    can.grid(row=12, column=1)

    def find(event):
        global label, labely
        x = event.x
        y = event.y
        can.create_rectangle(x, y, x+10, y+10, fill='magenta')
        label = can.create_text(x, y+10, text="x: " + str(x), fill="yellow")
        labely = can.create_text(x, y+20, text="y: " + str(y), fill="yellow")
    can.bind("<Button-1>", find)


def doc():
    Doc_Root = Tk()
    Doc_Root.title("Notes")
    text = Text(Doc_Root, width=50, height=26, undo=True)
    scroll = Scrollbar(Doc_Root, command=text.yview)
    text.config(yscrollcommand=scroll.set)
    text.grid(row=0, column=0)
    scroll.grid(row=0, column=1)


def save_as():
    global SAVED
    x = LAYERS_DICT['canvas'].winfo_y()+LAYERS_DICT['canvas'].winfo_rootx()
    y = LAYERS_DICT['canvas'].winfo_x()+LAYERS_DICT['canvas'].winfo_rooty()
    x1 = x+root.winfo_width()
    y1 = y+root.winfo_height()
    root.filename = filedialog.asksaveasfilename(initialfile='.jpg', title='Save As', filetypes=(
        ('JPG image', '*.jpg'), ('PNG images', '*.png'), ('JPEG images', '*.jpeg'), ('All files', '*.*')), defaultextension='.jpg')
    ImageGrab.grab().crop((x, y, x1, y1)).save(str(root.filename))
    root.title(f'Shape Editor • {str(root.filename)}')


def Save_Canvas():
    global SAVED
    if SAVED == False:
        x = LAYERS_DICT['canvas'].winfo_y()+LAYERS_DICT['canvas'].winfo_rootx()
        y = LAYERS_DICT['canvas'].winfo_x()+LAYERS_DICT['canvas'].winfo_rooty()
        x1 = x+root.winfo_width()
        y1 = y+root.winfo_height()
        root.filename = filedialog.asksaveasfilename(initialfile='.jpg', title='Save As', filetypes=(
            ('JPG image', '*.jpg'), ('PNG images', '*.png'), ('JPEG images', '*.jpeg'), ('All files', '*.*')), defaultextension='.jpg')
        root.title(f'Shape Editor • {str(root.filename)}')
        # ImageGrab.grab().crop(()).save(root.filename)
        ImageGrab.grab(bbox=(x, y, x1, y1)).save(root.filename)
        SAVED = True
    elif SAVED == True:
        x = LAYERS_DICT['canvas'].winfo_y()+LAYERS_DICT['canvas'].winfo_rootx()
        y = LAYERS_DICT['canvas'].winfo_x()+LAYERS_DICT['canvas'].winfo_rooty()
        x1 = x+root.winfo_width()
        y1 = y+root.winfo_height()
        # ImageGrab.grab().crop((x, y, x1, y1)).save(str(root.filename))
        ImageGrab.grab(bbox=(x, y, x1, y1)).save(str(root.filename))
        root.title(f'Shape Editor • {str(root.filename)}')


def Open_Image():
    global img, SAVED
    root.filename = filedialog.askopenfilename()
    if root.filename:
        img = Image.open(root.filename)
        img = img.filter(ImageFilter.SHARPEN())
        img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
        LAYERS_DICT.update({'image': img})
        canvas.image_tk = ImageTk.PhotoImage(img)
        image_id = LAYERS_DICT['canvas'].create_image(0, 0, anchor="nw")
        LAYERS_DICT['canvas'].itemconfigure(image_id, image=canvas.image_tk)
        LAYERS_DICT.update({'img': image_id})
        root.title(f'Shape Editor • {str(root.filename)} •')
        SAVED = True


def PaintBucket():
    color = colorchooser.askcolor()
    canvas = LAYERS_DICT['canvas']
    bucket = canvas.create_rectangle(
        0, 0, root.winfo_screenwidth(), root.winfo_screenheight(), fill=color[1])
    LAYERS_DICT.update({'Background': bucket})
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def grab_clipboard():
    global clipboard_image
    clipboard_image = ImageGrab.grabclipboard()
    clipboard_image = clipboard_image.resize(
        (root.winfo_screenwidth(), root.winfo_screenheight()))
    canvas.tk_image = ImageTk.PhotoImage(clipboard_image)
    img_placement = canvas.create_image(0, 0, anchor="nw")
    canvas.itemconfigure(img_placement, image=canvas.tk_image)
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def select_and_crop():
    def place_item(event):
        global x3, y3
        if 'CIRCLE3' in Circles:
            LAYERS_DICT['canvas'].delete(Circles['CIRCLE3'])
        x3 = event.x
        y3 = event.y
        circle3 = LAYERS_DICT['canvas'].create_oval(
            x3, y3, x3+5, y3+5, fill='black')
        Circles.update({'CIRCLE3': circle3})

    def go(event):
        global clipboard_image, x1, y1, x2, y2, x3, y3
        try:
            img = LAYERS_DICT['image']
            img = img.resize(
                (root.winfo_screenwidth(), root.winfo_screenheight()))
            img = img.crop((x1, y1, x2, y2))
            canvas.image_tk = ImageTk.PhotoImage(img)
            image_place = LAYERS_DICT['canvas'].create_image(
                x3, y3, image=canvas.image_tk)
            LAYERS_DICT['canvas'].itemconfigure(
                image_place, image=canvas.image_tk)
            LAYERS_DICT['image'] = img
            LAYERS_DICT['img'] = image_place
            LAYERS_DICT['canvas'].delete(Circles['CIRCLE1'])
            LAYERS_DICT['canvas'].delete(Circles['CIRCLE2'])
            LAYERS_DICT['canvas'].delete(Circles['CIRCLE3'])
            LAYERS_DICT['canvas'].delete(OUTLINES['OUTLINE'])
            del Circles['CIRCLE1']
            del Circles['CIRCLE2']
        except NameError:
            pass
        try:
            clipboard_image = ImageGrab.grabclipboard()
            clipboard_img = clipboard_image.resize(
                (root.winfo_screenwidth(), root.winfo_screenheight()))
            cropped_image = clipboard_img.crop((x, y, x2, y2))
            overlappers = LAYERS_DICT['canvas'].find_overlapping(x, y, x2, y2)
            canvas.image_tk = ImageTk.PhotoImage(cropped_image)
            image_place = LAYERS_DICT['canvas'].create_image(
                x3, y3, image=canvas.image_tk)
            LAYERS_DICT['canvas'].itemconfigure(
                image_place, image=canvas.image_tk)
            LAYERS_DICT['image'] = cropped_image
            LAYERS_DICT['img'] = image_place
            LAYERS_DICT['canvas'].delete(Circles['CIRCLE1'])
            LAYERS_DICT['canvas'].delete(Circles['CIRCLE2'])
            LAYERS_DICT['canvas'].delete(OUTLINES['OUTLINE'])
            del Circles['CIRCLE1']
            del Circles['CIRCLE2']
        except Exception:
            pass
        if SAVED == False:
            root.title('Shape Editor • Unsaved')
        else:
            root.title(f'Shape Editor • {str(root.filename)} •')
    root.bind("<Return>", go)
    LAYERS_DICT['canvas'].bind("<Button-1>", start_pos)
    LAYERS_DICT['canvas'].bind("<Button-3>", end_pos)
    LAYERS_DICT['canvas'].bind("<Button-2>", place_item)


def resize_image():
    def place_item(event):
        global x3, y3
        if 'CIRCLE3' in Circles:
            LAYERS_DICT['canvas'].delete(Circles['CIRCLE3'])
        x3 = event.x
        y3 = event.y
        circle3 = LAYERS_DICT['canvas'].create_oval(
            x3, y3, x3+5, y3+5, fill='black')
        Circles.update({'CIRCLE3': circle3})

    def go(event):
        global x1, y1, x2, y2, x3, y3
        img = LAYERS_DICT['image']
        img = img.resize((x1, y2))
        canvas.image_tk = ImageTk.PhotoImage(img)
        image_id = LAYERS_DICT['canvas'].create_image(
            x3, y3, image=canvas.image_tk)
        LAYERS_DICT['canvas'].itemconfigure(image_id, image=canvas.image_tk)
        LAYERS_DICT['image'] = img
        LAYERS_DICT['img'] = image_id
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE1'])
        LAYERS_DICT['canvas'].delete(Circles['CIRCLE2'])
        LAYERS_DICT['canvas'].delete(OUTLINES['OUTLINE'])
        del Circles['CIRCLE1']
        del Circles['CIRCLE2']
        if SAVED == False:
            root.title('Shape Editor • Unsaved')
        else:
            root.title(f'Shape Editor • {str(root.filename)} •')
    root.bind("<Return>", go)
    LAYERS_DICT['canvas'].bind("<Button-1>", start_pos)
    LAYERS_DICT['canvas'].bind("<Button-3>", end_pos)
    LAYERS_DICT['canvas'].bind("<Button-2>", place_item)


def find():
    global clipboard_image
    try:
        img = LAYERS_DICT['image']
        img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
        img = img.filter(ImageFilter.FIND_EDGES())
        canvas.image_tk = ImageTk.PhotoImage(img)
        image_id = LAYERS_DICT['canvas'].create_image(0, 0, anchor=NW)
        LAYERS_DICT['canvas'].itemconfigure(image_id, image=canvas.image_tk)
        LAYERS_DICT['image'] = img
        LAYERS_DICT['img'] = image_id
    except NameError:
        pass
    try:
        clipboard_image = ImageGrab.grabclipboard()
        clipboard_image = clipboard_image.resize(
            (root.winfo_screenwidth(), root.winfo_screenheight()))
        clipboard_image = clipboard_image.filter(ImageFilter.FIND_EDGES())
        canvas.image_tk = ImageTk.PhotoImage(clipboard_image)
        image_id = LAYERS_DICT['canvas'].create_image(0, 0, anchor=NW)
        LAYERS_DICT['canvas'].itemconfigure(image_id, image=canvas.image_tk)
        LAYERS_DICT['image'] = clipboard_image
        LAYERS_DICT['img'] = image_id
    except Exception:
        pass
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def emboss():
    global clipboard_image
    try:
        img = LAYERS_DICT['canvas']
        img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
        img = img.filter(ImageFilter.EMBOSS())
        canvas.image_tk = ImageTk.PhotoImage(img)
        image_id = LAYERS_DICT['canvas'].create_image(0, 0, anchor=NW)
        LAYERS_DICT['canvas'].itemconfigure(image_id, image=canvas.image_tk)
        LAYERS_DICT['image'] = img
        LAYERS_DICT['img'] = image_id
    except:
        pass
    try:
        clipboard_image = ImageGrab.grabclipboard()
        clipboard_image = clipboard_image.resize(
            (root.winfo_screenwidth(), root.winfo_screenheight()))
        clipboard_image = clipboard_image.filter(ImageFilter.EMBOSS())
        canvas.image_tk = ImageTk.PhotoImage(clipboard_image)
        image_id = LAYERS_DICT['canvas'].create_image(0, 0, anchor=NW)
        LAYERS_DICT['canvas'].itemconfigure(image_id, image=canvas.image_tk)
        LAYERS_DICT['image'] = clipboard_image
        LAYERS_DICT['img'] = image_id
    except:
        pass
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def lioi():
    global clipboard_image
    img = LAYERS_DICT['img']
    clipboard_image = ImageGrab.grabclipboard()
    clipboard_image = clipboard_image.resize(
        (root.winfo_screenwidth(), root.winfo_screenheight()))
    img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    mask = Image.new("L", img.size, 128)
    im = Image.composite(clipboard_image, img, mask)
    canvas.image_tk = ImageTk.PhotoImage(im)
    image_id = LAYERS_DICT['canvas'].create_image(0, 0, anchor=NW)
    LAYERS_DICT['canvas'].itemconfigure(image_id, image=canvas.image_tk)
    LAYERS_DICT['image'] = clipboard_image
    LAYERS_DICT['img'] = image_id
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


def without_color():
    global clipboard_image
    try:
        img = LAYERS_DICT['image']
        img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
        img = img.filter(ImageFilter.CONTOUR())
        canvas.image_tk = ImageTk.PhotoImage(img)
        image_id = LAYERS_DICT['canvas'].create_image(0, 0, anchor=NW)
        LAYERS_DICT['canvas'].itemconfigure(image_id, image=canvas.image_tk)
        LAYERS_DICT['image'] = img
        LAYERS_DICT['img'] = image_id
    except:
        pass
    try:
        clipboard_image = ImageGrab.grabclipboard()
        clipboard_image = clipboard_image.resize(
            (root.winfo_screenwidth(), root.winfo_screenheight()))
        clipboard_image = clipboard_image.filter(ImageFilter.CONTOUR())
        canvas.image_tk = ImageTk.PhotoImage(clipboard_image)
        image_id = LAYERS_DICT['canvas'].create_image(0, 0, anchor=NW)
        f = LAYERS_DICT['canvas'].itemconfigure(
            image_id, image=canvas.image_tk)
        LAYERS_DICT['image'] = clipboard_image
        LAYERS_DICT['img'] = image_id
    except:
        pass
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')

# def animation():
#     global count
#     if len(LAYERS_DICT) != 1:
        
#         animation_undo()
#         root.after(100, animation)
# def hide():
#     canvas.itemconfigure(LAYERS_DICT[list(LAYERS_DICT.keys())[1]], state='hidden')
# def animation_undo():
#     global count
#     # try:
#     if len(LAYERS_DICT) == 1:
#         return None
#     else:
#         LAYERS_DICT['canvas'].delete(LAYERS_DICT[list(LAYERS_DICT.keys())[1]])
#         # canvas.itemconfigure(LAYERS_DICT[list(LAYERS_DICT.keys())[1]], state='normal'/'hidden')
#         # count += 1
#         # canvas.update()
#         # LAYERS_DICT['canvas'].delete(LAYERS_DICT[list(LAYERS_DICT.keys())[1]])
#         # del LAYERS_DICT[list(LAYERS_DICT.keys())[1]]
#     # except Exception:
#     #     messagebox.showerror('ERROR', 'NOTHING LEFT TO UNDO!')
#     if SAVED == False:
#         root.title('Shape Editor • Unsaved')
#     else:
#         root.title(f'Shape Editor • {str(root.filename)} •')

def undo():
    global count
    try:
        if len(LAYERS_DICT) == 1:
            LAYERS_DICT['canvas'].destroy()
            del LAYERS_DICT['canvas']
        else:
            count += 1
            LAYERS_DICT['canvas'].delete(
                LAYERS_DICT[list(LAYERS_DICT.keys())[-1]])
            del LAYERS_DICT[list(LAYERS_DICT.keys())[-1]]
    except Exception:
        messagebox.showerror('ERROR', 'NOTHING LEFT TO UNDO!')
    if SAVED == False:
        root.title('Shape Editor • Unsaved')
    else:
        root.title(f'Shape Editor • {str(root.filename)} •')


# def add_keyframe():
#     print(list(LAYERS_DICT.items())[-1])
#     lay_dict = dict(list(LAYERS_DICT.items())[-1])
#     lay_dict(list(LAYERS_DICT.items())[-1]).
#     # LAYERS_DICT[list(LAYERS_DICT.keys())[-1]], state='hidden')
root.title("Shape Editor")
menubar = Menu(root)
CommandMenu = Menu(menubar, tearoff=0)
CommandMenu.add_command(label="Square     Alt+S", command=make_Square)
CommandMenu.add_command(label="Circle     Ctrl+Alt+C", command=make_Circle)
CommandMenu.add_command(label="Line       Ctrl+L", command=make_Line)
CommandMenu.add_command(label="Text       Ctrl+Alt+T", command=make_Text)
CommandMenu.add_command(label="Arc        Ctrl+A", command=Arc)
CommandMenu.add_command(label="Triangle   Ctrl+T", command=make_Triangle)
CommandMenu.add_separator()
CommandMenu.add_command(label="Delete Canvas    Ctrl+D", command=delete_all)
CommandMenu.add_separator()
CommandMenu.add_command(label="Clear Items      Ctrl+K", command=clear_canvas)
CommandMenu.add_command(label='Undo    Ctrl+Z', command=undo)
CommandMenu.add_command(label="Paste    Ctrl+V", command=grab_clipboard)
CommandMenu.add_command(label="New Canvas     Ctrl+N", command=New_Canvas)
CommandMenu.add_separator()
CommandMenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="Commands", menu=CommandMenu)
# # ===========================================================================
# AnimationMenu = Menu(menubar, tearoff=0)
# AnimationMenu.add_command(label='Add Keyframe', command=add_keyframe)
# AnimationMenu.add_command(label='Play Animation', command=animation)
# menubar.add_cascade(label='Animation', menu=AnimationMenu)
# # ===========================================================================
ViewMenu = Menu(menubar, tearoff=0)
submenu = Menu(ViewMenu, tearoff=0)
submenu.add_command(label="Smiley Face", command=smile)
ViewMenu.add_cascade(label="Templates", menu=submenu)
ViewMenu.add_separator()
ViewMenu.add_command(label="Ground", command=ground)
ViewMenu.add_separator()
ViewMenu.add_command(label="Document", command=doc)
menubar.add_cascade(label="View", menu=ViewMenu)
# ===========================================================================
EditMenu = Menu(menubar, tearoff=0)
EditMenu.add_command(label="Free Draw", command=Free_Draw)
EditMenu.add_separator()
EditMenu.add_command(label="Eraser", command=erase)
EditMenu.add_command(label="Coordinate Finder", command=coords_find)
EditMenu.add_command(label="Paint Bucket", command=PaintBucket)
EditMenu.add_separator()
EditMenu.add_command(label="Select and Crop", command=select_and_crop)
EditMenu.add_command(label="Resize", command=resize_image)
EditMenu.add_command(label="Find Edges", command=find)
EditMenu.add_command(label="Emboss Image", command=emboss)
EditMenu.add_command(label="Contour Image", command=without_color)
EditMenu.add_separator()
EditMenu.add_command(label="Mask Image on Image", command=lioi)
menubar.add_cascade(label="Edit", menu=EditMenu)
# =============================================================================
FileMenu = Menu(menubar, tearoff=0)
FileMenu.add_command(label="Open    Ctrl+O", command=Open_Image)
FileMenu.add_command(label="Save    Ctrl+S", command=Save_Canvas)
FileMenu.add_command(label="Save as    Ctrl+Alt+S", command=save_as)
menubar.add_cascade(label="File", menu=FileMenu)
root.configure(menu=menubar)
# =============================================================================
root.bind("<Alt-s>", shortcut)
root.bind("<Control-Alt-c>", shortcut2)
root.bind("<Control-t>", shortcut3)
root.bind("<Control-d>", shortcut4)
root.bind("<Control-l>", shortcut5)
root.bind("<Control-o>", shortcut6)
root.bind("<Control-s>", shortcut7)
root.bind("<Control-v>", shortcut8)
root.bind("<Control-k>", shortcut9)
root.bind("<Control-z>", shortcut13)
root.bind("<Control-Alt-t>", shortcut12)
root.bind("<Control-Alt-s>", shortcut14)
root.bind("<Control-n>", shortcut10)
root.bind("<Control-a>", shortcut11)
root.bind("<Escape>", escape)
root.protocol("WM_DELETE_WINDOW", Exit)
root.mainloop()
