#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import wx
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin
from contactWindow import ContactWindow

class AutoWidthListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        ListCtrlAutoWidthMixin.__init__(self)

class BookContactWindow(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(BookContactWindow, self).__init__(*args, **kwargs) 
        self.menubar = None
        self.contactBookMenu = None
        self.contactMenu = None    
        self.InitUI()
        
    def InitUI(self):

        self.init_menu()
        self.init_toolbar()
        self.init_list()
        
        self.SetSize((750, 650))
        self.SetTitle('Agenda')
        self.Centre()
        self.Show(True)
    
    def init_menu(self):
        self.menubar = wx.MenuBar()
        #menu Agenda
        self.contactBookMenu = wx.Menu()
        self.contactBookMenu.Append(wx.ID_NEW, '&Nuevo\tCtrl+N')
        #menu Contactos
        self.contactMenu = wx.Menu()
        self.createContact_mi = wx.MenuItem(self.contactMenu, wx.ID_NEW, '&Nuevo')
        self.contactMenu.AppendItem(self.createContact_mi)
        
        self.Bind(wx.EVT_MENU, self.createContact, self.createContact_mi)
        #menu reportes
        self.reportMenu = wx.Menu()
        self.reportMenu.Append(wx.ID_ANY, '&Reporte de contactos')
        #menu sistema
        self.systemMenu = wx.Menu()
        self.qmi = wx.MenuItem(self.systemMenu, wx.ID_EXIT, '&Salir\tCtrl+Q')
        self.systemMenu.AppendItem(self.qmi)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, self.qmi)
        #menubar
        self.menubar.Append(self.contactBookMenu, '&Agenda')
        self.menubar.Append(self.contactMenu, '&Contactos')
        self.menubar.Append(self.reportMenu, '&Reportes')
        self.menubar.Append(self.systemMenu, '&Sistema')
        self.SetMenuBar(self.menubar)
        
    def init_toolbar(self):
        self.toolbar = self.CreateToolBar()
        self.newContact_tool = self.toolbar.AddLabelTool(wx.ID_ANY, 'add', wx.Bitmap('images/contact-new.png'))
        self.editContact_tool = self.toolbar.AddLabelTool(wx.ID_ANY, 'edit', wx.Bitmap('images/contact_edit.png'))
        self.deleteContact_tool = self.toolbar.AddLabelTool(wx.ID_ANY, 'delete', wx.Bitmap('images/delete.png'))
        self.qtool = self.toolbar.AddLabelTool(wx.ID_EXIT, 'Quit', wx.Bitmap('images/quit.png'))
        self.toolbar.Realize()
        
        self.Bind(wx.EVT_TOOL, self.createContact, self.newContact_tool)
        self.Bind(wx.EVT_TOOL, self.editContact, self.editContact_tool)
        self.Bind(wx.EVT_TOOL, self.deleteContact, self.deleteContact_tool)
        self.Bind(wx.EVT_TOOL, self.OnQuit, self.qtool)
        
    def init_list(self):
        self.actresses = [('jessica alba', 'pomona', '1981'), ('sigourney weaver', 'new york', '1949'),
            ('angelina jolie', 'los angeles', '1975'), ('natalie portman', 'jerusalem', '1981'),
            ('rachel weiss', 'london', '1971'), ('scarlett johansson', 'new york', '1984' )]
        
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.panel = wx.Panel(self, -1)

        self.list = AutoWidthListCtrl(self.panel)
        self.list.InsertColumn(0, 'Nombre', width=140)
        self.list.InsertColumn(1, 'Apellido', width=130)
        self.list.InsertColumn(2, 'telefono', wx.LIST_FORMAT_RIGHT, 90)
        self.list.InsertColumn(3, 'Email', wx.LIST_FORMAT_RIGHT, 90)
        
        #va en el controller
        for i in self.actresses:
            index = self.list.InsertStringItem(sys.maxint, i[0])
            self.list.SetStringItem(index, 1, i[1])
            self.list.SetStringItem(index, 2, i[2])
        #hasta aqui
        self.hbox.Add(self.list, 1, wx.EXPAND)
        self.panel.SetSizer(self.hbox)
        
    def createContact(self, e):
        contactWindow = ContactWindow(self, 'Contacto')
        
    def editContact(self, e):
        itemId = self.list.GetFocusedItem()
        firstname = self.list.GetItem(itemId, 0).GetText()
        lastname = self.list.GetItem(itemId, 1).GetText()
        email = self.list.GetItem(itemId, 2).GetText()
        phone = self.list.GetItem(itemId, 3).GetText()
        contactWindow = ContactWindow(self, 'Contacto')
        firstname_txt = contactWindow.panel.GetSizer().GetItem(1).GetWindow()
        firstname_txt.SetValue(firstname)
        lastname_txt = contactWindow.panel.GetSizer().GetItem(3).GetWindow()
        lastname_txt.SetValue(lastname)
        email_txt = contactWindow.panel.GetSizer().GetItem(5).GetWindow()
        email_txt.SetValue(email)
        phone_txt = contactWindow.panel.GetSizer().GetItem(7).GetWindow()
        phone_txt.SetValue(phone)
        self.list.DeleteItem(itemId)
        
    def deleteContact(self, e):
        itemId = self.list.GetFocusedItem()
        self.list.DeleteItem(itemId)
            
    def OnQuit(self, e):
        self.Close()

def main():
    
    ex = wx.App()
    BookContactWindow(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()
