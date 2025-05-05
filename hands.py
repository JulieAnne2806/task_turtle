import turtle

class Hand:
    def __init__(self, hand_length, ratio=1, _x = 0, _y = 0):
        self.hand = turtle.Turtle()
        self.hand.speed(0)
        self.hand.hideturtle()
        self.hand.penup()
        self.hand.goto(_x, _y)
        self.length = hand_length
        self.ratio = ratio

    def draw(self, t):
        angle = self.ratio * 30 * t

        self.hand.clear()
        self.hand.penup()
        self.hand.goto(0, 0)
        self.hand.pendown()
        self.hand.setheading(90 - angle)
        self.hand.forward(self.length)