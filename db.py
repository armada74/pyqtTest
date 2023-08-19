import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextBrowser
import sqlite3

class DatabaseExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.init_db()

    def init_ui(self):
        self.setWindowTitle("Database Example")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter a name")
        layout.addWidget(self.name_input)

        self.add_button = QPushButton("Add to Database", self)
        self.add_button.clicked.connect(self.add_to_database)
        layout.addWidget(self.add_button)

        self.result_display = QTextBrowser(self)
        layout.addWidget(self.result_display)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def init_db(self):
        self.conn = sqlite3.connect("example.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS names (id INTEGER PRIMARY KEY, name TEXT)")

    def add_to_database(self):
        name = self.name_input.text()
        if name:
            self.cursor.execute("INSERT INTO names (name) VALUES (?)", (name,))
            self.conn.commit()
            self.result_display.append(f"Added: {name}")
            self.name_input.clear()

    def closeEvent(self, event):
        self.conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DatabaseExample()
    window.show()
    sys.exit(app.exec_())