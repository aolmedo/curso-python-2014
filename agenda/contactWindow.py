#!/usr/bin/python
# -*- coding: utf-8
import wx
import sys

class ContactWindow(wx.Frame):
    def __init__(self, parent, title):
        super(ContactWindow, self).__init__(parent, title=title,
            size=(500, 400))

        self.parent = parent

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        self.panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        titulo_lbl = wx.StaticText(self.panel, label="Ingrese los datos de contacto:")
        hbox.Add(titulo_lbl, flag=wx.LEFT, border=10)

        sizer = wx.GridBagSizer(8, 2)

        #fgs = wx.FlexGridSizer(3, 2, 9, 25)

        #label nombre
        firstname_lbl = wx.StaticText(self.panel, label="Nombre")
        sizer.Add(firstname_lbl, pos=(2, 0), flag=wx.LEFT, border=10)
        #text nombre
        firstname_txt = wx.TextCtrl(self.panel, size=(300, 25))
        sizer.Add(firstname_txt, pos=(2, 1), flag=wx.LEFT, border=10)
        #label apellido
        lastname_lbl = wx.StaticText(self.panel, label="Apellido")
        sizer.Add(lastname_lbl, pos=(3, 0), flag=wx.LEFT, border=10)
        #text apellido
        lastname_txt = wx.TextCtrl(self.panel, size=(300, 25))
        sizer.Add(lastname_txt, pos=(3, 1), flag=wx.LEFT, border=10)
        #label email
        email_lbl = wx.StaticText(self.panel, label="Email")
        sizer.Add(email_lbl, pos=(4, 0), flag=wx.LEFT, border=10)
        #email_txt
        email_txt = wx.TextCtrl(self.panel, size=(300, 25))
        sizer.Add(email_txt, pos=(4, 1), flag=wx.LEFT, border=10)
        #label phone
        phone_lbl = wx.StaticText(self.panel, label="Telefono")
        sizer.Add(phone_lbl, pos=(5, 0), flag=wx.LEFT, border=10)
        #phone_txt
        phone_txt = wx.TextCtrl(self.panel, size=(200, 25))
        sizer.Add(phone_txt, pos=(5, 1), flag=wx.LEFT, border=10)
        #tc3 = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)

        ok_button = wx.Button(self.panel, label='Ok')
        sizer.Add(ok_button, pos=(8, 0), flag=wx.LEFT, border=10)
        ok_button.Bind(wx.EVT_BUTTON, self.save)

        cancel_button = wx.Button(self.panel, label="Cancelar")
        sizer.Add(cancel_button, pos=(8, 1))
        cancel_button.Bind(wx.EVT_BUTTON, self.OnClose)

        sizer.AddGrowableCol(2)

        #hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        self.panel.SetSizer(sizer)

    def save(self, e):
        firstname_txt = self.panel.GetSizer().GetItem(1).GetWindow()
        lastname_txt = self.panel.GetSizer().GetItem(3).GetWindow()
        email_txt = self.panel.GetSizer().GetItem(5).GetWindow()
        phone_txt = self.panel.GetSizer().GetItem(7).GetWindow()

        #actualizo la lista
        list = self.parent.list
        index = list.InsertStringItem(sys.maxint, firstname_txt.GetValue())
        list.SetStringItem(index, 1, lastname_txt.GetValue())
        list.SetStringItem(index, 2, email_txt.GetValue())
        list.SetStringItem(index, 3, phone_txt.GetValue())
        self.Close()

    def OnClose(self, e):
        self.Close()

def main():

    ex = wx.App()
    ContactWindow(None, 'Contacto')
    ex.MainLoop()


if __name__ == '__main__':
    main()
