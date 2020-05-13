import tkinter as tk

screen = tk.Tk()
screen.title("Tkinter Calculator Tutorial")
screen.geometry("355x460")
screen.resizable(0,0)

upper_frame = tk.Frame(screen,width = 314,bd=5)
upper_frame.pack(side = tk.TOP)

display = ""

storing_variable = tk.StringVar()

def click_button(x):
    global display
    display = display + str(x)
    storing_variable.set(display)

def clear_button():
    global display
    display = ""
    storing_variable.set(display)

def equal_button():
    global display
    result = str(eval(display))
    storing_variable.set(result)
    display = ""
    
    


input_frame = tk.Entry(upper_frame,textvariable = storing_variable,width = 25,font=('arial',14,'bold'),bg='powder blue',bd = 5,
                    insertwidth = 6)
input_frame.grid(row = 0,column = 0)

but1= tk.Button(screen,padx = 14,pady = 14,bd = 4,bg = 'white',text = '1',font= ("Courier New",14,'bold'),command = lambda:click_button(1))
but1.place(x = 10,y = 100)

but2=tk.Button(screen,padx=14,pady=14,bd=4,bg='white',text="2",font=("comicsansms",14,'bold'),command = lambda:click_button(2))
but2.place(x=10,y=170)

but3=tk.Button(screen,padx=14,pady=14,bd=4,bg='white',text="3",font=("comicsansms",14,'bold'),command = lambda:click_button(3))
but3.place(x=10,y=240)

but4=tk.Button(screen,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(4),text="4",font=("comicsansms",14,'bold'))
but4.place(x=75,y=100)

but5=tk.Button(screen,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(5),text="5",font=("comicsansms",14,'bold'))
but5.place(x=75,y=170)

but6=tk.Button(screen,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(6),text="6",font=("comicsansms",14,'bold'))
but6.place(x=75,y=240)

but7=tk.Button(screen,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(7),text="7",font=("comicsansms",14,'bold'))
but7.place(x=140,y=100)

but8=tk.Button(screen,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(8),text="8",font=("comicsansms",14,'bold'))
but8.place(x=140,y=170)

but9=tk.Button(screen,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(9),text="9",font=("comicsansms",14,'bold'))
but9.place(x=140,y=240)

but0=tk.Button(screen,padx=14,pady=14,bd=4,bg='white',command=lambda:click_button(0),text="0",font=("comicsansms",14,'bold'))
but0.place(x=10,y=310)

butdot=tk.Button(screen,padx=47,pady=14,bd=4,bg='white',command=lambda:click_button("."),text=".",font=("comicsansms",14,'bold'))
butdot.place(x=75,y=310)

butpl=tk.Button(screen,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:click_button("+"),font=("comicsansms",14,'bold'))
butpl.place(x=205,y=100)

butsub=tk.Button(screen,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:click_button("-"),font=("comicsansms",14,'bold'))
butsub.place(x=205,y=170)

butml=tk.Button(screen,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:click_button("*"),font=("comicsansms",14,'bold'))
butml.place(x=205,y=240)

butdiv=tk.Button(screen,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:click_button("/"),font=("comicsansms",14,'bold'))
butdiv.place(x=205,y=310)

butclear=tk.Button(screen,padx=14,pady=119,bd=4,bg='white',text="CE",command=clear_button,font=("comicsansms",14,'bold'))
butclear.place(x=270,y=100)

butequal=tk.Button(screen,padx=151,pady=14,bd=4,bg='white',command=equal_button,text="=",font=("comicsansms",14,'bold'))
butequal.place(x=10,y=380)
screen.mainloop()







