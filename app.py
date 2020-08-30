from tkinter import * 


root = Tk()
root.title('Text Editor')
# root.iconbitmap('icon.ico')
root.geometry('1200x600')

# create main frame
frame = Frame(root)
frame.pack(pady=5)

# create scrollbar for text
text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)

# create textbox
text = Text(frame, width=97, height=25, font=('Helvetica', 16), selectbackground='yellow', selectforeground='black',
            undo=True, yscrollcommand=text_scroll.set)
text.pack()

# configure scrollbar
text_scroll.config(command=text.yview)

root.mainloop()
