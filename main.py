import tkinter
from random import shuffle

root = tkinter.Tk()
root.geometry("300x300")
root.title('Find the word !')


def test():

    mots =list(user_try.get())
    shuffle(mots)
    mots = "".join(mots)
    rematch = False
    if find.cget('text') == "Mélanger":
        word.config(text=mots)
        find.config(text='jouer')
        win.config(text=user_try.get())
        user_try.delete(0, tkinter.END)

    elif user_try.get() == win.cget('text'):
        word.config(text='Gagné !')
        rematch = True
    elif user_try.get() != win.cget('text'):
        word.config(text='Perdu : '+word.cget('text'))
        rematch = True
    if rematch:

        find.config(text="Mélanger")


word = tkinter.Label(root,
                     text="")
user_try = tkinter.Entry(root)
find = tkinter.Button(root,
                      text="Mélanger",
                      command=test)
win = tkinter.Label(root,
                    text="aaa")
word.pack()
user_try.pack()
find.pack()



root.mainloop()
