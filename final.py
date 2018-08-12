from tkinter import *
import PIL.Image, PIL.ImageTk
import MySQLdb
import smtplib
import random
    
wr=1360/1920
hr=768/1080

def bought(imgx,l1,l2,l3,l4,bx,e1,e2,e3,e4,id,a1,a2,a3,a4):
    send(id,a1,a2,a3,a4)

    t1 = Text(root, width=50,font=("Bradley Hand ITC",10,"bold"), bg="deepskyblue",relief="flat", )
    t1.insert(END, "YOUR ORDER HAS BEEN PLACED SUCCESSFULLY!")

    t1.place(x=1200*wr, y=850*hr)

def flush():
    pass


def send(mail,a1,a2,a3,a4):
    x=random.randint(1000,9999)
    conn=MySQLdb.connect(host='localhost', database='abc', user='root',
    password='Dhaval@1505')
    cursor=conn.cursor()
    str="insert into order_details(O_NO,NAME,EMAIL,PHONE,ADDRESS)values(%s,%s,%s,%s,%s)"
    
    #args=(ID)
    cursor.execute(str,(x,a1,a3,a4,a2))
    conn.commit()
    cursor.close()
    conn.close()

    
    sender = "deepme987@gmail.com"
    msg = '''Your order has been succesfully placed!
            Name:%s
            Address:%s
            Contact:%s
            Order No:%d

            For any queries, contact us at: support@bestmobiledeals.com'''%(a1,a2,a4,x)
    s = smtplib.SMTP('smtp.gmail.com')
    s.starttls()
    s.login(sender,"deepandbhoomi")
    s.sendmail(sender, mail, msg)
    s.quit()
    '''try:
        s = smtplib.SMTP('smtp.gmail.com')
        s.starttls()
        s.login(sender,"d")
        s.sendmail(sender, mail, msg)
        s.quit()
    except:
        Label(root, text="Unable to connect to internet, make sure you've a working connection!", height=2, width=50).place(x=900,y=500)'''


#for database
def retrieve_row(ID):
    conn=MySQLdb.connect(host='localhost', database='abc', user='root',
    password='Dhaval@1505')
    cursor=conn.cursor()
    str="select * from mobile_data1 where ID='%d'"
    args=(ID)
    cursor.execute(str % args)
    row = cursor.fetchall()
    if row is not None:
        for r in row:
            name=r[0]
            brand=r[1]
            price=r[2]
            ram=r[3]
            storage=r[4]
            camb=r[5]
            camf=r[7]
            screen=r[6]
        
    
        l_name=Label(text=" NAME :\t"+name,justify='left', width=20, font=('Aparajita', 10)).place(x=1500*wr, y=200*hr)
        l_brand=Label(text="BRAND :  "+brand,justify='left', width=20, font=('Aparajita', 10)).place(x=1500*wr, y=240*hr)
        l_price=Label(text="PRICE :\t"+price,justify='left', width=20, font=('Aparajita', 10)).place(x=1500*wr, y=280*hr)
        l_ram=Label(text="RAM :\t"+ram+" gb",justify='left', width=20, font=('Aparajita', 10)).place(x=1500*wr, y=320*hr)
        l_storage=Label(text="STORAGE : "+storage+" gb",justify='left', width=20, font=('Aparajita', 10)).place(x=1500*wr, y=360*hr)
        l_camb=Label(text="BACK CAM : "+camb+" mp",justify='left', width=20, font=('Aparajita', 10)).place(x=1500*wr, y=400*hr)
        l_camf=Label(text="FRONT CAM : %d mp"%camf,justify='left', width=20, font=('Aparajita', 10)).place(x=1500*wr, y=440*hr)
        l_screen=Label(text="SCREEN : "+screen,justify='left', width=20, font=('Aparajita', 10)).place(x=1500*wr, y=480*hr)
        
    cursor.close()
    conn.close()


def show(imgx,num):
    retrieve_row(num)
    
    lb=Label(root, image=imgx, height=220, width=250,bg='deepskyblue')
    b1=Button(root, text="  BUY  ",bg="navy",fg='white', command=lambda:buy(imgx,lb, b1, b2)) 
    b2=Button(root, text="CANCEL",bg="navy",fg='white')# command=lambda:destroyall())    

    lb.place(x=1100*wr, y=200*hr)
    b1.place(x=1370*wr,y=550*hr)
    b2.place(x=1470*wr,y=550*hr)
    
    
    
'''def reshow(imgx, bx, t1):
    bx.destroy()
    t1.destroy()
    show(imgx,num)'''

def destroyall(): 
    b1.destroy()
    b2.destroy()
    t.destroy()
    lb.destroy()
    

