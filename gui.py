import glob
import os
import wx
from wx.lib.pubsub import pub as Publisher
from checker import *
class ViewerPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        load()
        width, height = wx.DisplaySize()        
        self.photoMaxSize = 290
        self.layout()

    def layout(self):
        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.BoxSizer(wx.VERTICAL)        
        img = wx.Image(self.photoMaxSize,self.photoMaxSize)
        self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, 
                                         wx.Bitmap(img))
        self.imageCtrl2 = wx.StaticBitmap(self, wx.ID_ANY, 
                                         wx.Bitmap(img))
        uplBtn = wx.Button(self, label='Upload a Picture')
        uplBtn.Bind(wx.EVT_BUTTON,self.upload)
        runBtn = wx.Button(self, label='Run the Program')
        runBtn.Bind(wx.EVT_BUTTON,self.runProgram)
        self.rankBtn = wx.SpinCtrl(self, value="", min=1, initial=1, name="Rank")        
        self.Bind(wx.EVT_SPIN, self.OnSpin, self.rankBtn)
        self.rankBtn.Disable()
        self.inputdis = wx.RadioButton(self, -1, "Distance", style = wx.RB_GROUP)        
        self.inputcos = wx.RadioButton(self, -1, "Cosine")
        self.inputdis.Bind(wx.EVT_RADIOBUTTON, self.runProgram)
        self.inputcos.Bind(wx.EVT_RADIOBUTTON, self.runProgram)
        self.inputInt = wx.Slider(self, 10, 1, 1, 10, style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)
        self.n = self.inputInt.GetValue()
        self.mainSizer.Add(self.imageCtrl, 0, wx.ALL, 5)
        self.mainSizer.Add(self.imageCtrl2, 0, wx.ALL, 5)
        self.mainSizer.Add(sizer, 0, wx.ALL, 5)
        sizer.Add(uplBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(runBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.rankBtn, 0, wx.CENTER)
        sizer.Add(self.inputdis, 0, wx.ALL, 5)
        sizer.Add(self.inputcos, 0, wx.ALL, 5)
        sizer.Add(self.inputInt, 0, wx.ALL, 5)
        self.SetSizer(self.mainSizer)

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

    def runProgram(self,event):
        x = 0
        print(self.inputcos.GetValue())
        if (self.inputcos.GetValue() == True):
            x = 1
        arr = compareImage(self.address, x, self.n)
        self.rankBtn.Enable()
    
    def OnSpin(self,event):        
        i = (self.rankBtn.GetValue() - 1)
        img = wx.Image(self.arr[i], wx.BITMAP_TYPE_ANY)
        self.imageCtrl2.SetBitmap(wx.Bitmap(img))
        self.Refresh()
        self.mainSizer.Fit(self)

class ViewerFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="FaceRecog")
        panel = ViewerPanel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Show()
        self.sizer.Fit(self)
        self.Center()

if __name__ == "__main__":
    app = wx.App()
    frame = ViewerFrame()
    app.MainLoop()
