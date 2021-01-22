import pandas as pd
import LabellingUI as ui
import numpy as np

class LabelPandas(ui.LabellingUI):
    def __init__(self, name, top_columns,mid_columns, categories, df, newcol='Label'):
        assert type(top_columns) == list, type(top_columns)
        assert type(mid_columns) == list, type(mid_columns)
        assert type(df) == pd.DataFrame, type(df)
        self.__data = df
        self.__newCol = newcol
        self.__data[newcol] = np.nan
        self.__currentIndex = 0
        n_top = len(top_columns)
        n_mid = len(mid_columns)
        self.__topCols = top_columns
        self.__midCols = mid_columns

        super(LabelPandas, self).__init__(name, n_top, n_mid, categories)
        self._bindKeys(self._onLeftKey, self._onRightKey, self.__onReturnKey, self.__onBackKey)

    def __exit__(self,*args):
        print("Saving the data on exit...")
        self.__saveData()
        print("...done.")

    def __saveData(self):
        self.__data.to_csv("ExitSave_"+self._dataname+".csv")

    def __onReturnKey(self, *args):
        self.__recordLabel()
        if self.__currentIndex +1 == self.__data.shape[0]:
            exit()
        self.__currentIndex += 1
        self.__refreshUI()
        # Pass the new category and set the category activation accordingly
        super(LabelPandas,self)._onReturnKey(new_cat=self.__getCategoryOfCurrentRow())


    def __getCategoryOfCurrentRow(self):
        return self.__data.iloc[self.__currentIndex].loc[self.__newCol]

    def __onBackKey(self,*args):
        if self.__currentIndex -1 >=0:
            self.__currentIndex -=1
            self.__refreshUI()
            super(LabelPandas, self)._onBackKey(new_cat=self.__getCategoryOfCurrentRow())
        else:
            print("Reached first row already.")

    def __recordLabel(self):
        cat = self._getActiveCat()
        self.__data.iloc[self.__currentIndex, -1] = cat
        return cat

    def __refreshUI(self):
        mid_vals = self.__data.iloc[self.__currentIndex].loc[self.__midCols].tolist()
        top_vals = self.__data.iloc[self.__currentIndex].loc[self.__topCols].tolist()
        self.set_mids(self.__midCols, mid_vals)
        self.set_tops(self.__topCols, top_vals)

    def run(self):
        self.__refreshUI()
        super(LabelPandas, self).run()

if __name__ == '__main__':
    df = pd.read_csv("example.csv")
    cats = ["Sport","Politics","People","Technical", "Other", "Society","Comedy","History","Scientific","Art"]
    # print(df.loc(axis=1)[["Link","Title"]])

    lp = LabelPandas("Wiki",['LastEdited','Link'], ['Title','Text'],cats, df)
    with lp:
        lp.run()