#importing the module
from tkinter import *
tk=Tk()
tk.title("CALCULATOR")
tk.configure(bg="light green")

#pressing function
def press(number):
	current=e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))

#clear function
def clear():
	e.delete(0,END)

#addition function
def add():
	first_num=e.get()
	global fnum
	global math
	math="addition"
	fnum=int(first_num)
	e.delete(0,END)

#minus function
def minus():
	first_num=e.get()
	global fnum
	global math
	math="minus"
	fnum=int(first_num)
	e.delete(0,END)

#multiply function
def multiply():
	first_num=e.get()
	global fnum
	global math
	math="multiply"
	fnum=int(first_num)
	e.delete(0,END)

#addition function
def divide():
	first_num=e.get()
	global fnum
	global math
	math="divide"
	fnum=int(first_num)
	e.delete(0,END)

#Square function
def square():
	first_num=e.get()
	global fnum
	global math
	math="square"
	fnum=int(first_num)
	e.delete(0,END)

#square root function
def square_root():
	first_num=e.get()
	global fnum
	global math
	math="square_root"
	fnum=float(first_num)
	e.delete(0,END)
#cube funciton
def cube():
	first_num=e.get()
	global fnum
	global math
	math="cube"
	fnum=int(first_num)
	e.delete(0,END)

#cube root function
def cube_root():
	first_num=e.get()
	global fnum
	global math
	math="cube_root"
	fnum=float(first_num)
	e.delete(0,END)

#custom_root
def custom_root():
	first_num=e.get()
	global fnum
	global math
	math="custom_root"
	fnum=float(first_num)
	e.delete(0,END)

def power():
	first_num=e.get()
	global fnum
	global math
	math="power"
	fnum=int(first_num)
	e.delete(0,END)

#equal function
def equal():
	sec_num=e.get()
	e.delete(0,END)
	if(math=="addition"):
		e.insert(0,fnum+int(sec_num))
	if(math=="minus"):
		e.insert(0,fnum-int(sec_num))
	if(math=="multiply"):
		e.insert(0,fnum*int(sec_num))
	if(math=="square"):
		e.insert(0,fnum*fnum)
	if(math=="square_root"):
		e.insert(0,fnum**0.5)
	if(math=="cube"):
		e.insert(0,fnum*fnum*fnum)
	if(math=="cube_root"):
		e.insert(0,(fnum**(1/3)))
	if(math=="custom_root"):
		e.insert(0,(fnum**(1/float(sec_num))))
	if(math=="power"):
		second_num=int(sec_num)
		e.insert(0,fnum**second_num)
	try:
		if(math=="divide"):
			e.insert(0,fnum/int(sec_num))
	except ZeroDivisionError:
		e.insert(0,"MATH ERROR:CAN'T DIVIDED BY ZERO")


#Value Entry TAB
e=Entry(tk,width=50,borderwidth=1)
e.grid(row=0,column=0,columnspan=3,padx=100,pady=10)

#Label creation

label=Label(tk,text="Numbers")
label.place(x=50,y=50)

#buttons 0-9
button_0=Button(text="0",fg="black",bg="red",command=lambda :press(0),height=3,width=10)
button_0.grid(row=1,column=0)

button_1=Button(text="1",fg="black",bg="red",command=lambda: press(1),height=3,width=10)
button_1.grid(row=1,column=1)

button_2=Button(text="2",fg="black",bg="red",command=lambda: press(2),height=3,width=10)
button_2.grid(row=1,column=2)

button_3=Button(text="3",fg="black",bg="red",command=lambda: press(3),height=3,width=10)
button_3.grid(row=2,column=0)

button_4=Button(text="4",fg="black",bg="red",command=lambda: press(4),height=3,width=10)
button_4.grid(row=2,column=1)

button_5=Button(text="5",fg="black",bg="red",command=lambda: press(5),height=3,width=10)
button_5.grid(row=2,column=2)

button_6=Button(text="6",fg="black",bg="red",command=lambda: press(6),height=3,width=10)
button_6.grid(row=3,column=0)

button_7=Button(text="7",fg="black",bg="red",command=lambda: press(7),height=3,width=10)
button_7.grid(row=3,column=1)

button_8=Button(text="8",fg="black",bg="red",command=lambda: press(8),height=3,width=10)
button_8.grid(row=3,column=2)

button_9=Button(text="9",fg="black",bg="red",command=lambda: press(9),height=3,width=10)
button_9.grid(row=4,column=0)



#button +-*/ and clear
button_m=Button(text="+",fg="black",bg="red",command=add,height=3,width=10)
button_m.grid(row=5,column=0)

button_m=Button(text="-",fg="black",bg="red",command=minus,height=3,width=10)
button_m.grid(row=5,column=1)

button_m=Button(text="x",fg="black",bg="red",command=multiply,height=3,width=10)
button_m.grid(row=5,column=2)

button_m=Button(text="/",fg="black",bg="red",command=divide,height=3,width=10)
button_m.grid(row=6,column=0)

button_m=Button(text="square",fg="black",bg="red",command=square,height=3,width=10)
button_m.grid(row=6,column=1)

button_m=Button(text="cube",fg="black",bg="red",command=cube,height=3,width=10)
button_m.grid(row=6,column=2)

button_m=Button(text="pow()",fg="black",bg="red",command=power,height=3,width=10)
button_m.grid(row=7,column=0)

button_m=Button(text="Square root",fg="black",bg="red",command=square_root,height=3,width=10)
button_m.grid(row=7,column=1)

button_m=Button(text="cube root",fg="black",bg="red",command=cube_root,height=3,width=10)
button_m.grid(row=7,column=2)

button_m=Button(text="custom root",fg="black",bg="red",command=custom_root,height=3,width=10)
button_m.grid(row=8,column=0)

button_m=Button(text="clear",fg="black",bg="Purple",command=clear,height=3,width=10)
button_m.grid(row=8,column=1)

button_m=Button(text="=",fg="black",bg="Yellow",command=equal,height=3,width=10)
button_m.grid(row=8,column=2)



tk.mainloop()





#audio driver for linux (jack)se