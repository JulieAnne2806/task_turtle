from digit_shypilova import Digit
from hands_shypilova import Hand
import time
from math import sin, cos, pi

class Dial:
    def __init__(self, time_stretch):
        self.smallHand = Hand(hand_length=50)
        self.bigHand = Hand(hand_length=70, ratio=0.2)

        self.hours = 0
        self.minutes = 0
        self.digits = [Digit(i+1, 80*cos((pi * (14-i))/6), 80*sin((pi * (14-i))/6), 0.1, 3)() for i in range (0, 12)]
        self.t = time_stretch

        while True:
            self.draw()
            self.tick()
            time.sleep(time_stretch)

    def draw(self):
        self.smallHand.draw(self.hours)
        self.bigHand.draw(self.minutes)

    def tick(self):
        self.minutes += 5
        if self.minutes == 60:
            self.hours += 1
            self.minutes -= 60

if __name__ == "__main__":
    new_dial = Dial(time_stretch=1)