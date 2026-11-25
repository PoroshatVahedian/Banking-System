from tkinter import *
from random import randint
from time import sleep
root=Tk()
root.title('My Bank App')
root.geometry('1400x700')
root.configure(bg='#454545')
database={}
check=''
check_card=''


_4521596875324578={'firstname':'alice','lastname':'stone','card_number':'4521596875324578','amount':'23410400'}


def create_database(**kwargs):
    global check
    while True:
        if Security_entry.get()=='':
            Security_entry.delete(0,END)
            Security_entry.insert(0,'You have to enter the security code!')
            Security_entry.update()
            sleep(2)
            Security_entry.delete(0,END)
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            
        
        elif int(Security_entry.get())!=Security_code['text']:
            Security_entry.delete(0,END)
            Security_entry.insert(0,'Incorrect Security Code!')
            Security_entry.update()
            sleep(2)
            Security_entry.delete(0,END)
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            
        if lname_entry.get()=='':
            lname_entry.delete(0,END)
            lname_entry.insert(0,'!!You hve to Enter your name!!')
            lname_entry.update()
            sleep(2)
            lname_entry.delete(0,END)
            lname_entry.update()
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            
        elif fname_entry.get()=='':
            fname_entry.delete(0,END)
            fname_entry.insert(0,'!!You hve to Enter your name!!')
            fname_entry.update()
            sleep(2)
            fname_entry.delete(0,END)
            fname_entry.update()
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            

        if ID_entry.get()=='':
            ID_entry.delete(0,END)
            ID_entry.insert(0,'!!You hve to Enter your ID code!!')
            ID_entry.update()
            sleep(2)
            ID_entry.delete(0,END)
            ID_entry.update()
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            
        elif len(ID_entry.get())<10:
            ID_entry.delete(0,END)
            ID_entry.insert(0,'!!ID Code is not correct!!')
            ID_entry.update()
            sleep(2)
            ID_entry.delete(0,END)
            ID_entry.update()
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            
        if '+98' in phone_entry.get():
            for _ in range(3):
                phone_entry.delete(0)
            phone_entry.insert(0,'0')
            phone_entry.update()
            sleep(1)
        if phone_entry.get()=='':
            phone_entry.delete(0,END)
            phone_entry.insert(0,'!!You hve to Enter your phone number!!')
            phone_entry.update()
            sleep(2)
            phone_entry.delete(0,END)
            phone_entry.update()
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            
        elif len(phone_entry.get())!=11:
            phone_entry.delete(0,END)
            phone_entry.insert(0,'!!Phone Number is not correct!!')
            phone_entry.update()
            sleep(2)
            phone_entry.delete(0,END)
            phone_entry.update()
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            
        if post_entry.get()=='':
            post_entry.delete(0,END)
            post_entry.insert(0,'!!You hve to Enter your postal code!!')
            post_entry.update()
            sleep(2)
            post_entry.delete(0,END)
            post_entry.update()
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            
        elif len(post_entry.get())!=14:
            post_entry.delete(0,END)
            post_entry.insert(0,'!!Postal Code is not correct!!')
            post_entry.update()
            sleep(2)
            post_entry.delete(0,END)
            post_entry.update()
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            
        if address_entry.get()=='':
            address_entry.delete(0,END)
            address_entry.insert(0,'!!You hve to Enter your password!!')
            address_entry.update()
            sleep(2)
            address_entry.delete(0,END)
            address_entry.update()
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            
        if birth_year.get()=='':
            birth_year.delete(0,END)
            birth_year.insert(0,'Mandatory')
            birth_year.update()
            sleep(2)
            birth_year.delete(0,END)
            birth_year.update()
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            
        elif 2022<int(birth_year.get()) or 1892>int(birth_year.get()):
            birth_year.delete(0,END)
            birth_year.insert(0,'Incorrect')
            birth_year.update()
            sleep(2)
            birth_year.delete(0,END)
            birth_year.update() 
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            
        if birth_day.get()=='':
            birth_day.delete(0,END)
            birth_day.insert(0,'Mandatory')
            birth_day.update()
            sleep(2)
            birth_day.delete(0,END)
            birth_day.update()
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
            
        elif 31<int(birth_day.get()) or 1>int(birth_day.get()):
            birth_day.delete(0,END)
            birth_day.insert(0,'Incorrect')
            birth_day.update()
            sleep(2)
            birth_day.delete(0,END)
            birth_day.update() 
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
        
            
        if password_entry.get()=='':
            password_entry.delete(0,END)
            password_entry.insert(0,'!!You hve to Enter your password!!')
            password_entry.update()
            sleep(2)
            password_entry.delete(0,END)
            password_entry.update()
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()
        elif len(password_entry.get())<8:
            password_entry.delete(0,END)
            password_entry.insert(0,'!Please choose a harder password!')
            password_entry.update()
            sleep(2)
            password_entry.delete(0,END)
            password_entry.update()
            Security_code.config(text=randint(1010,9999))
            Security_entry.update()

        if kwargs['firstname']!='' and kwargs['lastname']!='' and kwargs['ID_code']!='' and kwargs['phone_number']!='' and kwargs['postal_code']!='' and kwargs['address']!='' and kwargs['year']!='' and kwargs['choose_month']!='Month' and kwargs['birthday']!='' and kwargs['password']!='' and str(Security_entry.get())==str(Security_code['text']):
            database.update(kwargs)
            person_1=open('data.py','w')
            person_1.write(str(database))
            person_1.close()
            success_notif=Label(text='Sign up was successful!',font=('arial rounded mt bold',18),bg='#454545',fg='#effb41')
            success_notif.place(x=100,y=425)
            success_notif.update()
            success_notif.update()
            sleep(1.5)
            check='true'
            success_notif.config(text=f'Hello {fname_entry.get()}',font=('arial rounded mt bold',18))
            success_notif.place(x=165,y=425)
            success_notif.update()
            break
        else:
            break

