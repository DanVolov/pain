import tkinter as tk
from tkinter import colorchooser, Scale
from tkinter import ttk

current_tool = 'pencil'
current_color = 'black'
brush_size = 3
start_x, start_y = None, None
eraser_size = 3

w = tk.Tk()
#w.geometry('800x600')
w.title('Paint')

toolbar = tk.Frame(w)
toolbar.pack(fill='x', padx=10, pady=10)
def clear_canvas():
    pass

def save_canvas():
    pass
def set_eraser_size(vlue):
    pass
def set_tool(a):
    pass
def set_color():
    pass

def set_brush_size(value):
    pass
tk.Button(toolbar, text='Карандаш', command=lambda: set_tool('pencil')).pack(side=tk.LEFT, padx=2)
tk.Button(toolbar, text='Кисть', command=lambda: set_tool('brush')).pack(side=tk.LEFT, padx=2)

tk.Button(toolbar, text='Ластик', command=lambda: set_tool('eraser')).pack(side=tk.LEFT, padx=2)

tk.Button(toolbar, text='Линия', command=lambda: set_tool('line')).pack(side=tk.LEFT, padx=2)

tk.Button(toolbar, text='Прмоугольник', command=lambda: set_tool('rectangle')).pack(side=tk.LEFT, padx=2)

tk.Button(toolbar, text='Овал', command=lambda: set_tool('oval')).pack(side=tk.LEFT, padx=2)

tk.Button(toolbar, text='Цвет', command=lambda: set_color).pack(side=tk.LEFT, padx=2)

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

tk.Button(control_frame, text='Очистить', command=lambda: clear_canvas).pack(side=tk.LEFT, padx=2)
tk.Button(control_frame, text='Сохранить', command=lambda: save_canvas).pack(side=tk.LEFT, padx=2)

canvas_frame = tk.Frame(w)
canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
canvas = tk.Canvas(canvas_frame, bg='white', cursor='crosshair')
canvas.pack(fill=tk.BOTH, expand=True)
def start_draw(event):
    print(event.x, event.y)

def draw(event):
    print(event.x, event.y)

def end_draw(event):
    print(event.x, event.y)

#добавить меню
#Функции
#file_menu
def new():
    pass
def open_file():
    pass
def save():
    pass
def save_as():
    pass
def exit_window():
    w.destroy()

#edit_menu
def cancel():
    pass
def cut():
    pass
def copy():
    pass
def paste():
    pass

#zoom_menu
def zoom_in():
    pass
def zoom_out():
    pass
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


status_label = tk.Label(w, text='', bg='white')
status_label.pack(fill=tk.X)


w.mainloop()