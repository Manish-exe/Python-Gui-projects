from tkinter import *
import datetime

def date_time():
    #Time function
    time = datetime.datetime.now()  
    hr = time.strftime("%H")
    mi = time.strftime("%M")
    sec = time.strftime("%S")
    am =  time.strftime("%p")

    lab_hr.config(text = hr)
    lab_min.config(text = mi)
    lab_sec.config(text = sec)
    lab_am.config(text = am)

    #Date function
    date = time.strftime("%d")
    month = time.strftime("%m")
    yr = time.strftime("%Y")
    day = time.strftime("%a")
   
    lab_date.config(text=date)
    lab_mon.config(text=month)
    lab_yr.config(text=yr)
    lab_day.config(text=day)

    lab_hr.after(200,date_time) # it recalls the program after 200ms

clock = Tk()
clock.title("    ****Digital Clock****    ")
clock.geometry('900x550')
clock.config(bg = 'black')

## Time ------------------------
lab_hr = Label(clock,text='00',font= ('Times New Roman',60,'bold'),bg='black',fg='white')
lab_hr.place(x=100,y=40,height=110,width=100)

lab_hr_txt = Label(clock,text='Hour',font= ('Times New Roman',30,'bold'),bg='black',fg='white')
lab_hr_txt.place(x=100,y=200,height=50,width=100)

lab_min = Label(clock,text='00',font= ('Times New Roman',60,'bold'),bg='black',fg='white')
lab_min.place(x=300,y=40,height=110,width=100)

lab_min_txt = Label(clock,text='Min',font= ('Times New Roman',30,'bold'),bg='black',fg='white')
lab_min_txt.place(x=300,y=200,height=50,width=100)

lab_sec = Label(clock,text='00',font= ('Times New Roman',60,'bold'),bg='black',fg='white')
lab_sec.place(x=500,y=40,height=110,width=100)

lab_sec_txt = Label(clock,text='Sec',font= ('Times New Roman',30,'bold'),bg='black',fg='white')
lab_sec_txt.place(x=500,y=200,height=50,width=100)

lab_am = Label(clock,text='00',font= ('Times New Roman',50,'bold'),bg='black',fg='white')
lab_am.place(x=700,y=40,height=110,width=100)

lab_am_txt = Label(clock,text='AM/PM',font= ('Times New Roman',25,'bold'),bg='black',fg='white')
lab_am_txt.place(x=700,y=200,height=50,width=110)


#-----------------x----------------x---Date---x----------------------x------------------#
lab_date = Label(clock,text='00',font= ('Times New Roman',60,'bold'),bg='black',fg='white')
lab_date.place(x=100,y=300,height=110,width=100)

lab_date_txt = Label(clock,text='Date',font= ('Times New Roman',30,'bold'),bg='black',fg='white')
lab_date_txt.place(x=100,y=460,height=50,width=100)

lab_mon = Label(clock,text='00',font= ('Times New Roman',60,'bold'),bg='black',fg='white')
lab_mon.place(x=300,y=300,height=110,width=100)

lab_mon_txt = Label(clock,text='Month',font= ('Times New Roman',30,'bold'),bg='black',fg='white')
lab_mon_txt.place(x=300,y=460,height=50,width=100)

lab_yr = Label(clock,text='00',font= ('Times New Roman',60,'bold'),bg='black',fg='white')
lab_yr.place(x=480,y=300,height=110,width=150)

lab_yr_txt = Label(clock,text='Year',font= ('Times New Roman',30,'bold'),bg='black',fg='white')
lab_yr_txt.place(x=500,y=460,height=50,width=100)

lab_day = Label(clock,text='00',font= ('Times New Roman',45,'bold'),bg='black',fg='white')
lab_day.place(x=700,y=300,height=110,width=100)

lab_day_txt = Label(clock,text='Day',font= ('Times New Roman',30,'bold'),bg='black',fg='white')
lab_day_txt.place(x=700,y=460,height=50,width=100)

date_time()
clock.mainloop()