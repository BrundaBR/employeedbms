#hello there###################################################################################################################

#imports for the employee management system######################################################################################
import tkinter
from tkinter import *
import py_mysql_connector
import pymysql
import mysql.connector
import tkinter.messagebox
from PIL import ImageTk, Image
# basic root window features####################################################################################################
root=Tk()
root.title("EMPLOYEE MANAGEMENT SYSTEM")
root.iconbitmap("favicon.ico")
root.minsize(500,500)
f=Frame(root)
frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
frame4=Frame(root)
frame5=Frame(root)
frame6=Frame(root)
label1=Label(root,text="EMPLOYEE RECORD SYSTEM")
label1.config(font=('Italic',40,'bold'), justify=CENTER,fg="black", anchor="center")
label1.pack(fill=X)
#####################################declarations##############################################################################
fname=StringVar()
lname=StringVar()
ssn=StringVar()
salary=StringVar()
address=StringVar()
gender=StringVar()

dname=StringVar()
deptno=StringVar()
mgr_ssn=StringVar()
mgr_start_date=StringVar()

pname=StringVar()
pnumber=StringVar()
plocation=StringVar()


transaction_id=StringVar()
emp_salary_month=StringVar()
emp_salary_year=StringVar()







#image at center################################################################################################################
img = ImageTk.PhotoImage(Image.open("teamwork.png"))
panel=Label(root,image = img)
panel.pack(fill="both")
##################################FUNCTIONS#################################################################################
def update_id():
    db = mysql.connector.connect(
        username='root',
        password='12345',
        database='project')
    cur = db.cursor()
    r1 = (fname.get())
    f = r1.lower()
    r2 = (lname.get())
    ff = r2.lower()
    r3 = (ssn.get())
    fff = r3.lower()
    r4 = (address.get())
    ffff = r4.lower()
    r5 = (gender.get())
    g = r5.lower()
    r6 = (salary.get())
    g1 = r6.lower()
    r7 = (deptno.get())
    g3 = r7.lower()
    cur.execute("update employee_details set fname='"+r1+"',lname='"+r2+"',address='"+r4+"',gender='"+r5+"',salary='"+r6+"',dno='"+r7+"' where ssn='"+r3+"'")
    tkinter.messagebox.askokcancel("STATEOFOPERATION", 'UPDATED SUCESSFULLY!!!!YOHO')
    db.commit()
def update():
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame1.pack_forget()
    frame6.pack_forget()
    emp3 = Label(frame5, text="Enter first name of the employee: ", font=('times new roman', 20), bg="white",
                           fg="black")
    emp3.grid(row=1, column=1, padx=10)
    e123 = Entry(frame5, textvariable=fname)
    e123.grid(row=1, column=2, padx=10)
    e123.focus()

    emp_la= Label(frame5, text="Enter last name of the employee: ", bg="white", fg="black",
                          font=('times new roman', 20))
    emp_la.grid(row=4, column=1, padx=10)
    e245 = Entry(frame5, textvariable=lname)
    e245.grid(row=4, column=2, padx=10)

    emp_firs = Label(frame5, text="Enter the ssn:", bg="white", fg="black", font=('times new roman', 20))
    emp_firs.grid(row=6, column=1, padx=10)
    e124 = Entry(frame5, textvariable=ssn)
    e124.grid(row=6, column=2, padx=10)
    e124.focus()

    emp_first_nam = Label(frame5, text="Enter the address:", bg="white", fg="black", font=('times new roman', 20))
    emp_first_nam.grid(row=8, column=1, padx=10)
    e1= Entry(frame5, textvariable=address)
    e1.grid(row=8, column=2, padx=10)

    emp_first_= Label(frame5, text="Enter the gender:", bg="white", fg="black", font=('times new roman', 20))
    emp_first_.grid(row=10, column=1, padx=10)
    e13 = Entry(frame5, textvariable=gender)
    e13.grid(row=10, column=2, padx=10)
    e13.focus()

    emp_sa = Label(frame5, text="Enter the salary:", bg="white", fg="black", font=('times new roman', 20))
    emp_sa.grid(row=11, column=1, padx=10)
    e134 = Entry(frame5, textvariable=salary)
    e134.grid(row=11, column=2, padx=10)
    e134.focus()
    emp_ge = Label(frame5, text="Enter the department number:", bg="white", fg="black", font=('times new roman', 20))
    emp_ge.grid(row=12, column=1, padx=10)
    eg1 = Entry(frame5, textvariable=deptno)
    eg1.grid(row=12, column=2, padx=10)
    eg1.focus()
    butt= Button(frame5, text="UPDATE", width=30, height=2, command=update_id, font=('times new roman', 10))
    butt.grid(row=13, column=4)
    frame5.config(background="lavender")
    frame5.pack()

