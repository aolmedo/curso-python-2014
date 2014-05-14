#!/usr/bin/python
# -*- coding: utf-8

import wx

class ContactWindow(wx.Frame):

    def __init__(self, parent, title):
        super(ContactWindow, self).__init__(parent, title=title, size=(500,400))
        self.parent = parent

        self.InitUI()

    def InitUI(self):
        self.panel = wx.Panel(self)

        grid = wx.GridBagSizer(8, 2)

        grid.AddGrowableCol(2)
        self.panel.SetSizer(grid)
        #fgs = wx.FlexGridSizer(3, 2, 9, 25)

        #label nombre
        firstname_lbl = wx.StaticText(self.panel, label="Nombre")
        grid.Add(firstname_lbl, pos=(2, 0), flag=wx.LEFT, border=10)

        #text nombre
        firstname_txt = wx.TextCtrl(self.panel, size=(300, 25))
        grid.Add(firstname_txt, pos=(2, 1), flag=wx.LEFT, border=10)
        #label apellido
        lastname_lbl = wx.StaticText(self.panel, label="Apellido")
        grid.Add(lastname_lbl, pos=(3, 0), flag=wx.LEFT, border=10)
        #text apellido
        lastname_txt = wx.TextCtrl(self.panel, size=(300, 25))
        grid.Add(lastname_txt, pos=(3, 1), flag=wx.LEFT, border=10)
        #label email
        email_lbl = wx.StaticText(self.panel, label="Email")
        grid.Add(email_lbl, pos=(4, 0), flag=wx.LEFT, border=10)
        #email_txt
        email_txt = wx.TextCtrl(self.panel, size=(300, 25))
        grid.Add(email_txt, pos=(4, 1), flag=wx.LEFT, border=10)
        #label phone
        phone_lbl = wx.StaticText(self.panel, label="Telefono")
        grid.Add(phone_lbl, pos=(5, 0), flag=wx.LEFT, border=10)
        #phone_txt
        phone_txt = wx.TextCtrl(self.panel, size=(200, 25))
        grid.Add(phone_txt, pos=(5, 1), flag=wx.LEFT, border=10)
        #tc3 = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)

        ok_button = wx.Button(self.panel, label='Ok')
        grid.Add(ok_button, pos=(8, 0), flag=wx.LEFT, border=10)
        ok_button.Bind(wx.EVT_BUTTON, self.save)

        cancel_button = wx.Button(self.panel, label="Cancelar")
        grid.Add(cancel_button, pos=(8, 1))
        cancel_button.Bind(wx.EVT_BUTTON, self.OnClose)

    def save(self, evt):
        #TODO
        self.Close()

    def OnClose(self, evt):
        self.Close()

def main():
    agenda = wx.App()
    contactWindow = ContactWindow(None, 'Contacto')
    #Centro la ventana y la muestro
    contactWindow.Centre()
    contactWindow.Show()
    agenda.MainLoop()

if __name__ == '__main__':
    main()
