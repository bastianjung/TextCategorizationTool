from tkinter import *

class LabellingUI():
    def __init__(self, dataset_name, n_top_items, n_mid_items, categories):
        self.__setFontsizes()
        self.__dataname = dataset_name
        self.__ntopitems = n_top_items
        self.__nmiditems = n_mid_items
        self.__cats = categories

        self.__setupMainWindow()
        self.__setupTopSection()
        self.__setupBottomSection()
        self.__setupMidSection()




    def __setupMainWindow(self):
        self.__mainWindow = Tk()
        self.__mainWindow.geometry("1200x1000")
        self.__mainWindow.title("Labelling Data: " + str(self.__dataname))
        self.__mainWindow.configure(background='black')


    def __setupTopSection(self):
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
            label.configure(bg='black', fg='white', font=('Arial', self.__TEXTSIZETOP))
            self.__toplabels.append(label)
            self.__toplabelTexts[i].set("TESTTEXT")


    def __setupBottomSection(self):
        self.__categorySection = Frame(master=self.__mainWindow)
        self.__categorySection.pack(side=BOTTOM, pady=10)
        self.__categorySection.configure(relief='solid', highlightbackground='white',
                                         highlightcolor='white',highlightthickness=2, background='black')
        self.__catlabels=[]
        for c in self.__cats:
            self.__catlabels.append(Label(master=self.__categorySection, text=c))
            self.__catlabels[-1].pack(side=LEFT, padx=20)
            self.__catlabels[-1].configure(bg='black',fg='white', font=('Arial',self.__TEXTSIZEBOT))

    def __setupMidSection(self):
        self.__midSection = Frame(master=self.__mainWindow)
        self.__midSection.configure(background='black')
        self.__midSection.pack()
        self.__midFrames = []
        self.__midLabels = []
        self.__midLabelTexts = []
        for i in range(self.__nmiditems):
            self.__midFrames.append(Frame(master=self.__midSection, background='black',pady=10))
            self.__midFrames[i].pack(side=TOP)
            self.__midLabelTexts.append({'desc': StringVar(), 'val':StringVar()})
            dlabel = Label(master=self.__midFrames[i], textvariable=self.__midLabelTexts[i]['desc'])
            dlabel.pack(side=TOP)
            dlabel.configure(bg='black', fg='white', font=('Arial',self.__TEXTSIZEMID1), anchor='n')
            vlabel = Label(master=self.__midFrames[i], textvariable=self.__midLabelTexts[i]['val'])
            vlabel.pack(side=TOP)
            vlabel.configure(bg='black', fg='white', font=('Arial', self.__TEXTSIZEMID2), justify='left', wraplength=1100, anchor='n')
            self.__midLabels.append({'desc':dlabel, 'val':vlabel})
            self.__midLabelTexts[i]['desc'].set("DESCRIPTOR")
            self.__midLabelTexts[i]['val'].set("VALUE")


    def __setFontsizes(self):
        self.__TEXTSIZETOP = 18
        self.__TEXTSIZEMID1 = 15
        self.__TEXTSIZEMID2 = 14
        self.__TEXTSIZEBOT = 18


    def run(self):
        self.__mainWindow.mainloop()

    def set_tops(self, descriptors,values):
        for t in self.__toplabelTexts:
            t.set(str(descriptors.pop(0))+ ": " + str(values.pop(0)))

    def set_mids(self, descriptors, values):
        for m in self.__midLabelTexts:
            m['desc'].set(str(descriptors.pop(0)).upper()+':')
            m['val'].set(self.__text_replacements(str(values.pop(0))))

    def __text_replacements(self, text):
        return str.replace(text,"\n","")

if __name__ == "__main__":
    with open("text.txt", 'r') as file:
        declaration = file.read()

    categories = ["Letter", "News Article", "Recipe",
                  "Press Release", "Contract", "Invoice", "Poem"]
    ui = LabellingUI("Text", 3,2,categories)
    ui.set_tops(["Index","Date","Url"],["12341","22.03.1992", "http://www.abc.com/asdasdawq"])
    ui.set_mids(["Title","Texts"],["Such a random title",declaration ])
    ui.run()