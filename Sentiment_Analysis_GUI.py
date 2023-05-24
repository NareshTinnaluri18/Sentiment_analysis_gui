import tkinter as Tk
import pandas as pd
from tkinter import *
from tkinter import ttk
import csv
root = Tk()
tree = ttk.Treeview(root, displaycolumns='#all')
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
import codecs
from re import search

df = pd.read_csv("output2.csv",encoding='ISO-8859-1')
df1 = pd.read_csv("exctracted.csv",encoding='ISO-8859-1')

my_font1=('times', 12, 'bold')
lb1 = Label(root,text='Read File & create DataFrame',
    width=30,font=my_font1)  

def load():
    f_types = [('CSV files',"*.csv"),('All',"*.*")]
    file = filedialog.askopenfilename(filetypes=f_types)
    lb1.config(text=file) # display the path 
    with open(file,encoding='ISO-8859-1') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            serial_number = row['Text']
            Mac_Id = row['Predicted Sentiment Score']
            tree.insert("", 0, values=(serial_number,Mac_Id))

def do_something(values):
    for index, row in df1.iterrows():
        if  values in row['Response']:
            print("index:",index, "Word_sentiment_Pairing:",row['Word_sentiment_Pairing'], "Sentiment_shade:",row['Sentiment_shade'],
                "social_behaviour_pattern:",row['social_behaviour_pattern'],"academic_distraction_problem:", row['academic_distraction_problem'])
            return index, row['Word_sentiment_Pairing'],row['Sentiment_shade'],row['social_behaviour_pattern'],row['academic_distraction_problem']

def Word_sentiment_Pairing(values):
    for index, row in df1.iterrows():
        if  values in row['Response']:
            return row['Word_sentiment_Pairing']

def Sentiment_shade(values):
    for index, row in df1.iterrows():
        if  values in row['Response']:
            return row['Sentiment_shade']
        
def social_behaviour_pattern(values):
    for index, row in df1.iterrows():
        if  values in row['Response']:
            return row['social_behaviour_pattern']
        
def academic_distraction_problem(values):
    for index, row in df1.iterrows():
        if  values in row['Response']:
            return row['academic_distraction_problem']

def Model_accuracy_dt():
    x="hi"
    return x
    
def predict():
    global screen2
    screen2 = Toplevel(root)
    screen2.title("Predicted_Analysis")
    screen2.geometry("530x290")
    item = tree.selection()[0]
    values = tree.item(tree.selection())['values'][0]
    result = Label(screen2, text=values)
    result.grid(row=2, column=0, columnspan=2)
    btn1 = Button(screen2, text='Predict',bg='#ffffff', activebackground='#00ff00')
    btn1.config(command=lambda: result.config(text=do_something(values)))
    btn2 = Button(screen2, text='Word_sentiment_Pairing',bg='#ffffff', activebackground='#00ff00')
    btn2.config(command=lambda: result.config(text=Word_sentiment_Pairing(values)))
    btn3 = Button(screen2, text='Sentiment_shade',bg='#ffffff', activebackground='#00ff00')
    btn3.config(command=lambda: result.config(text=Sentiment_shade(values)))
    btn4 = Button(screen2, text='social_behaviour_pattern',bg='#ffffff', activebackground='#00ff00')
    btn4.config(command=lambda: result.config(text=social_behaviour_pattern(values)))
    btn5 = Button(screen2, text='academic_distraction_problem',bg='#ffffff', activebackground='#00ff00')
    btn5.config(command=lambda: result.config(text=academic_distraction_problem(values)))
    btn6 = Button(screen2, text='Model accuracy score with decision-trees',bg='#ffffff', activebackground='#00ff00')
    btn6.config(command=lambda: result.config(text = "Model accuracy score with 10 decision-trees : 1.0000 \n Model accuracy score with 100 decision-trees : 1.0000"))
    btn6.grid(row=9, column=1, sticky=W, pady=4)
    btn7 = Button(screen2, text='Model accuracy score with K-Fold RF accuracy',bg='#ffffff', activebackground='#00ff00')
    btn7.config(command=lambda: result.config(text = "K-Fold RF accuracy : 0.30 "))
    btn7.grid(row=10, column=1, sticky=W, pady=4)
    btn1.grid(row=4, column=1, sticky=W, pady=4)
    btn2.grid(row=5, column=1, sticky=W, pady=4)
    btn3.grid(row=6, column=1, sticky=W, pady=4)
    btn4.grid(row=7, column=1, sticky=W, pady=4)
    btn5.grid(row=8, column=1, sticky=W, pady=4)
    
    screen2.mainloop()

def open_win():
   new= Toplevel(root)
   new.geometry("750x250")
   new.title("Predicted")
   Label(new, x, font=('Helvetica 17 bold')).pack(pady=30)

def OnDoubleClick(event):
    item = tree.selection()[0]
    values = tree.item(tree.selection())['values'][0]
    print("you clicked on", values)
    
    for index, row in df1.iterrows():
        if  values in row['Response']:
            print("index:",index, "Word_sentiment_Pairing:",row['Word_sentiment_Pairing'], "Sentiment_shade:",row['Sentiment_shade'],
                "social_behaviour_pattern:",row['social_behaviour_pattern'],"academic_distraction_problem:", row['academic_distraction_problem'])
    return values

root.title("Select Text for Predicting Sentiment Analysis")
width = 1920
height = 1080
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (1920, 1080, x, y))
root.resizable(0, 0)
TableMargin = Frame(root, width=1000)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Text"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Text', text="Text", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=1000)
tree.bind("<<TreeviewSelect>>", OnDoubleClick)
tree.pack()
button_submit = Button(text ="Browse File",width=20, command=load,bg='#ffffff', activebackground='#00ff00')
button_submit.place(rely=0.65, relx=0.10)
button_select =Button(text = "Predict", width = "30", height = "2", command = predict,bg='#ffffff', activebackground='#00ff00')
button_select.place(rely=0.90, relx=0.10)
Label(text = "").pack()
if __name__ == '__main__':
    root.mainloop()