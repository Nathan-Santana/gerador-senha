import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string
import pyperclip

class SecurePasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Gerador Seguro de Senhas")
        master.resizable(False, False)

        self.frame = ttk.Frame(master, padding="20")
        self.frame.grid(row=0, column=0)

        ttk.Label(self.frame, text="Senha Gerada:", font=('Arial', 12, 'bold')).grid(row=0, column=0, pady=5)

        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(self.frame, textvariable=self.password_var, 
                                       width=25, font=('Courier', 14), state='readonly',
                                       justify='center')
        self.password_entry.grid(row=1, column=0, pady=10)

        self.btn_frame = ttk.Frame(self.frame)
        self.btn_frame.grid(row=2, column=0, pady=10)
        
        ttk.Button(self.btn_frame, text="Gerar Nova Senha", command=self.generate_password).grid(row=0, column=0, padx=5)
        ttk.Button(self.btn_frame, text="Copiar", command=self.copy_password).grid(row=0, column=1, padx=5)

        self.generate_password()

    def generate_password(self):
        try:
            length = 16  
            min_lower = 2
            min_upper = 2
            min_digits = 2
            min_symbols = 2

            lower = string.ascii_lowercase
            upper = string.ascii_uppercase
            digits = string.digits
            symbols = string.punctuation  

            password = []
            password.extend(secrets.choice(lower) for _ in range(min_lower))
            password.extend(secrets.choice(upper) for _ in range(min_upper))
            password.extend(secrets.choice(digits) for _ in range(min_digits))
            password.extend(secrets.choice(symbols) for _ in range(min_symbols))
            
            remaining = length - (min_lower + min_upper + min_digits + min_symbols)
            all_chars = lower + upper + digits + symbols
            password.extend(secrets.choice(all_chars) for _ in range(remaining))
            
            secrets.SystemRandom().shuffle(password)
            final_password = ''.join(password)

            self.password_var.set(final_password)

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def copy_password(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SecurePasswordGenerator(root)
    root.mainloop()