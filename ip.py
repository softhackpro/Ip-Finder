#!/usr/bin/python3

from tkinter import *
import socket

def hostname():
	host = str(entry.get())
	addr = socket.gethostbyname(host)
	output_label.configure(text = ' IP address is {}'.format(addr))
	entry.delete(0,END)

root = Tk()
root.title("IP Finder")
root.geometry("650x350+10+10")
root.resizable(False, False)
message_label1 = Label(text=' Convert Hostname to Ip address \n ', font=('Verdana', 16, 'bold'), bg='white', fg='green')
message_label = Label(text='Enter Hostname: ', font=('Verdana', 16, 'bold'),bg='green', fg='white')
output_label = Label(font=('Verdana',12, 'bold'), bg='white', fg='red')
entry = Entry(font=('Verdana', 18),width=20, bg='white',bd=3, fg='green')
chang_button = Button(text='change', font=('Verdana', 16), bg='red', bd=3, fg='white', command=hostname)

message_label1.place(x=120, y=50)
message_label.place(x=50, y=150)
entry.place(x=300, y=150)
chang_button.place(x=250, y=220)
output_label.place(x=150, y=300)
mainloop()
