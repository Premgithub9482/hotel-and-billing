from tkinter import*

root=Tk()
root.geometry('1000x500+0+0')
root.title('BILL Management')
root.resizable(False,False)

def Reset():
    entry_dosa.delete(0,END)
    entry_idli.delete(0,END)
    entry_meals.delete(0,END)
    entry_tea.delete(0,END)
    entry_cofeef.delete(0,END)
    entry_juice.delete(0,END)

def Total():
    try:
        p1=int(Dosa.get())
    except:
        p1=0
    try:
        p2=int(Idli.get())
    except:
        p2=0
    try:
        p3=int(Meals.get())
    except:
        p3=0
    try:
        p4=int(Tea.get())
    except:
        p4=0
    try:
        p5=int(Coffee.get())
    except:
        p5=0
    
    ##identifying prices
    a=p1*50
    b=p2*40
    c=p3*100
    d=p4*10
    e=p5*12

    lbl_total=Label(f2,font=('aria',20,'bold'),text='Total',fg='lightyellow',width=16,bg='black')
    lbl_total.place(x=0,y=50)
    entry_total=Entry(f2,font=('arial',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg='lightgreen')
    entry_total.place(x=20,y=100)

    totalcost=a+b+c+d+e
    string_bill='Rs ',str('%.2f'%totalcost)
    Total_bill.set(string_bill)

lbl=Label(text='BILL MANAGEMENT SYSTEM',bg='gray',fg='white',font=('Arian',20,'bold'),width=300,height=2)
lbl.pack()

f=Frame(root,height=370,width=300,bg='red',)
f.place(x=10,y=110)
Label(f,text='Menu',font=('Arial',15,'bold'),bg='lightgreen',fg='black').place(x=100,y=0)
Label(f,text='Dosa....Rs 50/plate',font=('Lucida Calligraphy',15,'bold'),bg='lightgreen',fg='black').place(x=10,y=80)
Label(f,text='Idli....Rs 40/plate',font=('Lucida Calligraphy',15,'bold'),bg='lightgreen',fg='black').place(x=10,y=110)
Label(f,text='Meals....Rs 100/plate',font=('Lucida Calligraphy',15,'bold'),bg='lightgreen',fg='black').place(x=10,y=140)
Label(f,text='Tea....Rs 10',font=('Lucida Calligraphy',15,'bold'),bg='lightgreen',fg='black').place(x=10,y=200)
Label(f,text='Coffee....Rs 12',font=('Lucida Calligraphy',15,'bold'),bg='lightgreen',fg='black').place(x=10,y=230)
Label(f,text='Juice...Rs 40',font=('Lucida Calligraphy',15,'bold'),bg='lightgreen',fg='black').place(x=10,y=260)

#bill
f2=Frame(root,highlightbackground='black',highlightthickness=1,bg='lightyellow',width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text='Bill',font=('calibri',20,'bold'),bg='lightyellow')
Bill.place(x=120,y=10)

##Entry
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Dosa=StringVar()
Idli=StringVar()
Meals=StringVar()
Tea=StringVar()
Coffee=StringVar()
Juice=StringVar()
Total_bill=StringVar()


#Labels
lbl_dosa=Label(f1,font=('arial',20,'bold'),width=12,bg='lightpink',text='Dosa')
lbl_idli=Label(f1,font=('arial',20,'bold'),width=12,bg='lightpink',text='Idli')
lbl_meals=Label(f1,font=('arial',20,'bold'),width=12,bg='lightpink',text='Meals')
lbl_tea=Label(f1,font=('arial',20,'bold'),width=12,bg='lightpink',text='Tea')
lbl_coffee=Label(f1,font=('arial',20,'bold'),width=12,bg='lightpink',text='coffee')
lbl_juice=Label(f1,font=('arial',20,'bold'),width=12,bg='lightpink',text='juice')
# lbl_=Label(f1,font=('arial',20,bold),width=12,bg='lightpink')
lbl_dosa.grid(row= 1,column=0)
lbl_idli.grid(row=2,column=0)
lbl_meals.grid(row=3,column=0)
lbl_tea.grid(row=4,column=0)
lbl_coffee.grid(row=5,column=0)
lbl_juice.grid(row=6,column=0)

##Entry
entry_dosa=Entry(f1,font=('arial',20,'bold'),bd=6,textvariable=Dosa,width=8,bg='lightgreen')
entry_idli=Entry(f1,font=('arial',20,'bold'),bd=6,textvariable=Idli,width=8,bg='lightgreen')
entry_meals=Entry(f1,font=('arial',20,'bold'),bd=6,textvariable=Meals,width=8,bg='lightgreen')
entry_tea=Entry(f1,font=('arial',20,'bold'),bd=6,textvariable=Tea,width=8,bg='lightgreen')
entry_cofeef=Entry(f1,font=('arial',20,'bold'),bd=6,textvariable=Coffee,width=8,bg='lightgreen')
entry_juice=Entry(f1,font=('arial',20,'bold'),bd=6,textvariable=Juice,width=8,bg='lightgreen')

entry_dosa.grid(row=1,column=1)
entry_idli.grid(row=2,column=1)
entry_meals.grid(row=3,column=1)
entry_tea.grid(row=4,column=1)
entry_cofeef.grid(row=5,column=1)
entry_juice.grid(row=6,column=1)

but_reset=Button(f1,fg='black',bg='lightgreen',command=Reset,text='Reset',width=8)
but_reset.grid(row=8,column=0)
but_total=Button(f1,fg='black',bg='lightgreen',command=Reset,text='Total',width=8)
but_total.grid(row=8,column=1)

# lbl_bill=Label(f2,text='Bill')
# lbl_bill.grid(row=1,column=1)

root.mainloop()