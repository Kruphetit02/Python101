from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมตารางสอนนักเรียน')
GUI.geometry('1366x768')

# สร้าง Label สำหรับหัวข้อโปรแกรม
L1 =Label(GUI,text='โปรแกรมบันทึกตารางสอน ภาคเรียนที่ 2 ประจำปีการศึกษา 2565',font=('Angsana New',30),fg='green')
L1.place(x=380,y=20)

# สร้าง Button สำหรับแสดงตารางสอนของวันจันทร์
def Button1():
    text = text = 'คาบ 1 ฟิสิกส์ 1 ป.2/1 \nคาบ 2 ภาษาอังกฤษ ป.2/1 \nคาบ 3 สังคมศึกษา ป.2/1'
    messagebox.showinfo('วันจันทร์',text)

FB1=Frame(GUI)
FB1.place(x=120,y=100)
B1 = ttk.Button(FB1,text='วันจันทร์ ',command=Button1)
B1.pack(ipadx=150,ipady=20)


def Button2():
    text = 'คาบ 1 ฟิสิกส์ 1 ป.2/1 \nคาบ 2 ภาษาอังกฤษ ป.2/1 \nคาบ 3 สังคมศึกษา ป.2/1'
    messagebox.showinfo('วันอังคาร',text)

FB2=Frame(GUI)
FB2.place(x=120,y=220)
B2 = ttk.Button(FB2,text='วันอังคาร',command=Button2)
B2.pack(ipadx=150,ipady=20)

def Button3():
    text = 'คาบ 1 ฟิสิกส์ 1 ป.2/1 \nคาบ 2 ภาษาอังกฤษ ป.2/1  \nคาบ 4 ภาษาไทย ป.2/1 \nคาบ 5 สังคมศึกษา ป.2/1'
    messagebox.showinfo('วันพุธ',text)

FB3=Frame(GUI)
FB3.place(x=120,y=340)
B3 = ttk.Button(FB3,text='วันพุธ',command=Button3)
B3.pack(ipadx=150,ipady=20)

def Button4():
    text = 'คาบ 1 ฟิสิกส์ 1 ป.2/1 \nคาบ 2 ภาษาอังกฤษ ป.2/1 \nคาบ 3 สังคมศึกษา ป.2/1'
    messagebox.showinfo('วันพฤหัสบดี',text)

FB4=Frame(GUI)
FB4.place(x=120,y=460)
B4 = ttk.Button(FB4,text='วันพฤหัสบดี',command=Button4)
B4.pack(ipadx=150,ipady=20)

def Button5():
    text = 'คาบ 1 ฟิสิกส์ 1 ป.2/1 \nคาบ 2 ภาษาอังกฤษ ป.2/1 \nคาบ 3 สังคมศึกษา ป.2/1'
    messagebox.showinfo('วันศุกร์',text)

FB5=Frame(GUI)
FB5.place(x=120,y=580)
B5 = ttk.Button(FB5,text='วันศุกร์',command=Button5)
B5.pack(ipadx=150,ipady=20)

GUI.mainloop()

