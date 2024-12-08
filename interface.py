import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class FormulaFinderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formula Finder")
        self.setGeometry(100, 100, 600, 600)

        self.formula_database = self.read_database('bd.txt')

        self.layout = QVBoxLayout()

        self.letter_label = QLabel("Введите физическую величину (например, E, P, F):")
        self.letter_label.setFont(QFont("Arial", 12))
        self.letter_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.letter_label)

        self.letter_input = QLineEdit()
        self.letter_input.setStyleSheet("""
            background-color: #f0f8ff;
            border: 1px solid #87ceeb;
            border-radius: 5px;
            padding: 5px;
        """)
        self.layout.addWidget(self.letter_input)

        self.search_button = QPushButton("Найти законы")
        self.search_button.setStyleSheet("""
            background-color: #87ceeb;
            color: white;
            border-radius: 5px;
            padding: 10px;
        """)
        self.layout.addWidget(self.search_button)

        self.law_list = QListWidget()
        self.law_list.setStyleSheet("""
            background-color: #f0f8ff;
            border: 1px solid #87ceeb;
            border-radius: 5px;
            padding: 5px;
        """)
        self.layout.addWidget(self.law_list)

        self.select_law_button = QPushButton("Показать формулы закона")
        self.select_law_button.setStyleSheet("""
            background-color: #87ceeb;
            color: white;
            border-radius: 5px;
            padding: 10px;
        """)
        self.layout.addWidget(self.select_law_button)

        self.formula_list = QListWidget()
        self.formula_list.setStyleSheet("""
            background-color: #f0f8ff;
            border: 1px solid #87ceeb;
            border-radius: 5px;
            padding: 5px;
        """)
        self.layout.addWidget(self.formula_list)

        self.select_formula_button = QPushButton("Выбрать формулу")
        self.select_formula_button.setStyleSheet("""
            background-color: #87ceeb;
            color: white;
            border-radius: 5px;
            padding: 10px;
        """)
        self.layout.addWidget(self.select_formula_button)

        self.derived_formula_list = QListWidget()
        self.derived_formula_list.setStyleSheet("""
            background-color: #f0f8ff;
            border: 1px solid #87ceeb;
            border-radius: 5px;
            padding: 5px;
        """)
        self.layout.addWidget(self.derived_formula_list)

        self.setLayout(self.layout)

        self.search_button.clicked.connect(self.find_laws)
        self.select_law_button.clicked.connect(self.show_law_formulas)
        self.select_formula_button.clicked.connect(self.show_selected_formula)

    def read_database(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            bd_file = file.read().strip().split('\n')

        arr_bing = []
        for line in bd_file:
            parts = line.split('@')
            if len(parts) == 3:
                formula_part = parts[0].split(' = ')[0].strip()
                formula = parts[0].strip()
                description = parts[1].strip()
                law = parts[2].strip()

                arr_bing.append({
                    'formula_part': formula_part,
                    'formula': formula,
                    'description': description,
                    'law': law
                })
        return arr_bing

    def find_laws(self):
        letter = self.letter_input.text().strip()
        if letter:
            found_laws = {entry['law'] for entry in self.formula_database if letter in entry['formula_part']}
            if found_laws:
                self.law_list.clear()
                self.law_list.addItems(found_laws)
            else:
                QMessageBox.warning(self, "Not Found", "Не было найдено законов для данной физической величины")
                self.law_list.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Пожалуйста, введите физическую величину")

    def show_law_formulas(self):
        selected_law = self.law_list.currentItem()
        if selected_law:
            law_name = selected_law.text()
            found_formulas = [entry['formula'] for entry in self.formula_database if entry['law'] == law_name]
            if found_formulas:
                self.formula_list.clear()
                self.formula_list.addItems(found_formulas)
            else:
                QMessageBox.warning(self, "No Formulas", "Нет формул для выбранного закона")
        else:
            QMessageBox.warning(self, "No Selection", "Пожалуйста, выберите закон из списка")

    def show_selected_formula(self):
        selected_formula = self.formula_list.currentItem()
        if selected_formula:
            formula_text = selected_formula.text()
            for entry in self.formula_database:
                if entry['formula'] == formula_text:
                    self.derived_formula_list.clear()
                    self.derived_formula_list.addItem(f"Выводные формулы для {entry['formula']} (пока не реализовано)")
                    break
        else:
            QMessageBox.warning(self, "No Selection", "Пожалуйста, выберите формулу из списка")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormulaFinderApp()
    window.show()
    sys.exit(app.exec_())