def delete_id():
    db = mysql.connector.connect(
        username='root',
        password='12345',
        database='project')
    cur = db.cursor()
    f1=ssn.get()
    cur.execute("delete from employee_details where ssn="+f1+";")
    db.commit()
    tkinter.messagebox.askokcancel("STATEOFOPERATION", 'DELETED A RECORD SUCESSFULLY!!!!')

def delete():
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame1.pack_forget()
    emp_1 = Label(frame6, text="Enter the ssn:", bg="white", fg="black", font=('times new roman', 20))
    emp_1.grid(row=5, column=1, padx=10)
    e11= Entry(frame6, textvariable=ssn)
    e11.grid(row=5, column=2, padx=10)
    e11.focus()
    button41 = Button(frame6, text="DELETE", width=20, height=2, command=delete_id, font=('times new roman', 20))
    button41.grid(row=10, column=2)
    frame6.configure(background="lavender")
    frame6.pack()




def add_entries():
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()


    emp_first_name = Label(frame1, text="Enter first name of the employee: ",font=('times new roman',20), bg="white", fg="black")
    emp_first_name.grid(row=1, column=1, padx=10)
    e1 = Entry(frame1, textvariable=fname)
    e1.grid(row=1, column=2, padx=10)
    e1.focus()

    emp_last_name = Label(frame1, text="Enter last name of the employee: ", bg="white", fg="black",font=('times new roman',20))
    emp_last_name.grid(row=4, column=1, padx=10)
    e2 = Entry(frame1, textvariable=lname)
    e2.grid(row=4, column=2, padx=10)

    emp_first_name1 = Label(frame1, text="Enter the ssn:", bg="white", fg="black",font=('times new roman',20))
    emp_first_name1.grid(row=6, column=1, padx=10)
    e12 = Entry(frame1, textvariable=ssn)
    e12.grid(row=6, column=2, padx=10)
    e12.focus()

    emp_first_name2 = Label(frame1, text="Enter the address:", bg="white", fg="black",font=('times new roman',20))
    emp_first_name2.grid(row=8, column=1, padx=10)
    e13 = Entry(frame1, textvariable=address)
    e13.grid(row=8, column=2, padx=10)

    emp_first_name3 = Label(frame1, text="Enter the gender:", bg="white", fg="black",font=('times new roman',20))
    emp_first_name3.grid(row=10, column=1, padx=10)
    e131 = Entry(frame1, textvariable=gender)
    e131.grid(row=10, column=2, padx=10)
    e131.focus()

    emp_sal= Label(frame1, text="Enter the salary:", bg="white", fg="black", font=('times new roman', 20))
    emp_sal.grid(row=11, column=1, padx=10)
    e = Entry(frame1, textvariable=salary)
    e.grid(row=11, column=2, padx=10)
    e.focus()
    emp_gen = Label(frame1, text="Enter the department number:", bg="white", fg="black", font=('times new roman', 20))
    emp_gen.grid(row=12, column=1, padx=10)
    eg = Entry(frame1, textvariable=deptno)
    eg.grid(row=12, column=2, padx=10)
    eg.focus()

    button21 = Button(frame1, text="ADD DEPARTMENT", width=30, height=2, command=dept_details, font=('times new roman', 10))
    button21.grid(row=13, column=0)
    buttop1 = Button(frame1, text="PAYROLL", width=30, height=2, command=pro, font=('times new roman', 10))
    buttop1.grid(row=13, column=1)

    button4 = Button(frame1, text="ADD THE EMPLOYEE",width=30,height=2, command=add_db,font=('times new roman',10))
    button4.grid(row=13, column=1)
    button41 = Button(frame1, text="DELETE", width=30, height=2, command=delete, font=('times new roman', 10))
    button41.grid(row=13, column=2)
    button51 = Button(frame1, text="EXIT", width=30, height=2, command=root.destroy, font=('times new roman', 10))
    button51.grid(row=13, column=3)
    button61 = Button(frame1, text="UPDATE", width=30, height=2, command=update, font=('times new roman', 10))
    button61.grid(row=13, column=4)

    frame1.configure(background="misty rose")
    frame1.pack(pady=10)
