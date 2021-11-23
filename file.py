# import sys

# from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit,
#                              QVBoxLayout, QWidget)

# file = open("demofile.txt", "w")

# class Example(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):

#         hbox = QVBoxLayout(self)
        
#         self.lbl = QLabel(self)
#         qle = QLineEdit(self)

#         qle.textChanged[str].connect(self.onChanged)

#         hbox.addWidget(self.lbl)
#         hbox.addSpacing(20)
#         hbox.addWidget(qle)

#         self.resize(250, 200)
#         self.setWindowTitle('QLineEdit')
#         self.show()

#     def onChanged(self, text):
#         file = open("demofile.txt", "w")
#         file.write(text)
#         self.lbl.setText(text)
#         self.lbl.adjustSize()


# def main():
    
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()


n=0
j=0

with open("test.txt") as fp:
        for line in fp:
            j = line 
            print("line:",line)
            line = fp.readline()
            print(line)