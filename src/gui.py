import sys
import threading
import time
from PyQt5 import QtWidgets, QtCore
import tkinter as tk
from tkinter import ttk

import rich
import rich.text
import config
from util import console

overlay = None

# PyQt5 Transparent Overlay for Logs
class TransparentOverlay(QtWidgets.QWidget):    
    welcome_message = [
        "Welcome to Pazdikan's auto AFK script for DBD",
        "Your stats and logs will appear here.",
        "This is an overlay, so you don't have to",
        "alt tab to see the logs and stats.",
        "",
        "This message will be replaced with stats, after the first game ends.",
    ]

    def __init__(self):
        super().__init__()
        
        self.logs = []

        # Get screen size (1080p resolution)
        screen = QtWidgets.QApplication.desktop().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()
        # Set up the window (overlay)
        self.setWindowTitle("DBD AFK Logs Overlay")
        # Position the window on the left side of the screen (15% of the width and full height)
        self.setGeometry(0, 0, int(screen_width * 0.25), screen_height)

        # Set the window flags (frameless, stay on top, click-through)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.X11BypassWindowManagerHint)

        # Set window attributes for transparency and click-through
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)  # Makes window click-through
        
        # Set the background color (fully transparent background)
        self.setStyleSheet("background: rgba(0, 0, 0, 100);")  # Fully transparent

        # Create a label to show logs (in this case, use a non-transparent background)
        self.log_label = QtWidgets.QLabel(self)
        self.log_label.setText("\n".join(self.welcome_message))
        self.log_label.setStyleSheet("color: lime; font: bold 12pt Arial;")
        self.log_label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.log_label.setGeometry(10, 10, int(screen_width * 0.25) - 20, screen_height - 20)  # Adjust label to fit within the overlay

        # Set up event filters for mouse enter and leave
        self.installEventFilter(self)
        self.is_on_left = True

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Enter:
            self.switch_position()
        return super().eventFilter(source, event)

    def switch_position(self):
        screen = QtWidgets.QApplication.desktop().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()
        if self.is_on_left:
            self.setGeometry(int(screen_width * 0.6), 0, int(screen_width * 0.25), screen_height)
        else:
            self.setGeometry(0, 0, int(screen_width * 0.25), screen_height)
        self.is_on_left = not self.is_on_left

    def update_log(self, new_log):
        """Update the log displayed on the overlay."""

        if len(self.logs) >= 45:
            self.logs.pop(0)

        self.logs.append(new_log)

        if (config.games > 0):
            pure_stats = []

            for stat in console.get_stats():
                if isinstance(stat, rich.text.Text):
                    pure_stats.append(stat.plain)
                else:
                    pure_stats.append(stat)

            self.log_label.setText(f"{"\n".join(pure_stats)}\n\n{"\n".join(self.logs)}")
        else:
            self.log_label.setText(f"{"\n".join(self.welcome_message)}\n\n{"\n".join(self.logs)}")

# Tkinter GUI (Main App)
def create_main_gui():
    # Initialize main window
    root = tk.Tk()
    root.title("Main Application - DBD AFK")
    root.geometry("800x600")
    root.configure(bg="#121212")

    # Create frames with styling
    left_frame = tk.Frame(root, bg="#1e1e1e")
    left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    right_frame = tk.Frame(root, bg="#1e1e1e")
    right_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=5, pady=5)

    bottom_left_frame = tk.Frame(root, bg="#333333")
    bottom_left_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    # Make the layout flexible
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=4)
    root.grid_columnconfigure(1, weight=6)

    # Stats (Top left)
    stats_frame = tk.Frame(left_frame, bg="#1e1e1e", height=250)
    stats_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    stats_label = tk.Label(stats_frame, text="Game Stats", fg="#00FF00", font=("Arial", 16), bg="#1e1e1e")
    stats_label.pack(pady=10)

    # Logs (Bottom left)
    logs_frame = tk.Frame(bottom_left_frame, bg="#333333", height=200)
    logs_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    logs_label = tk.Label(logs_frame, text="Logs", fg="#FF5733", font=("Arial", 16), bg="#333333")
    logs_label.pack(pady=10)

    log_text = tk.Text(logs_frame, height=8, width=35, bg="#222222", fg="#FFFFFF", font=("Courier New", 10))
    log_text.pack(padx=5, pady=5)
    log_text.insert(tk.END, "Log entry example...\n")

    # Settings (Right side)
    settings_frame = tk.Frame(right_frame, bg="#1e1e1e")
    settings_frame.pack(fill="both", expand=True, padx=5, pady=5)
    settings_label = tk.Label(settings_frame, text="Settings", fg="#00FFFF", font=("Arial", 18), bg="#1e1e1e")
    settings_label.pack(pady=20)

    slider_value_label = tk.Label(settings_frame, text="Slider Value: 0", fg="#FFFFFF", bg="#1e1e1e", font=("Arial", 12))
    slider_value_label.pack(pady=10)

    slider = tk.Scale(settings_frame, from_=0, to=100, orient="horizontal", bg="#1e1e1e", fg="#00FF00", sliderlength=30)
    slider.pack(pady=10)

    select_label = tk.Label(settings_frame, text="Choose Option:", fg="#FFFFFF", bg="#1e1e1e", font=("Arial", 12))
    select_label.pack(pady=10)

    options = ["Option 1", "Option 2", "Option 3", "Option 4"]
    select_menu = ttk.Combobox(settings_frame, values=options, state="readonly", font=("Arial", 12))
    select_menu.pack(pady=10)

    # Main GUI loop
    root.mainloop()

# Thread for running the PyQt5 overlay
def run_overlay():
    global overlay
    app = QtWidgets.QApplication(sys.argv)
    overlay = TransparentOverlay()
    overlay.show()
    
    sys.exit(app.exec_())
