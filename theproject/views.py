import wx


# pylint: disable=fixme, no-member
class MyFrame(wx.Frame):
    image_size = 300
    def __init__(self, parent, title):
        
        super().__init__(parent, title=title, style=wx.CAPTION | wx.CLOSE_BOX, size=wx.Size(self.image_size, self.image_size))
        self.init_ui()
    

    def image_ratio(self, image:wx.Image):
        w = image.GetWidth()
        h = image.GetHeight()

        return w/h

    def init_ui(self):

        pan_image = wx.Panel(self)
        pan_buttons = wx.Panel(self)

        mainbox = wx.BoxSizer(wx.VERTICAL)
        mainbox.Add(pan_image, 5, wx.ALL | wx.EXPAND, 5)
        mainbox.Add(pan_buttons, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(mainbox)

        #img = wx.EmptyImage(self.image_size, self.image_size)
        img = wx.Image('pic.png', wx.BITMAP_TYPE_ANY)
        ratio = self.image_ratio(img)
        img.Rescale(self.image_size*ratio, self.image_size)
        self.SetSize(self.image_size*ratio, self.image_size+150)
        
        image_widget = wx.StaticBitmap(pan_image, bitmap=wx.BitmapFromImage(img))
        
        img_sizer = wx.BoxSizer(wx.HORIZONTAL)
        img_sizer.Add(image_widget, 1, wx.ALL|wx.EXPAND, 5)
        pan_image.SetSizer(img_sizer)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_lewd = wx.Button(pan_buttons, label='OwO!')
        btn_normal = wx.Button(pan_buttons, label='SFW')
        hbox.Add(btn_normal,1,  wx.ALL |wx.EXPAND, 10)
        hbox.Add(btn_lewd,3,  wx.ALL|wx.EXPAND,  10) 
        
        pan_buttons.SetSizer(hbox)


app = wx.App(False)
frame = MyFrame(None, "Lewd Control")
frame.Show(True)
app.MainLoop()