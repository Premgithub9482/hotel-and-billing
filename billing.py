from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random

# root=Tk()

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title('Bill Management')
        

        # ###### Variables ############
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


        #product category list
        self.Category=["Select option",'Clothing','Lifestyle','Mobiles']
        #subclothing
        self.CatClothing=['Pant','T-Shirt','Shirt']
        self.pant=['Levis','Spyker','Jeans']
        self.price_levis=5000
        self.price_spyker=7000
        self.price_jeans=4000

        self.T_shirt=['Polo','Jack&Jones','Roadster']
        self.price_polo=1500
        self.price_jakjones=1800
        self.price_roadsters=1700
 
        self.Shirt=['Peter England','Louis Phillipe','Park Avenue']
        self.price_peter=2100
        self.price_louis=2700
        self.price_park=2850
        
        #subcatlifestyle
        self.SubCatLifestyle=['Bath Soap','Face Cream','Hair Oil']
        self.Bath_soap=['Lux','Sandalwood','Dove']
        self.price_lux=25
        self.price_sandlwood=50
        self.price_dove=64
 
        self.Face_cream=['Ponds','Oley','Fair&Handsome']
        self.price_ponds=70
        self.price_oley=85
        self.price_fair_handsome=45

        self.Hair_oil=['Parroshoot','Jasmine','Coconutoil']
        self.price_parroshoot=70
        self.price_jasmine=85
        self.price_coconutoil=45

        self.SubCatMobiles=['Iphone','Samsung','Realme','One+','Xiome']
        self.Iphone=['Iphone_x','Iphone_11','Iphone_12']
        self.price_ix=40800
        self.price_i11=60000
        self.price_i12=85000

        #image1
        img=Image.open('image/veg.jpg')
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=120)
        #image2
        img_1=Image.open('image/girls.jpg')
        img_1=img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height=120)

        #image3
        img_2=Image.open('image/img4.jpg')
        img_2=img_2.resize((500,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=950,y=0,width=500,height=120)

        lbl_title=Label(self.root,text='BILLING SOFTWARE USING PYTHON',font=('times new roman',35,'bold'),bg='white',fg='red')
        lbl_title.place(x=0,y=120,width=1530,height=35)

        main_frame=Frame(self.root,bd=5,relief=GROOVE,bg='white')
        main_frame.place(x=0,y=160,width=1530,height=600)

        #customer label frame
        cust_frame=LabelFrame(main_frame,text='customer',font=('times new roman',12,'bold'),bg='white',fg='red')
        cust_frame.place(x=6,y=1,width=350,height=140)

        self.lbl_mob=Label(cust_frame,text='Mobile No',font=('times new roman',12,'bold'),bg='white',fg='red')
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(cust_frame,textvariable=self.c_phon,font=('times new roman',10,'bold'),width=24)
        self.entry_mob.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.txtcustName=Label(cust_frame,font=('times new roman',10,'bold'),bg='white',text='Customer Name',bd=4)
        self.txtcustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtcustName=ttk.Entry(cust_frame,textvariable=self.c_name,font=('times new roman',10,'bold'),width=24)
        self.txtcustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblemail=Label(cust_frame,font=('arial',12,'bold'),bg='white',text='Email',bd=4)
        self.lblemail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtemail=ttk.Entry(cust_frame,textvariable=self.c_email,font=('arial',12,'bold'),width=24)
        self.txtemail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
 
        #Product labelframe
        product_frame=LabelFrame(main_frame,text='Product',font=('times new roman',12,'bold'),bg='white',fg='red')
        product_frame.place(x=360,y=1,width=620,height=140) 
        
        #category
        self.lblcategory=Label(product_frame,font=('arial',12,'bold'),bg='white',text='Select Categories',bd=4)
        self.lblcategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.combo_category=ttk.Combobox(product_frame,value=self.Category,font=('arial',10,'bold'),width=24,state='readonly')
        self.combo_category.current(0)
        self.combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.combo_category.bind("<<ComboboxSelected>>",self.Categories)

        #subcategory
        self.lblsubcategory=Label(product_frame,font=('arial',12,'bold'),bg='white',text='Subcategory',bd=4)
        self.lblsubcategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.combosubcategory=ttk.Combobox(product_frame,value=[""],state='readonly',font=('arial',10,'bold'),width=24)
        self.combosubcategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.combosubcategory.bind("<<ComboboxSelected>>",self.product_add)

        #product name
        self.lblproduct=Label(product_frame,font=('arial',12,'bold'),bg='white',text='Product Name',bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.comboproduct=ttk.Combobox(product_frame,state='readonly',textvariable=self.product,font=('arial',10,'bold'),width=24)
        self.comboproduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.comboproduct.bind("<<ComboboxSelected>>",self.price)

        # Price
        self.lblprice=Label(product_frame,font=('arial',12,'bold'),bg='white',text='Price',bd=4)
        self.lblprice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.comboprice=ttk.Combobox(product_frame,state='readonly',textvariable=self.prices, font=('arial',10,'bold'),width=24)
        self.comboprice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Qty
        self.lblqty=Label(product_frame,font=('arial',12,'bold'),bg='white',text='Qty',bd=4)
        self.lblqty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.comboqty=ttk.Combobox(product_frame,textvariable=self.qty,font=('arial',10,'bold'),width=24)
        self.comboqty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        # Middle Frame
        middleFrame=Frame(main_frame,bd=10)
        middleFrame.place(x=8,y=140,width=960,height=320)

        #image1
        img12=Image.open('image/good.jpg')
        img12=img.resize((490,320),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl_img12=Label(middleFrame,image=self.photoimg12)
        lbl_img12.place(x=0,y=0,width=490,height=320)

        #image2
        img13=Image.open('image/mall.jpg')
        img13=img.resize((490,320),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(img13)

        lbl_img13=Label(middleFrame,image=self.photoimg13)
        lbl_img13.place(x=0,y=0,width=490,height=320)

        # Search
        search_frame=Frame(main_frame,bd=2,bg='white')
        search_frame.place(x=980,y=7,width=460,height=38)

        self.lblBill=Label(search_frame,font=('arial',12,'bold'),fg='white',bg='red',text='Bill Number')
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_entrysearch=ttk.Entry(search_frame,textvariable=self.search_bill,font=('arial',10,'bold'),width=24)
        self.txt_entrysearch.grid(row=0,column=1,sticky=W,padx=2)

        self.btnsearch=Button(search_frame,text='Search',font=('arial',15,'bold'),bg='orangered',fg='white',width=10,cursor='hand2')
        self.btnsearch.grid(row=0,column=2)

        #RightFrame Bill Area
        rightlblframe=Label(main_frame,text='Bill Area',font=('times new roman',12,'bold'),bg='white',fg='red')
        rightlblframe.place(x=980,y=45,width=400,height=400)

        scroll_y=Scrollbar(rightlblframe,orient=VERTICAL)
        self.textarea=Text(rightlblframe,yscrollcommand=scroll_y.set,bg='white',fg='blue',font=('times new roman',10,'bold'))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # Bill Counter Labelframe
        bottom_frame=LabelFrame(main_frame,text='Bill counter',font=('times new roman',12,'bold'),bg='white',fg='red')
        bottom_frame.place(x=0,y=400,width=1520,height=125)

        self.lblsubtotal=Label(bottom_frame,font=('arial',12,'bold'),bg='white',text='sub total',bd=4)
        self.lblsubtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entrysubtotal=ttk.Entry(bottom_frame,font=('arial',10,'bold'),width=24)
        self.entrysubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbltax=Label(bottom_frame,font=('arial',10,'bold'),bg='white',text='Govt. tax',bd=4)
        self.lbltax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(bottom_frame,font=('arial',10,'bold'),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lbltotalamount=Label(bottom_frame,font=('arial',10,'bold'),bg='white',text='Total',bd=4)
        self.lbltotalamount.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txt_total=ttk.Entry(bottom_frame,font=('arial',10,'bold'),width=24)
        self.txt_total.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Button Frame
        btn_frame=Frame(bottom_frame,bd=2,bg='white')
        btn_frame.place(x=320,y=0)

        self.btnaddtocart=Button(btn_frame,height=2,text='Add To Cart',font=('arial',15,'bold'),bg='orangered',fg='white',width=14)
        self.btnaddtocart.grid(row=0,column=0)

        self.btngenerate_bill=Button(btn_frame,height=2,text='Generate Bill',font=('arial',15,'bold'),bg='orangered',fg='white',width=14)
        self.btngenerate_bill.grid(row=0,column=1)

        self.btnsave=Button(btn_frame,height=2,text='Save Bill',font=('arial',15,'bold'),bg='orangered',fg='white',width=14)
        self.btnsave.grid(row=0,column=2,)

        self.btnprint=Button(btn_frame,height=2,text='Print',font=('arial',15,'bold'),bg='orangered',fg='white',width=14)
        self.btnprint.grid(row=0,column=3)

        self.btnclear=Button(btn_frame,height=2,text='Clear',font=('arial',15,'bold'),bg='orangered',fg='white',width=14)
        self.btnclear.grid(row=0,column=4)


    def Categories(self,event=''):
        if self.combo_category.get()=='Clothing':
            self.combosubcategory.config(value=self.CatClothing)
            self.combosubcategory.current(0)

        if self.combo_category.get()=='Lifestyle':
            self.combosubcategory.config(value=self.SubCatLifestyle)
            self.combosubcategory.current(0)

        if self.combo_category.get()=='Mobiles':
            self.combosubcategory.config(value=self.SubCatMobiles)
            self.combosubcategory.current(0)

    def product_add(self,event=''):
        if self.combosubcategory.get()=='Pant':
            self.comboproduct.config(value=self.pant)
            self.comboproduct.current(0)

        if self.combosubcategory.get()=='T-Shirt':
            self.comboproduct.config(value=self.T_shirt)
            self.comboproduct.current(0)
        
        if self.combosubcategory.get()=='Shirt':
            self.comboproduct.config(value=self.Shirt)
            self.comboproduct.ccurrent(0)

        # Lifestyle subproduccts
        if self.combosubcategory.get()=='Bath Soap':
            self.comboproduct.config(value=self.Bath_soap)
            self.comboproduct.current(0)
        
        if self.combosubcategory.get()=='Face Cream':
            self.comboproduct.config(value=self.Face_cream)
            self.comboproduct.current(0)
        
        if self.combosubcategory.get()=='Hair Oil':
            self.comboproduct.config(value=self.Hair_oil)
            self.comboproduct.current(0)

    def price(self,event=""):
        # Pant
        if self.Comboproduct.get()=='Levis':
            self.comboprice.config(value=self.price_levis)
            self.comboprice.curent(0)
            self.qty.set(1)
             
        if self.comboproduct.get()=='Spykar':
            self.comboprice.config(value=self.price_spyker)
            self.comboprice.current(0)
            self.qty.set(1)
        
        if self.comboproduct.get()=='Jeans':
            self.comboprice.config(value=self.price_jeans)
            self.comboprice.current(0)
            self.qty.set(1)

        # T-shirts
        if self.comboproduct.get()=='Polo':
            self.comboprice.config(value=self.price_polo)
            self.comboprice.current(0)
            self.qty.set(1)


if __name__=="__main__" :
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()