import tkinter
root = tkinter.Tk()
root.geometry("300x300")
root.title('Find the word !')


def test():
    rematch = False
    if find.cget('text') == "Mélanger":
        word.config(text=user_try.get())
        user_try.delete(0, tkinter.END)
        find.config(text='jouer')

    elif user_try.get() == word.cget('text'):
        find.config(text='Gagné')
    elif user_try.get() != word.cget('text'):
        word.config(text='Perdu : '+word.cget('text'))
        rematch = True
    if rematch:
        user_try.delete(0, tkinter.END)
        find.config(text="Mélanger")


word = tkinter.Label(root,
                     text="")
user_try = tkinter.Entry(root)
find = tkinter.Button(root,
                      text="Mélanger",
                      command=test)
win = tkinter.Label(root,
                    text="")
word.pack()
user_try.pack()
find.pack()
win.pack()


root.mainloop()
