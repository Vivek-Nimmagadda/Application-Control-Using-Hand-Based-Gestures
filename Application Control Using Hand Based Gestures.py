import sys
import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from mutagen.id3 import ID3
import pyautogui
import serial
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd

#MachineLearning using Naive Bayes Classifier
def MLRecPlayList():
    global index
    data = pd.read_csv('C:\\Users\\Sankeerth\\CoreProj.csv')
    x1=data['Genre']
    x2=data['Rating']
    y=data['Like']
    n = len(x1)
    x1n=[]
    for i in range(0,n-1):
        if i <=31:
            x1n.append(0)
        if i>=32 and i<=54:
            x1n.append(1)
        if i == 55:
            x1n.append(2)
        if i ==56 or i==58:
            x1n.append(3)
        if i==57:
            x1n.append(4)
        if i == 62:
            x1n.append(6)
        if (i>=58 and i<=61) or i == 63 or i==64:
            x1n.append(5)
        if i == 65:
            x1n.append(7)
    x2nn = np.array(x2)
    x1nn = np.array(x1n)
    
    x = []
    for i in range(0,n-1):
        x.append([x1nn[i],x2nn[i]])
    x.append([3,0])
    xn = np.array(x)
    
    model = GaussianNB()
    
    model.fit(xn, y)
    
    predicted= model.predict([[1,2],[0,5]])
    #print(predicted)
    listbox.delete(0,'end')
    for i in range(0,n-1):
        if y[i] == 1:
            listbox.insert(0,songlist[i])
    
    messagebox.showinfo("Playlist","The App usues Naive Bayes Classifier for recommending playlist")
    pygame.mixer.music.load(songlist[2])
    pygame.mixer.music.play()
    index=2
    update_song_name()
    
def Like():
    messagebox.showinfo("New Features", "Sorry!!!! Potential future scope where user can add new songs and receive a more efficient playlist recommendation!")
    
songlist = []

global Fact
Fact = 0
FunFacts = []
FunFacts.append('There are few activities in life that utilizes the entire brain, and music is one of them.')
FunFacts.append('Playing music regularly will physically alter your brain structure.')
FunFacts.append('Listening to music while exercising can significantly improve your work-out performance.')
FunFacts.append('Your heartbeat changes and mimics the music you listen to.')
FunFacts.append('According to a study, Learning a musical instrument can improve fine motor and reasoning skills.')

global index

index = 0
a=0
#Arduino_Serial = serial.Serial('com4',9600) 

#Button fucntionalities
def start_song(event):
    pygame.mixer.music.play()

def playpause_song(event):
    print('Play/Pause')
    global condition
    
    if condition == True:
        pygame.mixer.music.pause()
        condition = False
    elif condition == False:
        pygame.mixer.music.unpause()
        condition = True
    update_song_name()

def next_song(event):
    print('Next')
    global index 
    index +=1
    pygame.mixer.music.load(songlist[index])
    pygame.mixer.music.play()
    condition = True
    update_song_name()
    
def prev_song(event):
    print('Previous')
    global index
    if index > 0:
        index -=1
    pygame.mixer.music.load(songlist[index])
    pygame.mixer.music.play()
    condition = True
    update_song_name()
    
def stop_song(event):
    print('Stop')
    pygame.mixer.music.stop()
    st.set("")
    return songlist

#Key press function
#def key(event):
#    print(event)
#    if len(event.char) == 1:
#        next_song()

def update_song_name():
    global index
    global songlist
    st.set(songlist[index])
    return songlist
    
def Close(event):
    global quit
    quit= 'Quit'
    print(quit)
    Exit = messagebox.askyesno(title="Quit", message="Are you sure?")
    if Exit ==True:
        pygame.mixer.music.stop()
        root.destroy()
        return

#Dummy function for testing    
def Dummy():
    print("Do nothing")

def CurSelet(evt):
    global index
    a = listbox.curselection()
    index = int(a[0])
    pygame.mixer.music.load(songlist[index])
    pygame.mixer.music.play()
    condition = True
    update_song_name()

#Song file choose and load songs (Main)
def filechoose():
    directory = 'C:\\Users\\Sankeerth\\Music\\Songs'
    os.chdir(directory)
    
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            
            songlist.append(files)
    
    pygame.mixer.init()
    pygame.mixer.music.load(songlist[0])
    pygame.mixer.music.play()
    index = 0
    update_song_name()

#gesture functions
#def gesture_name():
#    global incoming_data
#    incoming_data = str(Arduino_Serial.readline())
#    g_st.set(incoming_data)
    
