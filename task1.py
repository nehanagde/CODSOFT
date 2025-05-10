import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List 📋")
        self.root.geometry("400x500")
        self.root.config(bg="#2e5d71")

        self.tasks = []

        self.title = tk.Label(root, text="To-Do List 📋", font=("Times new roman", 18, "bold"), bg="#2e5d71", fg="white")
        self.title.pack(pady=10)

        self.task_entry = tk.Entry(root, font=("Times new roman", 14), width=25)
        self.task_entry.pack(pady=10)

        self.add_btn = tk.Button(root, text="Add", font=("Times new roman", 12, "bold"), bg="green", fg="white", command=self.add_task)
        self.add_btn.pack(pady=5)

        self.task_frame = tk.Frame(root, bg="#2c2c54")
        self.task_frame.pack(pady=10)

    def add_task(self):
        task_text = self.task_entry.get()
        if not task_text:
            messagebox.showwarning("Warning", "Please enter a task!")
            return

        task_frame = tk.Frame(self.task_frame, bg="#2c2c54")
        task_frame.pack(fill="x", pady=2)

        var = tk.BooleanVar()

        check = tk.Checkbutton(task_frame, variable=var, command=lambda: self.toggle_task(var, label), bg="#2c2c54")
        check.pack(side="left", padx=5)

        label = tk.Label(task_frame, text=task_text, font=("Helvetica", 12), fg="white", bg="#2c2c54")
        label.pack(side="left")

        del_btn = tk.Button(task_frame, text="✖", bg="#ff6b6b", fg="white", command=lambda: self.delete_task(task_frame))
        del_btn.pack(side="right", padx=5)

        self.task_entry.delete(0, tk.END)

    def toggle_task(self, var, label):
        if var.get():
            label.config(fg="gray", font=("Helvetica", 12, "overstrike"))
        else:
            label.config(fg="white", font=("Helvetica", 12, "normal"))

    def delete_task(self, task_frame):
        task_frame.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
