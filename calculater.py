from tkinter import *

top = Tk()
top.title("Calculator")
top.minsize(250,250,)


numer1Label = Label(text = "First Number",fg='black' , bg='#4bbcfe')     #first text label
numer1Label.pack()                                                       #display the text
nuber1Entry = Entry(fg='red')                                            #first input
nuber1Entry.pack()                                                       #disply the input


numer2Label = Label(text = "Second Number" , bg='#4bbcfe')
numer2Label.pack()
nuber2Entry = Entry(fg='red')
nuber2Entry.pack()


def addNumber():                                                         #the function
    num1 = int(nuber1Entry.get())
    num2 = int(nuber2Entry.get())
    result = num1 + num2
    resultLabel = Label(text = "The result is "+str(result) , bg='#f06400')
    resultLabel.pack()



but = Button(text = "Add",command=addNumber,fg='black' , bg='#7aa300')
but.pack()


top.mainloop()
