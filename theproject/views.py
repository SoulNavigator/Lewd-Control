import wx


# pylint: disable=fixme, no-member
class MyFrame(wx.Frame):
    image_size = 800
    def __init__(self, parent, title):

        super().__init__(parent, title=title, style=wx.CAPTION | wx.CLOSE_BOX, size=wx.Size(self.image_size, self.image_size))
        self.init_ui()
    

    def __image_ratio(self, image:wx.Image):
        w = image.GetWidth()
        h = image.GetHeight()

        return w/h

    def __make_toolbar(self):
        toolbar = wx.MenuBar()
        menu_file = wx.Menu()
        toolbar.Append(menu_file, 'File')
        menu_file.Append(wx.ID_ANY, 'Scan folder')
        self.SetMenuBar(toolbar)

        return toolbar

    def __make_image_panel(self, sizer):
        pan_image = wx.Panel(self)
        sizer.Add(pan_image, 5, wx.ALL | wx.EXPAND, 5)

        img = wx.Image('pic4.jpg', wx.BITMAP_TYPE_ANY)
        ratio = self.__image_ratio(img)
        img.Rescale(self.image_size*ratio, self.image_size)
        self.SetSize(self.image_size*ratio, self.image_size+150)

        image_widget = wx.StaticBitmap(pan_image, bitmap=wx.BitmapFromImage(img))

        img_sizer = wx.BoxSizer(wx.HORIZONTAL)
        img_sizer.Add(image_widget, 1, wx.ALL|wx.EXPAND, 5)
        pan_image.SetSizer(img_sizer)

        return pan_image

    def __make_button_panel(self, sizer):
        pan_buttons = wx.Panel(self)
        sizer.Add(pan_buttons, 1, wx.ALL | wx.EXPAND, 5)

        return pan_buttons

    def __make_buttons(self, parent):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_lewd = wx.Button(parent, label='OwO!')
        #bind for lewd

        btn_normal = wx.Button(parent, label='SFW')
        #bind for normal
        
        hbox.Add(btn_normal,1,  wx.ALL |wx.EXPAND, 10)
        hbox.Add(btn_lewd,2,  wx.ALL|wx.EXPAND,  10) 
        parent.SetSizer(hbox)

        return (btn_lewd, btn_normal)

    def init_ui(self):
        self.toolbar = self.__make_toolbar()
        mainbox = wx.BoxSizer(wx.VERTICAL)
        self.pan_image = self.__make_image_panel(mainbox)
        self.pan_buttons = self.__make_button_panel(mainbox)
        self.SetSizer(mainbox)

        self.btn_nsfw, self.btn_sfw = self.__make_buttons(self.pan_buttons)

        #img = wx.EmptyImage(self.image_size, self.image_size)



        


app = wx.App(False)
frame = MyFrame(None, "Lewd Control")
frame.Show(True)
app.MainLoop()