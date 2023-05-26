import pandas as pd
import wx
import os
import wx.lib.agw.foldpanelbar as fpb
import wx.lib.scrolledpanel as scrolled
from checkbutPanel import InsertFrame

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Bio Pool Select')
        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        my_sizer = wx.BoxSizer(wx.VERTICAL)

        font = wx.Font(13, family=wx.FONTFAMILY_SWISS, style=0, weight=100,
                       underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)
        font2 = wx.Font(11, family=wx.FONTFAMILY_SWISS, style=0, weight=100,
                       underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT)

        #dobaviane na text label
        self.label = wx.StaticText(panel, label='Enter file name', style=wx.ALIGN_CENTRE)
        self.label.SetFont(font)
        my_sizer.Add(self.label, 0,  wx.ALL | wx.EXPAND, 8)

        #dobaviane na text field - za faila
        self.text_ctrl = wx.TextCtrl(panel)
        self.text_ctrl.SetFont(font2)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 15)
        #butona za chetene na faila
        my_btn = wx.Button(panel, label='Read it', size =(200, 40))
        my_btn.SetFont(font2)
        my_btn.SetBackgroundColour(wx.Colour(194,24,7))

        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        self.label2 = wx.StaticText(panel, label=' ', style=wx.ALIGN_CENTRE)
        my_sizer.Add(self.label2, 0, wx.ALL | wx.EXPAND, 10)
        panel.SetSizer(my_sizer)

        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            # chete samo colonite
            df = pd.read_csv(f'{value}', nrows=0)

            # spisuk s kolonite
            listColumns = list(df.columns)
            countCol = len(listColumns)
            self.label2.LabelText = f'Choose between {str(countCol)} columns'
            #writing to file
            file1 = open('choosenFile.txt', 'w')
            file1.write(f'{value}')
            file1.close()
            self.dlg =InsertFrame()
           # self.dlg.text.SetLabel(value)
           # print(df.columns[0])

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()





