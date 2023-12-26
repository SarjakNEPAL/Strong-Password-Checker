import tkinter as tk
from tkinter import ttk
from string import *

#main initializations
main=tk.Tk()
main.title("Is my password strong?")
main.geometry("500x300+20+20")
main.resizable(True,False)
main.iconbitmap('ico.ico')

#end of initializations

jojo=''
#variables

i=1
frame=ttk.Frame(main)
#functions

def desal():
    a.destroy()
    chk.destroy()
    b.destroy()
def exits():
    main.destroy()

def dispres(k,error):
    if k==True:
        tk.Label(main, text="Password is Strong enough").pack()
    else:
        tk.Label(main, text=f"password is no strong:\n    reasons:\n\t\t{error}").pack()
    
def check():
    desal()
    error=""
    pas=input_text.get("1.0", "end-1c") 
    pss=str(pas)
    input_text.destroy()

    succ=False
    speci=False
    uper=False
    lwer=False
    num=False
    
    if len(pss)>8:
        j=pss
        if "@" in j  or "!" in j or "$" in j or "%" in j or "_" in j or "-" in j or "=" in j:
            speci=True
            for i in j:
                if i.isupper()==True:uper=True
                if i.islower()==True:lwer=True
                if i.isdigit()==True:num=True
            if uper==True:
                if lwer==True:
                    if num==True:
                        succ=True
                    else:error+="\n Enter atleast a number"
                else:error+="\n Enter atleast a lowercase letter"
            else:error+="\n Enter atleast an uppercase"
        elif speci!=True:
            error=error+"\nEnter special character in the password"
    else:
        error=error+"\nPassword must be more than 8 characters"
    if succ==True:
        dispres(True,"")
    else: dispres(False,error)
    tk.Button(main, text="Exit",command= exits).pack()
#prompts

m="Password must contain at least 8 characters"
n="Password must contain at least 1 uppercase and lowecase character"
o="Password must contain at least a number and a special character"

#Labels
k=ttk.Label(main,text="Strong password checker version--- 0.0.1BETA---- BY SARJAK",font=("Helvetica", 100,))
a=ttk.Label(main, text="Enter Your password",font=("Helvetica", 25))
b=ttk.Label(main, text="Some ideas for Strong passwords: \n 1.{} \n 2.{} \n 3.{}".format(m,n,o))
input_text = tk.Text(main, height=5, width=30)

print()

#buttons
if(i<2):
    lolo="Check My Password"
else:
    lolo="Exit"
chk=ttk.Button(main, text=f"{lolo}",command=check)


#start of main codes
a.pack()
input_text.pack()
chk.pack()
b.pack()



#end of main codes



main.mainloop()
