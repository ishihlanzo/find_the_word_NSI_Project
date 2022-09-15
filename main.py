import tkinter
root = tkinter.Tk()
root.geometry("300x300")
root.title('Find the word !')


def test() :

    if word.cget('text') == "":
        word.config(text=user_try.get())
    else:
        if user_try.get() == word.cget('text') :
            win.config(text='Gagné')


word = tkinter.Label(root,
                     text="")
user_try = tkinter.Entry(root)
find = tkinter.Button(root,
                      text="Are you right ?",
                      command=test)
win = tkinter.Label(root,
                    text="")
word.pack()
user_try.pack()
find.pack()
win.pack()


root.mainloop()
