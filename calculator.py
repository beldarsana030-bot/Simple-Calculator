import tkinter as tk
window=tk.Tk()
window.title("Simple Calculator")
window.geometry("350x350+500+150")
window.resizable(False,False)
entry=tk.Entry(window,font=('Arial',20),borderwidth=3,justify='right',relief='sunken')

def press(button_value):
    current_text=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current_text + str(button_value))

def equal():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    except Exception:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")

def clear():
    entry.delete(0,tk.END)

def backspace():
    current_text=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current_text[:-1])

b1=tk.Button(window,text='1',width=10,height=3,command=lambda:press(1))
b2=tk.Button(window,text='2',width=10,height=3,command=lambda:press(2))
b3=tk.Button(window,text='3',width=10,height=3,command=lambda:press(3))
b4=tk.Button(window,text='4',width=10,height=3,command=lambda:press(4))
b5=tk.Button(window,text='5',width=10,height=3,command=lambda:press(5))
b6=tk.Button(window,text='6',width=10,height=3,command=lambda:press(6))
b7=tk.Button(window,text='7',width=10,height=3,command=lambda:press(7))
b8=tk.Button(window,text='8',width=10,height=3,command=lambda:press(8))
b9=tk.Button(window,text='9',width=10,height=3,command=lambda:press(9))
b0=tk.Button(window,text='0',width=10,height=3,command=lambda:press(0))
bback=tk.Button(window,text='backspace',width=10,height=3,command=backspace)

bplus=tk.Button(window,text='+',width=10,height=3,command=lambda:press('+'))
bminus=tk.Button(window,text='-',width=10,height=3,command=lambda:press('-'))
bmul=tk.Button(window,text='*',width=10,height=3,command=lambda:press('*'))
bdiv=tk.Button(window,text='/',width=10,height=3,command=lambda:press('/'))
bdot=tk.Button(window,text='.',width=10,height=3,command=lambda:press('.'))
bequal=tk.Button(window,text='=',width=10,height=3,command=equal)
bclear=tk.Button(window,text='C',width=20,height=5,command=clear)

entry.grid(row=1,column=0,columnspan=4)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
bplus.grid(row=2,column=3)

b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
bminus.grid(row=3,column=3)

b7.grid(row=4,column=0)
b8.grid(row=4,column=1)
b9.grid(row=4,column=2)
bmul.grid(row=4,column=3)

b0.grid(row=5,column=0)
bdot.grid(row=5,column=1)
bequal.grid(row=5,column=2)
bdiv.grid(row=5,column=3)
bclear.grid(row=6,column=0,columnspan=4)
bback.grid(row=6,column=0)

window.bind("<Return>",lambda event:equal())
window.bind("<Escape>",lambda event:clear())


window.mainloop()
























