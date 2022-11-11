
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.tix import IMAGETEXT
entry=""
top = tk.Tk()
top.geometry('350x600')
top.configure(bg='#30BFBF')
top.resizable(False, False)
top.title('CRAIGSLIST')

#----------------------------------------------------------------STARTING ELEMENTS-----------------------------------------------------------------
my_font1 = ('Times',18,'bold')
my_font2 = ('Times',16,'bold')
my_font3 = ('Times',12)

click_btn1= PhotoImage(file='logo.png')

img_label= Label(image=click_btn1,height = 2, width = 2)
ttk.Button(top, image=click_btn1, width=1).place(x=80,y=15)

l = Label(top, text="\nJOBS\n", font= my_font1, bg='#30BFBF', fg = 'white')
l.pack()

l=Label(top,text="\n____________________________________________________________________________________________________",bg='#30BFBF',fg="white").place(x=0,y=65)

#--------------------------------------------------------------------------------------------------------------------------

def fun1():  
    messagebox.showinfo("No Search Results", "\nCurrently not recruiting : (")

def fun2():
    root =Toplevel(top)
    root.geometry('350x600')
    root.configure(bg='#30BFBF')
    root.resizable(False, False)
    root.title('CRAIGSLIST')

    my_font1 = ('Times',18,'bold')
    my_font2 = ('Times',16,'bold')
    my_font3 = ('Times',12)
    
    click_btn3= PhotoImage(file='logo.png')
    img_label= Label(image=click_btn3,height = 2, width = 2)
    ttk.Button(root, image=click_btn3, width=1).place(x=100,y=15)
    
    l = Label(root, text="\nJOBS\n", font= my_font1, bg='#30BFBF', fg = 'white')
    l.pack()

    l=Label(root,text="____________________________________________________________________________________________________",bg='#30BFBF',fg="white").place(x=0,y=65)

    l = Label(root, text="\n CUSTOMER SERVICE\n", font= my_font2, bg='#30BFBF', fg = 'white')
    l.pack()

    #-----------------------------FOR SEARCH BUTTON---------------------------------------------------------------

    def display_text():
        string= entry.get()
        #label.configure(text=string)
        messagebox.showinfo("No Search Results","Sorry, there are currently no results available for your search   : (")
    
    click_btn= PhotoImage(file='button.png')
    img_label= Label(image=click_btn,height = 0.5, width = 1)
    ttk.Button(root, image=click_btn, width=1, command= display_text).place(x=234,y=164)
    #Create an Entry widget to accept User Input
    entry= Entry(root, width= 25)
    entry.focus_set()
    entry.place(x=100,y=165)

    #Create a Button to validate Entry Widget
    ttk.Button(root, image=click_btn, width=1, command= display_text).place(x=234,y=164)

    #-----------------------DRAGDROP MENU-------------------------------------------------------------------
    # Dropdown menu options
    options1 = [
        "List",
        "Thumb",
        "Gallery"
    ]
    
    # datatype of menu text
    clicked = StringVar()
    
    # initial menu text
    clicked.set( "List" )
    
    # Create Dropdown menu
    drop = OptionMenu( root , clicked , *options1 )
    drop.place(x=60,y=220)
    
    #------------------------------------------------------------------------------------------
    options2 = [
        "Newest",
        "Oldest"
    ]
    
    # datatype of menu text
    clicked = StringVar()
    
    # initial menu text
    clicked.set( "Newest" )
    
    # Create Dropdown menu
    drop = OptionMenu( root , clicked , *options2 )
    drop.place(x=210,y=220)
    
    #------------------------------------------OPTIONS ON MAIN PAGE------------------------------------------------------------------------------

    def fun1():  
        messagebox.showinfo("No Search Results", "\nCurrently not recruiting : (")

    b1 = Button(root ,text = "TECH Mahindra",command = fun1,height= 2, width=32, fg = "black",bg = "white")
    b1.place(x=60,y=300)

    b2 = Button(root ,text = "IGT Solutions",command = fun1,height= 2, width=32, fg = "black",bg = "white")
    b2.place(x=60,y=350)

    #-----------------------------FOR FOOTER-------------------------------------------------------------------------------------------
    l=Label(root,text="____________________________________________________________________________________________________",bg='#30BFBF',fg="white").place(x=0,y=440)

    label1=Label(root, text="Help,FAQs", font=("Times 12 bold"),bg='#30BFBF',fg='white')
    label1.place(x=60,y=480)

    label1=Label(root, text="About", font=("Times 12 bold"),bg='#30BFBF',fg='white')
    label1.place(x=200,y=480)

    label1=Label(root, text="Safety", font=("Times 12 bold"),bg='#30BFBF',fg='white')
    label1.place(x=60,y=500)

    label1=Label(root, text="CL is Hiring", font=("Times 12 bold"),bg='#30BFBF',fg='white')
    label1.place(x=200,y=500)

    label1=Label(root, text="Terms of Use", font=("Times 12 bold"),bg='#30BFBF',fg='white')
    label1.place(x=60,y=520)

    label1=Label(root, text="Feedback", font=("Times 12 bold"),bg='#30BFBF',fg='white')
    label1.place(x=200,y=520)

    label1=Label(root, text="Privacy Policy", font=("Times 12 bold"),bg='#30BFBF',fg='white')
    label1.place(x=60,y=540)

    label1=Label(root, text="Craigslist App", font=("Times 12 bold"),bg='#30BFBF',fg='white')
    label1.place(x=200,y=540)    

    lang_python = IMAGETEXT.PhotoImage(Image.open("button.png").resize((0,0)))
    lang_python_label = Label(image=lang_python,borderwidth = 0).place(x=1000,y=1000)


