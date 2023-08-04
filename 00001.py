from tkinter  import *
root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

label = Label(frame, text = "Hello world")
label.pack(padx = 4 , pady = 4)

button = Button(leftframe, text = "Button")
button.pack(padx = 3 , pady = 3  )

root.title("hi")
root.mainloop()


