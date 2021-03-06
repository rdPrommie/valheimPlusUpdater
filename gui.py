import wx

class GUIDrawing:
    def draw(self):
        app = wx.App()
        frame = wx.Frame(parent=None, title='Hello World')
        frame.Show()
        app.MainLoop()
