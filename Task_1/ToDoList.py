import tkinter as tk
from tkinter import ttk, messagebox
import random

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate To-Do List")
        self.root.geometry("500x500")
        self.root.resizable(True, True)
        
        self.tasks = []
        self.setup_ui()
        self.setup_styles()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('TFrame', background='#2D2D2D')
        style.configure('TLabel', background='#2D2D2D', foreground='white')
        style.configure('TButton', font=('Segoe UI', 10), relief='flat')
        style.map('TButton',
            background=[('active', '#404040'), ('!active', '#353535')],
            foreground=[('active', 'white'), ('!active', 'white')])
        
        style.configure('Listbox', 
            background='#404040', 
            foreground='white',
            selectbackground='#606060',
            selectforeground='white',
            font=('Segoe UI', 10))
        
        style.configure('Status.TLabel',
            background='#353535',
            foreground='white',
            font=('Segoe UI', 9))

    def setup_ui(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        ttk.Label(header_frame, text="TASK MANAGER", font=('Segoe UI', 16, 'bold')).pack(side=tk.LEFT)
        
        self.entry = ttk.Entry(main_frame, font=('Segoe UI', 12))
        self.entry.pack(fill=tk.X, pady=5)
        self.entry.bind('<Return>', lambda e: self.add_task())    
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(btn_frame, text="➕ Add Task", command=self.add_task).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="🗑️ Delete", command=self.delete_task).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="🎲 Random", command=self.choose_random_task).pack(side=tk.LEFT, padx=2)
        
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        self.listbox = tk.Listbox(list_frame)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(control_frame, text="🧹 Delete All", command=self.delete_all_tasks).pack(side=tk.LEFT, padx=2)
        ttk.Button(control_frame, text="📊 Task Count", command=self.show_number_of_tasks).pack(side=tk.LEFT, padx=2)
        ttk.Button(control_frame, text="🚪 Exit", command=self.root.quit).pack(side=tk.RIGHT, padx=2)
        
        self.status_bar = ttk.Label(main_frame, style='Status.TLabel')
        self.status_bar.pack(fill=tk.X, pady=(10, 0))

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
            self.show_status("Task added!", '#4CAF50')
        else:
            self.show_status("Please enter a task!", '#F44336')

    def delete_task(self):
        try:
            task = self.listbox.get(self.listbox.curselection())
            if task in self.tasks:
                self.tasks.remove(task)
                self.update_listbox()
                self.show_status("Task deleted!", '#4CAF50')
        except:
            self.show_status("No task selected!", '#F44336')

    def delete_all_tasks(self):
        if self.tasks:
            confirm = messagebox.askyesno("Delete All", "Clear all tasks?")
            if confirm:
                self.tasks.clear()
                self.update_listbox()
                self.show_status("All tasks deleted!", '#4CAF50')
        else:
            self.show_status("No tasks to delete!", '#F44336')

    def choose_random_task(self):
        if self.tasks:
            task = random.choice(self.tasks)
            self.show_status(f"Random task: {task}", '#2196F3')
        else:
            self.show_status("No tasks available!", '#F44336')

    def show_number_of_tasks(self):
        self.show_status(f"Total tasks: {len(self.tasks)}", '#9C27B0')

    def show_status(self, message, color):
        self.status_bar.config(foreground=color, text=message)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
