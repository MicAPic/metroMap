from tkinter import *
from tkinter import messagebox
from algorithm import Metro_Dijkstra
from PIL import Image, ImageTk
import init


def enter(e):
    if e.keycode == 2359309:  # keycode for enter on macos
        print(e.keycode)
        clicked()


def clicked():
    station = textbox.get()
    if station.isdigit() and 0 <= int(station) < init.N:
        stations.append(station)
    if len(stations) == 2:
        messagebox.showinfo('Кратчайший маршрут',
                            Metro_Dijkstra(init.N, int(stations[0]), int(stations[1]), init.routes))
        # textbox.configure(state='disabled')
        stations.clear()
    textbox.delete(0, END)
    textbox.insert(0, "")


stations = []
window = Tk()
window.title('Метро СПб')
window.geometry('595x692')
window.resizable(False, False)
window.bind('<Key>', enter)
icon = ImageTk.PhotoImage(Image.open('metro_icon.png'))  # source: commons.wikimedia.org
window.iconphoto(True, icon)

metro_map = ImageTk.PhotoImage(Image.open('metro_map.png'))  # source: metro-spb.ru
img = Label(window, image=metro_map)
img.image = metro_map
img.place(x=-5, y=-5)

prompt = Label(window, text='Выберите две станции по ID:')
prompt.grid(column=0, row=0, sticky='W')
textbox = Entry(window, width=10)
textbox.grid(column=0, row=1, sticky='W', padx='5', ipadx='42')
textbox.focus()
button = Button(window, text="Ввод", command=clicked)
button.grid(column=0, row=2, sticky='W', padx='5', ipadx='73')

window.mainloop()
