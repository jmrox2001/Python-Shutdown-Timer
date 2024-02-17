import tkinter as tk
import time
import threading
import subprocess

def shutdown():
    subprocess.run(["shutdown", "/s", "/f", "/t", "0"])

def start_timer():
    total_minutes = 0
    if hours_entry.get():
        total_minutes += int(hours_entry.get()) * 60
    if minutes_entry.get():
        total_minutes += int(minutes_entry.get())
    
    remaining_seconds = total_minutes * 60
    
    while remaining_seconds > 0:
        hours_remaining = remaining_seconds // 3600
        minutes_remaining = (remaining_seconds // 60) % 60
        seconds_remaining = remaining_seconds % 60
        timer_label.config(text=f"Time remaining: {hours_remaining} hours, {minutes_remaining} minutes, {seconds_remaining} seconds")
        time.sleep(1)
        remaining_seconds -= 1
    shutdown()

def start_timer_thread():
    timer_thread = threading.Thread(target=start_timer)
    timer_thread.start()

root = tk.Tk()
root.title("Shutdown Timer")

hours_label = tk.Label(root, text="Enter hours:")
hours_label.grid(row=0, column=0, padx=10, pady=10)

hours_entry = tk.Entry(root)
hours_entry.grid(row=0, column=1, padx=10, pady=10)

minutes_label = tk.Label(root, text="Enter minutes:")
minutes_label.grid(row=1, column=0, padx=10, pady=10)

minutes_entry = tk.Entry(root)
minutes_entry.grid(row=1, column=1, padx=10, pady=10)

start_button = tk.Button(root, text="Start Timer", command=start_timer_thread)
start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

timer_label = tk.Label(root, text="")
timer_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
