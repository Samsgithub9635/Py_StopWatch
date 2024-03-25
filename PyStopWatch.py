# 1. import the Tkinter and ttkthemes modules
# 2. We need a window with following elements:
#       -timer label
#       - button for starting/stopping
#       -button for resetting the timer to 0
#       - function 'count' to update the timer display every second while running
#       -the time should displayed in the 'h:m:s' format
import tkinter as tk
from tkinter.ttk import *
from ttkthemes import ThemedStyle


# Defines a class named Stopwatch which inherits from tk.Tk, making Stopwatch a subclass of the main Tkinter application window.
class Stopwatch(tk.Tk):
    # Initializes the Stopwatch class constructor.
    def __init__(self):
        # Calls the constructor of the superclass(tk.Tk) to initialize the main application window.
        super().__init__()
        self.title("Py StopWatch")
        self.geometry("500x190")
        self.time = 0
        self.running = False

        self.style = ThemedStyle(self)
        self.style.set_theme("adapta")

        self.label = tk.Label(self, text="00:00:00", pady=5, padx=5, font=("ds-digital", 50, 'bold'), bg="black", fg="magenta", width=20, height=1)
        self.label.pack()

        self.alarm_label = tk.Label(self, text="TIME'S UP!", font=("ds-digital", 20, 'bold'), fg="green")
        self.alarm_label.pack(pady=10)

        self.start_button = tk.Button(self, text="START", width=8, height=1, font=("Arial", 14, 'bold'), command=self.start)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self, text="STOP", pady=5, padx=5, width=5, height=1, font=("Arial", 14, 'bold'), command=self.stop)
        self.stop_button.place(x=210, y=135)


        self.reset_button = tk.Button(self, text="RESET", width=8, height=1, font=("Arial", 14, 'bold'), command=self.reset)
        self.reset_button.pack(side=tk.RIGHT)


    def start(self):
        self.running = True
        self.count()
        self.alarm_label.config(text="TIME IS RUNNING OUT")

    def stop(self):
        self.running = False
        self.alarm_label.config(text="TIME'S UP!")


    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="00:00:00")
        self.alarm_label.config(text="LETS  START")

    def count(self):
        if self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.config(text="{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
            self.after(100, self.count)


if __name__ == '__main__':
    stopwatch = Stopwatch()
    stopwatch.mainloop()





