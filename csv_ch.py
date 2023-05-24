from tkinter import *
import tkinter.ttk as ttk
import csv
import codecs
import pandas as pd
import csv
import time
from re import search
# Youtube Link: https://www.youtube.com/watch?v=PgLjwl6Br0k

from tkinter import *
import tkinter.ttk as ttk
import csv
import codecs
import pandas as pd
df = pd.read_csv("output2.csv",encoding='ISO-8859-1')
df1 = pd.read_csv("exctracted.csv",encoding='ISO-8859-1')
def OnDoubleClick(event):
    item = tree.selection()
    # print('item:', item)
    # print('event:', event)
    item = tree.selection()[0]
    #print("you clicked on", tree.item(item,"text"))
    values = tree.item(tree.selection())['values'][0]
    print("you clicked on", values)
    
    # filtering the rows where job is Govt
    for index, row in df1.iterrows():
        if  values in row['Response']:
            print("index:",index, "Word_sentiment_Pairing:",row['Word_sentiment_Pairing'], "Sentiment_shade:",row['Sentiment_shade'],
                "social_behaviour_pattern:",row['social_behaviour_pattern'],"academic_distraction_problem:", row['academic_distraction_problem'])
    # for ind in df['Text']:
    #     if search(values[0], ind):
    #         print(df1['Response'][ind], df1['Word_sentiment_Pairing'][ind], df1['Sentiment_shade'][ind],
    #             df1['social_behaviour_pattern'][ind], df1['academic_distraction_problem'][ind])


    # print(type(values[0]))
    # with open('/home/naresh/Desktop/aristocrat/6927_GUI/exctracted.csv',encoding= 'ISO-8859-1') as f:
    #     reader = csv.DictReader(f) # good point by @paco
    #     for row in reader:
    #         Response = row['Response']
    #         Word_sentiment_Pairing = row['Word_sentiment_Pairing']
    #         Sentiment_category = row['Sentiment_category']
    #         Sentiment_shade= row['Sentiment_shade']
    #         social_behaviour_pattern=row['social_behaviour_pattern']
    #         academic_distraction_problem=row['academic_distraction_problem']
    #     print("social_behaviour_pattern",social_behaviour_pattern)
    #     print("academic_distraction_problem",academic_distraction_problem)
        
    
root = Tk()
root.title("Python - Import CSV File To Tkinter Table")
width = 1920
height = 1080
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (1920, 1080, x, y))
root.resizable(0, 0)
TableMargin = Frame(root, width=800)
TableMargin.pack(side=TOP)

scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Text", "Sentiment Score"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Text', text="Text", anchor=W)
tree.heading('Sentiment Score', text="Sentiment Score", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=500)
tree.column('#2', stretch=NO, minwidth=0, width=500)
tree.bind("<<TreeviewSelect>>", OnDoubleClick)
tree.pack()
with open('/home/naresh/Desktop/aristocrat/6927_GUI/output2.csv',encoding='ISO-8859-1') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        serial_number = row['Text']
        Mac_Id = row['Predicted Sentiment Score']
        tree.insert("", 0, values=(serial_number, Mac_Id))
# with open('/home/naresh/Desktop/aristocrat/6927_GUI/exctracted.csv',encoding= 'ISO-8859-1') as f:
#      reader = csv.DictReader(f) # good point by @paco
#      for row in reader:
#         #pass
#         Response = row['Response']
#         Word_sentiment_Pairing = row['Word_sentiment_Pairing']
#         Sentiment_category = row['Sentiment_category']
#         Sentiment_shade= row['Sentiment_shade']
#         social_behaviour_pattern=row['social_behaviour_pattern']
#         academic_distraction_problem=row['academic_distraction_problem']

# if value
#         # tree.insert("", 0, values=(serial_number, Mac_Id))

    
#Main
if __name__ == '__main__':
    root.mainloop()


df = pd.read_csv("output2.csv",encoding='ISO-8859-1')
df1 = pd.read_csv("exctracted.csv",encoding='ISO-8859-1')


  
# iterating over rows with job as Govt and printing
for ind in df.index:
    if search("doing same and regular pattern of studies .like .sit in your front of parents,take book in hand and learn it as you daily. from this we cant enjoy the learning , not an joyfully means visiting studies spot , not have visualisation in studies make us feel in deep sorrowa big answer , unnecessarily points in it , doing the studies for only paper not for knowledge,some rules and regulations that write the answer in short not .not in brief if you can.. only  learn from digest target not from your own notes makers irritated the bothers like , the disturbance of vehicles created by them . are one of the one bothers that make sorrow us.no generally in our home the pressure was not created to do study because doing regular studies makes man unfit. distraction like mobiles tv is any gadgets makes us  unfamiliar to studies. the confussion like different answer of same question by different teacher. yes i hesitate to ask questions in class because is the question is arrogant or not familiar to answer.yes i compare myself by others because the other people's indirectly give us tont that he/she is better than you", df1['Response'][ind]):
        print(df1['Word_sentiment_Pairing'][ind], df1['Sentiment_shade'][ind],
              df1['social_behaviour_pattern'][ind], df1['academic_distraction_problem'][ind])
