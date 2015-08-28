from tkinter import *
import sys
import lib_db_handle



def cre():
    res = obj.__creat__()
    mlabel2=Label(mGui, text=res).pack()
    return
def ins():
    bname = name.get()
    bauth = auth.get()
    bprice = price.get()
    obj.__insert__(bname,bauth,bprice)
    return
def dele():
    obj.__dele__()
    return
def sel():
    res = ''
    res = obj.__select__(res)
    print (res)
    mlabel2=Label(mGui, text=res).pack()
    return
def clo():
    exit()
    
obj = lib_db_handle.db_handler()
mGui = Tk()
name = StringVar()
auth = StringVar()
price = StringVar()
mGui.geometry('450x450')
mGui.title('library')
createtbtn = Button(mGui, text = 'Create_Table', command=cre).pack()
isertbtn = Button(mGui, text = 'INSERT', command=ins).pack()
deletebtn = Button(mGui, text = 'DELETE', command=dele).pack()
selectbtn = Button(mGui, text = 'SELECT', command=sel).pack()
closebtn= Button(mGui, text = 'CLOSE', command=clo).pack()

label_n = Label(mGui, text='name:').pack()
mName = Entry(mGui, textvariable=name).pack()
label_n = Label(mGui, text='author:').pack()
mAuth = Entry(mGui, textvariable=auth).pack()
label_n = Label(mGui, text='price:').pack()
mPrice = Entry(mGui, textvariable=price).pack()
