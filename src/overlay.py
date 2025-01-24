import sys
import threading
import time
from PyQt5 import QtWidgets, QtCore
import tkinter as tk
from tkinter import ttk

import rich
import rich.text
import data
from util import console

overlay = None

# PyQt5 Transparent Overlay for Logs
class TransparentOverlay(QtWidgets.QWidget):    
    welcome_message = [
        "Welcome to Pazdikan's auto AFK script for DBD",
        "This is an overlay, so you don't have to alt tab to see stats",
        "Welcome message will be replaced with stat  after the first game ends.",
        "",
        "Check the web panel with settings at http://localhost:5000/",
    ]

    def __init__(self):
        super().__init__()
        
        self.logs = []
        self.shouldBeRendered = True

        # Get screen size (1080p resolution)
        screen = QtWidgets.QApplication.desktop().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()
        # Set up the window (overlay)
        self.setWindowTitle("DBD AFK Logs Overlay")
        # Position the window on the left side of the screen (15% of the width and full height)
        self.setGeometry(0, 0, int(screen_width * 0.25), int(screen_height * 0.75))

        # Set the window flags (frameless, stay on top, click-through)
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.Tool |
            QtCore.Qt.X11BypassWindowManagerHint
        )


        # Set window attributes for transparency and click-through
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)  # Makes window click-through
        
        # Set the background color (fully transparent background)
        self.setStyleSheet("background: rgba(0, 0, 0, 100);")  # Fully transparent

        # Create a label to show logs (in this case, use a non-transparent background)
        self.log_label = QtWidgets.QLabel(self)
        self.log_label.setText("\n".join(self.welcome_message))
        self.log_label.setStyleSheet("color: white; font: bold 10pt Arial; padding: 10px;")
        self.log_label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.log_label.setGeometry(10, 10, int(screen_width * 0.25) - 20, int(screen_height * 0.75) - 20)  # Adjust label to fit within the overlay

        # Set up event filters for mouse enter and leave
        self.installEventFilter(self)
        self.is_on_left = True

    def set_visibility(self, visibility):
        self.shouldBeRendered = visibility
        
        if not self.shouldBeRendered:
            QtCore.QTimer.singleShot(0, self.hide)
        else:
            QtCore.QTimer.singleShot(0, self.show)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Enter:
            self.switch_position()
        return super().eventFilter(source, event)

    def switch_position(self):
        screen = QtWidgets.QApplication.desktop().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()
        if self.is_on_left:
            self.setGeometry(int(screen_width * 0.6), 0, int(screen_width * 0.25), int(screen_height * 0.75))
        else:
            self.setGeometry(0, 0, int(screen_width * 0.25), int(screen_height * 0.75))
        self.is_on_left = not self.is_on_left

    def update_log(self, new_log):
        """Update the log displayed on the overlay."""
        
        if len(self.logs) >= 45:
            self.logs.pop(0)

        # Check if new log matches the last entry
        if self.logs and new_log in self.logs[-1]:
            # Extract existing count if present
            last_entry = self.logs[-1]
            if "(x" in last_entry:
                count = int(last_entry[last_entry.find("(x")+2:last_entry.find(")")])
                self.logs[-1] = f"{new_log} (x{count+1})"
            else:
                self.logs[-1] = f"{new_log} (x2)"
        else:
            self.logs.append(new_log)

        if (data.games > 0):
            pure_stats = []
            for stat in console.get_stats():
                if isinstance(stat, rich.text.Text):
                    pure_stats.append(stat.plain)
                else:
                    pure_stats.append(stat)
            self.log_label.setText(f"{'\n'.join(pure_stats)}\n\n{'\n'.join(self.logs)}")
        else:
            self.log_label.setText(f"{'\n'.join(self.welcome_message)}\n\n{'\n'.join(self.logs)}")

# Thread for running the PyQt5 overlay
def run_overlay():
    global overlay
    app = QtWidgets.QApplication(sys.argv)
    overlay = TransparentOverlay()
    overlay.show()
    
    sys.exit(app.exec_())