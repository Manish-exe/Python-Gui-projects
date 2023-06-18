import tkinter as tk
import random
import string



str = ""
def encryption():
    message = lab_in.get(1.0,tk.END)
    words = message.split()
    global str
    for word in words:
        if (len(word)>=3):
            en1= word[1:]+word[0]
            character = string.ascii_letters + string.digits + string.punctuation
            rndstr1 = random.sample(character,3)
            rndstr2 = random.sample(character,3)
            en2= "".join(rndstr1) + en1 + "".join(rndstr2)
            str = str + " " + en2
            # print(str)
        else:
            en3 = word[::-1]
            str = str + " " +en3
    lab_out.insert(1.0,f"{str}")
    print(str)

def decryption():
     
     str1=""
     message = lab_in.get(1.0,tk.END)
     nwords = message.split()
     for nword in nwords:
        if(len(nword)>=3):
            str1 = str1 + nword[-4]+  nword[3:len(nword)-4] +" "

        else:
            str1 = str1 + nword[::-1] +  " "
     lab_out.insert(1.0,f"{str1}")

def clear():
    global str
    str = ""
    lab_in.delete(1.0,tk.END)
    lab_out.delete(1.0,tk.END)

root = tk.Tk()
root.title("Encrpt or decrpt")
root.geometry('500x600')
root.resizable(False,False)

lab_entry = tk.Label(text = 'Enter the text to encrpt or decrypt',width=50,height=2,font=('Arial',11,'bold')).place(x=20,y=10)
lab_in=tk.Text(root,width=50,height=10,font=("arial",11,"bold"))
lab_in.place(x=50,y=50)


tk.Button(root,text='Encrpt',width=20 ,height=2,font=("arial",10,"bold"),bg='red',fg='white',command =lambda: encryption()).place(x=70,y=250)
tk.Button(root,text='Decrpt',width=20 ,height=2,font=("arial",10,"bold"),bg='blue',fg='white',command =lambda: decryption()).place(x=270,y=250)
tk.Button(root,text='Clear',width=40 ,height=2,font=("arial",10,"bold"),bg='#00CED1',fg='white',command= lambda: clear()).place(x=90,y=300)

lab_out = tk.Text(root,width=50,height=10)
lab_out.place(x=50,y=350)

# lab_out.insert(tk.END,)
# print(message)
root.mainloop()


