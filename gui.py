import glob
import os
import wx
from wx.lib.pubsub import pub as Publisher
from checker import *

class ViewerPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        load()
        width, height = wx.DisplaySize()        
        self.photoMaxSize = 290
        self.layout()
    #----------------------------------------------------------------------
    def layout(self):
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.BoxSizer(wx.HORIZONTAL)        
        img = wx.EmptyImage(self.photoMaxSize,self.photoMaxSize)
        self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, 
                                         wx.Bitmap(img))
        self.imageCtrl2 = wx.StaticBitmap(self, wx.ID_ANY, 
                                         wx.Bitmap(img))
        uplBtn = wx.Button(self, label='Upload a Picture')
        uplBtn.Bind(wx.EVT_BUTTON,self.upload)
        runBtn = wx.Button(self, label='Run the Program')
        runBtn.Bind(wx.EVT_BUTTON,self.runProgram)        
        sizer.Add(self.imageCtrl, 0, wx.ALL, 5)
        sizer.Add(self.imageCtrl2, 0, wx.ALL, 5)      
        self.mainSizer.Add(sizer, 0, wx.CENTER)
        self.mainSizer.Add(uplBtn, 0, wx.ALL|wx.CENTER, 5)
        self.mainSizer.Add(runBtn, 0, wx.ALL|wx.CENTER, 5)
        self.inputMode = wx.Choice(self, choices = ['Distribution', 'Cosine'])
        self.inputInt = wx.Slider(self, 10, 1, 1, 10, style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)
        self.n = self.inputInt.GetValue()        
        self.inputRank = wx.SpinButton(self, style=wx.SP_VERTICAL)        
        self.inputRank.SetRange(1, self.n)
        self.inputRank.SetValue(1)
        self.inputRank.Bind(wx.EVT_BUTTON,self.display)
        self.mainSizer.Add(self.inputMode, 0, wx.ALL, 5)        
        self.mainSizer.Add(self.inputRank, 0, wx.ALL, 5)
        self.mainSizer.Add(self.inputInt, 0, wx.ALL, 5)
        self.SetSizer(self.mainSizer)
    #----------------------------------------------------------------------
    def upload(self,event):
        wildcard = "JPEG files (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.address = dialog.GetPath()
        dialog.Destroy()
        img = wx.Image(self.address, wx.BITMAP_TYPE_ANY)
        self.imageCtrl.SetBitmap(wx.Bitmap(img))
        self.Refresh()
        self.mainSizer.Fit(self)
    #----------------------------------------------------------------------
    def mode(self):
        tipe = self.inputMode.GetSelection()
        if (tipe == 'Distribution'):
            return 0;
        if (tipe == 'Cosine'):
            return 1;
    #----------------------------------------------------------------------
    def runProgram(self,event):
        arr = compareImage(self.address, self.mode, self.n)
        self.inputRank.Enable()
        return arr
    #----------------------------------------------------------------------
    def display(self,event):
        i = self.inputRank.GetValue()
        img = self.RunProgram()
        self.imageCtrl2.SetBitmap(wx.Bitmap(img[i]))
        self.Refresh()
        self.mainsizer.Fit(self)
#----------------------------------------------------------------------
class ViewerFrame(wx.Frame):
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, title="FaceRecog")
        panel = ViewerPanel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Show()
        self.sizer.Fit(self)
        self.Center()
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App()
    frame = ViewerFrame()
    app.MainLoop()
