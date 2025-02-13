import tkinter as tk
from tkinter import ttk, messagebox
import string
import random

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x250")
        self.master.resizable(False, False)
        self.setup_style()
        
        self.create_widgets()
        self.setup_layout()

    def setup_style(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Segoe UI', 10))
        self.style.configure('TButton', font=('Segoe UI', 10), foreground='white')
        self.style.configure('TEntry', font=('Segoe UI', 12))
        self.style.configure('TCombobox', font=('Segoe UI', 10))
        self.style.configure('TRadiobutton', background='#f0f0f0', font=('Segoe UI', 10))
        self.style.map('Generate.TButton',
                      background=[('active', '#45a049'), ('!disabled', '#4CAF50')])
        self.style.map('Copy.TButton',
                      background=[('active', '#1976D2'), ('!disabled', '#2196F3')])

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.master, padding=15)
        self.main_frame.pack(fill='both', expand=True)


        self.length_label = ttk.Label(self.main_frame, text="Password Length:")
        self.length_var = tk.IntVar(value=12)
        self.length_combobox = ttk.Combobox(
            self.main_frame, 
            textvariable=self.length_var,
            values=[8, 12, 16, 20, 24],
            width=5,
            state='readonly'
        )

        self.char_type_label = ttk.Label(self.main_frame, text="Character Type:")
        self.char_type_var = tk.StringVar(value="all") 
        self.char_type_frame = ttk.Frame(self.main_frame)
        
        self.letters_only = ttk.Radiobutton(
            self.char_type_frame,
            text="Letters Only",
            variable=self.char_type_var,
            value="letters"
        )
        self.letters_numbers = ttk.Radiobutton(
            self.char_type_frame,
            text="Letters + Numbers",
            variable=self.char_type_var,
            value="letters_numbers"
        )
        self.letters_symbols = ttk.Radiobutton(
            self.char_type_frame,
            text="Letters + Symbols",
            variable=self.char_type_var,
            value="letters_symbols"
        )
        self.all_chars = ttk.Radiobutton(
            self.char_type_frame,
            text="All Characters",
            variable=self.char_type_var,
            value="all"
        )
        self.generate_btn = ttk.Button(
            self.main_frame,
            text='Generate Password',
            command=self.generate_password,
            style='Generate.TButton'
        )

        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.password_var,
            font=('Segoe UI', 12),
            state='readonly',
            width=25
        )
        self.copy_btn = ttk.Button(
            self.main_frame,
            text='Copy',
            command=self.copy_to_clipboard,
            style='Copy.TButton',
            width=8
        )

    def setup_layout(self):
        self.length_label.grid(row=0, column=0, padx=(0, 5), pady=5, sticky='e')
        self.length_combobox.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.generate_btn.grid(row=0, column=2, padx=(10, 5), pady=5, sticky='ew')
        
        self.char_type_label.grid(row=1, column=0, padx=(0, 5), pady=5, sticky='e')
        self.char_type_frame.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='w')
        
        self.letters_only.pack(anchor='w')
        self.letters_numbers.pack(anchor='w')
        self.letters_symbols.pack(anchor='w')
        self.all_chars.pack(anchor='w')
        
        self.password_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=15, sticky='ew')
        self.copy_btn.grid(row=2, column=2, padx=5, pady=15, sticky='ew')

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)

    def generate_password(self):
        try:
            length = self.length_var.get()
            if length < 4:
                messagebox.showerror("Error", "Password length must be at least 4 characters")
                return
        except tk.TclError:
            messagebox.showerror("Error", "Please enter a valid number")
            return
          
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        numbers = string.digits
        symbols = string.punctuation

        char_type = self.char_type_var.get()
        if char_type == "letters":
            chars = lower + upper
        elif char_type == "letters_numbers":
            chars = lower + upper + numbers
        elif char_type == "letters_symbols":
            chars = lower + upper + symbols
        else: 
            chars = lower + upper + numbers + symbols

        password = ''.join(random.sample(chars, length))
        self.password_var.set(password)
        self.copy_to_clipboard(show_message=False)
        messagebox.showinfo("Success", "Password generated and copied to clipboard!")

    def copy_to_clipboard(self, show_message=True):
        password = self.password_var.get()
        if password:
            self.master.clipboard_clear()
            self.master.clipboard_append(password)
            if show_message:
                messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