def buy(imgx,lb,b1,b2): 
    l1=Label(root, text="Enter Your Name: ",font=("Viner Hand ITC",10,"bold"),bg="deepskyblue")
    l2 = Label(root, text="Address: ",font=("Viner Hand ITC",10,"bold"),bg="deepskyblue" )
    l3 = Label(root, text="Email Address: ",font=("Viner Hand ITC",10,"bold"),bg="deepskyblue")
    l4 = Label(root, text="Contact No: ",font=("Viner Hand ITC",10,"bold"),bg="deepskyblue")

    l1.place(x=1200*wr, y=650*hr)
    l2.place(x=1200*wr, y=690*hr)
    l3.place(x=1200*wr, y=730*hr)
    l4.place(x=1200*wr, y=770*hr)

    e1 = Entry(root, width=25, bg="cadetblue1",relief="raised", font=('Arial', 10))
    e2 = Entry(root,width=25,   bg="cadetblue1",relief="raised", font=('Arial', 10))
    e3 = Entry(root, width=25, bg="cadetblue1",relief="raised", font=('Arial', 10))
    e4 = Entry(root, width=25, bg="cadetblue1",relief="raised", font=('Arial', 10))

    e1.place(x=1500*wr, y=650*hr)
    e2.place(x=1500*wr, y=690*hr)
    e3.place(x=1500*wr, y=730*hr)
    e4.place(x=1500*wr, y=770*hr)

    bx=Button(root, text="Place Order!", bg="navy",fg="white" ,command=lambda:bought(imgx,l1,l2,l3,l4,bx, e1,e2,e3,e4,e3.get(),e1.get(),e2.get(),e3.get(),e4.get()))
    bx.place(x=1400*wr, y=850*hr)


'''def filterside():
    l1 = Label(root, text="Filters", bg="deepskyblue", font=("Aparajita", 20, "bold"))
    l1.place(x=1200*wr, y=30*hr)

    f1 = Label(root, text="Price", bg="deepskyblue", font=("Aparajita", 15,"bold"))
    f1.place(x=1200*wr, y=80*hr)

    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()

    c11 = Checkbutton(root, text="<15k", variable=v1, bg="deepskyblue", font=("Aparajita", 10,"bold"))
    c12 = Checkbutton(root, text="15k-25k", variable=v2, bg="deepskyblue", font=("Aparajita", 10,"bold"))
    c13 = Checkbutton(root, text="25k-50k", variable=v3, bg="deepskyblue", font=("Aparajita", 10,"bold"))
    c14 = Checkbutton(root, text="50k+", variable=v4, bg="deepskyblue", font=("Aparajita", 10,"bold"))

    c11.place(x=1200*wr, y=110*hr)
    c12.place(x=1160*wr, y=110*hr)
    c13.place(x=1260*wr, y=110*hr)
    c14.place(x=1360*wr, y=110*hr)

    f2 = Label(root, text="Brand", bg="deepskyblue", font=("Aparajita", 15,"bold"))
    f2.place(x=1200*wr, y=150*hr)

    v5 = IntVar()
    v6 = IntVar()
    v7 = IntVar()
    v8 = IntVar()

    c21 = Checkbutton(root, text="Apple", variable=v5, bg="deepskyblue", font=("Aparajita", 10,"bold"))
    c22 = Checkbutton(root, text="Google", variable=v6, bg="deepskyblue", font=("Aparajita", 10,"bold"))
    c23 = Checkbutton(root, text="Samsung", variable=v7, bg="deepskyblue", font=("Aparajita", 10,"bold"))
    c24 = Checkbutton(root, text="Others", variable=v8, bg="deepskyblue", font=("Aparajita", 10,"bold"))

    c21.place(x=1200*wr, y=180*hr)
    c22.place(x=1160*wr, y=180*hr)
    c23.place(x=1260*wr, y=180*hr)
    c24.place(x=1360*wr, y=180*hr)

    f3 = Label(root, text="Internal Storage", bg="deepskyblue", font=("Aparajita", 15,"bold"))
    f3.place(x=1500*wr, y=80*hr)

    v9 = IntVar()
    v10 = IntVar()
    v11 = IntVar()
    v12 = IntVar()

    c31 = Checkbutton(root, text="32", variable=v9, bg="deepskyblue", font=("Aparajita", 10,"bold"))
    c32 = Checkbutton(root, text="64", variable=v10, bg="deepskyblue", font=("Aparajita", 10,"bold"))
    c33 = Checkbutton(root, text="128", variable=v11, bg="deepskyblue", font=("Aparajita", 10,"bold"))
    c34 = Checkbutton(root, text="256", variable=v12, bg="deepskyblue", font=("Aparajita", 10,"bold"))


    c31.place(x=1500*wr, y=110*hr)
    c32.place(x=1600*wr, y=110*hr)
    c33.place(x=1700*wr, y=110*hr)
    c34.place(x=1800*wr, y=110*hr)

    f4 = Label(root, text="RAM", bg="deepskyblue", font=("Aparajita", 15,"bold"))
    f4.place(x=1500*wr, y=150*hr)

    v13 = IntVar()
    v14 = IntVar()
    v15 = IntVar()
    v16 = IntVar()

    c41 = Checkbutton(root, text="3", variable=v13, bg="deepskyblue", font=("Aparajita", 10,"bold"))
    c42 = Checkbutton(root, text="4", variable=v14, bg="deepskyblue", font=("Aparajita", 10,"bold"))
    c43 = Checkbutton(root, text="6", variable=v10, bg="deepskyblue", font=("Aparajita", 10,"bold"))
    c44 = Checkbutton(root, text="8", variable=v16, bg="deepskyblue", font=("Aparajita", 10,"bold"))

    c41.place(x=1500*wr, y=180*hr)
    c42.place(x=1600*wr, y=180*hr)
    c43.place(x=1700*wr, y=180*hr)
    c44.place(x=1800*wr, y=180*hr)

    lx = Button(root, text="Search", font=("Helvetica", 10),bg="gray70",command=lambda:disp(v1, v2, v3, v4))
    lx.place(x=1100*wr, y=230*hr)'''

