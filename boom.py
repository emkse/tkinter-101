import tkinter as tk
import time

window = tk.Tk()

colors = ["green", "yellow", "orange", "red", "black"]

Height = 50
Size = 100
x = 0

def changer():
    global x, Height, Size
    Height += 50
    Size += 50
    print(5-x)
    window.config(bg=colors[x])
    window.geometry(str(Height) + "x" + str(Size))
    x += 1

window.config(bg="White")
window.geometry("50x50")
print(6)
for y in range(1, 6):
    window.after(2000*y, changer)
def explode():
    time.sleep(1)
    print("Booooom!")
    window.destroy()
window.after(12000, explode)

window.mainloop()