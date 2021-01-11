#!/usr/bin/python3

from tkinter import *
import socket

def hostname():
	host = str(entry.get())
	addr = socket.gethostbyname(host)
	output_label.configure(text = ' IP address is {}'.format(addr))
	entry.delete(0,END)

root = Tk()
message_label1 = Label(text=' Convert Hostname to Ip address \n ', font=('Verdana', 16, 'bold'), bg='white', fg='green')
message_label = Label(text='Enter Hostname: ', font=('Verdana', 16, 'bold'),bg='green', fg='white')
output_label = Label(font=('Verdana',16, 'bold'), bg='white', fg='red')
entry = Entry(font=('Verdana', 20),width=15, bg='white', fg='green')
chang_button = Button(text='change', font=('Verdana', 16), bg='red', fg='white', command=hostname)

message_label1.grid(row=0, column=0)
message_label.grid(row=1, column=0)
entry.grid(row=2, column=0)
chang_button.grid(row=3, column=0)
output_label.grid(row=4, column=0, columnspan=3)
mainloop()