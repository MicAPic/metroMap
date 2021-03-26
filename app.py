from tkinter import *
from tkinter import messagebox
from algorithm import Metro_Dijkstra
from PIL import Image, ImageTk
import init


def enter(e):
    if e.keycode == 2359309:  # keycode for enter on macos
        clicked()


def clicked(*args):
    node = textbox.get()
    if node.isdigit() and 0 <= int(node) < init.N:
        stations.append(node)
    if len(stations) == 2:
        messagebox.showinfo('Кратчайший маршрут',
                            Metro_Dijkstra(init.N, int(stations[0]), int(stations[1]), init.routes))
        stations.clear()
    textbox.delete(0, END)
    textbox.insert(0, "")


def clicked_node(e=None, num=0):
    textbox.delete(0, END)
    textbox.insert(0, num)
    clicked()


def create_circle(x, y, r, num, color, canvas_name):
    transfer_half_list = [26, 43, 44, 50, 52, 64]
    if num in transfer_half_list:
        canvas_name.create_arc(x - r, y - r, x + r, y + r,
                               fill=f'{color}',
                               tags=f'c_{num}',
                               outline='white',
                               start=90,
                               extent=-180)
    elif num == 49:
        canvas_name.create_arc(x - r, y - r, x + r, y + r,
                               fill=f'{color}',
                               tags=f'c_{num}',
                               outline='white',
                               start=300,
                               extent=120)
    elif num == 65:
        canvas_name.create_arc(x - r, y - r, x + r, y + r,
                               fill=f'{color}',
                               tags=f'c_{num}',
                               outline='white',
                               start=60,
                               extent=120)
    else:
        canvas_name.create_oval(x - r, y - r, x + r, y + r,
                                fill=f'{color}',
                                outline='white',
                                tags=f'c_{num}',)
    canvas.tag_bind(f'c_{num}', '<Button>', lambda e: clicked_node(e, num))


stations = []
window = Tk()
window.title('Метро СПб')
window.geometry('595x692')
window.resizable(False, False)
window.bind('<Key>', enter)
icon = ImageTk.PhotoImage(Image.open('metro_icon.png'))  # source: commons.wikimedia.org
window.iconphoto(True, icon)

canvas = Canvas(window, width=600, height=697)
canvas.place(x=-5, y=-5)
metro_map = ImageTk.PhotoImage(Image.open('metro_map.png'))  # source: metro-spb.ru
img = canvas.create_image(301, 352, image=metro_map)

prompt = Label(window, text='Выберите две станции по ID\nили нажмите на них:', justify=LEFT)
prompt.grid(column=0, row=0, sticky='W')
textbox = Entry(window, width=10)
textbox.grid(column=0, row=1, sticky='W', padx='5', ipadx='42')
# textbox.focus()
button = Button(window, text="Ввод", command=clicked)
button.grid(column=0, row=2, sticky='W', padx='5', ipadx='73')

for station in init.Station.registry:
    if station.coordinates is not None:
        if station.transfer:
            radius = 9
        else:
            radius = 6
        create_circle(station.coordinates[0], station.coordinates[1], radius, station.id, station.line, canvas)

window.mainloop()
