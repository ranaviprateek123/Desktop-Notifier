import tkinter as tk
from tkinter import messagebox
from plyer import notification
import winsound
from datetime import datetime, timedelta
from tkinter import ttk

class ReminderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reminder Application")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.reminder_label = tk.Label(self, text="Set Reminder Time (HH:MM:SS):", font=("Helvetica", 12))
        self.reminder_label.pack(pady=10)

        self.reminder_entry = tk.Entry(self, font=("Helvetica", 12))
        self.reminder_entry.pack(pady=5)

        self.notes_label = tk.Label(self, text="Notes:", font=("Helvetica", 12))
        self.notes_label.pack(pady=10)

        self.notes_entry = tk.Entry(self, font=("Helvetica", 12))
        self.notes_entry.pack(pady=5)

        self.set_button = tk.Button(self, text="Set Reminder", command=self.set_reminder, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief=tk.FLAT)
        self.set_button.pack(pady=10, ipadx=10, ipady=5)

        self.progress_label = tk.Label(self, text="Time Remaining:", font=("Helvetica", 12))
        self.progress_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self, orient='horizontal', length=300, mode='determinate')
        self.progress_bar.pack(pady=5)

    def set_reminder(self):
        try:
            hours, minutes, seconds = map(int, self.reminder_entry.get().split(':'))
            reminder_time = datetime.now() + timedelta(hours=hours, minutes=minutes, seconds=seconds)
            current_time = datetime.now()
            if reminder_time <= current_time:
                messagebox.showwarning("Invalid Time", "Please enter a future time.")
                return

            time_diff = (reminder_time - current_time).total_seconds()
            self.progress_bar["maximum"] = time_diff
            self.progress_bar["value"] = time_diff

            self.after(1000, lambda: self.update_progress(time_diff))
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter time in HH:MM:SS format.")

    def update_progress(self, remaining_time):
        if remaining_time > 0:
            remaining_time -= 1
            self.progress_bar["value"] = remaining_time
            self.after(1000, lambda: self.update_progress(remaining_time))
        else:
            self.show_notification()

    def show_notification(self):
        notification_title = "Reminder"
        notification_text = f"Time to attend to your task!\nNotes: {self.notes_entry.get()}"

        notification.notify(
            title=notification_title,
            message=notification_text,
            app_icon=None,
            timeout=10,
        )
        winsound.Beep(1000, 3000)
        winsound.Beep(2000, 3000)
        winsound.Beep(1000, 3000)
         # Beep sound effect

if __name__ == "__main__":
    app = ReminderApp()
    app.mainloop()
