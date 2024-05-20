#за це я зможу закрити тему з фнформатики?
import random
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


den = {
    'День': ['Пон.', 'Вів.', 'Сер.', 'Чет.', 'Пят.', 'Суб.', 'Нед.'],
    'Температура': [11, 17, 14, 66, 8, -822, 666]
}
df = pd.DataFrame(den)

q = tk.Tk()
q.title("Температура 13.05-19.05. Поставте 12 будь ласка")

def zakrit():
    top = tk.Toplevel(q)
    top.title("Вихід")
    top.geometry("300x150")
    
    def xexexe(event):
        new_x = random.randint(0, top.winfo_width() - button.winfo_width())
        new_y = random.randint(0, top.winfo_height() - button.winfo_height())
        button.place(x=new_x, y=new_y)
    
    label = tk.Label(top, text="Ви дійсно йдете?")
    label.pack(pady=20)
    
    button = tk.Button(top, text="Випусти:(", command=q.destroy)
    button.place(x=100, y=70)
    button.bind("<Enter>", xexexe)
    
    cancel_button = tk.Button(top, text="Я залишусь", command=top.destroy)
    cancel_button.pack()

q.protocol("WM_DELETE_WINDOW", zakrit)

fig, ax = plt.subplots()
ax.plot(df['День'], df['Температура'], marker='o')
ax.set_title('Температура по дянм неділі')
ax.set_xlabel('День')
ax.set_ylabel('Температура (°C)')
ax.grid(True)

canvas = FigureCanvasTkAgg(fig, master=q)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

q.mainloop()