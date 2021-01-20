from tkinter import *

class LabellingUI():
    def __init__(self, dataset_name, n_top_items, n_mid_items, categories):
        self.__ntopitems = n_top_items
        self.__nmiditems = n_mid_items
        self.__cats = categories

        self.__mainWindow = Tk()
        self.__mainWindow.geometry("1000x800")
        self.__mainWindow.title("Labelling Data: " + str(dataset_name))
        self.__mainWindow.configure(background='black')
        # setup for the top
        self.__topSection = Frame(master=self.__mainWindow)
        self.__topSection.pack(side=TOP, pady=10)
        self.__topSection.configure(relief='solid', highlightbackground='white',
                                         highlightcolor='white',
                                         highlightthickness=1, background='black')
        self.__toplabels = []
        self.__toplabelTexts = []
        for i in range(self.__ntopitems):
            self.__toplabelTexts.append(StringVar())
            label = Label(master=self.__topSection, textvariable=self.__toplabelTexts[i])
            label.pack(side=LEFT, padx=20)
            label.configure(bg='black', fg='white', font=('Arial',12))
            self.__toplabels.append(label)
            self.__toplabelTexts[i].set("TESTTEXT")

        # setup for the bottom
        self.__categorySection = Frame(master=self.__mainWindow)
        self.__categorySection.pack(side=BOTTOM, pady=10)
        self.__categorySection.configure(relief='solid', highlightbackground='white',
                                         highlightcolor='white',highlightthickness=2, background='black')
        self.__catlabels=[]
        for c in self.__cats:
            self.__catlabels.append(Label(master=self.__categorySection, text=c))
            self.__catlabels[-1].pack(side=LEFT, padx=20)
            self.__catlabels[-1].configure(bg='black',fg='white', font=('Arial',20))


        # setup for the middle
        self.__midSection = Frame(master=self.__mainWindow)
        self.__midSection.configure(background='black')
        self.__midSection.pack()
        self.__midLabels = []
        self.__midLabelTexts = []
        for i in range(self.__nmiditems):
            self.__midLabelTexts.append({'desc': StringVar(), 'val':StringVar()})
            dlabel = Label(master=self.__midSection, textvariable=self.__midLabelTexts[i]['desc'])
            dlabel.pack(side=TOP)
            dlabel.configure(bg='black', fg='white', font=('Arial',14))
            vlabel = Label(master=self.__midSection, textvariable=self.__midLabelTexts[i]['val'])
            vlabel.pack(side=TOP)
            vlabel.configure(bg='black', fg='white', font=('Arial', 10))
            self.__midLabels.append({'desc':dlabel, 'val':vlabel})
            self.__midLabelTexts[i]['desc'].set("DESCRIPTOR")
            self.__midLabelTexts[i]['val'].set("VALUE")

    def run(self):
        self.__mainWindow.mainloop()


if __name__ == "__main__":
    categories = ["Letter", "News Article", "Recipe",
                  "Press Release", "Contract", "Invoice", "Poem"]
    ui = LabellingUI("Text", 5,2,categories)
    ui.run()