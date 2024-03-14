import tkinter as tk
from tkinter import messagebox
import webbrowser

def about_us():
    def callback(url):
        webbrowser.open_new_tab(url)
    
    about_window = tk.Toplevel()
    about_window.title("About Us")

    about_label = tk.Label(about_window, text="This program helps you for adding \na list of names, surnames, and ages.")
    about_label.pack(padx=10, pady=10)

    link_label = tk.Label(about_window, text="GitHub", fg="blue", cursor="hand2")
    link_label.pack(pady=1)
    link_label.bind("<Button-1>", lambda e: callback("https://github.com/FarshidRA"))

    mail_label = tk.Label(about_window, text="E-mail", fg="blue", cursor="hand2")
    mail_label.pack(pady=1)
    mail_label.bind("<Button-1>", lambda e: callback("mailto:adernis@yahoo.com"))

    version_label = tk.Label(about_window, text="Version 1.6.17")
    version_label.pack(pady=0)

    copyright_label = tk.Label(about_window, text="© 2023 - 2024")
    copyright_label.pack(pady=1)


