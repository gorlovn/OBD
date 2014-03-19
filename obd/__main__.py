#!/usr/bin/env python
# encoding: utf8

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from obdII import OBDConnection
from obdII import OBDException


class ItemListItem(BoxLayout):
    item_name = StringProperty()
    item_value = StringProperty()
    background = ObjectProperty()


class ItemList(BoxLayout):
    list_view = ObjectProperty()

    def __init__(self):
        super(ItemList, self).__init__()
        self.app = OBD.get_running_app()
        self.list_view.adapter.data = self.app.obdLink.getState()

    def obd_converter(self, index, item_name):
        result = {
            "item_name": item_name,
            "item_value": str(self.app.obdLink.getState()[item_name])
        }
        if index % 2:
            result["background"] = (0, 0, 0, 1)
        else:
            result["background"] = (0.5, 0.5, 0.7, 1)

        return result

    def force_list_view_update(self):
        self.list_view.adapter.update_for_new_data()
        self.list_view._trigger_reset_populate()


class OBDRoot(BoxLayout):
    def remove_item_list(self, *args):
        self.remove_widget(self.item_list)
        self.button.text = "Connect"

    def show_item_list(self):
        self.orientation = 'vertical'
        self.clear_widgets()
        self.item_list = ItemList()
        self.add_widget(self.item_list)


class ConnectionModal(ModalView):
    def __init__(self):
        super(ConnectionModal, self).__init__(auto_dismiss=False,
            anchor_y="bottom")
        self.label = Label(text="Connecting to OBD...")
        self.add_widget(self.label)
        self.on_open = self.connect_to_obd

    def connect_to_obd(self):
        app = OBD.get_running_app()
        try:
            app.connect_to_obd()
            app.root.show_item_list()
            self.dismiss()
        except OBDException:
            self.label.text = "Sorry, couldn't connect"
            button = Button(text="Try Again")
            button.size_hint = (1.0, None)
            button.height = "40dp"
            button.bind(on_press=self.dismiss)
            self.add_widget(button)


class OBDDetailsForm(AnchorLayout):

    def connect(self):
        modal = ConnectionModal()
        modal.open()
        app = OBD.get_running_app()
        try:
            app.connect_to_obd()
            modal.label.text = "Connected!"
            connected = True
        except OBDException:
            modal.label.text = "Sorry, couldn't connect"
            connected = False
        if connected:
            state = app.state
            for name in state:
                sout = "{0}: {1}".format(name, state[name])
                print(sout)


class OBD(App):
    def __init__(self):
        super(OBD, self).__init__()
        self.obdLink = None
        self.state = None

    def connect_to_obd(self):
        self.obdLink = OBDConnection()
        if self.obdLink.status_code != 200:
            raise OBDException("Unable to connect")
        self.state = self.obdLink.getState()

OBD().run()
