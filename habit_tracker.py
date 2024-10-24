import tkinter as tk
from tkinter import messagebox
import os

# File to save tasks
FILE_NAME = "habit_tracker_tasks.txt"

class HabitTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Habit Tracker")
        self.root.geometry("400x400")
        self.root.config(bg="white")
        
        # Task list
        self.tasks = []
        
        # Load tasks from file
        self.load_tasks()
        
        # Title label
        title_label = tk.Label(root, text="Habit Tracker", font=("Arial", 20), bg="white", fg="black")
        title_label.pack(pady=10)
        
        # Entry for new tasks
        self.task_entry = tk.Entry(root, font=("Arial", 14), width=25)
        self.task_entry.pack(pady=10)
        
        # Buttons to add and remove tasks
        add_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Arial", 12), bg="black", fg="white")
        add_button.pack(pady=5)
        
        clear_button = tk.Button(root, text="Clear Task", command=self.clear_tasks, font=("Arial", 12), bg="black", fg="white")
        clear_button.pack(pady=5)
        
        # Task display list
        self.task_listbox = tk.Listbox(root, font=("Arial", 14), bg="white", fg="red", selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        self.update_task_listbox()
        
        # Save button
        save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks, font=("Arial", 12), bg="black", fg="white")
        save_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def clear_tasks(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to clear.")

    def save_tasks(self):
        with open(FILE_NAME, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        messagebox.showinfo("Save", "Tasks saved successfully!")

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                self.tasks = [line.strip() for line in file]
                self.update_task_listbox()


# Running the app
if __name__ == "__main__":
    root = tk.Tk()
    app = HabitTrackerApp(root)
    root.mainloop()
