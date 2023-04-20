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
        self.setWindowTitle("BMI Calculator")
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

        self.combo_box = QComboBox()
        for i in range(45,280):
            self.combo_box.addItem(str(i))
        dialoglayout.addWidget(self.combo_box)

        hor_layout2 = QHBoxLayout()
        dialoglayout.addLayout(hor_layout2)

        self.r2_rbtn_cms = QRadioButton("Cms")
        self.r2_rbtn_inches = QRadioButton("Inches")
        hor_layout2.addWidget(self.r2_rbtn_cms)
        hor_layout2.addWidget(self.r2_rbtn_inches)

        self.rbtn_group_height.addButton(self.r2_rbtn_cms)
        self.rbtn_group_height.addButton(self.r2_rbtn_inches)

        self.weight = QLineEdit()
        formlayout.addRow("Enter the weight:", self.weight)
        dialoglayout.addLayout(formlayout)

        hor_layout3 = QHBoxLayout()
        dialoglayout.addLayout(hor_layout3)

        self.r3_rbtn_wt_kgs = QRadioButton("Kgs")
        self.r3_rbtn_wt_lbs = QRadioButton("Lbs")
        hor_layout3.addWidget(self.r3_rbtn_wt_kgs)
        hor_layout3.addWidget(self.r3_rbtn_wt_lbs )

        self.rbtn_group_weight.addButton(self.r3_rbtn_wt_kgs)
        self.rbtn_group_weight.addButton(self.r3_rbtn_wt_lbs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyGUIWindow()
    window.show()
    sys.exit(app.exec())