#def gesture_playpause_song():
#    global condition
#    if condition:
#        pygame.mixer.music.pause()
#        condition = False
#    elif not condition:
#        pygame.mixer.music.unpause()
#        condition = True
#    update_song_name()

#MenuBar Gesture Recognition Description funcitons
def playpause_gesture():
    messagebox.showinfo("Play/Pause Gesture", "Place your hand at a distance of 5-15 cm from the right sensor!")

def next_gesture():
    messagebox.showinfo("Next Song Gesture", "Place you hand at a distance of 25-40 cm in front of right sensor and move forward")
    
def prev_gesture():
    messagebox.showinfo("Previous Song Gesture", "Place you hand at a distance of 25-40 cm in front of right sensor and move back")
    
def v_up_gesture():
    messagebox.showinfo("Volume Up Gesture", "Place your hand at a distance of 25-40 cm in front of left sensor and move forward")

def v_down_gesture():
    messagebox.showinfo("Next Song Gesture", "Place your hand at a distance of 25-40 cm in front of left sensor and move back")

#Toolbar button fucntions
def TicTacToe(event):
    window=Tk()
    window.title("Welcome to TIC-Tac-Toe ")
    window.geometry("400x300")

    lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','15'))
    lbl.grid(row=0,column=0)
    lbl=Label(window,text="Player 1: X",font=('Helvetica','10'))
    lbl.grid(row=1,column=0)
    lbl=Label(window,text="Player 2: O",font=('Helvetica','10'))
    lbl.grid(row=2,column=0)
    global turn 
    turn=1; #For first person turn.

    def clicked1():
        global turn
        if btn1["text"]==" ":   #For getting the text of a button
            if turn==1:
                turn =2;
                btn1["text"]="X"
            elif turn==2:
                turn=1;
                btn1["text"]="O"
            check();
    def clicked2():
        global turn
        if btn2["text"]==" ":
            if turn==1:
                turn =2;
                btn2["text"]="X"
            elif turn==2:
                turn=1;
                btn2["text"]="O"
            check();
    def clicked3():
        global turn
        if btn3["text"]==" ":
            if turn==1:
                turn =2;
                btn3["text"]="X"
            elif turn==2:
                turn=1;
                btn3["text"]="O"
            check();
    def clicked4():
        global turn
        if btn4["text"]==" ":
            if turn==1:
                turn =2;
                btn4["text"]="X"
            elif turn==2:
                turn=1;
                btn4["text"]="O"
            check();
    def clicked5():
        global turn
        if btn5["text"]==" ":
            if turn==1:
                turn =2;
                btn5["text"]="X"
            elif turn==2:
                turn=1;
                btn5["text"]="O"
            check();
    def clicked6():
        global turn
        if btn6["text"]==" ":
            if turn==1:
                turn =2;
                btn6["text"]="X"
            elif turn==2:
                turn=1;
                btn6["text"]="O"
            check();
    def clicked7():
        global turn
        if btn7["text"]==" ":
            if turn==1:
                turn =2;
                btn7["text"]="X"
            elif turn==2:
                turn=1;
                btn7["text"]="O"
            check();
    def clicked8():
        global turn
        if btn8["text"]==" ":
            if turn==1:
                turn =2;
                btn8["text"]="X"
            elif turn==2:
                turn=1;
                btn8["text"]="O"
            check();
    def clicked9():
        global turn
        if btn9["text"]==" ":
            if turn==1:
                turn =2;
                btn9["text"]="X"
            elif turn==2:
                turn=1;
                btn9["text"]="O"
            check();
    global flag
    flag=1;
    def check():
        global flag;
        b1 = btn1["text"];
        b2 = btn2["text"];
        b3 = btn3["text"];
        b4 = btn4["text"];
        b5 = btn5["text"];
        b6 = btn6["text"];
        b7 = btn7["text"];
        b8 = btn8["text"];
        b9 = btn9["text"];
        flag=flag+1;
        if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
            win(btn1["text"])
        if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
            win(btn4["text"]);
        if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
            win(btn7["text"]);
        if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
            win(btn1["text"]);
        if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
            win(btn2["text"]);
        if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
            win(btn3["text"]);
        if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
            win(btn1["text"]);
        if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
            win(btn7["text"]);
        if flag ==10:
            Exit = messagebox.askyesno(title="Tie", message="Play another game?")
            if Exit ==True:
                TicTacToe(event)
            window.destroy()

    def win(player):
        ans = "Game complete " + player + " wins, Play another? ";
        Exit = messagebox.askyesno(title="Congratulations", message=ans)
        if Exit ==True:
            TicTacToe(event)
        window.destroy() 


    btn1 = Button(window, text=" ",bg="#E6CF38", fg="#021A6B",width=3,height=1,font=('Helvetica','20'),command=clicked1)
    btn1.grid(column=1, row=1)
    btn2 = Button(window, text=" ",bg="#E6CF38", fg="#021A6B",width=3,height=1,font=('Helvetica','20'),command=clicked2)
    btn2.grid(column=2, row=1)
    btn3 = Button(window, text=" ",bg="#E6CF38", fg="#021A6B",width=3,height=1,font=('Helvetica','20'),command=clicked3)
    btn3.grid(column=3, row=1)
    btn4 = Button(window, text=" ",bg="#E6CF38", fg="#021A6B",width=3,height=1,font=('Helvetica','20'),command=clicked4)
    btn4.grid(column=1, row=2)
    btn5 = Button(window, text=" ",bg="#E6CF38", fg="#021A6B",width=3,height=1,font=('Helvetica','20'),command=clicked5)
    btn5.grid(column=2, row=2)
    btn6 = Button(window, text=" ",bg="#E6CF38", fg="#021A6B",width=3,height=1,font=('Helvetica','20'),command=clicked6)
    btn6.grid(column=3, row=2)
    btn7 = Button(window, text=" ",bg="#E6CF38", fg="#021A6B",width=3,height=1,font=('Helvetica','20'),command=clicked7)
    btn7.grid(column=1, row=3)
    btn8 = Button(window, text=" ",bg="#E6CF38", fg="#021A6B",width=3,height=1,font=('Helvetica','20'),command=clicked8)
    btn8.grid(column=2, row=3)
    btn9 = Button(window, text=" ",bg="#E6CF38", fg="#021A6B",width=3,height=1,font=('Helvetica','20'),command=clicked9)
    btn9.grid(column=3, row=3)

    window.mainloop()


    