def card_info(**kwargs):
    global check_card,check
    global card_number_graphic
    global database
    global mnth,year_show,slsh,cvv2_showval,name_card
    if check=='true':
        while True:
            if cardnum_entry.get()=='':
                cardnum_entry.delete(0,END)
                cardnum_entry.insert(0,'!!You hve to Enter your card number!!')
                cardnum_entry.update()
                sleep(2)
                cardnum_entry.delete(0,END)
                card_number_graphic=Label(root,text='****   ****   ****   ****',font=('arial rounded mt bold',25),bg='#ef4461',fg='#fcdede')
                card_number_graphic.place(x=742,y=570)
                mnth=Label(root,text='--',font=('arial rounded mt bold',20),bg='#ef4461',fg='#fcdede').place(x=935,y=625)
                slsh=Label(root,text='/',font=('arial rounded mt bold',20),bg='#ef4461',fg='#fcdede').place(x=965,y=625)
                year_show=Label(root,text='--',font=('arial rounded mt bold',20),bg='#ef4461',fg='#fcdede').place(x=985,y=625)
                cardnum_entry.update()

            if len(cardnum_entry.get())!=16:
                cardnum_entry.delete(0,END)
                cardnum_entry.insert(0,'!!Card Number is not correct!!')
                cardnum_entry.update()
                sleep(2)
                cardnum_entry.delete(0,END)
                card_number_graphic=Label(root,text='****   ****   ****   ****',font=('arial rounded mt bold',25),bg='#ef4461',fg='#fcdede')
                card_number_graphic.place(x=742,y=575)
                mnth=Label(root,text='--',font=('arial rounded mt bold',20),bg='#ef4461',fg='#fcdede').place(x=935,y=625)
                slsh=Label(root,text='/',font=('arial rounded mt bold',20),bg='#ef4461',fg='#fcdede').place(x=965,y=625)
                year_show=Label(root,text='--',font=('arial rounded mt bold',20),bg='#ef4461',fg='#fcdede').place(x=985,y=625)
                cardnum_entry.update()
            elif len(cardnum_entry.get())==16:
                cardnum_entry.insert(4,'-')
                cardnum_entry.insert(9,'-')
                cardnum_entry.insert(14,'-')
            if cvv2_entry.get()=='':
                cvv2_entry.delete(0,END)
                cvv2_entry.insert(0,'!!You hve to Enter your CVV2!!')
                cvv2_entry.update()
                sleep(2)
                cvv2_entry.delete(0,END)
                cvv2_entry.update()
            elif len(cvv2_entry.get())!=3 and len(cvv2_entry.get())!=4:
                cvv2_entry.delete(0,END)
                cvv2_entry.insert(0,'!!CVV2 is not correct!!')
                cvv2_entry.update()
                sleep(2)
                cvv2_entry.delete(0,END)
                cvv2_entry.update()
            if kwargs['card_number']!='' and kwargs['cvv2']!='' and kwargs['expiration_year']!=''and kwargs['expiration_month']!='' and len(kwargs['card_number'])==16 and len(kwargs['cvv2'])==3 or len(kwargs['cvv2'])==4:
                kwargs['amount']=account_balance
                account_id=kwargs['card_number']
                account_id=database
                account_id.update(kwargs)
                person_1=open('data.py','w')
                person_1.write(str(database))
                person_1.close()
                welcome_label.config(text=f'Welcome {fname_entry.get()} {lname_entry.get()}')
                counter=0
                cardnum_prt1=''
                cardnum_prt2=''
                cardnum_prt3=''
                cardnum_prt4=''
                for i in str(cardnum_entry.get()):
                    counter+=1
                    if i=='-':
                        counter-=1
                        continue
                    if counter<5:
                        cardnum_prt1+=str(i)
                    elif counter<9:
                        cardnum_prt2+=str(i)
                    elif counter<13:
                        cardnum_prt3+=str(i)
                    elif counter<17:
                        cardnum_prt4+=str(i)
                    else:
                        continue
                card_number_graphic.config(text=f'{cardnum_prt1}   {cardnum_prt2}   {cardnum_prt3}   {cardnum_prt4}',font=('arial rounded mt bold',25),bg='#ef4461',fg='#fcdede')
                card_number_graphic.place(x=690,y=575)
                cvv2_showval.config(text=cvv2_entry.get(),font=('arial rounded mt bold',15),bg='#ef4461',fg='#fcdede')
                cvv2_showval.place(x=1029,y=528)
                mnth.config(text=Edate_month_entry.get(),font=('arial rounded mt bold',15),bg='#ef4461',fg='#fcdede')
                mnth.place(x=935,y=625)
                year_show.config(text=Edate_year_entry.get(),font=('arial rounded mt bold',15),bg='#ef4461',fg='#fcdede')
                name_card.config(text=f'{fname_entry.get()} {lname_entry.get()}',font=('arial rounded mt bold',12),bg='#ef4461',fg='#fcdede')
                name_card.place(x=700,y=655)
                account_balance.config(text=f'{account_balance.get()} RIALS')
                break
            else:
                break
    else:
        error=Label(text='!!You have to create an account!!',font=('arial rounded mt bold',18),bg='#454545',fg='#effb41')
        error.place(x=45,y=425)
        error.update()
        sleep(4)
        error.config(text='')

