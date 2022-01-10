import tkinter as tk


root = tk.Tk()
root.title("Clicker")
root.geometry("200x200")
root.config(bg = "grey")
count = 0 
countLabel = tk.Label(root,text = count)

def colourChanges():
    global count
    if count > 0:
        root.configure(bg = "green")
    elif count < 0:
        root.configure(bg = "red")
    else:
        root.configure(bg = "grey")
        
def Up():
    global count
    count += 1
    countLabel.configure(text = count)
    colourChanges()

def Down():
    global count
    count -= 1
    countLabel.configure(text = count)
    colourChanges()

buttonUp = tk.Button(
    root,
    command = Up,
    text = "Up"    
)

buttonDown = tk.Button(
    root,
    command = Down,
    text = "Down"    
)

buttonUp.pack(
ipadx = 55, 
side = "top",
expand = True
)

countLabel.pack(
    ipadx = 60,
)       

buttonDown.pack(
    ipadx = 45,
    side = "bottom",
    expand = True
)

root.mainloop()