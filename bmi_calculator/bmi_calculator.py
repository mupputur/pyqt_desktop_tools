# Auther: Ravi
# Reviewer: Dheeraj, Sai
# Created Date: 20-04-2023
# Modified Date: 23-04-2023
# License: VDAC 2023

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QComboBox,
    QButtonGroup,
    QRadioButton,
    QLineEdit,
    QPushButton,
)
class BMICalWindow(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        # Set window properties
        self.setStyleSheet("background-color: lightblue;")
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(400, 200, 400, 300)
        # Create vertical layout
        dialoglayout = QVBoxLayout()
        self.setLayout(dialoglayout)
        # Create group of Radio buttons
        self.rbtn_group_gender = QButtonGroup()
        self.rbtn_group_height = QButtonGroup()
        self.rbtn_group_weight = QButtonGroup()

        # Create widget
        gender = QLabel("Select the Gender:")
        dialoglayout.addWidget(gender)
        # Create radio buttons
        self.r1_rbtn_male = QRadioButton("Male")
        self.r1_rbtn_female = QRadioButton("Female")
        # Create horizontal layout
        hor_layout1 = QHBoxLayout()
        dialoglayout.addLayout(hor_layout1)
        hor_layout1.addWidget(self.r1_rbtn_male)
        hor_layout1.addWidget(self.r1_rbtn_female)
        # Group of radio buttons
        self.rbtn_group_gender.addButton(self.r1_rbtn_male)
        self.rbtn_group_gender.addButton(self.r1_rbtn_female)

        # Create widget
        height = QLabel("Enter the Height:")
        dialoglayout.addWidget(height)
        # Create radio buttons
        self.r2_rbtn_cms = QRadioButton("Cms")
        self.r2_rbtn_inches = QRadioButton("Inches")
        # Create horizontal layout
        hor_layout2 = QHBoxLayout()
        dialoglayout.addLayout(hor_layout2)
        hor_layout2.addWidget(self.r2_rbtn_cms)
        hor_layout2.addWidget(self.r2_rbtn_inches)
        # Group of radio buttons
        self.rbtn_group_height.addButton(self.r2_rbtn_cms)
        self.rbtn_group_height.addButton(self.r2_rbtn_inches)
        # Create combobox
        self.combo_box = QComboBox()
        self.combo_box.setStyleSheet("border: 1px solid black;")
        self.combo_box.setStyleSheet("background-color: lightgrey;")
        # Connect signals and slots
        self.r2_rbtn_cms.clicked.connect(self.update_combo_box)
        self.r2_rbtn_inches.clicked.connect(self.update_combo_box)
        dialoglayout.addWidget(self.combo_box)

        # Create widget
        self.text_filed_weight = QLineEdit()
        self.text_filed_weight.setStyleSheet("border: 1px solid black;")
        self.text_filed_weight.setStyleSheet("background-color: lightgrey;")
        weight = QLabel("Enter the weight:")
        dialoglayout.addWidget(weight)
        # Create radio buttons
        self.r3_rbtn_wt_kgs = QRadioButton("Kgs")
        self.r3_rbtn_wt_lbs = QRadioButton("Lbs")
        # Create horizontal layout
        hor_layout3 = QHBoxLayout()
        dialoglayout.addLayout(hor_layout3)
        hor_layout3.addWidget(self.r3_rbtn_wt_kgs)
        hor_layout3.addWidget(self.r3_rbtn_wt_lbs )
        # Group of radio buttons
        self.rbtn_group_weight.addButton(self.r3_rbtn_wt_kgs)
        self.rbtn_group_weight.addButton(self.r3_rbtn_wt_lbs)
        dialoglayout.addWidget(self.text_filed_weight)

        # Create Buttons
        button_calculate = QPushButton("Calulate bmi", self)
        button_calculate.setStyleSheet("border: 1px solid black;")
        button_calculate.setStyleSheet("background-color: lightgreen;")
        button_clear = QPushButton("Clear", self)
        button_clear.setStyleSheet("border: 1px solid black;")
        button_clear.setStyleSheet("background-color: red;")
        # Connect signals and slots
        button_calculate.clicked.connect(self.bmi_calculate)
        button_clear.clicked.connect(self.clear_input_fields)
        # Create horizontal layout
        hor_layout4 = QHBoxLayout()
        dialoglayout.addLayout(hor_layout4)
        hor_layout4.addWidget(button_calculate)
        hor_layout4.addWidget(button_clear)
        self.setLayout(dialoglayout)

        # Create widget
        self.bmi = QLineEdit()
        self.bmi.setStyleSheet("border: 1px solid black;")
        self.bmi.setStyleSheet("background-color: lightgrey;")
        BMI = QLabel("BMI is:")
        dialoglayout.addWidget(BMI)
        dialoglayout.addWidget(self.bmi)

    def update_combo_box(self):
        if self.r2_rbtn_cms.isChecked()==True:
            self.combo_box.clear()
            for i in range(45, 280):
                self.combo_box.addItems([str(i)])
        elif self.r2_rbtn_inches.isChecked()==True:
            self.combo_box.clear()
            for i in range(18, 110):
                self.combo_box.addItems([str(i)])


    def bmi_calculate(self):
        try:
            if self.r2_rbtn_cms.isChecked() == True and self.r3_rbtn_wt_kgs.isChecked() == True:
                height = int(self.combo_box.currentText())
                weight = int(self.text_filed_weight.text())
                bmi = weight/((height/100)**2)
                self.bmi.setText(str(bmi))
            elif self.r2_rbtn_inches.isChecked() == True and self.r3_rbtn_wt_lbs.isChecked() == True:
                height = int(self.combo_box.currentText())
                weight = int(self.text_filed_weight.text())
                bmi = (weight*703)/(height**2)
                self.bmi.setText(str(bmi))
            else:
                self.bmi.setText("Error: Data you have entered is invalid.")
        except Exception as e:
            self.bmi.setText("Error: Data you have entered is invalid.")

    def clear_input_fields(self):
        # Unselect the male and female buttons
        self.rbtn_group_gender.setExclusive(False)
        self.r1_rbtn_male.setChecked(False)
        self.r1_rbtn_female.setChecked(False)
        self.rbtn_group_gender.setExclusive(True)
        # Unselect the cms and inches buttons
        self.rbtn_group_height.setExclusive(False)
        self.r2_rbtn_cms.setChecked(False)
        self.r2_rbtn_inches.setChecked(False)
        self.rbtn_group_height.setExclusive(True)
        # Unselect the kgs and lbs buttons
        self.rbtn_group_weight.setExclusive(False)
        self.r3_rbtn_wt_kgs.setChecked(False)
        self.r3_rbtn_wt_lbs.setChecked(False)
        self.rbtn_group_weight.setExclusive(True)
        # Clear the inputs filed
        self.combo_box.clear()
        self.text_filed_weight.clear()
        self.bmi.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalWindow()
    window.show()
    sys.exit(app.exec())