def recode():
    Security_code.config(text=randint(1010,9999))
    Security_entry.update()

def transfer():
    global account_balance
    while True:
        if origin_cardnum_entry.get()=='':
            origin_cardnum_entry.delete(0,END)
            origin_cardnum_entry.insert(0,'!!You hve to enter origin card number!!')
            origin_cardnum_entry.update()
            sleep(2)
            origin_cardnum_entry.delete(0,END)
            origin_cardnum_entry.update()
        elif len(origin_cardnum_entry.get())!=16:
            origin_cardnum_entry.delete(0,END)
            origin_cardnum_entry.insert(0,'!!Card Number is not correct!!')
            origin_cardnum_entry.update()
            sleep(2)
            origin_cardnum_entry.delete(0,END)
            origin_cardnum_entry.update()

        if destination_cardnum_entry.get()=='':
            destination_cardnum_entry.delete(0,END)
            destination_cardnum_entry.insert(0,'!!You hve to enter destination card number!!')
            destination_cardnum_entry.update()
            sleep(2)
            destination_cardnum_entry.delete(0,END)
            destination_cardnum_entry.update()
        elif len(destination_cardnum_entry.get())!=16:
            destination_cardnum_entry.delete(0,END)
            destination_cardnum_entry.insert(0,'!!Card Number is not correct!!')
            destination_cardnum_entry.update()
            sleep(2)
            destination_cardnum_entry.delete(0,END)
            destination_cardnum_entry.update()
        if amount_num_entry.get()=='':
            amount_num_entry.delete(0,END)
            amount_num_entry.insert(0,'!!You have to enter the transfer amount!!')
            amount_num_entry.update()
            sleep(2)
            amount_num_entry.delete(0,END)
            amount_num_entry.update()
        elif int(amount_num_entry.get())<50000 or int(amount_num_entry.get())>100000000:
            amount_num_entry.delete(0,END)
            amount_num_entry.insert(0,'!!Invalid Amount!!')
            amount_num_entry.update()
            sleep(2)
            amount_num_entry.delete(0,END)
            amount_num_entry.update()
        else:
            d_card='_'+str(destination_cardnum_entry.get())
            account_balance=int(account_balance)+int(amount_num_entry.get())
            d_card['amount']=int(d_card['amount'])-int(amount_num_entry.get())
 
            break



    
