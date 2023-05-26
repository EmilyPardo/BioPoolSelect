from cgitb import enable

import wx
import pandas as pd
import wx.lib.agw.foldpanelbar as fpb
import wx.lib.scrolledpanel as scrolled
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyPanel(scrolled.ScrolledPanel):

  def __init__(self, parent):
    scrolled.ScrolledPanel.__init__(self, parent=parent,
                                    size=parent.GetSize(),
                                    style=wx.ALL | wx.EXPAND)

    self.SetupScrolling()
    self.boxSizer = wx.BoxSizer(wx.VERTICAL)
    m_pnl = fpb.FoldPanelBar(self, wx.ID_ANY, wx.DefaultPosition, (400, 1200),
                             fpb.FPB_VERTICAL)
    m_pnl.SetBackgroundColour(wx.Colour(255, 255, 255))
    self.pnl = m_pnl

    btnAccept = wx.Button(m_pnl, label='Save new file')
    btnAccept.Bind(wx.EVT_BUTTON, self.on_press)
    self.boxSizer.Add(btnAccept, 20, wx.LEFT, 5)

    self.boxSizer.Add(m_pnl)
    self.pnl = m_pnl
    self.SetSizer(self.boxSizer)


    # chetene na imeto na faila
    file2 = open('choosenFile.txt', 'r')
    fName = file2.read()
    file2.close()
    self.text = wx.StaticText(self, -1, fName)

    df = pd.read_csv(f'{fName}', nrows=0)
    listColumns = list(df.columns)
    countCol = len(listColumns)

    pos_y = 10
    for i in range(int(countCol)):
      pos_y += 20
      cb = wx.CheckBox(m_pnl, id=i, label=df.columns[i], pos=(20, pos_y))

      cb.SetFocus()


    self.Bind(wx.EVT_CHECKBOX, self.onChecked)

    self.SetupScrolling()
    self.pnl = m_pnl
    self.SetSizer(self.boxSizer)

  def onChecked(self, e):
    cb = e.GetEventObject()
    print(cb.GetLabel(), ' is clicked', cb.GetValue())

  def OnChecked(self, event):
    clicked = event.GetEventObject()
    print(clicked.GetName())
    print(event.IsChecked())

  def on_press(self, event):
    print("ready!")

class MyApp(wx.App):

  def OnInit(self):
    frame = InsertFrame(parent=None, id=-1)
    frame.Show()
    return True

class InsertFrame(wx.Frame):

  def __init__(self):

    wx.Frame.__init__(self, None, title="Choose columns")
    panel = MyPanel(self)
    #pnl = wx.Panel(self)
   #self.cb3 = wx.CheckBox(pnl, label='Value C', pos=(10, 70))
    #if self.cb3.IsEnabled():
      #print("YES")
    self.Show(True)



#if __name__ == "__main__":
app = wx.App(False)
frame = InsertFrame()
app.MainLoop()
