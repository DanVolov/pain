import tkinter as tk
from tkinter import colorchooser, Scale, filedialog, messagebox
from PIL import Image, ImageTk, ImageGrab

current_tool = 'pencil'
current_color = 'black'
brush_size = 3
start_x, start_y = None, None
eraser_size = 3
current_file = None
temp_item = None
copy_content = None
copy_type = None

w = tk.Tk()
print()

def on_mousewheel(event):
    if event.delta > 0:
        zoom_in_(event)
    else:
        zoom_out_(event)

#w.geometry('800x600')
w.title('Paint')

toolbar = tk.Frame(w)
toolbar.pack(fill='x', padx=10, pady=10)
def clear_canvas():
    print(1)
    if canvas.find_all():
        canvas.delete('all')

def set_eraser_size(value):
    global eraser_size
    eraser_size = int(value)


def set_tool(a):
    global current_tool
    current_tool = a

def set_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

def set_brush_size(value):
    global brush_size
    brush_size = int(value)

tk.Button(toolbar, text='Карандаш', command=lambda: set_tool('pencil')).pack(side=tk.LEFT, padx=2)
tk.Button(toolbar, text='Кисть', command=lambda: set_tool('brush')).pack(side=tk.LEFT, padx=2)

tk.Button(toolbar, text='Ластик', command=lambda: set_tool('eraser')).pack(side=tk.LEFT, padx=2)

tk.Button(toolbar, text='Линия', command=lambda: set_tool('line')).pack(side=tk.LEFT, padx=2)

tk.Button(toolbar, text='Прмоугольник', command=lambda: set_tool('rectangle')).pack(side=tk.LEFT, padx=2)

tk.Button(toolbar, text='Овал', command=lambda: set_tool('oval')).pack(side=tk.LEFT, padx=2)

tk.Button(toolbar, text='Цвет', command=lambda: set_color()).pack(side=tk.LEFT, padx=2)

size_frame = tk.Frame(toolbar)
size_frame.pack(side=tk.LEFT, padx=10)
tk.Label(size_frame, text='Размер кисти').grid(row=0, column=0)

brush_scale = Scale(size_frame, from_=0, to=20, orient=tk.HORIZONTAL, command=set_brush_size, length=100)
brush_scale.set(brush_size)
brush_scale.grid(row=1,column=0)

tk.Label(size_frame, text='Размер астика').grid(row=0, column=1)
eraser_scale = Scale(size_frame, from_=0, to=20, orient=tk.HORIZONTAL, command=set_eraser_size, length=100)
eraser_scale.set(eraser_size)
eraser_scale.grid(row=1,column=1)


control_frame = tk.Frame(toolbar)
control_frame.pack(side=tk.RIGHT, padx=10)

tk.Button(control_frame, text='Очистить', command=lambda: clear_canvas()).pack(side=tk.LEFT, padx=2)
tk.Button(control_frame, text='Сохранить', command=lambda: save()).pack(side=tk.LEFT, padx=2)

canvas_frame = tk.Frame(w)
canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
canvas = tk.Canvas(canvas_frame, bg='white', cursor='crosshair')
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind('<Button-4>', lambda e: zoom_in())
canvas.bind('<Button-5>', lambda e: zoom_out())

def start_draw(event):
    #canvas.create_oval()
    global start_x, start_y, current_tool, current_color, temp_item
    start_x, start_y = event.x, event.y
    if current_tool in ['pencil', 'brush', 'eraser']:
        if current_tool == 'eraser':
            color = 'white'
        else:
            color = current_color
        if current_tool == 'eraser':
            size = eraser_size
        else:
            size = brush_size
        canvas.create_line(event.x, event.y, event.x+1, event.y+1,width=size,fill=color, capstyle=tk.ROUND)
    elif current_tool in ['line', 'rectangle', 'oval']:
        color = current_color
        width = brush_size
        if current_tool == 'line':
            temp_item = canvas.create_line(start_x,start_y, event.x, event.y, width=width, fill=color)
        elif current_tool == 'oval':
            temp_item = canvas.create_oval(start_x, start_y, event.x, event.y, width=width, fill=color)
        elif current_tool == 'rectangle':

            temp_item = canvas.create_rectangle(start_x, start_y, event.x, event.y, width=width, fill=color)



def draw(event):
    global temp_item, start_x, start_y
    if current_tool in ['pencil', 'brush', 'eraser']:
        if current_tool == 'eraser':
            color = 'white'
        else:
            color = current_color
        if current_tool == 'eraser':
            size = eraser_size
        else:
            size = brush_size

        canvas.create_line(start_x, start_y, event.x, event.y,width=size,fill=color)
        start_x, start_y = event.x, event.y
    elif current_tool in ['line', 'rectangle', 'oval'] and temp_item:
        if current_tool == 'line':
            canvas.coords(temp_item, start_x, start_y, event.x, event.y)
        elif current_tool == 'oval':
            canvas.coords(temp_item, start_x, start_y, event.x, event.y)
        elif current_tool == 'rectangle':
            canvas.coords(temp_item, start_x, start_y, event.x, event.y)




