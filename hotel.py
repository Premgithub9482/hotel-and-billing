from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_win

class HotelManagement(Cust_win):
    def __init__(self,root):
        self.root=root
        self.root.title('HOTEL MANAGEMENT SYSTEM')
        self.root.geometry('1530x800+0+0')
    
    ##########1st image#############
        img1=Image.open(r"images/hotel1.png")
        img1=img1.resize((1530,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        labeling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        labeling.place(x=0,y=0,width=1530,height=140)

    ##########2nd image#############
        img2=Image.open(r"images/logohotel.png")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        labeling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        labeling.place(x=0,y=0,width=230,height=140)   

    ###Label title####
        lbltitle=Label(self.root,text='HOTEL MANAGEMENT SYSTEM',font=('times new roman',35,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbltitle.place(x=0,y=140,width=1530,height=40)
    
    ### Main FRame ###
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=180,width=1530,height=620)

    ### Menu ###
        lbl_menu=Label(main_frame,text='Menu',font=('times new roman',20,'bold'),bg='black',fg='gold',bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

    ### btn Frame ###
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text='CUSTOMER',command=self.cust_details,font=('times new roman',14,'bold'),bg='black',fg='gold',bd=0,width=22)
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text='ROOM',font=('times new roman',14,'bold'),bg='black',fg='gold',bd=0,width=22)
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text='DETAILS',font=('times new roman',14,'bold'),bg='black',fg='gold',bd=0,width=22)
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text='REPORT',font=('times new roman',14,'bold'),bg='black',fg='gold',bd=0,width=22)
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text='LOGOUT',font=('times new roman',14,'bold'),bg='black',fg='gold',bd=0,width=22)
        logout_btn.grid(row=4,column=0,pady=1)
    ### Right Side Image ###
        img3=Image.open(r"images\slide3.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg3.place(x=225,y=0,width=1350,height=500)

    ### Down Side Image ###
        img4=Image.open(r"images\myh.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg4.place(x=0,y=225,width=230,height=170)

        img5=Image.open(r"images\khana.jpg")
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg5=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg5.place(x=0,y=390,width=230,height=150)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)

if __name__=='__main__':
    root=Tk()
    obj=HotelManagement(root)
    root.mainloop()