from record_manager import add_record
from about import about_us
import tkinter as tk
from tkinter import ttk
import os
import subprocess

class CustomEntry(ttk.Entry):
    def __init__(self, master=None, placeholder="", color='gray'):
        super().__init__(master,width=25)
        self.placeholder = placeholder
        self.color = color
        self.insert(0, self.placeholder)
        self.bind("<FocusIn>", self.on_entry_click)
        self.bind("<FocusOut>", self.on_focus_out)
        self.configure(foreground=self.color)
    def on_entry_click(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.configure(foreground='black')

    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.configure(foreground=self.color)
            
def on_add_record():
    name = name_entry.get()
    sname = sname_entry.get()
    age = age_entry.get()
    result_label.config(text=add_record(name, sname, age))
    
def on_about_us():
    about_us()

def open_excel_file():
    excel_file_path = 'user_records.xlsx'
    if os.path.exists(excel_file_path):
        subprocess.Popen(['start', excel_file_path], shell=True)
    else:
        messagebox.showerror("Error", "Excel file not Found.")

def clear_placeholder(event, entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title('User Records')

frame = ttk.Frame(root, padding='10')
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text='Name:').grid(column=0, row=0, sticky=tk.W)
name_entry = CustomEntry(frame, placeholder="What's Your Name?")
name_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text='Sure Name:').grid(column=0, row=1, sticky=tk.W)
sname_entry = CustomEntry(frame, placeholder="What's Your Sure Name?")
sname_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text='Sure Name:').grid(column=0, row=2, sticky=tk.W)
age_entry = CustomEntry(frame, placeholder="How Old Are You?")
age_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))

result_label = ttk.Label(frame, text='')
result_label.grid(column=0, row=3, columnspan=2, sticky=tk.W)

add_button = ttk.Button(frame, text='Add Record', command=on_add_record)
add_button.grid(column=0, row=4, columnspan=2, pady=2)

about_button = ttk.Button(frame, text='About Us', command=on_about_us)
about_button.grid(column=0, row=5, columnspan=2, pady=1)

excel_button = ttk.Button(frame, text='Excel', command=open_excel_file)
excel_button.grid(column=0, row=6, columnspan=2, pady=2)

root.mainloop()
