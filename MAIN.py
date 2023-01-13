from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk

root=Tk()#crearting window
root.title('E-Sport')
#root.iconbitmap('icon.ico')
root.configure(bg='#6E6E8B')
root.geometry('525x325')

#background
img =Image.open('bg.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(root, image=bg)
label.place(x = 0,y = 0)


# Add image
img=ImageTk.PhotoImage(Image.open('img.jpg'))
my_Label=Label(image=img)
my_Label.grid(row=1,column=2,rowspan=4)

def data_back():
    D.destroy()
    root.geometry('525x325')
    
def update():
    #connect to database
    con=sqlite3.connect('teams.db')
    c=con.cursor()
    #to update data
    c.execute("""UPDATE team  SET p1=:p1,
p2=:p2,
p3=:p3,
p4=:p4,
p5=:p5
WHERE t_c="""+data_code.get(),
              {'p1':py1.get(),
               'p2':py2.get(),
               'p3':py3.get(),
               'p4':py4.get(),
               'p5':py5.get()
                  })
    
    con.commit()
    
    con.close()
    #print('succesful!')
    
def data_show():
    #connect to database
    con=sqlite3.connect('teams.db')
    c=con.cursor()
    
    c.execute('SELECT t_c FROM team')
    #fetching all team codes
    codes=c.fetchall()
    #getting entered code
    team_c=data_code.get()
    #loop to check if entered code exists in table
    for tc in codes:
        for i in tc:
#             print(i)
            if team_c in str(i):
                #to display team name of entered code
                c.execute('SELECT * FROM team WHERE t_c='+team_c)
                records=c.fetchall()
                
                for record in records:
                    global frame_data
                    global py1
                    global py2
                    global py3
                    global py4
                    global py5
                    frame_data=LabelFrame(D)
                    frame_data.grid(row=3,column=1,columnspan=2,padx=10)
                    Label(frame_data,text='Team Code:').grid(row=0,column=0)
                    Label(frame_data,text=record[0]).grid(row=0,column=1)
                    Label(frame_data,text='Team Name:').grid(row=1,column=0)
                    Label(frame_data,text=record[1]).grid(row=1,column=1)
                    Label(frame_data,text='Player 1').grid(row=2,column=0)
                    py1=Entry(frame_data,width=30)
                    py1.grid(row=2,column=1)
                    py1.insert(0,record[2])
                    Label(frame_data,text='Player 2').grid(row=3,column=0)
                    py2=Entry(frame_data,width=30)
                    py2.grid(row=3,column=1)
                    py2.insert(0,record[3])
                    Label(frame_data,text='Player 3').grid(row=4,column=0)
                    py3=Entry(frame_data,width=30)
                    py3.grid(row=4,column=1)
                    py3.insert(0,record[4])
                    Label(frame_data,text='Player 4').grid(row=5,column=0)
                    py4=Entry(frame_data,width=30)
                    py4.grid(row=5,column=1)
                    py4.insert(0,record[5])
                    Label(frame_data,text='Player 5').grid(row=6,column=0)
                    py5=Entry(frame_data,width=30)
                    py5.grid(row=6,column=1)
                    py5.insert(0,record[6])
                    
                    Button(frame_data,text='Update',command=update).grid(row=7,column=0,columnspan=2)

def show_data():
    #connect to database
    con=sqlite3.connect('teams.db')
    c=con.cursor()
    
    c.execute('SELECT t_c FROM team')
    #fetching all team codes
    codes=c.fetchall()
    #getting entered code
    team_c=t_code_box.get()
    #loop to check if entered code exists in table
    for tc in codes:
        for i in tc:
#             print(i)
            if team_c in str(i):
                print(str((team_c)*2))
                #to display team name of entered code
                c.execute('SELECT * FROM team WHERE t_c='+team_c)
                records=c.fetchall()
                
                for record in records:
                    frame=LabelFrame(R)
                    frame.grid(row=2,column=1,columnspan=2)
                    Label(frame,text='Team Code').grid(row=0,column=0)
                    Label(frame,text=record[0]).grid(row=0,column=1)
                    Label(frame,text='Team Name').grid(row=1,column=0)
                    Label(frame,text=record[1]).grid(row=1,column=1)
                    R.geometry('230x150')
                    
    con.commit()
    con.close()

def data():
    global D
    D=Tk()
    D.configure(bg='#6E6E8B')
    D.title('E-SPORT ANALYSIS')
    root.geometry('0x0')
    D.geometry('630x540')
    
    con=sqlite3.connect('teams.db')
    c=con.cursor()
    
    c.execute('SELECT * FROM team')
    players=c.fetchall()
    sr_no=[]
    for i in players:
        sr_no.append(i[0])
        print(i[0],i[1])
    print(sr_no)
        
    con.commit()
    
    con.close()
    
#     print('data')
        
    Label(D,text='E-sport Matches').grid(row=0,column=0,columnspan=5,padx=10,pady=10)
    Label(D,text='Team Code').grid(row=1,column=1,padx=10,pady=10)
    global data_code
    data_code=Entry(D,width=15)
    data_code.grid(row=1,column=2,padx=10)
    
    Button(D,text='Show Data',command=data_show,padx=20).grid(row=2,column=1,columnspan=2,padx=10)
    Button(D,text='Back',command=data_back,padx=20,pady=5).grid(row=4,column=2,columnspan=2,padx=10)
    
    t_n=[]
    for i in players:
        t_n.append(i[1])
    
    win=[]
    loose=[]
    x=[]
    for i in t_n:
        a=np.random.randint(0,10)
        win.append(a)
        b=(10-a)
        loose.append(b)
        x.append(0.2)
#         print(i,win,loose)
    print(win,loose)
    print(sum(win)+sum(loose))
    df=pd.DataFrame({'Team Name':t_n,'Won':win,'lose':loose},index=sr_no)
    print(df)
    df.sort_values(by='Won', ascending=False)
    print(df)
    
    frameChartsLT = Frame(D)
    frameChartsLT.grid(row=1,column=3,rowspan=3)

    fig = Figure(figsize=(3.2,2), dpi=100) # create a figure object
    ax = fig.add_subplot(111) # add an Axes to the figure

    ax.pie(win, radius=1, labels=t_n,autopct='%0.2f%%', shadow=True,explode=x)
    
    chart1 = FigureCanvasTkAgg(fig,frameChartsLT)
    chart1.get_tk_widget().grid(row=1,column=3)
    #defined columns
    columns=('team name','won','lost')
    #creating treeview 
    tree=ttk.Treeview(D,columns=columns, show='headings')
    
    #define heading
    tree.heading('team name',text='Team Name')
    tree.heading('won',text='Won')
    tree.heading('lost',text='Lost')
    
    value=[]
    for i in players:
        value.append((i[1],win[len(value)],loose[len(value)]))
    print(value)
    
    for v in value:
        tree.insert('', END, values=v)
    
    
    tree.grid(row=5, column=1,columnspan=4)
    
    # add a scrollbar
    scrollbar = ttk.Scrollbar(D, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=5, column=5,sticky='ns')
        
def delete():
    #connect to database
    con=sqlite3.connect('teams.db')
    c=con.cursor()
    
    c.execute('SELECT t_c FROM team')
    #fetching all team codes
    codes=c.fetchall()
    
    team_c=t_code_box.get()
    
    #to check wether the entered code exists in table
    for tc in codes:
        for i in tc:
#             print(i)
            if team_c in str(i):
                #to delete team data from table
                c.execute('DELETE FROM team WHERE t_c='+team_c)
                
    
    con.commit()
    con.close()
    
def close_R():
    R.destroy()
    root.geometry('525x325')
    
def remove():
    global R
    R=Tk()
    R.configure(bg='#6E6E8B')
    R.title('Add Team')
    root.geometry('0x0')
    R.geometry('230x100')
    #enter the team code
    global t_code_box
    Label(R,text='TIP:Enter Valid Team Code',bg='light green').grid(row=0,column=0,columnspan=4,padx=10,pady=10)
    t_code=Label(R,text='Team Code',bg='light blue').grid(row=1,column=1)
    t_code_box=Entry(R,width=10,bg='light blue')
    t_code_box.grid(row=1,column=2)
    
    Button(R,text='Remove',padx=15,command=delete).grid(row=3,column=1,pady=10)
    Button(R,text='Back',padx=22,command=close_R).grid(row=3,column=2,pady=10)
    Button(R,text='Show Data',command=show_data).grid(row=1,column=3)
    
def exit():
    response=messagebox.askyesno('Using databases GUI','Do You Want To Exit')
#     Label(root,text=response).pack()
    if response==1:
        root.destroy()

def inert():
    response=messagebox.askyesno('Team Details','Do You Want add This data !')
    if response==1:
        
#         Label(root,text=str(Team_name_box.get())).grid(row=5,column=0)
        
        #adding data to data base
        con=sqlite3.connect('teams.db')
        
        c=con.cursor()
        
        #create table
        c.execute('CREATE TABLE if not exists team (t_c integer,t_name text,p1 text,p2 text,p3 text,p4 text,p5 text)')
        
        #to check tables in database
#         c.execute("SELECT name from sqlite_master where type = 'tables'")
#         tables=c.fetchall()
#         print(tables)

        #insert data
        c.execute('INSERT INTO team VALUES(:t_c,:t_name,:p1,:p2,:p3,:p4,:p5)',
                  {'t_c':code,
                   't_name':Team_name_box.get(),
                   'p1':Player1_box.get(),
                   'p2':Player2_box.get(),
                   'p3':Player3_box.get(),
                   'p4':Player4_box.get(),
                   'p5':Player5_box.get(),
                      }) 
        
        
        print('succesful!')
        con.commit()
        
        con.close()
        
        win.destroy()
        root.geometry('525x325')
        
def add():
    global win
    win=Tk()
    win.configure(bg='#6E6E8B')
    win.title('Add Team')
    root.geometry('0x0')
    
    WARNING=Label(win,text='WARRNING! TEAM WITH FIVE (5) PLAYERS , ARE ONLY ELIGIBLE FOR THE PLAY.',bg='indianred',fg='yellow',padx=50).grid(row=0,column=1,columnspan=5,padx=10,pady=10)
    global code
    global Team_name_box
    global Player1_box
    global Player2_box
    global Player3_box
    global Player4_box
    global Player5_box
    code=np.random.randint(1000,9999)
    Team_code_text=Label(win,text='Team Code:').grid(row=1,column=1,padx=10)
    Team_code=Label(win,text=str(code),bg='light blue',padx=125).grid(row=1,column=2,padx=10)
    Team_name=Label(win,text='Team Name').grid(row=2,column=1,padx=10)
    Team_name_box=Entry(win,width=50)
    Team_name_box.grid(row=2,column=2)
    Player1=Label(win,text='Player1').grid(row=3,column=1,padx=10)
    Player1_box=Entry(win,width=50)
    Player1_box.grid(row=3,column=2)
    Player2=Label(win,text='Player2').grid(row=4,column=1,padx=10)
    Player2_box=Entry(win,width=50)
    Player2_box.grid(row=4,column=2)
    Player3=Label(win,text='Player3').grid(row=5,column=1,padx=10)
    Player3_box=Entry(win,width=50)
    Player3_box.grid(row=5,column=2)
    Player4=Label(win,text='Player4').grid(row=6,column=1,padx=10)
    Player4_box=Entry(win,width=50)
    Player4_box.grid(row=6,column=2)
    Player5=Label(win,text='Player5').grid(row=7,column=1,padx=10)
    Player5_box=Entry(win,width=50)
    Player5_box.grid(row=7,column=2)
    bt=Button(win,text='ADD',command=inert).grid(row=8,column=1,columnspan=5)
    
    
intro=Label(root,text='Welcome To E-SPORTS',bg='deep pink',font="Times 20 italic bold",padx=100).grid(row=0,column=0,padx=10,pady=10,columnspan=8)
#ADDING TEAM
Add_Team=Button(root,text='Add Team',padx=10,pady=10,command=add).grid(row=1,column=0,padx=10,pady=5)

#REMOVE A TEAM
Remove_Team=Button(root,text='Remove Team',padx=2,pady=10,command=remove).grid(row=2,column=0,padx=5,pady=5)

#TEAM DATA
Team_data=Button(root,text='Team Data',padx=10,pady=10,command=data).grid(row=3,column=0,padx=5,pady=5)

#exit
exit=Button(root,text='Exit',command=exit,padx=30,pady=10).grid(row=4,column=0)

root.mainloop()