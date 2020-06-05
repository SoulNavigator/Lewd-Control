import wx


# pylint: disable=fixme, no-member
class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, style=wx.CAPTION | wx.CLOSE_BOX, size=wx.Size(800, 1000))
        self.make_ui()

    def make_ui(self):
        self.toolbar = Menubar(self)
        mainbox = wx.BoxSizer(wx.VERTICAL)
        self.pan_image = ImagePanel(self, mainbox)
        self.pan_buttons = ButtonPanel(self, mainbox)
        self.SetSizer(mainbox)

class ImagePanel(wx.Panel):
    default_size = 800
    def __init__(self, parent, sizer):
        self.parent = parent
        super().__init__(parent)
        sizer.Add(self, 5, wx.ALL | wx.EXPAND, 5)

        img = wx.EmptyImage(self.default_size, self.default_size)
        img.Rescale(self.default_size, self.default_size)
        parent.SetSize(self.default_size, self.default_size+150)

        self.image_widget = wx.StaticBitmap(self, bitmap=wx.BitmapFromImage(img))

        img_sizer = wx.BoxSizer(wx.HORIZONTAL)
        img_sizer.Add(self.image_widget, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(img_sizer)

    def image_ratio(self, image:wx.Image):
        w = image.GetWidth()
        h = image.GetHeight()

        return w/h

    def update_image(self, path):
        img = wx.Image(path, wx.BITMAP_TYPE_ANY)
        ratio = self.image_ratio(img)
        img.Rescale(self.default_size*ratio, self.default_size)

        self.parent.SetSize(self.default_size*ratio, self.default_size+150)
        
        self.image_widget.SetBitmap(wx.BitmapFromImage(img))
        img_sizer = wx.BoxSizer(wx.HORIZONTAL)
        img_sizer.Add(self.image_widget, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(img_sizer)

class ButtonPanel(wx.Panel):
    def __init__(self, parent, sizer):
        self.parent = parent
        super().__init__(parent)
        sizer.Add(self, 1, wx.ALL | wx.EXPAND, 5)
        self.init_buttons()

    def init_buttons(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.btn_yes = wx.Button(self, label='OwO!')
        self.btn_no = wx.Button(self, label='SFW')

        self.bind_buttons()

        hbox.Add(self.btn_no,  1, wx.ALL|wx.EXPAND, 10)
        hbox.Add(self.btn_yes, 2, wx.ALL|wx.EXPAND, 10) 
        self.SetSizer(hbox)  

    def bind_buttons(self):
        self.btn_yes.Bind(wx.EVT_BUTTON, self.OnNSFWbuttonPress)
        self.btn_no.Bind(wx.EVT_BUTTON, self.OnSFWbuttonPress)

    def OnNSFWbuttonPress(self, event):
        print("This picture is NSFW")

    def OnSFWbuttonPress(self, event):
        print("This picture is SFW")
    
class Menubar(wx.MenuBar):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        menubar = wx.MenuBar()
        file = wx.Menu()
        menubar.Append(file, 'File')
        self.i_scan = file.Append(wx.ID_ANY, 'Scan folder')
        parent.SetMenuBar(menubar)
        self.bind_items()

    def bind_items(self):
        self.parent.Bind(wx.EVT_MENU, self.OnMenuScanPress, self.i_scan)
        
    def OnMenuScanPress(self, event):
        wildcard = "pictures (*.jpeg,*.png,*.jpg)|*.jpeg;*.png;*.jpg"
        with wx.FileDialog(self, "Pick file", wildcard=wildcard) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = file_dialog.GetPath()
            self.parent.pan_image.update_image(pathname)

def start_gui():
    app = wx.App(False)
    frame = MainFrame(None, "Lewd Control")
    frame.Show(True)
    app.MainLoop()