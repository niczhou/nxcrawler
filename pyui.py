#coding = utf-8

import tkinter as tk

var_psw = tk.StringVar()
var_console = tk.StringVar()
  
    
def login_cancel():
    print("login canceled")
    et_user["bg"]="red"
    
top = tk.Tk()
top.title("nxstock")
top.geometry("560x328")

fr_login = tk.Frame(top,width=260,height=28)
fr_login.pack(side=tk.TOP,fill=tk.X)

bt_login = tk.Button(fr_login,text="login",font="Arial 8",width=8,height=1)
bt_login.pack(side=tk.RIGHT,padx=8)
et_psw = tk.Entry(fr_login,width=8,textvariable=var_psw)
et_psw.pack(side=tk.RIGHT,padx=6)
et_psw['show'] = '*'
lb_psw = tk.Label(fr_login,text="Password:",font="Arial 8",width=8)
lb_psw.pack(side=tk.RIGHT,padx=0)
et_user = tk.Entry(fr_login,width=8)
et_user.pack(side=tk.RIGHT,padx=6)
lb_user = tk.Label(fr_login,text="user:",font="Arial 8",width=8)
lb_user.pack(side=tk.RIGHT,padx=0)

fr_console = tk.Frame(top,width=260,height=36,bg="#B0C4DE")
fr_console.pack(side=tk.TOP,fill=tk.X)
lb_console = tk.Label(fr_console,textvariable=var_console)
lb_console.pack(side=tk.LEFT)

def login_confirm():
    print("login confirmed")
    var_console = et_user.get()

bt_login['command']='login_confirm'

##lb_psw = tk.Label(top,text="Password:",width=8,font="Arial 12",justify=tk.RIGHT)
##lb_psw.grid(row=2,column=0)
##
##et_user = tk.Entry(top)
##et_user.grid(row=1,column=1)
##et_user = tk.Entry(top)
##et_user.grid(row=2,column=1)
##
##var = tk.IntVar()
##cb_rem = tk.Checkbutton(top,text="remember username",variable=var)
##cb_rem.grid(row=3,column=1)
##

##    
##bt_login = tk.Button(top,text="confirm",command=login_confirm)
##bt_login.grid(row=4,column=0)
##bt_cancel = tk.Button(top,text="cancel",command=login_cancel)
##bt_cancel.grid(row=4,column=1)


top.mainloop()
