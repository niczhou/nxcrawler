#coding = utf-8

import tkinter as tk

window = tk.Tk()
window.title('first')
window.geometry('520x346')

var=tk.StringVar()
var.set('start')

isClick=True

def click_yes():
##    print("button1 clicked")
    global isClick
    if isClick==False:
        isClick=True
        var.set('recovered')
    else:
        isClick=False
        var.set('clicked')
def printEvent(event):
    print('<Key>',event.keycode)

lb=tk.Label(window,bg='grey',text="Select",width=12,height=3)
lb.pack()

################################## menubar 
menubar=tk.Menu(window)

filemenu=tk.Menu(menubar,tearoff=0)
filemenu.add_command(label="file open",command=click_yes)
filemenu.add_command(label="file close",command=click_yes)
menubar.add_cascade(label='file',menu=filemenu)

menubar.add_command(label="option",command=click_yes)
##########################################
frame=tk.Frame(window,width=352,height=160,bg='pink')
frame.pack()

##bt=tk.Button(frame,bg='orange',text="click",command=click_yes)
##bt.pack()

listbox=tk.Listbox(frame,width=20)
listbox.pack(side=tk.LEFT)
languages=['java','python','javascript','php']
for la in languages:
    listbox.insert(tk.END,la)
listbox.pack()


window.bind('<Key>',printEvent)
window.config(menu=menubar)
window.mainloop()
