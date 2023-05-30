from tkinter import *
import os
import subprocess


def theory():
    file1 = "Theory.py"
    
    p = subprocess.Popen(file1, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()

def one():
    file1 = "DiskScheduling.py"
    
    p = subprocess.Popen(file1, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


def two():
    file2 = "PageReplacement.py"
    
    p = subprocess.Popen(file2, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


def three():
    
    file3 = 'your scheduling file.py'
    os.system(file3)


def four():
    
    file4 = 'your concurrency file.py'
    os.system(file4)


Menu = Tk()

Menu.title("MP PBL GROUP-2 C2")
Menu.overrideredirect(False)

Menu.geometry("800x700+0+0")
Menu.resizable(False, False)

L1 = Label(width="900", height="2", text="Cache Replacement", font=("Century Gothic", 30), bg="black", fg="white")
L1.pack()
f1 = Frame(bg="white").pack()
l1 = Label(text="Menu: ", font=("Century Gothic", 15))
l1.pack(pady="40")
Button2 = Button(f1, text="Page Replacement Algorithm", borderwidth="0", bg="#e8e8e8", fg="green",
                 font=("Century Gothic", 15), activeforeground="black", activebackground="#bbbfca", command=two).pack(
    pady="30")

Button4 = Button(f1, text="Study Material", borderwidth="0", bg="#e8e8e8", fg="green",
                 font=("Century Gothic", 15), activeforeground="black", activebackground="#bbbfca", command=theory).pack(
    pady="30")

Menu.mainloop()
