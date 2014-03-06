#!/usr/bin/env python
# encoding: utf8

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty


class OBDDetailsForm(AnchorLayout):
    speed_box = ObjectProperty()
    rpm_box = ObjectProperty()
    throttle_box = ObjectProperty()
    temp_box = ObjectProperty()
    time_box = ObjectProperty()

    def connect(self):
        print(self.speed_box.text)
        print(self.rpm_box.text)
        print(self.throttle_box.text)
        print(self.temp_box.text)
        print(self.time_box.text)


class OBD(App):

    def connect_to_obd(self):
        pass

OBD().run()
