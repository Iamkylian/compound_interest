import sys
import pandas as pd
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                             QComboBox, QRadioButton, QVBoxLayout,
                             QPushButton, QMessageBox)

class CompoundInterestCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Compound Interest Calculator')
        self.setGeometry(100, 100, 400, 400)

        # Create layout
        layout = QVBoxLayout()

        # Initial Amount Input
        self.initial_amount_label = QLabel('Initial Amount (€):')
        self.initial_amount_input = QLineEdit()
        self.initial_amount_input.setPlaceholderText("Enter initial amount")
        
        # Interest Rate Input
        self.interest_rate_label = QLabel('Interest Rate (%):')
        self.interest_rate_input = QComboBox()
        self.interest_rate_input.addItems([str(i) for i in range(1, 11)])  # Options from 1% to 10%
        
        # Duration Input
        self.duration_label = QLabel('Duration (years):')
        self.duration_input = QComboBox()
        self.duration_input.addItems([str(i) for i in range(1, 21)])  # Options from 1 to 20 years

        # Frequency Input
        self.frequency_label = QLabel('Frequency:')
        self.frequency_weekly = QRadioButton("Weekly")
        self.frequency_bi_monthly = QRadioButton("Bi-monthly")
        self.frequency_monthly = QRadioButton("Monthly")
        self.frequency_weekly.setChecked(True)  # Default selection

        # Calculate Button
        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate_compound_interest)

        # Save to Excel Button
        self.save_button = QPushButton('Save to Excel')
        self.save_button.clicked.connect(self.save_to_excel)

        # Add widgets to layout
        layout.addWidget(self.initial_amount_label)
        layout.addWidget(self.initial_amount_input)
        
        layout.addWidget(self.interest_rate_label)
        layout.addWidget(self.interest_rate_input)
        
        layout.addWidget(self.duration_label)
        layout.addWidget(self.duration_input)

        layout.addWidget(self.frequency_label)
        layout.addWidget(self.frequency_weekly)
        layout.addWidget(self.frequency_bi_monthly)
        layout.addWidget(self.frequency_monthly)

        layout.addWidget(self.calculate_button)
        layout.addWidget(self.save_button)

        # Set the main layout
        self.setLayout(layout)

    def calculate_compound_interest(self):
        try:
            initial_amount = float(self.initial_amount_input.text())  # Get the initial amount from input
            interest_rate = float(self.interest_rate_input.currentText())
            duration = int(self.duration_input.currentText())
            
            # Determine frequency
            if self.frequency_weekly.isChecked():
                n = 52  # Weekly compounding
            elif self.frequency_bi_monthly.isChecked():
                n = 26  # Bi-monthly compounding
            elif self.frequency_monthly.isChecked():
                n = 12  # Monthly compounding
            
            # Calculate final amount using compound interest formula
            final_amount = initial_amount * (1 + (interest_rate / 100)) ** (n * duration)

            # Show result in a message box
            QMessageBox.information(self, 'Final Amount', 
                                    f'Final amount after {duration} years: {final_amount:,.2f} €')
        
            return final_amount  # Return final amount for saving later

        except ValueError:
            QMessageBox.warning(self, 'Error', 'Please enter valid values.')

    def save_to_excel(self):
        try:
            initial_amount = float(self.initial_amount_input.text())
            interest_rate = float(self.interest_rate_input.currentText())
            duration = int(self.duration_input.currentText())

            if not initial_amount or not interest_rate or not duration:
                raise ValueError("Please provide all parameters.")

            results = []
            
            for year in range(1, duration + 1):
                if self.frequency_weekly.isChecked():
                    n = 52
                elif self.frequency_bi_monthly.isChecked():
                    n = 26
                elif self.frequency_monthly.isChecked():
                    n = 12
                
                final_amount = initial_amount * (1 + (interest_rate / 100)) ** (n * year)
                results.append({
                    "Year": year,
                    "Final Amount (€)": final_amount
                })

            df = pd.DataFrame(results)
            df.to_excel('compound_interest_results.xlsx', index=False)
            
            QMessageBox.information(self, 'Success', 'Results saved to compound_interest_results.xlsx')

        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CompoundInterestCalculator()
    calculator.show()
    sys.exit(app.exec_())