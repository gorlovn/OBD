#!/usr/bin/env python
# encoding: utf8

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from obdII import OBDConnection
from obdII import OBDException


class ConnectionModal(ModalView):
    def __init__(self):
        super(ConnectionModal, self).__init__(auto_dismiss=False,
            anchor_y="bottom")
        self.label = Label(text="Connecting to OBD...")
        self.add_widget(self.label)


class OBDDetailsForm(AnchorLayout):
    speed_box = ObjectProperty()
    rpm_box = ObjectProperty()
    throttle_box = ObjectProperty()
    temp_box = ObjectProperty()
    time_box = ObjectProperty()

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

        print(self.speed_box.text)
        print(self.rpm_box.text)
        print(self.throttle_box.text)
        print(self.temp_box.text)
        print(self.time_box.text)


class OBD(App):

    def connect_to_obd(self):
        self.obdLink = OBDConnection()
        if self.obdLink.status_code != 200:
            raise OBDException("Unable to connect")
        self.state = self.obdLink.getState()

OBD().run()