#----------------------------------------FOR BUTTONS--------------------------------------------------------------------------------------------------------------
b1 = Button(top ,text = "Customer Service",command = fun2,height= 2, width=15, fg = "black",bg = "white")
b1.place(x=60,y=120)

b2 = Button( top,text = "Manufacturing",command = fun1,height= 2, width=15, fg = "black",bg = "white")
b2.place(x=180,y=120)

b1 = Button(top ,text = "Human Resources",command = fun1,height= 2, width=15, fg = "black",bg = "white")
b1.place(x=60,y=175)

b2 = Button(top ,text = "Real Estate",command = fun1,height= 2, width=15, fg = "black",bg = "white")
b2.place(x=180,y=175)

b1 = Button(top ,text = "Legal/Paralegal",command = fun1,height= 2, width=15, fg = "black",bg = "white")
b1.place(x=60,y=230)

b2 = Button(top ,text = "Education",command = fun1,height= 2, width=15, fg = "black",bg = "white")
b2.place(x=180,y=230)

b1 = Button(top ,text = "Marketing",command = fun1,height= 2, width=15, fg = "black",bg = "white")
b1.place(x=60,y=285)

b2 = Button(top ,text = "Government",command = fun1,height= 2, width=15, fg = "black",bg = "white")
b2.place(x=180,y=285)

b1 = Button(top ,text = "Web Design",command = fun1,height= 2, width=15, fg = "black",bg = "white")
b1.place(x=60,y=340)

b2 = Button(top ,text = "Tech Support",command = fun1,height= 2, width=15, fg = "black",bg = "white")
b2.place(x=180,y=340)

b1 = Button(top ,text = "Writing",command = fun1,height= 2, width=15, fg = "black",bg = "white")
b1.place(x=60,y=395)

b2 = Button(top ,text = "Transport",command = fun1,height= 2, width=15, fg = "black",bg = "white")
b2.place(x=180,y=395)

#----------------------------------------FOR FOOTER--------------------------------------------------------------------------------------------------------------
l=Label(top,text="____________________________________________________________________________________________________",bg='#30BFBF',fg="white").place(x=0,y=440)

label1=Label(top, text="Help,FAQs", font=("Times 12 bold"),bg='#30BFBF',fg='white')
label1.place(x=60,y=480)

label1=Label(top, text="About", font=("Times 12 bold"),bg='#30BFBF',fg='white')
label1.place(x=200,y=480)

label1=Label(top, text="Safety", font=("Times 12 bold"),bg='#30BFBF',fg='white')
label1.place(x=60,y=500)

label1=Label(top, text="CL is Hiring", font=("Times 12 bold"),bg='#30BFBF',fg='white')
label1.place(x=200,y=500)

label1=Label(top, text="Terms of Use", font=("Times 12 bold"),bg='#30BFBF',fg='white')
label1.place(x=60,y=520)

label1=Label(top, text="Feedback", font=("Times 12 bold"),bg='#30BFBF',fg='white')
label1.place(x=200,y=520)

label1=Label(top, text="Privacy Policy", font=("Times 12 bold"),bg='#30BFBF',fg='white')
label1.place(x=60,y=540)

label1=Label(top, text="Craigslist App", font=("Times 12 bold"),bg='#30BFBF',fg='white')
label1.place(x=200,y=540)

top.mainloop()