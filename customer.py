from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector as m
from tkinter import messagebox


class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title('Hospital Management System')
        self.root.geometry("1295x550+30+20")


        #######Variables@#####
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()

        ###### Title #######
        lbl_title=Label(self.root,text='ADD CUSTOMER SYSTEM',font=('times new roman',18,'bold'),bg='black',fg='gold',relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        ## logo ###
        img2=Image.open(r"images\logohotel.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        ######Label frame############
        lblframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Customer Details',font=('times new roman',12,'bold'))
        lblframeleft.place(x=5,y=50,width=425,height=500)

        ######## Labels and Etry#####
        ##lbl cust ref
        lbl_cust_ref=Label(lblframeleft,text='Customer Ref',font=('times new roman',12,'bold'),padx=2,pady=5)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=Entry(lblframeleft,width=22,textvariable=self.var_ref,font=('times new roman',12,'bold'),state='readonly')
        entry_ref.grid(row=0,column=1)

        ## cust name entry
        lbl_cust_name=Label(lblframeleft,text='Customer name',font=('times new roman',12,'bold'),padx=2,pady=5)
        lbl_cust_name.grid(row=1,column=0,sticky=W)

        entry_name=Entry(lblframeleft,width=22,textvariable=self.var_cust_name,font=('times new roman',12,'bold'))
        entry_name.grid(row=1,column=1)

        ##cust mothername
        lbl_cust_mothname=Label(lblframeleft,text='Mother name',font=('times new roman',12,'bold'),padx=2,pady=5)
        lbl_cust_mothname.grid(row=2,column=0,sticky=W)

        entry_mothname=Entry(lblframeleft,width=22,textvariable=self.var_mother,font=('times new roman',12,'bold'))
        entry_mothname.grid(row=2,column=1)

        ## entry gender combobox
        lbl_cust_gender=Label(lblframeleft,text='Gender',font=('times new roman',12,'bold'),padx=2,pady=5)
        lbl_cust_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(lblframeleft,textvariable=self.var_gender,font=('arial',12,'bold'),width=27,state='readonly')
        combo_gender.current()
        combo_gender['value']=['Male','Female','Other']
        combo_gender.grid(row=3,column=1)

        ##Postcode
        lblpostcode=Label(lblframeleft,font=('arial',12,'bold'),text='PostCode:',padx=2,pady=5)
        lblpostcode.grid(row=4,column=0,sticky=W)
        textpostcode=ttk.Entry(lblframeleft,textvariable=self.var_post,font=('arial',13,'bold'),width=29)
        textpostcode.grid(row=4,column=1)

        ##Mobile NUmber
        lblmobnum=Label(lblframeleft,font=('arial',12,'bold'),text='Mob Num:',padx=2,pady=5)
        lblmobnum.grid(row=5,column=0,sticky=W)
        textmobnum=ttk.Entry(lblframeleft,textvariable=self.var_mobile,font=('arial',13,'bold'),width=29)
        textmobnum.grid(row=5,column=1)
       
        ##Email
        lblemail=Label(lblframeleft,font=('arial',12,'bold'),text='Email:',padx=2,pady=5)
        lblemail.grid(row=6,column=0,sticky=W)
        textemail=ttk.Entry(lblframeleft,textvariable=self.var_email,font=('arial',13,'bold'),width=29)
        textemail.grid(row=6,column=1)

         ##Natianlity
        lblnationality=Label(lblframeleft,font=('arial',12,'bold'),text='Nationality:',padx=2,pady=5)
        lblnationality.grid(row=7,column=0,sticky=W)

        combo_nationality=ttk.Combobox(lblframeleft,textvariable=self.var_nationality,font=('arial',12,'bold'),width=27,state="readonly")
        combo_nationality.current()
        combo_nationality['value']=['Indian','Italy','England','America','Japan','Germany','Russia','South Africa']
        combo_nationality.grid(row=7,column=1)

        ###idproof combobox
        lblidproof=Label(lblframeleft,font=('arial',12,"bold"),text='Id Proof Type:',pady=6,padx=2)
        lblidproof.grid(row=8,column=0,sticky=W)

        combo_idproof=ttk.Combobox(lblframeleft,textvariable=self.var_id_proof,font=('arial',12,'bold'),width=27,state='readonly')
        combo_idproof.current()
        combo_idproof['value']=['Adhar','Pancard','Driving licence','Voter Id']
        combo_idproof.grid(row=8,column=1)

        ##Id number
        lblidnumber=Label(lblframeleft,font=('arial',12,'bold'),text='Id Number:',padx=2,pady=5)
        lblidnumber.grid(row=9,column=0,sticky=W)

        txtidnumber=ttk.Entry(lblframeleft,textvariable=self.var_id_number,font=('arial',12,'bold'),width=29)
        txtidnumber.grid(row=9,column=1)

        ##Address
        lbladdress=Label(lblframeleft,font=('arial',12,'bold'),text='Address:',padx=2,pady=5)
        lbladdress.grid(row=10,column=0,sticky=W)
        txtaddress=ttk.Entry(lblframeleft,textvariable=self.var_address,font=('arial',12,'bold'),width=29)
        txtaddress.grid(row=10,column=1)

        #####buttons######
        btn_frame=Frame(lblframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frame,text='Add',command=self.add_data,font=('arila',12,'bold'),bg='black',fg='gold',width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text='Update',font=('arila',12,'bold'),bg='black',fg='gold',width=9)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text='Delete',font=('arila',12,'bold'),bg='black',fg='gold',width=9)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text='Reset',font=('arila',12,'bold'),bg='black',fg='gold',width=9)
        btn_reset.grid(row=0,column=3,padx=1)

        #####table Frame####
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text='View Details And Search System',font=('arial',12,'bold'),padx=2)
        table_frame.place(x=435,y=50,width=860,height=490)

        lblsearchby=Label(table_frame,font=('arial',12,'bold'),text='Search By:',bg='red',fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        combo_search=ttk.Combobox(table_frame,font=('arial',12,'bold'),width=24,state='readonly')
        combo_search.current()
        combo_search['value']=['Mobile','Ref']
        combo_search.grid(row=0,column=1,padx=2)

        txtsearch=ttk.Entry(table_frame,font=('arial',12,'bold'),width=24)
        txtsearch.grid(row=0,column=2,padx=2)

        btn_search=Button(table_frame,text='Search',font=('arial',11,'bold'),bg='black',fg='gold',width=10)
        btn_search.grid(row=0,column=3,padx=1)

        btnshowall=Button(table_frame,text='Show All',font=('arial',11,'bold'),bg='black',fg='gold',width=10)
        btnshowall.grid(row=0,column=4,padx=1)

        ######## Show data table ###########
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_table=ttk.Treeview(details_table,column=('ref','name','mother','gender','post','mobile','email','nationality','idproof','idnumber','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_table.xview)
        scroll_y.config(command=self.Cust_Details_table.yview)

        self.Cust_Details_table.heading('ref',text='Refer No')
        self.Cust_Details_table.heading('name',text='Name')
        self.Cust_Details_table.heading('mother',text='Mother Name')
        self.Cust_Details_table.heading('gender',text='Gender')
        self.Cust_Details_table.heading('post',text='Postcode')
        self.Cust_Details_table.heading('mobile',text='Mobile')
        self.Cust_Details_table.heading('email',text='Email')
        self.Cust_Details_table.heading('nationality',text='Nationality')
        self.Cust_Details_table.heading('idproof',text='Id Proof')
        self.Cust_Details_table.heading('idnumber',text='Id Number')
        self.Cust_Details_table.heading('address',text='Address')

        self.Cust_Details_table['show']='headings'

        self.Cust_Details_table.column('ref',width=100)
        self.Cust_Details_table.column('name',width=100)
        self.Cust_Details_table.column('mother',width=100)
        self.Cust_Details_table.column('gender',width=100)
        self.Cust_Details_table.column('post',width=100)
        self.Cust_Details_table.column('mobile',width=100)
        self.Cust_Details_table.column('email',width=100)
        self.Cust_Details_table.column('nationality',width=100)
        self.Cust_Details_table.column('idproof',width=100)
        self.Cust_Details_table.column('idnumber',width=100)
        self.Cust_Details_table.column('address',width=100)

        self.Cust_Details_table.pack(fill=BOTH,expand=1)
        self.Cust_Details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if (self.var_mobile.get()=='') or (self.var_mother.get()==''):
            messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                con_obj=m.connect(host='localhost',username='root',password='root',database='customer')
                cur_obj=con_obj.cursor()
                cur_obj.execute("insert into new_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"(
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get(),
                    ))
                con_obj.commit()
                self.fetch_data()
                con_obj.close()
                messagebox.showinfo('Success','Customer has been added',parent=self.root)
            except Exception as es:
                messagebox.showwarning('warning',f'some things went wrong:{str(es)}',parent=self.root)

    def fetch_data(self):
        con_obj=m.connect(username='root',password='root',host='localhost',database='customer')
        cur_obj=con_obj.cursor()
        cur_obj.execute('select * from new_table')
        rows=cur_obj.fetchall()
        if len(rows)!=0:
            self.Cust_Details_table.delete(*self.Cust_Details_table.get_children())
            for i in rows:
                self.Cust_Details_table.insert('',END,values=i)
            con_obj.commit()
        con_obj.close()
    
    def get_cursor(self,event=''):
        cursor_row=self.Cust_Details_table.focus()
        content=self.Cust_Details_table.item(cursor_row)
        row=content['values']

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])        


if __name__=='__main__':
    root=Tk()
    obj=Cust_win(root)
    root=mainloop()