def FunFact(event):
    global Fact
    if Fact == 5:
        Fact = 0
    messagebox.showinfo("Fun Fact", FunFacts[Fact])
    Fact+=1

#MenuBar Songs Functions
def allsongs():
    global index
    listbox.delete(0,'end')
    songlist.reverse()

    for items in songlist:
        listbox.insert(0,items)

    songlist.reverse()
    pygame.mixer.music.load(songlist[0])
    pygame.mixer.music.play()
    index=0
    update_song_name()
    
def English():
    global index
    index = 0
    listbox.delete(0,'end')
    
    songlist.reverse()
    
    for items in songlist:
        if index>=3 and index<=15:
            listbox.insert(0,items)
        index+=1
    songlist.reverse()
    pygame.mixer.music.load(songlist[51])
    pygame.mixer.music.play()
    index=51
    update_song_name()

def Hindi():
    global index
    index = 0
    listbox.delete(0,'end')
    
    songlist.reverse()
    
    for items in songlist:
        if index>=38 and index<=66:
            listbox.insert(0,items)
        index+=1
    songlist.reverse()
    pygame.mixer.music.load(songlist[0])
    pygame.mixer.music.play()
    index=0
    update_song_name()

def Telugu():
    global index
    index = 0
    listbox.delete(0,'end')
    
    songlist.reverse()
    for items in songlist:
        if index>=16 and index<=37:
            listbox.insert(0,items)
        index+=1
    songlist.reverse()
    pygame.mixer.music.load(songlist[29])
    pygame.mixer.music.play()
    index=29
    update_song_name()

#main window
root = Tk()
#root.minsize(620,520)

Window_frame1 = Frame(root, bg = '#FFBE73')

menu = Menu(Window_frame1)
root.config(menu=menu)

#MenuBar
Submenu1 = Menu(menu)
menu.add_cascade(label="Files", menu = Submenu1)
Submenu1.add_command(label="All Songs", command = allsongs)
Submenu1.add_separator()
Submenu1.add_command(label="English Songs", command = English)
Submenu1.add_command(label="Hindi Songs", command = Hindi)
Submenu1.add_command(label="Telugu Songs", command = Telugu)

Submenu2 = Menu(menu)
menu.add_cascade(label="Gestures", menu = Submenu2)
Submenu2.add_command(label="Pause/Play Gesture", command = playpause_gesture)
Submenu2.add_command(label="Next Song Gesture", command = next_gesture)
Submenu2.add_command(label="Previous Song Gesture", command = prev_gesture)
Submenu2.add_command(label="Volume Up/Down Gesture", command = v_up_gesture)
Submenu2.add_command(label="Volume Down Gesture", command = v_down_gesture)

