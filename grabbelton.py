import tkinter
import random



#make the window
window = tkinter.Tk()
window.title("Grabbleton")
window.geometry("325x75")
window.config(bg = "white")

var = tkinter.StringVar()
prize = tkinter.StringVar()
y = True

#item
list1 = ["kaas", "tv", "batterij", "Switch", "PS5", "laptop", "XBOX", "controller", "aa batterij", "tafel"]
def prizes():
    global var
    x = len(list1)
    if x > 1:
        textVar = ("Er zijn nog "+str(x)+" prijzen")
    elif x == 1:
        textVar = ("Er is nog 1 prijs")
    else:
        textVar = ("Er zijn geen prijzen meer")
        button.destroy()
        window.geometry("325x50")
    var.set(textVar)

#make the label
prizes()
label = tkinter.Label(
    window,
    bg = "white",
    fg = "black",
    textvariable = var
    )

def button_press():
    global y
    if y == True:
        reward = tkinter.Label(
            window,
            bg = "white",
            textvariable = prize
            )
        y = False
        reward.pack()
    rngPrize =random.choice(list1)
    prize.set("Gefeliciteerd, je hebt een " + rngPrize + " gegrabbeld!")
    list1.remove(rngPrize)
    prizes()



#make the button
button = tkinter.Button(
    window,
    text = "grabbelen",
    command = button_press
    )
label.pack()
button.pack()

window.mainloop()
