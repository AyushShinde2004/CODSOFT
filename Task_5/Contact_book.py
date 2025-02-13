import tkinter as tk
from tkinter import ttk, messagebox

class ContactManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")
        self.master.geometry("800x500")
        self.master.resizable(True, True)
        self.contacts = []
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.master, padding=20)
        self.main_frame.pack(fill="both", expand=True)
        self.input_frame = ttk.LabelFrame(self.main_frame, text="Contact Details", padding=10)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.name_label = ttk.Label(self.input_frame, text="Name:")
        self.phone_label = ttk.Label(self.input_frame, text="Phone:")
        self.email_label = ttk.Label(self.input_frame, text="Email:")
        self.address_label = ttk.Label(self.input_frame, text="Address:")
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.name_entry = ttk.Entry(self.input_frame, textvariable=self.name_var, width=30)
        self.phone_entry = ttk.Entry(self.input_frame, textvariable=self.phone_var, width=30)
        self.email_entry = ttk.Entry(self.input_frame, textvariable=self.email_var, width=30)
        self.address_entry = ttk.Entry(self.input_frame, textvariable=self.address_var, width=30)
        self.button_frame = ttk.Frame(self.main_frame, padding=10)
        self.button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.add_button = ttk.Button(self.button_frame, text="➕ Add Contact", command=self.add_contact)
        self.view_button = ttk.Button(self.button_frame, text="👀 View Contacts", command=self.view_contacts)
        self.search_button = ttk.Button(self.button_frame, text="🔍 Search Contact", command=self.search_contact)
        self.update_button = ttk.Button(self.button_frame, text="✏️ Update Contact", command=self.update_contact)
        self.delete_button = ttk.Button(self.button_frame, text="🗑️ Delete Contact", command=self.delete_contact)
        self.tree_frame = ttk.Frame(self.main_frame, padding=10)
        self.tree_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        self.tree = ttk.Treeview(
            self.tree_frame,
            columns=("Name", "Phone", "Email", "Address"),
            show="headings",
            selectmode="browse"
        )
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

    def setup_layout(self):
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.email_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.address_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.address_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.add_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.view_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.search_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        self.update_button.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        self.delete_button.grid(row=0, column=4, padx=5, pady=5, sticky="ew")
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(2, weight=1)
        self.tree_frame.columnconfigure(0, weight=1)
        self.tree_frame.rowconfigure(0, weight=1)

    def add_contact(self):
        name = self.name_var.get().strip()
        phone = self.phone_var.get().strip()
        email = self.email_var.get().strip()
        address = self.address_var.get().strip()
        
        if not name or not phone:
            messagebox.showwarning("Input Error", "Name and Phone are required!")
            return
        for contact in self.contacts:
            if contact["phone"] == phone:
                messagebox.showwarning("Duplicate", "Contact with this phone number already exists!")
                return
        self.contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")
        
        messagebox.showinfo("Success", "Contact added successfully!")
        self.view_contacts()

    def view_contacts(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for contact in self.contacts:
            self.tree.insert("", "end", values=(
                contact["name"],
                contact["phone"],
                contact["email"],
                contact["address"]
            ))

    def search_contact(self):
        search_term = self.name_var.get().strip() or self.phone_var.get().strip()
        if not search_term:
            messagebox.showwarning("Input Error", "Please enter a name or phone number to search!")
            return
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
                results.append(contact)
        
        if not results:
            messagebox.showinfo("Not Found", "No matching contacts found!")
            return
        self.tree.delete(*self.tree.get_children())
        for contact in results:
            self.tree.insert("", "end", values=(
                contact["name"],
                contact["phone"],
                contact["email"],
                contact["address"]
            ))

    def update_contact(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a contact to update!")
            return
        selected_item = self.tree.item(selected)
        name, phone, email, address = selected_item["values"]
        for contact in self.contacts:
            if contact["phone"] == phone:
                contact["name"] = self.name_var.get().strip()
                contact["phone"] = self.phone_var.get().strip()
                contact["email"] = self.email_var.get().strip()
                contact["address"] = self.address_var.get().strip()
                
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.view_contacts()
                return

    def delete_contact(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a contact to delete!")
            return
        selected_item = self.tree.item(selected)
        name, phone, email, address = selected_item["values"]
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete {name}?")
        if not confirm:
            return
        self.contacts = [contact for contact in self.contacts if contact["phone"] != phone]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        self.view_contacts()

    def on_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        selected_item = self.tree.item(selected)
        name, phone, email, address = selected_item["values"]
        self.name_var.set(name)
        self.phone_var.set(phone)
        self.email_var.set(email)
        self.address_var.set(address)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
