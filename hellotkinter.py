import tkinter as tk

window = tk.Tk()
window.title("Hallo")
window.geometry("512x512")
window.configure(bg="gray")

Frame = tk.Label(
    window,
    text="Hallo tkinter!", font = ('Calibri', 40, 'bold'),
    fg="yellow",
    bg="green"
)

Frame.pack(
    ipadx=100,
    ipady=10,
    expand=True
)

window.mainloop()