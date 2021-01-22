from tkinter import *


# The functions __onReturnKey, __onLeftKey, __onRightKey shall be overloaded to provide the
# functionality that is specific to the data format
# This class only takes care of the UI part
class LabellingUI():
    def __init__(self, dataset_name, n_top_items, n_mid_items, categories):
        self.__setLook()
        self._dataname = dataset_name
        self.__ntopitems = n_top_items
        self.__nmiditems = n_mid_items
        self.__cats = categories
        self.__setupMainWindow()
        self.__setupTopSection()
        self.__setupBottomSection()
        self.__setupMidSection()

    def __enter__(self, *args):
        pass

    def __exit__(self, *args):
        pass


    def __setupMainWindow(self):
        self.__mainWindow = Tk()

        self.__mainWindow.geometry("1200x1000")
        self.__mainWindow.title("Labelling Data: " + str(self._dataname))
        self.__mainWindow.configure(background='black')


    def _bindKeys(self,left,right,_return, back):
        self.__mainWindow.bind(sequence='<KeyPress-Return>', func=_return)
        self.__mainWindow.bind(sequence='<KeyPress-Right>', func=right)
        self.__mainWindow.bind(sequence='<KeyPress-Left>', func=left)
        self.__mainWindow.bind(sequence='<KeyPress-b>',func=back)

    def _onLeftKey(self, *args):
        self.__deactivate(self.__activeCatIndex)
        self.__decreaseActiveIndex()
        self.__activate(self.__activeCatIndex)


    def _onRightKey(self, *args):
        self.__deactivate(self.__activeCatIndex)
        self.__increaseActiveIndex()
        self.__activate(self.__activeCatIndex)

    def _getActiveCat(self):
        return self.__catlabels[self.__activeCatIndex].cget('text')


    def _setActiveCat(self, value):
        assert type(value) == str, type(value)
        assert value in self.__cats, value
        for index,cat in enumerate(self.__catlabels):
            if cat.cget('text') == value:
                self.__activate(index, color=self.__WRITTENCOLOR)
                self.__activeCatIndex = index
            else:
                self.__deactivate(index)



    def _onReturnKey(self, new_cat = None, *args):
        print("Category chosen: " + str(self.__catlabels[self.__activeCatIndex].cget('text')))
        if new_cat in self.__cats:
            self._setActiveCat(new_cat)
        else:
            self.__resetActivation()


    def _onBackKey(self, new_cat=None,*args):
        print("Going one step backwards...")
        if new_cat in self.__cats:
            self._setActiveCat(new_cat)
        else:
            self.__resetActivation()


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
            label.configure(bg='black', fg='white', font=(self.__FONT, self.__TEXTSIZETOP))
            self.__toplabels.append(label)


    def __setupBottomSection(self):
        self.__categorySection = Frame(master=self.__mainWindow)
        self.__categorySection.pack(side=BOTTOM, pady=10)
        self.__categorySection.configure(relief='solid', highlightbackground='white',
                                         highlightcolor='white',highlightthickness=2, background='black')
        self.__catlabels=[]
        for c in self.__cats:
            self.__catlabels.append(Label(master=self.__categorySection, text=c))
            self.__catlabels[-1].pack(side=LEFT, padx=0)
            self.__catlabels[-1].configure(bg='black',fg='white', font=(self.__FONT,self.__TEXTSIZEBOT))
        self.__activeCatIndex = 0
        self.__resetActivation()




    def __resetActivation(self):
        mid_index = int((len(self.__catlabels)-1)/2)
        self.__deactivate(self.__activeCatIndex)
        self.__activeCatIndex = mid_index
        self.__activate(mid_index)


    def __decreaseActiveIndex(self):
            max_i = len(self.__catlabels)
            if self.__activeCatIndex - 1 < 0:
                self.__activeCatIndex = max_i - 1
            else:
                self.__activeCatIndex -= 1


    def __increaseActiveIndex(self):
            max_i = len(self.__catlabels)
            if self.__activeCatIndex + 1 >= max_i:
                self.__activeCatIndex = 0
            else:
                self.__activeCatIndex += 1


    def __activate(self, index, color=None):
        if color == None:
            color = self.__ACTIVECOLOR
        self.__catlabels[index].configure(bg=color, fg='black', font=(self.__FONT,self.__TEXTSIZEBOT))

    def __deactivate(self, index):
        self.__catlabels[index].configure(bg='black', fg='white', font=(self.__FONT,self.__TEXTSIZEBOT))


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
            dlabel.configure(bg='black', fg='white', font=(self.__FONT,self.__TEXTSIZEMID1), anchor='n')
            vlabel = Label(master=self.__midFrames[i], textvariable=self.__midLabelTexts[i]['val'])
            vlabel.pack(side=TOP)
            vlabel.configure(bg='black', fg='white', font=(self.__FONT, self.__TEXTSIZEMID2), justify='left', wraplength=1100, anchor='n')
            self.__midLabels.append({'desc':dlabel, 'val':vlabel})



    def __setLook(self):
        self.__FONT = 'Helvetica'
        self.__TEXTSIZETOP = 16
        self.__TEXTSIZEMID1 = 15
        self.__TEXTSIZEMID2 = 14
        self.__TEXTSIZEBOT = 18
        self.__ACTIVECOLOR = '#DA3054'
        self.__WRITTENCOLOR = '#' \
                              '' \
                              '7BBCDF'


    def run(self):
        self.__mainWindow.mainloop()
        self.__resetActivation()


    def set_tops(self, descriptors,values):
        for i,label in enumerate(self.__toplabelTexts):
            label.set(str(descriptors[i])+ ": " + str(values[i]))


    def set_mids(self, descriptors, values):
        for i,label in enumerate(self.__midLabelTexts):
            label['desc'].set(str(descriptors[i]).upper()+':')
            label['val'].set(self.__text_replacements(str(values[i])))


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