def end_draw(event):
    global  start_x, start_y, temp_item
    temp_item = None
    start_x, start_y = None, None

#добавить меню
#Функции
#file_menu
def new():
    global current_file
    canvas_items = canvas.find_all()
    if canvas_items and not current_file:
        result = messagebox.askyesnocancel('Сохранение', 'Сохранить файл перед созданием нового?')
        if result is True:
            old_current_file = current_file
            save_as()
            if current_file != old_current_file and current_file:
                canvas.delete('all')
                current_file = None
                w.title('Paint')
        elif result is False:
            canvas.delete('all')
            current_file = None
            w.title('Paint')
    else:
        canvas.delete('all')
        current_file = None
        w.title('Paint')

def open_file():
    global current_file
    filename = filedialog.askopenfilename(
        defaultextension='.png',
        filetypes=[('PNG files', '*.png'), ('JPEG files', '*.jpg'), ('All files', '*.*')]
    )
    if filename:
        try:
            image = Image.open(filename)
            canvas.delete('all')
            canvas.image = ImageTk.PhotoImage(image)
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()
            if canvas_width <= 1:
                canvas_width = image.width
            if canvas_height <= 1:
                canvas_height = image.height
            canvas.create_image(0, 0, anchor=tk.NW, image=canvas.image)
            current_file = filename
            w.title(f'Paint - {filename}')
        except Exception as e:
            messagebox.showerror('Ошибка', f'Не удалось открыть файл:\n{e}')

def save():
    global current_file
    if current_file:
        try:
            x = w.winfo_rootx() + canvas.winfo_x()
            y = w.winfo_rooty() + canvas.winfo_y()
            x1 = x + canvas.winfo_width()
            y1 = y + canvas.winfo_height()

            screen = ImageGrab.grab(bbox=(x, y, x1, y1))
            screen.save(current_file)
            messagebox.showinfo('Success', f'Файл сохранен {current_file}')
        except Exception as e:
            messagebox.showerror('Error', f'Не удалось сохранить файл: {e}')
    else:
        save_as()


def save_as():
    global current_file
    filename = filedialog.asksaveasfilename(
        defaultextension='.png',
        filetypes=[('PNG files', '*.png'),('JPEG files', '*.jpg')]
    )
    if filename:
        try:
            x = w.winfo_rootx() + canvas_frame.winfo_x() + canvas.winfo_x()
            y = w.winfo_rooty() + canvas_frame.winfo_y() +  canvas.winfo_y()
            x1 = x + canvas.winfo_width()
            y1 = y + canvas.winfo_height()

            screen = ImageGrab.grab(bbox=(x, y, x1, y1))
            screen.save(filename)
            current_file = filename
            messagebox.showinfo('Success', f'Файл сохранен {current_file}')
        except Exception as e:
            messagebox.showerror('Error', f'Не удалось сохранить файл: {e}')


def exit_window():
    w.destroy()

#edit_menu
def cancel():
    pass
def cut():
    canvas.delete('all')

def copy():
    global copy_type, copy_content
    sel_items = canvas.find_all()
    if sel_items:
        messagebox.showinfo('Copy', 'Нет элементов для копирования')
        return
    copy_content = []
    for i in sel_items:
        item = {
            'type': canvas.type(i),
            'coords': canvas.coords(i),
            'color': canvas.itemcget(i, 'fill'),
            'width': canvas.itemcget(i, 'width')
        }
        copy_content.append(item)
    copy_type = 'elements'
    messagebox.showinfo('Copy','Copy successful')

def paste():
    pass

#zoom_menu
def zoom_in():
    print(11)
    canvas.scale('all', 0, 0, 1.2, 1.2)
def zoom_in_(event):
    canvas.scale('all', 0, 0, 1.2, 1.2)
def zoom_out():
    canvas.scale('all', 0, 0, 0.8, 0.8)
def zoom_out_(event):
    canvas.scale('all', 0, 0, 0.8, 0.8)
def restore_zoom():
    pass

#menubar
main_menu = tk.Menu(w)

#file_menu
file_menu = tk.Menu(tearoff=0)
file_menu.add_command(label='New', command=new)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_window)

#edit_menu
edit_menu = tk.Menu(tearoff=0)
edit_menu.add_command(label="Cancel", command=cancel)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

#zoom_menu in view_menu
zoom_menu = tk.Menu(tearoff=0)
zoom_menu.add_command(label="Zoom in", command=zoom_in)
zoom_menu.add_command(label="Zoom out", command=zoom_out)
zoom_menu.add_command(label="Restore default zoom", command=restore_zoom)

#view_menu
view_menu = tk.Menu(tearoff=0)
view_menu.add_cascade(label="Zoom", menu=zoom_menu)

#menu
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_cascade(label="View", menu=view_menu)

w.config(menu=main_menu)


canvas.bind('<Button-1>', start_draw)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease>', end_draw)
canvas.bind('<MouseWheel>', on_mousewheel)



status_label = tk.Label(w, text='', bg='white')
status_label.pack(fill=tk.X)


w.mainloop()