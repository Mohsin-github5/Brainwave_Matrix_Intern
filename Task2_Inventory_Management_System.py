
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

Accounts_cred = {"admin": "12345", "staff": "ufgw"}
stock_of_data = {}

def authenticate():
    user = simpledialog.askstring("Login", "Enter The Username:")
    pwrd = simpledialog.askstring("Login", "Enter the Password: ", show="*")
    if user in Accounts_cred and Accounts_cred[user] == pwrd:
        messagebox.showinfo("Login Successful", f"Welcome {user}!")
        launch_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def launch_dashboard():
    global dashbrd
    dashbrd = tk.Toplevel(main_window)
    dashbrd.title("Inventory Management System")
    dashbrd.geometry("780x500")
    headers = ("Code", "Product Name", "Stock", "Price")
    global table
    table = ttk.Treeview(dashbrd, columns=headers, show="headings")
    for header in headers:
        table.heading(header, text=header)
        table.column(header, width=150, anchor="center")
    table.pack(fill=tk.BOTH, expand=True)

    control_panel = tk.Frame(dashbrd)
    control_panel.pack(pady=12)
    tk.Button(control_panel, text="➕ Add Product", width=12, command=add_product).grid(row=0, column=0, padx=6)
    tk.Button(control_panel, text="✏️ Edit Product", width=12, command=modify_product).grid(row=0, column=1, padx=6)
    tk.Button(control_panel, text="❌ Delete Product", width=12, command=delete_product).grid(row=0, column=2, padx=6)
    tk.Button(control_panel, text="⚠️ Stock Alert", width=12, command=alert_low_stock).grid(row=0, column=3, padx=6)
    reload_table()

def reload_table():
    table.delete(*table.get_children())
    for code, details in stock_of_data.items():
        table.insert("", "end", iid=code, values=(code, details["Name"], details["Amount"], details["Price"]))

def add_product():
    code = simpledialog.askstring("Add Product", "Enter Product Code:")
    if not code:
        return
    if code in stock_of_data:
        messagebox.showerror("Duplicate Code", "Product Code already exists.")
        return
    title = simpledialog.askstring("Add Product", "Enter Product Name:")
    try:
        amount = int(simpledialog.askstring("Add Product", "Enter Stock Amount:"))
        price = float(simpledialog.askstring("Add Product", "Enter Stock Price:"))
    except:
        messagebox.showerror("Invalid Input", "Please enter valid number for stock and price.")
        return
    stock_of_data[code] = {"Name": title, "Amount": amount, "Price": price}
    reload_table()

def modify_product():
    chosen = table.selection()
    if not chosen:
        messagebox.showwarning("Edit product", "Please select a product to edit.")
        return
    code = chosen[0]
    prod = stock_of_data[code]
    try:
        new_title = simpledialog.askstring("Edit Product", "Enter new Product Name:", initialvalue=prod["Name"])
        new_amount = int(simpledialog.askstring("Edit Product", "Enter new Product Quantity:", initialvalue=prod["Amount"]))
        new_price = float(simpledialog.askstring("Edit Product", "Enter new Product Price:", initialvalue=prod["Price"]))
    except:
        messagebox.showerror("invalid Input", "Please Enter valid number for stock and price.")
        return
    stock_of_data[code] = {"Name": new_title, "Amount": new_amount, "Price": new_price}
    reload_table()

def delete_product():
    chosen = table.selection()
    if not chosen:
        messagebox.showwarning("Delete product", "Please select a product to delete.")
        return
    code = chosen[0]
    confirm = messagebox.askyesno("Confirm", f"Remove {stock_of_data[code]['Name']} ?")
    if confirm:
        del stock_of_data[code]
        reload_table()

def alert_low_stock():
    alerts = [f"{d['Name']} (Qty: {d['Amount']})" for c, d in stock_of_data.items() if d["Amount"] <= 5]
    if alerts:
        messagebox.showwarning("Low Stock", "\n".join(alerts))
    else:
        messagebox.showinfo("Stock Status", "All good!")

# Main window code at top-level
main_window = tk.Tk()
main_window.title("Login - Inventory Management System")
main_window.geometry("320x180")
tk.Label(main_window, text="Inventory Management System", font=("Arial", 16, "bold")).pack(pady=20)
tk.Button(main_window, text="Login", width=15, command=authenticate).pack()
main_window.mainloop()

            
        

                    
