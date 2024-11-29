#!/usr/bin/python3
from hashlib import *
from tkinter import *
root = Tk()
root.geometry("400x520+1000+80")
root.configure(background="cyan")
root.title("Application")

#====================[Code]===========

entry1 = StringVar()
entry2 = StringVar()
def has():
    x = entry1.get()
    n = entry2.get()
    if n == 'md5':
        m = md5(x.encode()).hexdigest()
        ent3.insert(0.0,m)
    elif n == 'sha1':
        b = sha1(x.encode()).hexdigest()
        ent3.insert(0.0,b)
    elif n == 'sha224':
        v = sha224(x.encode()).hexdigest()
        ent3.insert(0.0,v)
    elif n == 'sha256':
        a = sha256(x.encode()).hexdigest()
        ent3.insert(0.0,a)
    elif n == 'sha384':
        o = sha384(x.encode()).hexdigest()
        ent3.insert(0.0,o)
    elif n == 'sha512':
        y = sha512(x.encode()).hexdigest()
        ent3.insert(0.0,y)
    else:
        ent3.insert(0.0,"Not Found")
        
#=================[Style]============    

l = Label(root,text="md5 ")
l.place(x=20,y=360)
l1 = Label(root,text="sha1 ")
l1.place(x=20, y=420)
l2 = Label(root,text="sha224 ")
l2.place(x=20, y=480)
l3 = Label(root,text="sha256 ")
l3.place(x=20, y=540)
l4 = Label(root,text="sha384")
l4.place(x=20, y=600)
l5 = Label(root,text="sha512")
l5.place(x=20, y=660)

l6 = Label(root,text="Enter The Text")
l6.place(x=10, y=860)

e = Entry(root,width=18,bd=5,font=("arial",12,"bold"),textvariable=entry1)
e.place(x=330 ,y=850)

l7 = Label(root,text="Enter The Type")
l7.place(x=10, y=1110)

e1 = Entry(root,width=10,bd=5,font=("arial",12,"bold"),textvariable=entry2)
e1.place(x=330 ,y=1100)

ent3 = Text(root,width=26,height=8,bd=5,font=("arial",12,"bold"))
ent3.place(x=50 ,y=1300)

b = Button(root,text="Enter",width=8,font=("arial",12,"bold"),bd=5,command=has)
b.place(x=130 ,y=2000)
root.mainloop()        
