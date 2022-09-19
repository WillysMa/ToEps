# -* coding: utf-8 -*-
'''
@File: GUI_ex1.py
@Author: Mengyuan Ma
@Contact: mamengyuan410@gmail.com
@Time: 2022-09-16 17:47
'''
# coding:utf-8
# GUI界面编程
from tkinter import *  # 控件基础包，导入这个包后，这个包下的所有函数可以直接调用
from tkinter.messagebox import showinfo, showwarning, showerror  # 各种类型的提示框
import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image

file_name = []
def open_file():
    global source_file_path
    global file_name
    global file_type
    source_file_path = filedialog.askopenfilename(title='Please choose a figure file', initialdir=(os.path.expanduser('')))
    print('Your choosen file is：', source_file_path)
    split_file = os.path.split(source_file_path)[-1]
    file_name, file_type = split_file.split('.')
    print(f'file_type: {file_type}')
    print(f'file name；{file_name}')
    if len(source_file_path):
        lb.config(text="Your choosen file is：\n"+ source_file_path)
    else:
        lb.config(text="Please select a figure!")


def save_file():
    global target_file_path
    global file_name
    global file_type
    if len(file_name):
        target_file_path = filedialog.asksaveasfilename(title='Save file',initialfile=file_name,filetypes=[('eps file','*.eps')]) #
        print('Saved file：', target_file_path)

        # file_text = text1.get('1.0', tk.END)
        if len(target_file_path):
            file_name = source_file_path
            file_rename = target_file_path + '.eps'
            try:
                fig = Image.open(file_name)
                fig = fig.convert('RGB')
                fig.save(file_rename)
                fig.close()
                lb.config(text="Your saved file is：\n" + file_rename)
            except Exception:
                tk.messagebox.showerror(title='Error',message='Only figure is accepted!')
        else:
            lb.config(text="Please specify a directory!")
    else:
        tk.messagebox.showwarning(title='Warning', message='Please select a figure first!')

def close_window():
    window.destroy()
if __name__ == '__main__':
    window = tk.Tk()
    window.title('ToEPS')  # 标题
    window.geometry('400x300')  # 窗口尺寸
    window.resizable(0,0)  # forbidden scaling of window size
    # var = tk.StringVar()

    lb = tk.Label(window, text='No file selected', bg='#808080', font=('Times', 12), fg='white', width=50,
             height=5, wraplength=400,justify='center')
    lb.pack(fill=X)


    bt1 = tk.Button(window, text='Select figure', relief='raised',width=15, height=2, bg='#696969', fg='white',
                    command=open_file)
    bt1.place(relx=0.1, rely=0.5, anchor='nw')
    bt2 = tk.Button(window, text='Save EPS to', relief='raised', width=15, height=2, bg='#696969', fg='white',
                    command=save_file)
    bt2.place(relx=0.5, rely=0.5, anchor='nw')

    window_exit = tk.Button(window, text='Exit', relief='raised', width=10, height=2, bg='#F8F8FF', fg='red',
                            command=close_window)
    window_exit.place(relx=0.35, rely=0.75, anchor='nw')
    window.mainloop()  # 显示
