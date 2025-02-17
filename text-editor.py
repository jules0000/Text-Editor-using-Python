import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")])
    if file:
        text_area.delete(1.0, tk.END)
        text_area.insert(1.0, file.read())
        file.close()

def save_file():
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")])
    if file:
        file.write(text_area.get(1.0, tk.END))
        file.close()

def exit_app():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("600x400")

text_area = tk.Text(root, wrap="word", undo=True)
text_area.pack(expand=1, fill="both")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()