def add_db(*args):
    db=mysql.connector.connect(
        username='root',
        password='12345',
        database='project' )
    cur=db.cursor()
    f1=(fname.get())
    f=f1.lower()
    f2=(lname.get())
    ff=f2.lower()
    f3=(ssn.get())
    fff=f3.lower()
    f4=(address.get())
    ffff=f4.lower()
    f5=(gender.get())
    g=f5.lower()
    f6 = (salary.get())
    g1 = f5.lower()
    f7 = (deptno.get())
    g3 = f5.lower()
    #cur.execute("create table basic(employeename varchar(20),employeenamel varchar(20),employeedept varchar(20),salary varchar(20),designation varchar(20))")
    query = ("insert into employee_details(fname,lname,ssn,address,gender,salary,dno) values('"+(f1)+"','"+(f2)+"','"+(f3)+"','"+(f4)+"','"+(f5)+"','"+(f6)+"','"+(f7)+"')")
    cur.execute(query)

    db.commit()
    tkinter.messagebox.askokcancel("STATEOFOPERATION",'INSERTED SUCESSFULLY!!!!')
def dept_details():
    frame1.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()

    emp_dept = Label(frame2, text="ENTER DEPARTMENT: ", font=('times new roman', 20), bg="white",fg="black")
    emp_dept.grid(row=1, column=1, padx=10)
    dn = Entry(frame2, textvariable=dname)
    dn.grid(row=1, column=2, padx=10)
    dn.focus()

    dno = Label(frame2, text="ENTER DEPARTMENT NUMBER: ", bg="white", fg="black",font=('times new roman', 20))
    dno.grid(row=4, column=1, padx=10)
    d2 = Entry(frame2, textvariable=deptno)
    d2.grid(row=4, column=2, padx=10)

    mgs= Label(frame2, text="ENTER MANAGER SSN:", bg="white", fg="black", font=('times new roman', 20))
    mgs.grid(row=6, column=1, padx=10)
    mgrs = Entry(frame2, textvariable=mgr_ssn)
    mgrs.grid(row=6, column=2, padx=10)
    mgrs.focus()

    strd = Label(frame2, text="ENTER START DATE:", bg="white", fg="black", font=('times new roman', 20))
    strd.grid(row=8, column=1, padx=10)
    dat = Entry(frame2, textvariable=mgr_start_date)
    dat.grid(row=8, column=2, padx=10)


    button4e = Button(frame2, text="ADD DEPARTMENT", width=20, height=2, command=dept_add, font=('times new roman', 10))
    button4e.grid(row=12, column=2)

    button5 = Button(frame2, text="ADD EMPLOYEE", width=20, height=2, command=add_entries, font=('times new roman', 10))
    button5.grid(row=12, column=1)
    buttonn = Button(frame2, text="DELETE", width=30, height=2, command=delete, font=('times new roman', 10))
    buttonn.grid(row=12, column=0)
    butto = Button(frame2, text="EXIT", width=30, height=2, command=root.destroy, font=('times new roman', 10))
    butto.grid(row=12, column=3)
    buttop = Button(frame2, text="PAYROLL", width=30, height=2, command=pro, font=('times new roman', 10))
    buttop.grid(row=12, column=4)

    frame2.configure(background="misty rose")
    frame2.pack(pady=10)
def dept_add():
    db = mysql.connector.connect(
        username='root',
        password='12345',
        database='project')
    cur = db.cursor()

    d1 = (dname.get())
    dep = d1.lower()
    d2 = (deptno.get())
    dep2 = d2.lower()
    d3 = (mgr_ssn.get())
    dep3 = d3.lower()
    d4 = (mgr_start_date.get())
    dep4 = d4.lower()

    # cur.execute("create table basic(employeename varchar(20),employeenamel varchar(20),employeedept varchar(20),salary varchar(20),designation varchar(20))")
    query = ("insert into department_details(dname,dno,mgr_ssn,mgr_start_date) values('" + (d1) + "','" + (d2) + "','" + (d3) + "','" + (d4) + "')")
    cur.execute(query)
    db.commit()
    tkinter.messagebox.askokcancel("STATEOFOPERATION", 'INSERTED SUCESSFULLY!!!!')

