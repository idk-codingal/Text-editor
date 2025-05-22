from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Best text editor")
window.geometry("400x400")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def open_file():
    """Open a file for editing"""
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, END)

    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
        window.title(f"Best text editor")

def save_file():
    """save a file"""
    filepath = asksaveasfilename(defaultextension= "txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, END)

    with open(filepath, "w") as output_file:
        text = output_file.read()
        txt_edit.insert(END, text)
        output_file.close()
        window.title(f"Best text editor - {filepath}")

txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="To open", command=open_file)
btn_save = Button(fr_buttons, text="To save", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=1, column=0, sticky="nsew")

window.mainloop