Submenu3 = Menu(menu)
menu.add_cascade(label="Playlists", menu = Submenu3)
Submenu3.add_command(label="Recommended Playlist", command = MLRecPlayList)
Submenu3.add_separator()
Submenu3.add_command(label="tell us what you like", command = Like)

toolbar = Frame(Window_frame1, bg='#A1BDFF')

t_label_1 = Label(toolbar,text='Bored? :', bg='#A1BDFF')
t_label_1.pack(side=LEFT)

t_button_1 = Button(toolbar,text='Tic Tac Toe', relief = GROOVE, bg='#FEE9CC', activebackground='#336699')
t_button_1.bind('<Button-1>',TicTacToe)
t_button_1.pack(side=LEFT)

t_button_2 = Button(toolbar, text='Fun Fact', relief = GROOVE, bg='#FEE9CC', activebackground='#336699')
t_button_2.bind('<Button-1>',FunFact)
t_button_2.pack(side=LEFT)

toolbar.pack(side=TOP,fill=X)

st = StringVar()
try :
    filechoose()
except OSError:
    print("")
condition = pygame.mixer.music.get_busy()

Main_Frame = Frame(Window_frame1, bg= '#FFBE73')
#Title
title = Label(Main_Frame,text='SVS Music Player',bg='#7184B2')
title.pack(side=TOP)

##Gesture Name
#Gesture_name = Label(Main_Frame, textvariable=g_st,width=40,bg='#7184B2')
#Gesture_name.pack(side=TOP)

#Song Name Label
songlabel = Label(Main_Frame,textvariable=st,width=40,bg='#7184B2')
songlabel.pack(side=TOP, fill=X)

#ListBox for songs 
listbox = Listbox(Main_Frame, bg='#FFBE73')
listbox.bind('<Double-Button-1>',CurSelet)
listbox.pack(side=TOP, fill=X)

songlist.reverse()

for items in songlist:
    listbox.insert(0,items)

songlist.reverse()

#Buttons for functionality
Button_Frame3 = Frame(Main_Frame, bg='#FFBE73')

stop_button = Button(Button_Frame3,text='Stop Music',activebackground='#336699', relief=RIDGE, bg='#FEE9CC')
stop_button.bind("<Button-1>",stop_song)
stop_button.pack(side=LEFT)

close_button = Button(Button_Frame3,text='Quit',activebackground='#336699', relief=RIDGE, bg='#FEE9CC')
close_button.bind("<Button-1>",Close)
close_button.pack(side=BOTTOM)

Button_Frame3.pack(side=BOTTOM)


Button_Frame2 = Frame(Main_Frame, bg='#FFBE73')

next_button = Button(Button_Frame2,text='Next Song',activebackground='#336699', relief=RIDGE, bg='#FEE9CC')
next_button.bind("<Button-1>",next_song)
next_button.pack(side=LEFT)

prev_button = Button(Button_Frame2,text='Previous Song',activebackground='#336699', relief=RIDGE, bg='#FEE9CC')
prev_button.bind("<Button-1>",prev_song)
prev_button.pack(side=LEFT)

Button_Frame2.pack(side=BOTTOM)


Button_Frame1 = Frame(Main_Frame, bg='#FFBE73')

play_button = Button(Button_Frame1,text='Play/Pause Song',activebackground='#336699', relief=RIDGE, bg='#FEE9CC')
play_button.bind("<Button-1>",playpause_song)
play_button.pack(side=TOP)

Button_Frame1.pack(side=BOTTOM)


Main_Frame.pack(side=TOP, fill = X)

status_bar = Label(Window_frame1, text = "Enjoy the Music...", bd=2, relief = SUNKEN, bg='#FEE9CC', anchor=W)
status_bar.pack(side=BOTTOM, fill=X)

condition = pygame.mixer.music.get_busy()


Window_frame1.bind('<KeyRelease-a>',playpause_song)
Window_frame1.bind('<KeyRelease-n>',next_song)
Window_frame1.bind('<KeyRelease-p>',prev_song)
Window_frame1.bind('<KeyRelease-s>',stop_song)
Window_frame1.pack()
Window_frame1.focus_set()

root.configure(background="#FFBE73")
root.mainloop()
pygame.mixer.music.stop()