def pro():
    frame2.pack_forget()
    frame1.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()




    pronam = Label(frame3, text="ENTER PROJECT NAME: ", font=('times new roman', 20), bg="white",fg="black")
    pronam.grid(row=1, column=1, padx=10)
    pr = Entry(frame3, textvariable=pname)
    pr.grid(row=1, column=2, padx=10)
    pr.focus()

    pno = Label(frame3, text="ENTER PROJECT NUMBER: ", bg="white", fg="black",
                font=('times new roman', 20))
    pno.grid(row=4, column=1, padx=10)
    pp = Entry(frame3, textvariable=pnumber)
    pp.grid(row=4, column=2, padx=10)

    loc = Label(frame3, text="ENTER PROJECT LOCATION:", bg="white", fg="black", font=('times new roman', 20))
    loc.grid(row=6, column=1, padx=10)
    plo= Entry(frame3, textvariable=plocation)
    plo.grid(row=6, column=2, padx=10)
    plo.focus()

    sdno = Label(frame3, text="DEPARTMENT NUMBER:", bg="white", fg="black", font=('times new roman', 20))
    sdno.grid(row=8, column=1, padx=10)
    dat1 = Entry(frame3, textvariable=deptno)
    dat1.grid(row=8, column=2, padx=10)

    prb= Button(frame3, text="ADD PROJECT", width=20, height=2, command=pro_add, font=('times new roman', 10))
    prb.grid(row=12, column=2)
    buttop2 = Button(frame3, text="PAYROLL", width=30, height=2, command=pro, font=('times new roman', 10))
    buttop2.grid(row=12, column=4)

    prb1 = Button(frame3, text="ADD EMPLOYEE", width=20, height=2, command=add_entries, font=('times new roman', 10))
    prb1.grid(row=12, column=1)
    prb2 = Button(frame3, text="ADD DEPARTMENT", width=20, height=2, command=dept_details, font=('times new roman', 10))
    prb2.grid(row=12, column=1)
    prb3 = Button(frame3, text="DELETE", width=30, height=2, command=delete, font=('times new roman', 10))
    prb3.grid(row=12, column=0)
    prb5 = Button(frame3, text="EXIT", width=30, height=2, command=root.destroy, font=('times new roman', 10))
    prb5.grid(row=12, column=3)

    frame3.configure(background="misty rose")
    frame3.pack(pady=10)
def pro_add():
    db = mysql.connector.connect(
        username='root',
        password='12345',
        database='project')
    cur = db.cursor()

    p1 = (pname.get())
    pr = p1.lower()
    p2 = (pnumber.get())
    pr2 = p2.lower()
    p3 = (plocation.get())
    pr3 = p3.lower()
    p4= (deptno.get())
    pr4 = p4.lower()

    # cur.execute("create table basic(employeename varchar(20),employeenamel varchar(20),employeedept varchar(20),salary varchar(20),designation varchar(20))")
    query = ("insert into project_details(pname,pnumber,plocation,dno) values('" + (p1) + "','" + (
        p2) + "','" + (p3) + "','" + (p4) + "')")
    cur.execute(query)
    db.commit()
    tkinter.messagebox.askokcancel("STATEOFOPERATION", 'INSERTED SUCESSFULLY!!!!')

