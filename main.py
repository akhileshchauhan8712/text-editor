# Import tkinter for creating GUI apps
import tkinter as tk
from tkinter import filedialog, messagebox

# Main window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("700x490")


# Create text area
text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12))
text.pack(expand=True, fill=tk.BOTH)


# Function 1 - Create a new file
def new_file():
    text.delete(1.0, tk.END)


# Function 2 - Open a file
def open_file():
    # Open file dialog
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = file.read()

            text.delete(1.0, tk.END)
            text.insert(tk.END, data)

        except Exception as error:
            messagebox.showerror("Error", f"Unable to open file:\n{error}")


# Function 3 - Save the file
def save_file():
    # Open save file dialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )

    if file_path:
        # Make sure .txt extension is added
        if not file_path.lower().endswith(".txt"):
            file_path += ".txt"

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text.get(1.0, tk.END))

            messagebox.showinfo("Success", "File saved successfully!")

        except Exception as error:
            messagebox.showerror("Error", f"Unable to save file:\n{error}")


# Menu
menu = tk.Menu(root)
root.config(menu=menu)

# File menu
file_menu = tk.Menu(root, tearoff=0)

# Add File menu to menu bar
menu.add_cascade(label="File", menu=file_menu)

# New, Open, Save, Exit
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


# Start application
root.mainloop()
