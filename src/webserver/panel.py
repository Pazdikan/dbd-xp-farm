import os


def init(app):
    @app.route("/")
    def index():
        try:
            with open("src/webserver/panel.html", "r") as file:
                return file.read()
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return f"File not found. Working directory is: {os.getcwd()}"
