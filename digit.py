import turtle

class Digit:
    def __init__(self, number, _x=0, _y=0, _ratio=1, _width=15):
        self.n = int(number)
        self._x = _x
        self._y = _y
        self._ratio = _ratio
        self._width = _width

    def __call__(self):
        def draw_segment(x, y, dx, dy, active):
            if active:
                turtle.width(self._width)
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                turtle.goto(x + dx, y + dy)
                turtle.penup()

        def draw_digit(digit, x_offset=0):
            segments = {
                '0': [1, 1, 1, 1, 1, 1, 0],
                '1': [0, 1, 1, 0, 0, 0, 0],
                '2': [1, 1, 0, 1, 1, 0, 1],
                '3': [1, 1, 1, 1, 0, 0, 1],
                '4': [0, 1, 1, 0, 0, 1, 1],
                '5': [1, 0, 1, 1, 0, 1, 1],
                '6': [1, 0, 1, 1, 1, 1, 1],
                '7': [1, 1, 1, 0, 0, 0, 0],
                '8': [1, 1, 1, 1, 1, 1, 1],
                '9': [1, 1, 1, 1, 0, 1, 1]
            }
            seg = segments[str(digit)]
            positions = [
                (x_offset + self._x, self._y, 40*self._ratio, 0),
                (x_offset + self._x + 40 * self._ratio, self._y, 0, -50 * self._ratio),
                (x_offset + 40 * self._ratio + +self._x, -50 * self._ratio + self._y, 0, -50 * self._ratio),
                (x_offset + self._x, -100 * self._ratio + self._y, 40 * self._ratio, 0),
                (x_offset + self._x, -50 * self._ratio + self._y, 0, -50 * self._ratio),
                (x_offset + self._x, self._y, 0, -50*self._ratio),
                (x_offset + self._x, -50 * self._ratio + self._y, 40 * self._ratio, 0)
            ]
            for i in range(7):
                draw_segment(*positions[i], seg[i])

        turtle.speed(0)
        turtle.delay(0)

        if self.n > 9:
            draw_digit(self.n // 10)
            draw_digit(self.n % 10, 8)
        else:
            draw_digit(self.n)

        turtle.hideturtle()