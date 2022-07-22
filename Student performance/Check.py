from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title("Student Performance Prediction System")
    root.configure(background="Black")
    
    gender = tk.IntVar()
    Nationlity = tk.IntVar()
    PlaceofBirth = tk.IntVar()
    StageID = tk.IntVar()
    GradeID = tk.IntVar()
    Topic = tk.IntVar()
    Semester = tk.IntVar()
    VisitedResources= tk.IntVar()
    AnnouncementsView= tk.IntVar()
    Discussion = tk.IntVar()
    ParentAnsweringSurvey = tk.DoubleVar()
    ParentsShoolSatisfaction = tk.IntVar()
    StudentAbsenceDays = tk.IntVar()
   
    
    #===================================================================================================================
    def Detect():
        e1= gender.get()
        print(e1)
        e2=Nationlity.get()
        print(e2)
        e3= PlaceofBirth.get()
        print(e3)
        e4=StageID.get()
        print(e4)
        e5=GradeID.get()
        print(e5)
        e6=Topic.get()
        print(e6)
        e7=Semester.get()
        print(e7)
        e8=VisitedResources.get()
        print(e8)
        e9=AnnouncementsView.get()
        print(e9)
        e10=Discussion.get()
        print(e10)
        e11=ParentAnsweringSurvey.get()
        print(e11)
        e12=ParentsShoolSatisfaction.get()
        print(e12)
        e13=StudentAbsenceDays.get()
        print(e13)
        
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('RF_student_performance.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9,e10, e11, e12, e13]])
        print(v)
        if v[0]==0:
            print("High")
            yes = tk.Label(root,text="Performance is Above 75%",background="red",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=750,y=500)
                     
        elif v[0]==1:
            print("Medium")
            no = tk.Label(root, text="Performace is 50%-70% ", background="red", foreground="white",font=('times', 20, ' bold '),width=20)
            no.place(x=750, y=500)
            
            
        else:
            print("Low")
            no = tk.Label(root, text="Performace is 10% - 40%", background="green", foreground="white",font=('times', 20, ' bold '),width=20)
            no.place(x=750, y=500)
            


    l1=tk.Label(root,text="gender",background="cyan",font=('times', 20, ' bold '),width=15)
    l1.place(x=5,y=5)
    ts1=tk.Label(root,text="Male:0 Female:1",background="yellow",font=('times', 16, ' bold '),width=15)
    ts1.place(x=600,y=5)
    gender=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=gender)
    gender.place(x=400,y=1)
    

    l2=tk.Label(root,text="Nationlity",background="cyan",font=('times', 20, ' bold '),width=15)
    l2.place(x=5,y=50)
    Nationlity=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Nationlity)
    Nationlity.place(x=400,y=50)
    ts2= tk.Label(root,text="KW:0,LIB:1,EGY:2,Saudi:3,USA:4,IND:5,\nVZN:6,IRN:7,TUK:8,MOR:9,SYR:10,AUS:11,IRQ:12",background="yellow",font=('times', 12, ' bold '),width=40)
    ts2.place(x=600,y=50)
    l3=tk.Label(root,text="PlaceofBirth",background="cyan",font=('times', 20, ' bold '),width=15)
    l3.place(x=5,y=100)
    
    PlaceofBirth=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=PlaceofBirth)
    PlaceofBirth.place(x=400,y=100)
    
    l4=tk.Label(root,text="StageID",background="cyan",font=('times', 20, ' bold '),width=15)
    l4.place(x=5,y=150)
    ts3=tk.Label(root,text="Lowerlvl:0,MiddleLvl:1,HighLvl:2",background="yellow",font=('times', 16, ' bold '),width=25)
    ts3.place(x=600,y=160)
    StageID=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=StageID)
    StageID.place(x=400,y=160)

    l5=tk.Label(root,text="GradeID",background="cyan",font=('times', 20, ' bold '),width=15)
    l5.place(x=5,y=200)
   
    ts4 = tk.Label(root,text="Grade02:0 to Grade12:9",background="yellow",font=('times', 16, ' bold '),width=25)
    ts4.place(x=600,y=200)
    GradeID=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=GradeID)
    GradeID.place(x=400,y=200)

    l6=tk.Label(root,text="Topic",background="cyan",font=('times', 20, ' bold '),width=15)
    l6.place(x=5,y=250)
    ts5 = tk.Label(root,text="IT:0,Math:1,Arabic:2,Sci:3,Eng:4,Quaran:5,\nSpain:6,His:7,Frn:8,Bio:9,Chem:10,Geo:11",background="yellow",font=('times', 16, ' bold '),width=35)
    ts5.place(x=600,y=250)
    Topic=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Topic)
    Topic.place(x=400,y=250)

    l7=tk.Label(root,text="Semester",background="cyan",font=('times', 20, ' bold '),width=15)
    
    l7.place(x=5,y=300)
    ts6 = tk.Label(root,text="Sem-I:0 SemII:1",background="yellow",font=('times', 16, ' bold '),width=25)
    ts6.place(x=600,y=310)
    Semester=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Semester)
    Semester.place(x=400,y=300)

    l8=tk.Label(root,text="VisitedResources",background="cyan",font=('times', 20, ' bold '),width=15)
    l8.place(x=5,y=350)
    VisitedResources=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=VisitedResources)
    VisitedResources.place(x=400,y=350) 
    ts7 = tk.Label(root,text="Visited Resources may vary on Student max(100)",background="yellow",font=('times', 16, ' bold '),width=38)
    ts7.place(x=600,y=360)

    l9=tk.Label(root,text="AnnouncementsView",background="cyan",font=('times', 20, ' bold '),width=17)
    l9.place(x=5,y=400)
    AnnouncementsView=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=AnnouncementsView)
    AnnouncementsView.place(x=400,y=400)
    ts8 = tk.Label(root,text="Resources provided by Teacher",background="yellow",font=('times', 16, ' bold '),width=35)
    ts8.place(x=600,y=400)

    l10=tk.Label(root,text="Discussion",background="cyan",font=('times', 20, ' bold '),width=10)
    l10.place(x=5,y=450)
    ts = tk.Label(root,text="To be fulfiled by teacher ",background="yellow",font=('times', 16, ' bold '),width=35)
    ts.place(x=600,y=450)
    
    Discussion=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Discussion)
    Discussion.place(x=400,y=450)

    l11=tk.Label(root,text="ParentAnsweringSurvey",background="cyan",font=('times', 20, ' bold '),width=20)
    l11.place(x=5,y=500)
    ts11 = tk.Label(root,text="Yes:0 No:1",background="yellow",font=('times', 16, ' bold '),width=35)
    ts11.place(x=600,y=500)
    ParentAnsweringSurvey=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=ParentAnsweringSurvey)
    ParentAnsweringSurvey.place(x=400,y=500)
    ts9 = tk.Label(root,text="Good:0 Bad:1",background="yellow",font=('times', 16, ' bold '),width=25)
    ts9.place(x=600,y=550)
    l12=tk.Label(root,text="ParentsShoolSatisfaction",background="cyan",font=('times', 20, ' bold '),width=20)
    l12.place(x=5,y=550)
    ParentsShoolSatisfaction=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=ParentsShoolSatisfaction)
    ParentsShoolSatisfaction.place(x=400,y=550)

    l13=tk.Label(root,text="StudentAbsenceDays",background="cyan",font=('times', 20, ' bold '),width=17)
    l13.place(x=5,y=600)
    ts10 = tk.Label(root,text="under 7:0 Above 7:1",background="yellow",font=('times', 16, ' bold '),width=35)
    ts10.place(x=600,y=575)
    StudentAbsenceDays=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=StudentAbsenceDays)
    StudentAbsenceDays.place(x=400,y=600)


    
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=600,y=615)


    root.mainloop()

Train()