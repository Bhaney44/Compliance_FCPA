mydict = {'good':0.8, 'average':0.6, 'optimal': 1, 'unacceptable': 0, 'bad': 0.2}

# Widgets:
from tkinter import *
from tkinter.messagebox import *

master = Tk()
label2 = Label(master, text = 'Autonomy & Resources', relief = 'groove', width = 40)
label3 = Label(master, text = 'Training & Communications', relief = 'groove', width = 40)
label4 = Label(master, text = 'Reporting & Investigation', relief = 'groove', width = 40)
label5 = Label(master, text = 'Incentives & Disciplinary Measures', relief = 'groove', width = 40)
label6 = Label(master, text = 'Improvement, Testing, & Review', relief = 'groove', width = 40)
label7 = Label(master, text = 'Remediation of Underlying Conflict', relief = 'groove', width = 40)
label8 = Label(master, text = 'Bribery & Accounting', relief = 'groove', width = 40)
label9 = Label(master, text = 'Third Party Management', relief = 'groove', width = 40)
label11 = Label(master, text = 'Senior & Middle Management', relief = 'groove', width = 40)
label12 = Label(master, text = 'Score', relief = 'groove', width = 20)
entry1 = Entry(master, relief = 'groove', width = 10)
entry2 = Entry(master, relief = 'groove', width = 10)
entry3 = Entry(master, relief = 'groove', width = 10)
entry4 = Entry(master, relief = 'groove', width = 10)
entry5 = Entry(master, relief = 'groove', width = 10)
entry6 = Entry(master, relief = 'groove', width = 10)
entry7 = Entry(master, relief = 'groove', width = 10)
entry8 = Entry(master, relief = 'groove', width = 10)
entry9 = Entry(master, relief = 'groove', width = 10)
blank1 = Entry(master, relief = 'groove', width = 10)



def show_answer():
    b = 1/9
    Ans1 = float( mydict[entry1.get()] ) * float( mydict[entry2.get()] ) * float( mydict[entry3.get()] ) * float( mydict[entry4.get()]) *float( mydict[entry5.get()]) * float( mydict[entry6.get()]) *float( mydict[entry7.get()]) *float( mydict[entry8.get()]) *float( mydict[entry9.get()]) 
    Ans11 = Ans1**b
    blank1.insert(0, Ans11)



button1 = Button(master, text = 'Calculate Compliance Score', relief = 'groove', width = 30, command =show_answer)


#Geometry
label2.grid( row = 2, column = 1, padx = 10 )
label3.grid( row = 3, column = 1, padx = 10 )
label4.grid( row = 4, column = 1, padx = 10 )
label5.grid( row = 5, column = 1, padx = 10 )
label6.grid( row = 6, column = 1, padx = 10 )
label7.grid( row = 7, column = 1, padx = 10 )
label8.grid( row = 8, column = 1, padx = 10 )
label9.grid( row = 9, column = 1, padx = 10 )
label11.grid( row = 10, column = 1, padx = 10 )
label12.grid( row = 11, column = 1, padx = 10 )
entry1.grid( row = 2, column = 2, padx = 10 )
entry2.grid( row = 3, column = 2, padx = 10 )
entry3.grid( row = 4, column = 2, padx = 10 )
entry4.grid( row = 5, column = 2, padx = 10 )
entry5.grid( row = 6, column = 2, padx = 10 )
entry6.grid( row = 7, column = 2, padx = 10 )
entry7.grid( row = 8, column = 2, padx = 10 )
entry8.grid( row = 9, column = 2, padx = 10 )
entry9.grid( row = 10, column = 2, padx = 10 )
blank1.grid( row = 11, column = 2, padx = 10 )
button1.grid( row = 12, column = 1, columnspan = 2)

#Static Properties
master.title('Compliance Calculator')
