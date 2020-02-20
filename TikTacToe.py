import tkinter as tk
import tkinter.messagebox

class TikTacToe:
  def __init__(self, root):
   self.click=True  # checks turn
   self.flag=0
   self.buttons=tk.StringVar()
   self.p1=tk.StringVar()
   self.p2=tk.StringVar()
   self.label1=tk.Label(root,text="Player 1",font="Times 15",height=2,width=7).grid(column=0,row=0)
   self.label2=tk.Label(root,text="Player 2",font="Times 15",height=2,width=7).grid(column=0,row=1)
   self.entry1=tk.Entry(root,textvariable=self.p1,bd=2).grid(column=1,row=0,columnspan=8)
   self.entry2=tk.Entry(root,textvariable=self.p2,bd=2).grid(column=1,row=1,columnspan=8)
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
    tkinter.messagebox.showinfo("TikTacToe",self.p1.get()+" won !!!")
   elif (self.button1["text"]=="O" and self.button2["text"]=="O" and self.button3["text"]=="O")or (self.button4["text"]=="O" and self.button5["text"]=="O" and self.button6["text"]=="O" )or ( self.button7["text"]=="O" and self.button8["text"]=="O" and self.button9["text"]=="O" )or ( self.button1["text"]=="O" and self.button4["text"]=="O" and self.button7["text"]=="O" )or ( self.button2["text"]=="O" and self.button5["text"]=="O" and self.button8["text"]=="O" )or ( self.button3["text"]=="O" and self.button6["text"]=="O" and self.button9["text"]=="O" )or ( self.button1["text"]=="O" and self.button5["text"]=="O" and self.button9["text"]=="O" )or ( self.button3["text"]=="O" and self.button5["text"]=="O" and self.button7["text"]=="O" ):
    tkinter.messagebox.showinfo("TikTacToe",self.p2.get()+" won !!!")
   elif self.flag>7:
     tkinter.messagebox.showinfo("Tik Tac Toe," ,"Its a Tie !!!")
    
    
if __name__=="__main__":
    root=tk.Tk()
    #button=tk.StringVar()
    root.title("TikTacToe")
    root.geometry("400x400")
    root.resizable(1,1)
    tiktactoe=TikTacToe(root)
    root.mainloop()
    