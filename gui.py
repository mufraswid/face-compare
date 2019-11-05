import glob
import os
import wx
from wx.lib.pubsub import pub as Publisher
from modeller import *

class ViewerPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        width, height = wx.DisplaySize()        
        self.photoMaxSize = height - 200
        self.layout()
    #----------------------------------------------------------------------
    def layout(self):
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)        
        img = wx.EmptyImage(self.photoMaxSize,self.photoMaxSize)
        self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, 
                                         wx.BitmapFromImage(img))
        uplBtn = wx.Button(self, label='Upload a Picture')
        uplBtn.Bind(wx.EVT_BUTTON,self.upload)
        runBtn = wx.Button(self, label='Run the Program')
        runBtn.Bind(wx.EVT_BUTTON, run)        
        btnSizer.Add(uplBtn, 0, wx.ALL|wx.CENTER, 5)
        btnSizer.Add(runBtn, 0, wx.ALL|wx.CENTER, 5)
        self.mainSizer.Add(btnSizer, 0, wx.CENTER)           
        self.SetSizer(self.mainSizer)
    #----------------------------------------------------------------------
    def upload(self,event):
        wildcard = "JPEG files (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            address = dialog.GetPath()
        return address
        dialog.Destroy()
        self.OnView()
    #----------------------------------------------------------------------
    def onView(self):
        filepath = self.photoTxt.GetValue()
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        W = img.GetWidth()
        H = img.GetHeight()
        img = img.Scale(W,H)
        self.SetBitmap(wx.BitmapFromImage(img))
        self.panel.Refresh()
        self.mainSizer.Fit(self.frame)



#----------------------------------------------------------------------
class ViewerFrame(wx.Frame):
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, title="FaceRecog")
        panel = ViewerPanel(self)
        self.initToolbar()        
        self.folderPath = ""
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Show()
        self.sizer.Fit(self)
        self.Center()
        
        
    #----------------------------------------------------------------------
    def initToolbar(self):
        self.toolbar = self.CreateToolBar()
        self.toolbar.SetToolBitmapSize((16,16))
        open_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (16,16))
        openTool = self.toolbar.AddSimpleTool(wx.ID_ANY, open_ico, "Open", "Open an Image Directory")
        self.Bind(wx.EVT_MENU, self.onOpenDirectory, openTool)
        self.toolbar.Realize()
        
    #----------------------------------------------------------------------
    def onOpenDirectory(self, event):
        """
        Opens a DirDialog to allow the user to open a folder with pictures
        """
        dlg = wx.FileDialog(frame, "Open", "", "", 
      "JPEG files (*.jpg)|*.jpg", 
       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        
        if dlg.ShowModal() == wx.ID_OK:
            self.folderPath = dlg.GetPath()
            print(self.folderPath)
            self.photoTxt.SetValue(dialog.GetPath())
        dialog.Destroy() 
        self.onView()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App()
    frame = ViewerFrame()
    app.MainLoop()
