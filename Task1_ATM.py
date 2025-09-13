import tkinter as tkk
from tkinter import messagebox
class ATM_App:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Application")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.balance = 5000
        self.pin = "13779"
        self.transaction_history = []
        self.pin_attempts = 0
        self.login_screen()
    def authenticate(self):
        if self.pin_entry.get() == self.pin:
             self.pin_attempts = 0
             self.menu_screen()
             
        else:
             self.pin_attempts += 1
             if self.pin_attempts >= 3:
                 messagebox.showerror("Blocked!", "Too many wrong attempts")
                 self.root.quit()
             else:
                 messagebox.showerror("Error", f"The Pin is Invalid. Attempts left: {3 - self.pin_attempts}")
    def menu_screen(self):
        self.clear_screen()
        tkk.Label(self.root, text="Welcome to ATM Application", font=("Arial", 16)).pack(pady=20)
        tkk.Button(self.root, text="....Check Balance....", command=self.check_balance).pack()
        tkk.Button(self.root, text="....Deposit Money....", command=self.deposit_screen).pack()
        tkk.Button(self.root, text="....Withdraw Money....", command=self.withdraw_screen).pack()
        tkk.Button(self.root, text="....Exit....", command=self.root.quit).pack()
        tkk.Button(self.root, text="Bank Statement", command=self.show_statment).pack()
        tkk.Button(self.root, text="....Change PIN....", command=self.change_pin_screen).pack()
        tkk.Button(self.root, text="....Logout....", command=self.root.quit).pack()
       
    def deposit_screen(self):
        self.clear_screen()
        tkk.Label(self.root, text="Enter the Amount to Deposit:", font=("Arial", 15)).pack(pady=20)
        self.amount_entry = tkk.Entry(self.root)
        self.amount_entry.pack()
        tkk.Button(self.root, text="Deposit", command=self.deposit).pack(pady=10)
        
    def deposit(self):
            try:
                amount = float(self.amount_entry.get())
                if amount > 0:
                    self.balance += amount
                    self.transaction_history.append(f"Deposited Rs. {amount} | Balance: Rs. {self.balance}")
                    messagebox.showinfo("Successfully", "Deposit Successful")
                    self.menu_screen()
            except ValueError:
                messagebox.showerror("Error", "Invalid amount entered. Please enter a valid number.")
                
    def withdraw_screen(self):
        self.clear_screen()
        tkk.Label(self.root, text="Enter the Amount to Withdraw:", font=("Arial", 15)).pack(pady=20)
        self.amount_entry = tkk.Entry(self.root)
        self.amount_entry.pack()
        tkk.Button(self.root, text="Withdraw", command=self.withdraw).pack(pady=10)
        
    def withdraw(self):
            try:
                amount = float(self.amount_entry.get())
                if amount > 0 and amount <= self.balance:
                     self.balance -= amount
                     self.transaction_history.append(f"Withdraw Rs. {amount} | Balance: Rs.{self.balance}")
                     messagebox.showinfo("Success", "Withdrawal Successful")
                     self.menu_screen()
            except ValueError:
                messagebox.showerror("Error", "Invalid amount entered. Please enter a valid number.")
    def show_statment(self):
            if not self.transaction_history:
                messagebox.showinfo("Bank Statment" , "No Transaction History.")
            else:
                 history = "\n".join(self.transaction_history[-5:])
                 messagebox.showinfo("Bank Statment", history)
    def change_pin_screen(self):
        self.clear_screen()
        tkk.Label(self.root, text="Enter the New PIN: ", font=("Arial", 15)).pack(pady=20)
        self.new_pin_entry = tkk.Entry(self.root, show="*")
        self.new_pin_entry.pack()
        tkk.Button(self.root, text="Change PIN: ", command=self.update_pin).pack(pady=10)
        
    def update_pin(self):
        new_pin = self.new_pin_entry.get()
        if new_pin:
                self.pin = new_pin
                messagebox.showinfo("Congrats!", "The PIN is changed successfully.")
                self.menu_screen()
        else:
                messagebox.showerror("Error Found", "Please Enter valid PIN.")
    def check_balance(self):
        messagebox.showinfo("Balance", f"Your Balance is Rs. {self.balance}")
                    
    def login_screen(self):
         self.clear_screen()
         tkk.Label(self.root, text="🏦 Welcome to the ATM", font=("Arial", 16)).pack(pady=20)
         self.pin_entry = tkk.Entry(self.root, show= "*")
         self.pin_entry.pack(pady=10)
         tkk.Button(self.root, text="Login", command=self.authenticate).pack(pady=10)
        
    def clear_screen(self):
            for widget in self.root.winfo_children():
                widget.destroy()

      

if __name__ == "__main__":
    root = tkk.Tk()
    app = ATM_App(root)
    root.mainloop()
