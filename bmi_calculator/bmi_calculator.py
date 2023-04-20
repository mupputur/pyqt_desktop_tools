import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QWidget,
    QLabel,
    QRadioButton,
    QHBoxLayout,
    QComboBox,
    QButtonGroup,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
)
class MyGUIWindow(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setStyleSheet("background-color: lightblue;")
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(400,200,400,300)

        dialoglayout = QVBoxLayout()
        self.setLayout(dialoglayout)

        formlayout = QFormLayout()
        #Radio button groups
        self.rbtn_group_gender = QButtonGroup()
        self.rbtn_group_height = QButtonGroup()
        self.rbtn_group_weight = QButtonGroup()

        gender = QLabel("Select the Gender:")
        dialoglayout.addWidget(gender)

        hor_layout1 = QHBoxLayout()
        dialoglayout.addLayout(hor_layout1)

        self.r1_rbtn_male = QRadioButton("Male")
        self.r2_rbtn_female = QRadioButton("Female")
        hor_layout1.addWidget(self.r1_rbtn_male)
        hor_layout1.addWidget(self.r2_rbtn_female)

        self.rbtn_group_gender.addButton(self.r1_rbtn_male)
        self.rbtn_group_gender.addButton(self.r2_rbtn_female)


        height = QLabel("Enter the Height:")
        dialoglayout.addWidget(height)

        hor_layout2 = QHBoxLayout()
        dialoglayout.addLayout(hor_layout2)

        self.r2_rbtn_cms = QRadioButton("Cms")
        self.r2_rbtn_inches = QRadioButton("Inches")
        hor_layout2.addWidget(self.r2_rbtn_cms)
        hor_layout2.addWidget(self.r2_rbtn_inches)

        self.rbtn_group_height.addButton(self.r2_rbtn_cms)
        self.rbtn_group_height.addButton(self.r2_rbtn_inches)

        self.combo_box = QComboBox()
        self.combo_box.setStyleSheet("border: 1px solid black;")
        self.combo_box.setStyleSheet("background-color: lightgrey;")
        for i in range(45,280):
            self.combo_box.addItem(str(i))
        dialoglayout.addWidget(self.combo_box)


        self.weight = QLineEdit()
        self.weight.setStyleSheet("border: 1px solid black;")
        self.weight.setStyleSheet("background-color: lightgrey;")

        weight = QLabel("Enter the weight:")
        dialoglayout.addWidget(weight)

        hor_layout3 = QHBoxLayout()
        dialoglayout.addLayout(hor_layout3)

        self.r3_rbtn_wt_kgs = QRadioButton("Kgs")
        self.r3_rbtn_wt_lbs = QRadioButton("Lbs")
        hor_layout3.addWidget(self.r3_rbtn_wt_kgs)
        hor_layout3.addWidget(self.r3_rbtn_wt_lbs )

        self.rbtn_group_weight.addButton(self.r3_rbtn_wt_kgs)
        self.rbtn_group_weight.addButton(self.r3_rbtn_wt_lbs)

        dialoglayout.addWidget(self.weight)

        button_save = QPushButton("Calulate bmi", self)
        button_save.setStyleSheet("border: 1px solid black;")
        button_save.setStyleSheet("background-color: lightgreen;")
        button_clear = QPushButton("Clear", self)
        button_save.clicked.connect(self.bmi_calculate)
        button_clear.clicked.connect(self.clear_data)
        button_clear.setStyleSheet("border: 1px solid black;")
        button_clear.setStyleSheet("background-color: red;")


        hor_layout4 = QHBoxLayout()
        dialoglayout.addLayout(hor_layout4)
        hor_layout4.addWidget(button_save)
        hor_layout4.addWidget(button_clear)
        self.setLayout(dialoglayout)

        self.bmi = QLineEdit()
        self.bmi.setStyleSheet("border: 1px solid black;")
        self.bmi.setStyleSheet("background-color: lightgrey;")
        a = QLabel("BMI is:")
        dialoglayout.addWidget(a)
        dialoglayout.addWidget(self.bmi)

    def bmi_calculate(self):
        height = int(self.combo_box.currentText())
        weight = int(self.weight.text())
        bmi = weight/((height/100)**2)

        self.bmi.setText(str(bmi))

    def clear_data(self):
        self.weight.clear()
        self.bmi.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyGUIWindow()
    window.show()
    sys.exit(app.exec())