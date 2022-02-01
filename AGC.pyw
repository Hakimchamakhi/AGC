from tkinter import *
import tkinter as tk
from tkinter import ttk
import os

def openf1():
    os.startfile("MainGC.exe")
def openf2():
    os.startfile("Archive.exe")
def openf3():
    os.startfile("Chkaya.exe")
def openf4():
    os.startfile("Tahkik.exe")
def openf5():
    os.startfile("Ataab.exe")

root = Tk()
wrapper = LabelFrame(root)

wrapper.pack(fill="both", expand="yes", side=TOP, padx=20, pady=10)

btn1 = Button(wrapper, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=20, text="قائمة الملفات الحالية", command=openf1)
btn2 = Button(wrapper, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=20, text="قائمة الأرشيف", command=openf2)
btn3 = Button(wrapper, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=20, text="قائمة الشكايات", command=openf3)
btn4 = Button(wrapper, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=20, text="قائمة التحقيق", command=openf4)
btn5 = Button(wrapper, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=20, text="قائمة الأتعاب", command=openf5)

btn1.pack(pady=30)
btn2.pack()
btn3.pack(pady=30)
btn4.pack()
btn5.pack(pady=30)

root.title("AGC")
root.geometry("350x350")
root.minsize(350,350)
root.resizable(0,0)
root.iconphoto(False, tk.PhotoImage(file='AGC.png'))
root.mainloop()
