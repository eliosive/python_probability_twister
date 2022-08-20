import random  
import math
import tkinter as tk
import customtkinter as ct

# ----------------------------------------------------#
def game_generator():
    num = math.ceil(random.random()*3)
    if num ==1:
        game = ["true","false","false"]
    if num ==2:
        game = ["false","true","false"]
    if num ==3:
        game = ["false","false","true"]
    return game

def calc():
    countA=0
    countB=0
    countC=0
    count_correct=0
    newchoice = 0
    count_correct_new=0
    trials= int(entry.get())
    for i in range(trials):
        game = game_generator()
        if game[0]=="true":
            countA += 1
        elif game[1]=="true":
            countB += 1
        else:
            countC +=1  

        choice = math.ceil(random.random()*3) 
        if game[choice-1]=="true":
            count_correct +=1

        if choice==1:
            if game[1]=="false":
                game.pop(1)
                newchoice = 1
            else:
                game.pop(2)
                newchoice = 1
        if choice==2:
            if game[0]=="false":
                game.pop(0)
                newchoice = 1
            else:
                game.pop(2)
                newchoice = 0
        if choice==3:
            if game[1]=="false":
                game.pop(1)
                newchoice = 0
            else:
                game.pop(0)
                newchoice = 0
        if game[newchoice]=="true":
            count_correct_new+=1
    # displaying results#
    #-------------------------------------------------------#
    label_1.configure(text=str(countA))
    label_2.configure(text=str(countB))
    label_3.configure(text=str(countC))
    label_4.configure(text=str(count_correct/trials))
    label_5.configure(text=str(count_correct_new/trials))
    #-------------------------------------------------------#

# -------------------gui setup----------------------- #
root =ct.CTk()
root.title("Probability Twister")
root.geometry("500x500")

ct.set_appearance_mode("dark")  
ct.set_default_color_theme("blue")  


label = ct.CTkLabel(root,text ="Number of Trials")
label.pack(pady=30)
entry = tk.Entry(root)
entry.pack(pady=20)

button = ct.CTkButton(text="calc", command=calc)
button.pack()
label_12= ct.CTkLabel(root,text="Behind door 1")
label_12.pack()
label_1= ct.CTkLabel(root,text="")
label_1.pack()
label_22= ct.CTkLabel(root,text="Behind door 2")
label_22.pack()
label_2= ct.CTkLabel(root,text="")
label_2.pack()
label_32= ct.CTkLabel(root,text="Behind door 3")
label_32.pack()
label_3= ct.CTkLabel(root,text="")
label_3.pack()
label_42= ct.CTkLabel(root,text="probability without switching")
label_42.pack()
label_4= ct.CTkLabel(root,text="")
label_4.pack()
label_52= ct.CTkLabel(root,text="Probability with switching")
label_52.pack()
label_5= ct.CTkLabel(root,text="")
label_5.pack()

#-----------------------------------------------------#



root.mainloop()



