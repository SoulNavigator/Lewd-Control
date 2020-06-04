import wx


# pylint: disable=fixme, no-member
class MyFrame(wx.Frame):
    image_size = 800
    def __init__(self, parent, title):

        super().__init__(parent, title=title, style=wx.CAPTION | wx.CLOSE_BOX, size=wx.Size(self.image_size, self.image_size))
        self.init_ui()
        self.__make_binds()

    # EVENTS:
    def OnNSFWbuttonPress(self, event):
        print("This picture is NSFW")

    def OnSFWbuttonPress(self, event):
        print("This picture is SFW")
    
    def OnMenuScanPress(self, event):
        wildcard = "pictures (*.jpeg,*.png,*.jpg)|*.jpeg;*.png;*.jpg"
        with wx.FileDialog(self, "Pick file", wildcard=wildcard) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = file_dialog.GetPath()
            print(pathname)
            self.open_image(pathname)


    def __image_ratio(self, image:wx.Image):
        w = image.GetWidth()
        h = image.GetHeight()

        return w/h

    def __make_toolbar(self):
        toolbar = wx.MenuBar()
        menu_file = wx.Menu()
        toolbar.Append(menu_file, 'File')
        self.__i_scan = menu_file.Append(wx.ID_ANY, 'Scan folder')
        self.SetMenuBar(toolbar)

        return toolbar

    def open_image(self, path):
        img = wx.Image(path, wx.BITMAP_TYPE_ANY)
        ratio = self.__image_ratio(img)
        img.Rescale(self.image_size*ratio, self.image_size)
        self.SetSize(self.image_size*ratio, self.image_size+150)
        
        self.image_widget.SetBitmap(wx.BitmapFromImage(img))
        img_sizer = wx.BoxSizer(wx.HORIZONTAL)
        img_sizer.Add(self.image_widget, 1, wx.ALL|wx.EXPAND, 5)
        self.__pan_image.SetSizer(img_sizer)

        #self.Refresh()

    def __make_image_panel(self, sizer):
        pan_image = wx.Panel(self)
        sizer.Add(pan_image, 5, wx.ALL | wx.EXPAND, 5)

        image_path = 'pic3.jpg'
        #img = self.open_image(pan_image, image_path)
        img = wx.EmptyImage(self.image_size, self.image_size)
        ratio = self.__image_ratio(img)
        img.Rescale(self.image_size*ratio, self.image_size)
        self.SetSize(self.image_size*ratio, self.image_size+150)
        self.image_widget = wx.StaticBitmap(pan_image, bitmap=wx.BitmapFromImage(img))
        img_sizer = wx.BoxSizer(wx.HORIZONTAL)
        img_sizer.Add(self.image_widget, 1, wx.ALL|wx.EXPAND, 5)
        pan_image.SetSizer(img_sizer)
        
        return pan_image

    def __make_button_panel(self, sizer):
        pan_buttons = wx.Panel(self)
        sizer.Add(pan_buttons, 1, wx.ALL | wx.EXPAND, 5)

        return pan_buttons

    def __make_buttons(self, parent):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        btn_lewd = wx.Button(parent, label='OwO!')

        btn_normal = wx.Button(parent, label='SFW')

        hbox.Add(btn_normal,1,  wx.ALL |wx.EXPAND, 10)
        hbox.Add(btn_lewd,2,  wx.ALL|wx.EXPAND,  10) 
        parent.SetSizer(hbox)

        return (btn_lewd, btn_normal)

    def __make_binds(self):
        #Buttons
        self.__btn_nsfw.Bind(wx.EVT_BUTTON, self.OnNSFWbuttonPress)
        self.__btn_sfw.Bind(wx.EVT_BUTTON, self.OnSFWbuttonPress)
        #Menu items
        self.Bind(wx.EVT_MENU, self.OnMenuScanPress, self.__i_scan)
        
    def init_ui(self):
        self.toolbar = self.__make_toolbar()
        mainbox = wx.BoxSizer(wx.VERTICAL)
        self.__pan_image = self.__make_image_panel(mainbox)
        self.__pan_buttons = self.__make_button_panel(mainbox)
        self.SetSizer(mainbox)

        self.__btn_nsfw, self.__btn_sfw = self.__make_buttons(self.__pan_buttons)

        #img = wx.EmptyImage(self.image_size, self.image_size)

    


        


app = wx.App(False)
frame = MyFrame(None, "Lewd Control")
frame.Show(True)
app.MainLoop()