import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QDoubleValidator, QIcon


class EuroChangeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ресто Калкулатор (ЕВРО/ЛЕВА)')
        self.setWindowIcon(QIcon('vladpos_logo.png'))
        self.setMinimumWidth(420)

        self.setStyleSheet("""
            QWidget {
                background-color: #f2f2f7;
                font-size: 16px;
            }
            QLabel {
                font-weight: bold;
                padding: 4px;
            }
            QLineEdit {
                padding: 6px;
                border: 2px solid #cccccc;
                border-radius: 8px;
                background: white;
            }
            QPushButton {
                padding: 10px;
                font-size: 16px;
                background-color: #4a90e2;
                color: white;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #357ac8;
            }
        """)

        # Labels
        self.label_due = QLabel('Дължима сума (ЕВРО):')
        self.label_paid_lev = QLabel('Платено в ЛЕВА:')
        self.label_paid_eur = QLabel('Платено в ЕВРО:')
        self.label_result = QLabel('Ресто в ЕВРО:')

        # Inputs
        # (Validator removed) We'll normalize inputs on calculation to accept both '.' and ','.

        self.input_due = QLineEdit()
        self.input_due.setText("0.00")
        self.input_due.editingFinished.connect(lambda: self.reset_if_empty(self.input_due))

        self.input_paid_lev = QLineEdit()
        self.input_paid_lev.setText("0.00")
        self.input_paid_lev.editingFinished.connect(lambda: self.reset_if_empty(self.input_paid_lev))

        self.input_paid_eur = QLineEdit()
        self.input_paid_eur.setText("0.00")

        # helper to parse amounts (accepts both comma and dot). Empty/invalid -> 0.0
        def parse_amount(text):
            if text is None:
                return 0.0
            s = text.strip()
            if s == "":
                return 0.0
            s = s.replace(',', '.')
            try:
                return float(s)
            except ValueError:
                return 0.0

        self.parse_amount = parse_amount
        self.input_paid_eur.editingFinished.connect(lambda: self.reset_if_empty(self.input_paid_eur))

        # Connect Enter key
        self.input_due.returnPressed.connect(self.calculate_change)
        self.input_paid_lev.returnPressed.connect(self.calculate_change)
        self.input_paid_eur.returnPressed.connect(self.calculate_change)

        # Button
        self.btn_calc = QPushButton('Изчисли ресто')
        self.btn_calc.clicked.connect(self.calculate_change)

        # Layout
        layout = QVBoxLayout()
        layout.setSpacing(12)

        for lbl, inp in [
            (self.label_due, self.input_due),
            (self.label_paid_lev, self.input_paid_lev),
            (self.label_paid_eur, self.input_paid_eur)
        ]:
            row = QHBoxLayout()
            row.setSpacing(10)
            row.addWidget(lbl)
            row.addWidget(inp)
            layout.addLayout(row)

        layout.addWidget(self.btn_calc)
        layout.addWidget(self.label_result)

        self.setLayout(layout)

    def reset_if_empty(self, field):
        if field.text().strip() == "":
            field.setText("0.00")

    def calculate_change(self):
        # Read and normalize inputs (accept both '.' and ','). Empty or invalid -> 0.00
        due = self.parse_amount(self.input_due.text())
        paid_lev = self.parse_amount(self.input_paid_lev.text())
        paid_eur = self.parse_amount(self.input_paid_eur.text())

        rate = 1.95583
        total_paid_eur = paid_eur + (paid_lev / rate)
        change_eur = total_paid_eur - due

        # Update fields to show normalized format with two decimals
        self.input_due.setText(f"{due:.2f}")
        self.input_paid_lev.setText(f"{paid_lev:.2f}")
        self.input_paid_eur.setText(f"{paid_eur:.2f}")

        self.label_result.setText(f'Ресто в ЕВРО: {change_eur:.2f}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EuroChangeCalculator()
    window.show()
    sys.exit(app.exec())
