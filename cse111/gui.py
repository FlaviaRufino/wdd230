import tkinter as tk
from tkinter import messagebox
from number_entry import FloatEntry

def main():
    root = tk.Tk()
    root.title("Rectangle Area Calculator")

    lbl_width = tk.Label(root, text="Width:")
    lbl_width.grid(row=0, column=0, padx=5, pady=5)

    txt_width = FloatEntry(root)
    txt_width.grid(row=0, column=1, padx=5, pady=5)

    lbl_height = tk.Label(root, text="Height:")
    lbl_height.grid(row=1, column=0, padx=5, pady=5)

    txt_height = FloatEntry(root)
    txt_height.grid(row=1, column=1, padx=5, pady=5)

    btn_calculate = tk.Button(root, text="Calculate", command=lambda: calculate_area(txt_width, txt_height))
    btn_calculate.grid(row=2, column=0, padx=5, pady=5)

    lbl_result = tk.Label(root, text="Area:")
    lbl_result.grid(row=2, column=1, padx=5, pady=5)

    btn_clear = tk.Button(root, text="Clear", command=lambda: clear_inputs(txt_width, txt_height, lbl_result))
    btn_clear.grid(row=3, column=0, padx=5, pady=5)

    root.mainloop()

def calculate_area(width_entry, height_entry):
    try:
        width = width_entry.get()
        height = height_entry.get()

        area = width * height

        lbl_result.config(text=f"Area: {area}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def clear_inputs(width_entry, height_entry, result_label):
    width_entry.clear()
    height_entry.clear()
    result_label.config(text="Area:")

if __name__ == "__main__":
    main()