Label(bg='#ef4461',height=15,width=60).place(x=680,y=460)
create_title_label=Label(root,text='Create Your Account!',font=('arial rounded mt bold',25),bg='#454545',fg='#f07a97')
create_title_label.place(x=50,y=20)
firstname=Label(root,text='Firstname',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
firstname.place(x=20,y=80)
fname_entry=Entry(root,text='Firstname',width=40,bg='#f19372',fg='black')
fname_entry.place(x=170,y=85)

lastname=Label(root,text='Lastname',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
lastname.place(x=20,y=108)
lname_entry=Entry(root,text='Lastname',width=40,bg='#f19372',fg='black')
lname_entry.place(x=170,y=113)
ID_code=Label(root,text='ID Code',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
ID_code.place(x=20,y=136)
ID_entry=Entry(root,width=40,bg='#f19372',fg='black')
ID_entry.place(x=170,y=141)

phone_number=Label(root,text='Phone Number',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
phone_number.place(x=20,y=164)
phone_entry=Entry(root,width=40,bg='#f19372',fg='black')
phone_entry.place(x=170,y=169)

postal_code=Label(root,text='Postal Code',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
postal_code.place(x=20,y=192)
post_entry=Entry(root,text='Postal Code',width=40,bg='#f19372',fg='black')
post_entry.place(x=170,y=197)

address=Label(root,text='address',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
address.place(x=20,y=220)
address_entry=Entry(root,width=40,bg='#f19372',fg='black')
address_entry.place(x=170,y=225)

birth=Label(root,text='Date of birth',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
birth.place(x=20,y=248)
year=Label(root,text='Year',bg='#454545',fg='#f19372',font=('arial rounded mt bold',8))
year.place(x=165,y=253)
birth_year=Entry(root,width=8,bg='#f19372',fg='black')
birth_year.place(x=195,y=253)
choose_month=Spinbox(root,values=['Month','January','February','March','April','May','June','July','August','September','October','November','December'],width=10,bg='#f19372',fg='black')
choose_month.place(x=256,y=253)
birthday=Label(root,text='Day',bg='#454545',fg='#f19372',font=('arial rounded mt bold',8))
birthday.place(x=335,y=253)
birth_day=Entry(root,width=8,bg='#f19372',fg='black')
birth_day.place(x=362,y=253)


password=Label(root,text='Password',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
password.place(x=20,y=276)
password_entry=Entry(root,width=40,bg='#f19372',fg='black')
password_entry.place(x=170,y=281)


email=Label(root,text='Email (optional)',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
email.place(x=20,y=304)
email_entry=Entry(root,width=40,bg='#f19372',fg='black')
email_entry.place(x=170,y=309)

Security_label=Label(root,text='Security code',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
Security_label.place(x=20,y=332)

Security_code=Label(root,text=randint(1111,9999),font=('arial rounded mt bold',14),bg='white',fg='#454545')
Security_code.place(x=170,y=334)

recode_btn=Button(text='🔄',font=('arial rounded mt bold',12),bg='#454545',fg='#fcdede',command=recode)
recode_btn.place(x=220,y=333) 

Security_entry=Entry(root,width=22,bg='#f19372',fg='black')
Security_entry.place(x=278,y=337)

Label(bg='#fcdede').pack(anchor=NW,padx=500,fill=Y,expand=True)

Label(root,text='______________________________________',font=('arial rounded mt bold',11,'bold'),bg='#ef4461',fg='#fcdede',height=1).place(x=716,y=492)
Label(root,bg='#effb41',width=8,height=2).place(x=715,y=525)

card_number_graphic=Label(root,text='****   ****   ****   ****',font=('arial rounded mt bold',25),bg='#ef4461',fg='#fcdede')
card_number_graphic.place(x=742,y=575)
welcome_label=Label(root,text='Welcome Dear User',font=('arial rounded mt bold',35),bg='#454545',fg='#f07a97')
welcome_label.place(x=670,y=10)

Label(root,text='DEBIT CARD',font=('arial rounded mt bold',15),bg='#ef4461',fg='#fcdede').place(x=960,y=470)
Label(root,text='VALID\n THRU',font=('arial rounded mt bold',9),bg='#ef4461',fg='#fcdede').place(x=890,y=625)
mnth=Label(root,text='--',font=('arial rounded mt bold',20),bg='#ef4461',fg='#fcdede')
mnth.place(x=935,y=625)
slsh=Label(root,text='/',font=('arial rounded mt bold',20),bg='#ef4461',fg='#fcdede')
slsh.place(x=970,y=620)
year_show=Label(root,text='--',font=('arial rounded mt bold',20),bg='#ef4461',fg='#fcdede')
year_show.place(x=985,y=625)

cvv2_show=Label(root,text='CVV2:',font=('arial rounded mt bold',15),bg='#ef4461',fg='#fcdede')
cvv2_show.place(x=960,y=528)


cvv2_showval=Label(root,text='....',font=('arial rounded mt bold',15),bg='#ef4461',fg='#fcdede')
cvv2_showval.place(x=1030,y=524)

name_card=Label(root,text='Card Holder',font=('arial rounded mt bold',15),bg='#ef4461',fg='#fcdede')
name_card.place(x=713,y=645)


Label(text='Money Transfer',font=('arial rounded mt bold',20),bg='#454545',fg='#fcb499').place(x=785,y=172)
account_balance=5400000000

Label(text='ACCOUNT BALANCE:',font=('arial rounded mt bold',20,'bold'),bg='#454545',fg='#fcdede').place(x=620,y=100)
account_balance=Label(text='                       RIALS',font=('arial rounded mt bold',21,'bold'),bg='#454545',fg='#fcdede')
account_balance.place(x=938,y=102)

origin_cardnum=Label(root,text='Origin Card Number',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
origin_cardnum.place(x=650,y=225)

origin_cardnum_entry=Entry(root,font=('arial rounded mt bold',14),width=25,bg='#f19372',fg='black')
origin_cardnum_entry.place(x=850,y=227)

destination_cardnum=Label(root,text='Destination Card Number',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
destination_cardnum.place(x=604,y=267)
destination_cardnum_entry=Entry(root,font=('arial rounded mt bold',14),width=25,bg='#f19372',fg='black')
destination_cardnum_entry.place(x=850,y=267)

amount_num=Label(root,text='Amount',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
amount_num.place(x=760,y=310)
amount_num_entry=Entry(root,font=('arial rounded mt bold',14),width=25,bg='#f19372',fg='black')
amount_num_entry.place(x=850,y=310)

Label(text='Minimum: 50,000 Rials\nMaximum: 100,000,000 Rials',font=('arial rounded mt bold',10),bg='#454545',fg='#effb41').place(x=567,y=308)
    

transfer_btn=Button(root,text='TRANSFER',font=('arial rounded mt bold',15),bg='#f07a97',fg='black',command=transfer)
transfer_btn.place(x=930,y=355)


sign_up_btn=Button(root,text='SIGN UP',font=('arial rounded mt bold',15),bg='#f07a97',fg='black',command=lambda: create_database(firstname=fname_entry.get(),lastname=lname_entry.get(),
ID_code=ID_entry.get(),phone_number=phone_entry.get(),postal_code=post_entry.get(),address=address_entry.get(),year=birth_year.get()
,choose_month=choose_month.get(),birthday=birth_day.get(),password=password_entry.get(),email=email_entry.get()))
sign_up_btn.place(x=215,y=380)

Enter_card_title=Label(root,text='Enter your card information!',font=('arial rounded mt bold',25),bg='#454545',fg='#f07a97')
Enter_card_title.place(x=15,y=458)

card_number=Label(root,text='Card Number',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
card_number.place(x=20,y=505)
cardnum_entry=Entry(root,width=40,bg='#f19372',fg='black')
cardnum_entry.place(x=170,y=510)

cvv2=Label(root,text='CVV2',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
cvv2.place(x=20,y=538)
cvv2_entry=Entry(root,width=40,bg='#f19372',fg='black')
cvv2_entry.place(x=170,y=542)

expiration_date=Label(root,text='Expiration Date',font=('arial rounded mt bold',14),bg='#454545',fg='#f07a97')
expiration_date.place(x=20,y=570)
Edate_year_entry=Spinbox(root,value=['year','22','23','24','25','26','27'],width=10,bg='#f19372',fg='black')
Edate_year_entry.place(x=208,y=575)
slash=Label(root,text='/',font=('arial rounded mt bold',15),bg='#454545',fg='#f19372')
slash.place(x=288,y=573)
Edate_month_entry=Spinbox(root,value=['month','01','02','03','04','05','06','07','08','09','10','11','12'],width=10,bg='#f19372',fg='black')
Edate_month_entry.place(x=308,y=575)

submit_card_info=Button(root,text='SUBMIT',font=('arial rounded mt bold',15),bg='#f07a97',fg='black',
command=lambda:card_info(card_number=cardnum_entry.get(),cvv2=cvv2_entry.get(),expiration_month=Edate_month_entry.get(),expiration_year=Edate_year_entry.get(),amount=account_balance))
submit_card_info.place(x=215,y=625)


root.mainloop()
