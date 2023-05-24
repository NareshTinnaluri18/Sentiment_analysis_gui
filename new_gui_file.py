# import pandas as pd
# import tkinter  as tk 
# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# # root = Tk()
# my_w = tk.Tk()
# tree = ttk.Treeview(my_w, displaycolumns='#all')

# #my_w.geometry("500x350") 
# width = 1920
# height = 1080
# screen_width = my_w.winfo_screenwidth()
# screen_height = my_w.winfo_screenheight()
# x = (screen_width/2) - (width/2)
# y = (screen_height/2) - (height/2)
# my_w.geometry("%dx%d+%d+%d" % (1920, 1080, x, y))
# my_w.resizable(0, 0) # Size of the window 
# my_w.title('GUI')

# my_font1=('times', 12, 'bold')
# lb1 = tk.Label(my_w,text='Read File & create DataFrame',
#     width=30,font=my_font1)  
# lb1.grid(row=1,column=1)
# b1 = tk.Button(my_w, text='Browse File', 
#    width=20,command = lambda:upload_file())
# b1.grid(row=2,column=1,pady=5) 
# lb2=tk.Label(my_w,width=40,text='',bg='lightyellow')
# lb2.grid(row=3,column=1,padx=5)
# l1=[] # List to hold headers of the Treeview 


# def upload_file():
#     global df ,l1
#     f_types = [('CSV files',"*.csv"),('All',"*.*")]
#     file = filedialog.askopenfilename(filetypes=f_types)
#     lb1.config(text=file) # display the path 
#     df=pd.read_csv(file,encoding='ISO-8859-1') # create DataFrame
#     l1=list(df) # List of column names as header 
#     l1=['S No', 'Text']
#     str1="Rows:" + str(df.shape[0])+ " , Columns:"+str(df.shape[1])
#     #print(str1)
#     lb2.config(text=str1) # add to Text widget
#     trv_refresh() # show Treeview 
	
# def trv_refresh(): # Refresh the Treeview to reflect changes
#     global df,trv,l1 
#     r_set=df.to_numpy().tolist() # create list of list using rows
    
#     trv=ttk.Treeview(my_w,selectmode='browse',height=1080,
#         show='headings',columns=l1,)
#     trv.grid(row=4,column=1,columnspan=3,padx=10,pady=20)
    
#     for i in l1:
#         trv.column(i,width=90,anchor='c')
#         trv.heading(i,text=str(i))
#     for dt in r_set:
#         v=[r for r in dt]
#         trv.insert("",'end',iid=v[0],values=v)
# my_w.mainloop()  # Keep the window open

# from tkinter import *
# import os
# import time
# from tkinter import simpledialog

# def new_window():
#     global screen6
#     screen6 = Toplevel(screen)
#     screen6.title("Sucess")
#     screen6.geometry("150x100")
#     Label("screen4", text = "New Window Openned Successfully").pack()

# def login():
#     global screen2
#     screen2 = Toplevel(screen)
#     screen2.title("Login")
#     screen2.geometry("530x290")
#     Label(screen2, text = "please enter details below to login").pack()
#     Label(screen2, text = "").pack()
   
#     calibration1 = StringVar()
#     calibration2 = StringVar()
#     calibration3 = StringVar()
   
#     global calibration1_entry
#     global calibration2_entry
#     global calibration3_entry
   
#     calibration1_entry= Entry(screen2, textvariable = calibration1).place(x=350, y=70)
#     calibration2_entry = Entry(screen2, textvariable = calibration2).place(x=350, y=120)
#     calibration3_entry = Entry(screen2, textvariable = calibration3).place(x=350, y=170)

# def main_screen():
#     global screen
#     screen = Tk()
#     screen.geometry("530x290")
#     screen.title("Remote Monitoring Site 1")
#     Label(text = "Remote Monitoring Site 1", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
#     Label(text = "").pack()
#     Button(text = "Login", width = "30", height = "2", command = login).pack()
#     Label(text = "").pack()
   
#     screen.mainloop()

# main_screen()

import tkinter as tk

def do_something(phrase):
    return phrase + phrase

def main():
    root = tk.Tk()
    root.title("Demo")

    tk.Label(root, text="Please enter a sentence: ").grid(row=0)
    user_input = tk.Entry(root)
    user_input.grid(row=0, column=1)
    result = tk.Label(root, text='')
    result.grid(row=2, column=0, columnspan=2)
    btn = tk.Button(root, text='Do something')
    btn.config(command=lambda: result.config(text=do_something(user_input.get())))
    btn.grid(row=1, column=1, sticky=tk.W, pady=4)

    root.mainloop()

if __name__ == "__main__":
    main()