def pay():
    frame2.pack_forget()
    frame1.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()


    pronam1 = Label(frame4, text="ENTER TRANSACTION ID: ", font=('times new roman', 20), bg="white", fg="black")
    pronam1.grid(row=1, column=1, padx=10)
    pr1 = Entry(frame4, textvariable=transaction_id)
    pr1.grid(row=1, column=2, padx=10)
    pr1.focus()

    pno1 = Label(frame4, text="ENTER EMPLOYEE ID: ", bg="white", fg="black",
                font=('times new roman', 20))
    pno1.grid(row=4, column=1, padx=10)
    pp1 = Entry(frame4, textvariable=ssn)
    pp1.grid(row=4, column=2, padx=10)
    pp1.focus()

    loc1 = Label(frame4, text="ENTER SALARY PER MONTH:", bg="white", fg="black", font=('times new roman', 20))
    loc1.grid(row=6, column=1, padx=10)
    plo1 = Entry(frame4, textvariable=emp_salary_month)
    plo1.grid(row=6, column=2, padx=10)
    plo1.focus()

    sdno1 = Label(frame4, text="ENTER SALARY PER YEAR:", bg="white", fg="black", font=('times new roman', 20))
    sdno1.grid(row=8, column=1, padx=10)
    dat11 = Entry(frame4, textvariable=emp_salary_year)
    dat11.grid(row=8, column=2, padx=10)

    sde = Label(frame4, text="ENTER DEPARTMENT ID:", bg="white", fg="black", font=('times new roman', 20))
    sde.grid(row=9, column=1, padx=10)
    dat111 = Entry(frame4, textvariable=deptno)
    dat111.grid(row=9, column=2, padx=10)

    prb1 = Button(frame4, text="ADD PROJECT", width=20, height=2, command=pro, font=('times new roman', 10))
    prb1.grid(row=12, column=2)
    buttop3 = Button(frame4, text="PAYROLL", width=30, height=2, command=pay_add, font=('times new roman', 10))
    buttop3.grid(row=12, column=4)

    prb11 = Button(frame4, text="ADD EMPLOYEE", width=20, height=2, command=add_entries, font=('times new roman', 10))
    prb11.grid(row=12, column=1)
    prb21 = Button(frame4, text="ADD DEPARTMENT", width=20, height=2, command=dept_details, font=('times new roman', 10))
    prb21.grid(row=12, column=1)
    prb31 = Button(frame4, text="DELETE", width=30, height=2, command=delete, font=('times new roman', 10))
    prb31.grid(row=12, column=0)
    prb51 = Button(frame4, text="EXIT", width=30, height=2, command=root.destroy, font=('times new roman', 10))
    prb51.grid(row=12, column=3)

    frame4.configure(background="misty rose")
    frame4.pack(pady=10)
def pay_add():
    db = mysql.connector.connect(
        username='root',
        password='12345',
        database='project')
    cur = db.cursor()

    pa1 = (transaction_id.get())
    prr = pa1.lower()
    pa2 = (ssn.get())
    prr2 = pa2.lower()
    pa3 = (emp_salary_month.get())
    prr3 = pa3.lower()
    pa4 = (emp_salary_year.get())
    prr4 = pa4.lower()
    pa5=(deptno.get())
    prr5=pa5.lower()

    query = ("insert into payroll(transaction_id,ssn,emp_salary_month,emp_salary_year,dno) values('" + (pa1) + "','" + (
        pa2) + "','" + (pa3) + "','" + (pa4) + "','"+(pa5)+"')")
    cur.execute(query)
    db.commit()
    tkinter.messagebox.askokcancel("STATEOFOPERATION", 'INSERTED SUCESSFULLY!!!!')







#buttons########################################################################################################################

button1=Button(f,text="EMPLOYEE", background="peach puff", fg="black", command=add_entries, width=20,height=7)
button1.pack(side=LEFT,ipadx=20,pady=10)
button2=Button(f,text="DEPARTMENT", background="cornsilk2", fg="black", width=20,height=7,command=dept_details)
button2.pack(side=LEFT,ipadx=20,pady=10)
button3=Button(f,text="PROJECT", background="peach puff", fg="black",width=20,height=7,command=pro)
button3.pack(side=LEFT,ipadx=20,pady=10)
button6=Button(f,text="PAYROLL", background="cornsilk2", fg="black", width=20,height=7,command=pay)
button6.pack(side=LEFT,ipadx=20,pady=10)
button8=Button(f,text="UPDATE", background="peach puff", fg="black",width=20,height=7,command=update)
button8.pack(side=LEFT,ipadx=20,pady=10)
button7=Button(f,text="EXIT", background="peach puff", fg="black",width=20,height=7,command=root.destroy)
button7.pack(side=LEFT,ipadx=20,pady=10)

f.configure(background="lavender")
f.pack()


tkinter.messagebox.askokcancel("GREETINGS!!!!",'HELLO,WELCOME ADMIN!!!!')





root.mainloop()
