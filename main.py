# made by ø
# import library
import tkinter
from random import shuffle

# create the windows
root = tkinter.Tk()
root.geometry("257x240")
root.title('Find the word !')


def play():
    # change the order of the letter in the word
    answer = list(user_try.get())
    shuffle(answer)
    answer = "".join(answer)
    rematch = False

    # for the start of the game
    if find.cget('text') == "Shuffle":
        word.config(text=answer)
        win.config(text=user_try.get())
        find.config(text='play')
        user_try.delete(0, tkinter.END)

    # see if the player have won or not
    elif (user_try.get()).lower() == win.cget('text').lower():
        word.config(text='Win !')
        rematch = True
    elif user_try.get() != win.cget('text'):
        word.config(text='Lost : '+win.cget('text'))
        rematch = True

    # restart the game
    if rematch:
        find.config(text="Shuffle")


def dim():
    print("*********Size of the window*********")
    print("width :", root.winfo_width())
    print("height :", root.winfo_height())
    print("******Coordinate of the window******")
    print("x :", root.winfo_x())
    print("y :", root.winfo_y())
    print("------------------------------------")


# create all the widget
word = tkinter.Label(root, text="")
user_try = tkinter.Entry(root)
find = tkinter.Button(root, text="Shuffle", command=play)
author = tkinter.Label(root, text="Made by ø")
get_dim = tkinter.Button(root, text="Get Dim", command=dim)

# it's the only way I find to save the answer, so it's normal if it's not show
win = tkinter.Label(root, text="")

# place all the widget (except "win")
# enable "get_dim" only if you want to modify some settings, if you don't it's just useless
pad = 3
word.pack(pady=pad)
user_try.pack(pady=pad)
find.pack(pady=pad)
# get_dim.pack(pady=20)
author.pack(side=tkinter.BOTTOM)


# show the windows
root.mainloop()