def disp(v1,v2,v3,v4):
    lb=Label(root, text=str(v1.get())+str(v2.get())+str(v3.get())+str(v4.get()))
    lb.place(x=1100*wr,y=800*hr)


def data():
    Button(frame, image=img1, command=lambda:show(img1,1)).grid(row=0, column=0)

    Button(frame,  image=img2, command=lambda:show(img2,2)).grid(row=0, column=1)

    Button(frame, image=img3, command=lambda:show(img3,3)).grid(row=0, column=2)

    Button(frame, image=img4, command=lambda:show(img4,4)).grid(row=0, column=3)

    Button(frame, image=img5, command=lambda:show(img5,5)).grid(row=1, column=0)

    Button(frame,  image=img6, command=lambda:show(img6,6)).grid(row=1, column=1)

    Button(frame, image=img7, command=lambda:show(img7,7)).grid(row=1, column=2)

    Button(frame,  image=img8, command=lambda:show(img8,8)).grid(row=1, column=3)

    Button(frame, image=img9, command=lambda:show(img9,9)).grid(row=2, column=0)

    Button(frame, image=img10, command=lambda:show(img10,10)).grid(row=2, column=1)

    Button(frame,  image=img11, command=lambda:show(img11,11)).grid(row=2, column=2)

    Button(frame, image=img12, command=lambda:show(img12,12)).grid(row=2, column=3)

    Button(frame, image=img13, command=lambda:show(img13,13)).grid(row=3, column=0)

    Button(frame, image=img14, command=lambda:show(img14,14)).grid(row=3, column=1)

    Button(frame, image=img10, command=lambda:show(img15,15)).grid(row=3, column=2)

    Button(frame, image=img16, command=lambda:show(img16,16)).grid(row=3, column=3)

    Button(frame,  image=img17, command=lambda:show(img17,17)).grid(row=4, column=0)

    Button(frame, image=img18, command=lambda:show(img18,18)).grid(row=4, column=1)

    Button(frame, image=img19, command=lambda:show(img19,19)).grid(row=4, column=2)

    Button(frame, image=img15, command=lambda:show(img20,20)).grid(row=4, column=3)

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=1020*wr,height=970*hr)

root=Tk()
root.title("MOBILE SHOP")
root.geometry("1366x768")
root.configure(background="DeepSkyBlue")

myframe=Frame(root,relief="raised",width=200*wr,height=200*hr,bd=1)
myframe.place(x=0,y=0)

canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)

x = PIL.Image.open('img1.jpg')
img1 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img2.jpg')
img2 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img3.jpg')
img3 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img4.jpeg')
img4 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img5.jpg')
img5 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img6.jpg')
img6 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img7.jpg')
img7 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img8.jpg')
img8 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img9.jpg')
img9 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img10.jpg')
img10 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img11.jpg')
img11 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img12.jpeg')
img12 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img13.jpeg')
img13 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img14.jpg')
img14 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img15.jpg')
img15 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img16.jpeg')
img16 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img17.jpg')
img17 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img18.jpg')
img18 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img19.jpg')
img19 = PIL.ImageTk.PhotoImage(x)

x = PIL.Image.open('img20.jpg')
img20 = PIL.ImageTk.PhotoImage(x)

l0 = Label(root, text="MOBILE  STORE",font=("Viner Hand ITC",28,"bold"),bg="deepskyblue")
l0.place(x=1300*wr, y=10*hr)

data()
#filterside()

root.mainloop()
