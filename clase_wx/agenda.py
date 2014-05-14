#!/usr/bin/python
# -*- coding: utf-8
import sys
import wx
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin

from contactWindow import ContactWindow

class AgendaModel:

    def __init__(self, contacts):
        self.contacts = contacts

    def add(self, aContact):
        self.contacts.append(aContact)

    def edit(self, aContact):
        pass

    def delete(self):
        pass

class AgendaController:
    pass

class AutoWidthListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        ListCtrlAutoWidthMixin.__init__(self)

class BookContactWindow(wx.Frame):

    def __init__(self, parent, title):
        super(BookContactWindow, self).__init__(parent, title=title)
        self.parent = parent
        self.model = AgendaModel([('Agustín', 'Olmedo', '43554332')])
        self.contactBookMenu = None
        self.InitUI()

    def InitUI(self):
        self.init_menu()
        self.init_toolbar()
        self.init_list()
        self.SetSize((750, 650))
        self.SetTitle('Agenda')

    def init_menu(self):
        self.menubar = wx.MenuBar()
        #menu Agenda
        self.contactBookMenu = wx.Menu()
        self.contactBookMenu.Append(wx.ID_NEW, '&Nuevo\tCtrl+N')

        self.menubar.Append(self.contactBookMenu, '&Agenda')

        #menu Contactos
        self.contactMenu = wx.Menu()
        self.menubar.Append(self.contactMenu, '&Contactos')
        self.createContact_mi = wx.MenuItem(self.contactMenu, wx.ID_NEW, '&Nuevo\tCtrl+C')
        self.contactMenu.AppendItem(self.createContact_mi)

        self.Bind(wx.EVT_MENU, self.createContact, self.createContact_mi)

        #menu reportes
        self.reportMenu = wx.Menu()
        self.reportMenu.Append(wx.ID_ANY, '&Reporte de contactos')
        self.menubar.Append(self.reportMenu, '&Reportes')

        #menu sistema
        self.systemMenu = wx.Menu()
        self.qmi = wx.MenuItem(self.systemMenu, wx.ID_EXIT, '&Salir\tCtrl+Q')
        self.systemMenu.AppendItem(self.qmi)
        self.menubar.Append(self.systemMenu, '&Sistema')

        self.Bind(wx.EVT_MENU, self.OnQuit, self.qmi)

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
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.panel = wx.Panel(self, -1)

        self.list = AutoWidthListCtrl(self.panel)
        self.list.InsertColumn(0, 'Nombre', width=200)
        self.list.InsertColumn(1, 'Apellido', width=200)
        self.list.InsertColumn(2, 'telefono', width=150)
        self.list.InsertColumn(3, 'Email', wx.LIST_FORMAT_CENTRE, 90)

        for i in self.model.contacts:
            index = self.list.InsertStringItem(sys.maxint, i[0])
            self.list.SetStringItem(index, 1, i[1])
            self.list.SetStringItem(index, 2, i[2])

        self.hbox.Add(self.list, 1, wx.EXPAND)
        self.panel.SetSizer(self.hbox)


    def createContact(self, evt):
        contactWindow = ContactWindow(self, 'Nuevo Contacto')
        contactWindow.Centre()
        contactWindow.Show()

    def editContact(self, evt):
        contactWindow = ContactWindow(self, 'Modificar Contacto')
        contactWindow.Centre()
        contactWindow.Show()

    def deleteContact(self, evt):
        pass

    def OnQuit(self, evt):
        self.Close()



def main():

    agenda = wx.App()
    bookContactWindow = BookContactWindow(None, 'Agenda')
    bookContactWindow.Centre()
    bookContactWindow.Show()
    agenda.MainLoop()


if __name__ == '__main__':
    main()
