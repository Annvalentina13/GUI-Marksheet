import tkinter as tk
from tkinter import messagebox

def calculate_result():
    try:
        s1 = float(entry_sub1.get())
        s2 = float(entry_sub2.get())
        s3 = float(entry_sub3.get())
        s4 = float(entry_sub4.get())
        s5 = float(entry_sub5.get())

        total = s1 + s2 + s3 + s4 + s5
        percent = total / 5

        if percent >= 90:
            grade = "A+"
        elif percent >= 80:
            grade = "A"
        elif percent >= 70:
            grade = "B"
        elif percent >= 60:
            grade = "C"
        elif percent >= 50:
            grade = "D"
        else:
            grade = "F"

        result_label.config(text=f"Total: {total}/500\nPercentage: {percent:.2f}%\nGrade: {grade}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all subjects.")

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    for entry in [entry_sub1, entry_sub2, entry_sub3, entry_sub4, entry_sub5]:
        entry.delete(0, tk.END)
    result_label.config(text="")

# GUI Window
root = tk.Tk()
root.title("Student Marksheet")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

# Labels & Entry Fields
tk.Label(root, text="Student Marksheet", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="Name:", bg="#f0f0f0").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Roll No:", bg="#f0f0f0").pack()
entry_roll = tk.Entry(root)
entry_roll.pack()

tk.Label(root, text="Subject 1:", bg="#f0f0f0").pack()
entry_sub1 = tk.Entry(root)
entry_sub1.pack()

tk.Label(root, text="Subject 2:", bg="#f0f0f0").pack()
entry_sub2 = tk.Entry(root)
entry_sub2.pack()

tk.Label(root, text="Subject 3:", bg="#f0f0f0").pack()
entry_sub3 = tk.Entry(root)
entry_sub3.pack()

tk.Label(root, text="Subject 4:", bg="#f0f0f0").pack()
entry_sub4 = tk.Entry(root)
entry_sub4.pack()

tk.Label(root, text="Subject 5:", bg="#f0f0f0").pack()
entry_sub5 = tk.Entry(root)
entry_sub5.pack()

# Buttons
tk.Button(root, text="Calculate", command=calculate_result, bg="#4CAF50", fg="white", width=15).pack(pady=10)
tk.Button(root, text="Clear", command=clear_fields, bg="#FFA500", width=15).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, bg="#f44336", fg="white", width=15).pack(pady=5)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)

root.mainloop()
