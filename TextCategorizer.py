import pandas as pd
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

with open("text.txt", 'r') as file:
    declaration = file.read()

def lengths_equal(self, *args, length = None):
    first = args[0]
    correctLen = True
    if length != None:
        correctLen = (length == len(first))

    for arg in args:
        if (not len(arg) == len(first)) or (not correctLen):
            raise Exception("All arguments must have the same length.")
    return True



class window(QWidget):
    def __init__(self, title="Labelling_Tool"):
        self.__name = title
        super(window, self).__init__()
        self.setWindowTitle(title)
        self.setStyleSheet("""QWidget{background-color: #000000; color:#C3C3C3;border:1px solid; border-color:#878787;}""")
        self.resize(1000,800)


class labelpair(QWidget):
    def __init__(self,parent):
        super(labelpair, self).__init__(parent)
        self.__w = QWidget(self)
        self.__w.setStyleSheet(""".QWidget{border: 1px solid; border-color:#434343;}""")
        self.setStyleSheet("""QLabel{border:none;}""")
        self.__horizontal = QHBoxLayout()
        self.__w.setLayout(self.__horizontal)
        self.__label = QLabel(self.__w)
        self.__label.setAlignment(Qt.AlignCenter)
        self.__horizontal.addWidget(self.__label)


    def setTexts(self, desc, val):
        desc = str(desc) + ": "
        val = str(val)
        self.__label.setText(desc+val)


    def setSizePolicy(self,*args):
        return self.__w.setSizePolicy(*args)

    def sizeHint(self, *args):
        return self.__w.sizeHint(*args)

# Cross Section at the Top
class topSection(QWidget):
    def __init__(self, parent, n_items):
        super(topSection, self).__init__(parent)
        self.__w = QWidget(self)
        self.setMinimumHeight(70)
        self.__horizontal = QGridLayout()
        self.__w.setLayout(self.__horizontal)
        self.__label_pairs = []
        for i in range(n_items):
            pair = labelpair(self.__w)
            self.__label_pairs.append(pair)
            self.__horizontal.addWidget(pair, 0, i)

    def set_texts(self, desc, vals):
        lengths_equal(desc, vals, length=len(self.__label_pairs))
        for lp in self.__label_pairs:
            lp.setTexts(desc.pop(0), vals.pop(0))

    def setSizePolicy(self,*args):
        return self.__w.setSizePolicy(*args)

    def sizeHint(self, *args):
        return self.__w.sizeHint(*args)

class midSection(QWidget):
    def __init__(self, parent, n_items):
        super(midSection, self).__init__(parent)
        self.__w = QWidget(self)
        self.__grid = QGridLayout()
        self.__w.setLayout(self.__grid)
        self.__grid.setColumnStretch(0,1)
        self.__grid.setColumnStretch(1,4)
        self.setStyleSheet("border:1px solid; border-color: #434343; color:white")
        self.__grid_items = []
        for i in range(n_items):
            self.__grid_items.append([QLabel(self.__w),QLabel(self.__w)])
            self.__grid.addWidget(self.__grid_items[i][0])
            self.__grid.addWidget(self.__grid_items[i][1])
            self.__grid_items[i][1].setWordWrap(True)

    def setTexts(self, desc, val):
        lengths_equal(desc, val, length=len(self.__grid_items))
        for item in self.__grid_items:
            item[0].setText(str(desc.pop(0)))
            item[1].setText(str(val.pop(0)))

    def setSizePolicy(self,*args):
        return self.__w.setSizePolicy(*args)

    def sizeHint(self, *args):
        return self.__w.sizeHint(*args)


class bottomSection(QWidget):
    def __init__(self, parent, categories):
        self.__cats = categories
        super(bottomSection, self).__init__(parent)
        self.__w = QWidget(self)
        self.setMinimumHeight(150)
        self.__horizontal = QHBoxLayout()
        self.__w.setLayout(self.__horizontal)
        self.__catLabels=[]
        for i in range(len(self.__cats)):
            self.__catLabels.append(QPushButton(self.__w))
            self.__horizontal.addWidget(self.__catLabels[i])
            self.__catLabels[i].clicked.connect(self.catetgory_clicked)
        self.setTexts(self.__cats)

    def catetgory_clicked(self):
        print("1")

    def setSizePolicy(self, *args):
        return self.__w.setSizePolicy(*args)

    def sizeHint(self, *args):
        return self.__w.sizeHint(*args)

    def setTexts(self, cats):
        lengths_equal(cats, self.__catLabels)
        for c in self.__catLabels:
            c.setText(cats.pop(0))


class LabellingUI():
    def __init__(self, dataset_name, topN, midN, categories):
        self.__dataName = dataset_name
        self.__topN = topN
        self.__midN = midN
        self.__categories = categories

        self.__qapp = QApplication(sys.argv)
        self.__mainWindow = window(title=self.__dataName)
        self.__vertical = QVBoxLayout()
        self.__vertical.setAlignment(Qt.AlignHCenter)
        self.__mainWindow.setLayout(self.__vertical)
        self.__TOP = topSection(self.__mainWindow,topN)
        self.__MID = midSection(self.__mainWindow,midN)
        self.__CATS = bottomSection(self.__mainWindow,self.__categories)

        # Stack the sections vertically
        self.__vertical.addWidget(self.__TOP)
        self.__vertical.addWidget(self.__MID)
        self.__vertical.addWidget(self.__CATS)





    def run(self):
        self.__mainWindow.show()
        sys.exit(self.__qapp.exec())

    def set_mid_items(self, descriptors, values):
        self.__MID.setTexts(descriptors, values)

    def set_top_items(self, descriptors, values):
        self.__TOP.set_texts(descriptors, values)


if __name__ == '__main__':
    categories = ["Letter", "News Article", "Recipe",
                  "Press Release", "Contract", "Invoice", "Poem"]
    ui = LabellingUI("ExampleSet",5,3,categories)
    ui.set_mid_items(["Title","Source", "Text"],["This article is nonsense","www.news.com",declaration])
    ui.set_top_items(["Index", "Date","Number", "Bla", "Bla"],[1, 2, 3, "22-03-2014",3])
    ui.run()


