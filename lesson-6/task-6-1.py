from tkinter import Tk, Frame, Label
import time
import _thread
from itertools import cycle


class TrafficLight:
    _last_light_time = 0
    __color = "RED"
    __rules = [{"RED": 5}, {"YELLOW": 1}, {"GREEN": 5}, {"YELLOW": 2}]
    __light_colors = {"RED": ["red", "lemon chiffon", "DarkSeaGreen1"],
                      "YELLOW": ["antique white", "orange2", "DarkSeaGreen1"],
                      "GREEN": ["antique white", "lemon chiffon", "green3"],
                      "GREENFLASH": "DarkSeaGreen1"}

    def update_light_time(self, new_time):
        self._last_light_time = new_time
        if new_time >= 1:
            if self.__color == "RED":
                l1['text'] = int(new_time)
            elif self.__color == "GREEN":
                l3['text'] = int(new_time)
        else:
            self.reset_light_timer()

    def reset_light_timer(self):
        l1['text'], l2['text'], l3['text'] = "", "", ""

    def set_color(self, color):
        self.__color = color
        self.reset_light_timer()
        l1['bg'] = self.__light_colors.get(color)[0]
        l2['bg'] = self.__light_colors.get(color)[1]
        l3['bg'] = self.__light_colors.get(color)[2]

    def flash_color(self, color):
        if self.__color == "GREEN" and l3['bg'] == self.__light_colors.get(color)[2]:
            l3['bg'] = self.__light_colors.get("GREENFLASH")
        else:
            l3['bg'] = self.__light_colors.get(color)[2]

    def change_color(self):
        for dict in cycle(self.__rules):
            for color, t in dict.items():
                last_time = t
                self.set_color(color)
                self.update_light_time(last_time)
                while last_time > 0:
                    if last_time <= 3:
                        self.flash_color(color)
                    time.sleep(0.5)
                    self.update_light_time(last_time)
                    last_time -= 0.5

    def __init__(self, rules=""):
        if rules:
            self.__rules = rules


traffic_light = TrafficLight()
window = Tk()
f_top = Frame(window)
f_center = Frame(window)
f_bot = Frame(window)

l1 = Label(f_top, width=3, height=2, font="Arial 50")
l2 = Label(f_center, width=3, height=2, font="Arial 50")
l3 = Label(f_bot, width=3, height=2, font="Arial 50")

f_top.pack()
f_center.pack()
f_bot.pack()

l1.pack()
l2.pack()
l3.pack()

_thread.start_new_thread(traffic_light.change_color, ())
window.mainloop()
