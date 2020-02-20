import tkinter as tk
import tkinter.messagebox

class TikTacToe:
  def __init__(self, root): 
   self.player=True
   self.click=True  # checks turn
   self.flag=0
   self.player1_score=0
   self.player2_score=0
   
   self.buttons=tk.StringVar()
   self.p1=tk.StringVar()
   self.p2=tk.StringVar()
   self.p3=tk.StringVar()
   self.winner=tk.StringVar()
   #label
   self.label1=tk.Label(root,text="Player 1",font="Times 15",height=2,width=7).grid(column=0,row=0)
   self.label2=tk.Label(root,text="Player 2",font="Times 15",height=2,width=7).grid(column=0,row=1)
   #entry
   self.entry1=tk.Entry(root,textvariable=self.p1,bd=2).grid(column=1,row=0,columnspan=8)
   self.entry2=tk.Entry(root,textvariable=self.p2,bd=2).grid(column=1,row=1,columnspan=8)
   
   #play buttons
   self.button1=tk.Button(root,text=" ",command=lambda: self.onClick(self.button1),width=10,height=5)
   self.button1.grid(column=1,row=3)
   self.button2=tk.Button(root,text=" ",command=lambda: self.onClick(self.button2),width=10,height=5)
   self.button2.grid(column=2,row=3)
   self.button3=tk.Button(root,text=" ",command=lambda: self.onClick(self.button3),width=10,height=5)
   self.button3.grid(column=3,row=3)
   self.button4=tk.Button(root,text=" ",command=lambda: self.onClick(self.button4),width=10,height=5)
   self.button4.grid(column=1,row=4)
   self.button5=tk.Button(root,text=" ",command=lambda: self.onClick(self.button5),width=10,height=5)
   self.button5.grid(column=2,row=4)
   self.button6=tk.Button(root,text=" ",command=lambda: self.onClick(self.button6),width=10,height=5)
   self.button6.grid(column=3,row=4)
   self.button7=tk.Button(root,text=" ",command=lambda: self.onClick(self.button7),width=10,height=5)
   self.button7.grid(column=1,row=5)
   self.button8=tk.Button(root,text=" ",command=lambda: self.onClick(self.button8),width=10,height=5)
   self.button8.grid(column=2,row=5)
   self.button9=tk.Button(root,text=" ",command=lambda: self.onClick(self.button9),width=10,height=5)
   self.button9.grid(column=3,row=5) 
   #options
   self.button10=tk.Button(root,text="New\nGame",command=lambda: self.onNewGame(),width=6,height=3)
   self.button10.grid(column=1,row=6,padx=10,pady=10)
   self.button11=tk.Button(root,text="Exit",command=lambda:self.close(),width=6,height=3)
   self.button11.grid(column=3,row=6,padx=10,pady=10)
   self.button12=tk.Button(root,text="Play\nAgain",command=lambda: self.onPlayAgain(),width=6,height=3)
   self.button12.grid(column=2,row=6,padx=10,pady=10)
   
  def close(self):
   root.destroy()
   
  def onPlayAgain(self):
   self.flag=0
   self.click=True
   self.button1["text"]=" "
   self.button2["text"]=" "
   self.button3["text"]=" "
   self.button4["text"]=" "
   self.button5["text"]=" "
   self.button6["text"]=" "
   self.button7["text"]=" "
   self.button8["text"]=" "
   self.button9["text"]=" "
   if self.p1.get()=="" and self.p2.get()=="":
    tkinter.messagebox.showinfo("Tik Tac Toe","\n"+"Player 1 : "+str(self.player1_score)+"\n"+"Player 2 : "+str(self.player2_score))
   else:
    tkinter.messagebox.showinfo("Tik Tac Toe","\n"+self.p1.get()+" : "+str(self.player1_score)+"\n"+self.p2.get()+" : "+str(self.player2_score))
    
    
  def onNewGame(self):
   self.player1_score=0
   self.player2_score=0
   self.p1.set("")
   self.p2.set("")
   self.p2.set("")
   self.flag=0
   self.click=True
   self.button1["text"]=" "
   self.button2["text"]=" "
   self.button3["text"]=" "
   self.button4["text"]=" "
   self.button5["text"]=" "
   self.button6["text"]=" "
   self.button7["text"]=" "
   self.button8["text"]=" "
   self.button9["text"]=" "
   tkinter.messagebox.showinfo("Tik Tac Toe","New game !!!")
   
   
  def onClick(self,button):
   self.buttons=button
   if self.buttons["text"]==" " and self.click==True:
    self.buttons["text"]="X"
    self.flag+=1
    self.click=False
    self.checkWinner()
   elif self.click!=True and self.buttons["text"]==" " :
    self.buttons["text"]="O"
    self.flag+=1
    self.click=True
    self.checkWinner()
   else:
    tkinter.messagebox.showinfo("","Already clicked !!!")
  
  def checkWinner(self):
   if (self.button1["text"]=="X" and self.button2["text"]=="X" and self.button3["text"]=="X")or (self.button4["text"]=="X" and self.button5["text"]=="X" and self.button6["text"]=="X" )or ( self.button7["text"]=="X" and self.button8["text"]=="X" and self.button9["text"]=="X" )or ( self.button1["text"]=="X" and self.button4["text"]=="X" and self.button7["text"]=="X" )or ( self.button2["text"]=="X" and self.button5["text"]=="X" and self.button8["text"]=="X" )or ( self.button3["text"]=="X" and self.button6["text"]=="X" and self.button9["text"]=="X" )or ( self.button1["text"]=="X" and self.button5["text"]=="X" and self.button9["text"]=="X" )or ( self.button3["text"]=="X" and self.button5["text"]=="X" and self.button7["text"]=="X" ):
    self.player=True
    self.player1_score+=1
    if self.p1.get()!="":
     self.winner.set(self.p1.get())
    else:
     self.winner.set("Player 1 ")
    tkinter.messagebox.showinfo("TikTacToe",self.winner.get()+" won")
    
   elif (self.button1["text"]=="O" and self.button2["text"]=="O" and self.button3["text"]=="O")or (self.button4["text"]=="O" and self.button5["text"]=="O" and self.button6["text"]=="O" )or ( self.button7["text"]=="O" and self.button8["text"]=="O" and self.button9["text"]=="O" )or ( self.button1["text"]=="O" and self.button4["text"]=="O" and self.button7["text"]=="O" )or ( self.button2["text"]=="O" and self.button5["text"]=="O" and self.button8["text"]=="O" )or ( self.button3["text"]=="O" and self.button6["text"]=="O" and self.button9["text"]=="O" )or ( self.button1["text"]=="O" and self.button5["text"]=="O" and self.button9["text"]=="O" )or ( self.button3["text"]=="O" and self.button5["text"]=="O" and self.button7["text"]=="O" ):
    self.player=False
    self.player2_score+=1
    if self.p2.get()!="":
     self.winner.set(self.p2.get())
    else:
     self.winner.set("Player 1 ")
    tkinter.messagebox.showinfo("TikTacToe",self.winner.get()+" won")
   elif self.flag==9:
     tkinter.messagebox.showinfo("Tik Tac Toe," ,"Its a Tie !!!")
    
    
if __name__=="__main__":
    root=tk.Tk()
    #button=tk.StringVar()
    root.title("TikTacToe")
    root.geometry("400x500")
    root.resizable(1,1)
    tiktactoe=TikTacToe(root)
    root.mainloop()
    