from tkinter import *
from scipy.optimize import fsolve
import sympy
from PIL import Image, ImageDraw, ImageFont
import random


def rl():
    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return random.choice(uppercase_alphabet)


def main():
    root = Tk()
    w = 1100
    h = 850
    canvas = Canvas(root, height=h, width=w)
    canvas.pack()
    image = Image.open("peripheral_awareness\peripheral_awareness_blank.png")
    draw = ImageDraw.Draw(image)

    def get_on_a(x: int = None, y: int = None) -> int:
        if x:
            return (850 / 1100) * x
        if y:
            return (1100 / 850) * y

    def get_on_b(x: int = None, y: int = None) -> int:
        if x:
            return ((-1 * (850 / 1100)) * x) + 850
        if y:
            return ((-1 * (1100 / 850)) * y) - 850

    canvas.create_line(0, 0, w, h, fill="black")
    canvas.create_line(0, h, w, 0, fill="black")

    canvas.create_oval(w / 2 - 25, h / 2 - 25, w / 2 + 25, h / 2 + 25, fill="red")
    font = ImageFont.truetype(r"C:\Users\System-Pc\Desktop\arial.ttf", 60)
    draw.text((w / 2, h / 2), text=rl(), font=font, fill="red", anchor="mm")

    x = 0
    y = 0
    xc = w / 2
    yc = h / 2

    # rectangle A
    canvas.create_rectangle(110, 85, w - 110, h - 85)
    xi = 110  # x increment
    xl = x + xi  # x left
    xr = w - xi  # x right

    yi = get_on_a(x=xl)  # y increment
    yt = y + yi  # y top
    yb = h - yi  # y left

    font_a = ("Arial", 85)
    canvas.create_text(xl, yt, text=rl(), font=font_a)
    canvas.create_text(xc, yt, text=rl(), font=font_a)
    canvas.create_text(xr, yt, text=rl(), font=font_a)

    canvas.create_text(xl, yc, text=rl(), font=font_a)
    canvas.create_text(xr, yc, text=rl(), font=font_a)

    canvas.create_text(xl, yb, text=rl(), font=font_a)
    canvas.create_text(xc, yb, text=rl(), font=font_a)
    canvas.create_text(xr, yb, text=rl(), font=font_a)

    font = ImageFont.truetype(r"C:\Users\System-Pc\Desktop\arial.ttf", 85)
    draw.text((xl, yt), text=rl(), font=font, anchor="mm")
    draw.text((xc, yt), text=rl(), font=font, anchor="mm")
    draw.text((xr, yt), text=rl(), font=font, anchor="mm")
    draw.text((xl, yc), text=rl(), font=font, anchor="mm")
    draw.text((xr, yc), text=rl(), font=font, anchor="mm")
    draw.text((xl, yb), text=rl(), font=font, anchor="mm")
    draw.text((xc, yb), text=rl(), font=font, anchor="mm")
    draw.text((xr, yb), text=rl(), font=font, anchor="mm")

    # rectangle B
    canvas.create_rectangle(
        250,
        get_on_a(x=250),
        w - 250,
        get_on_a(x=w - 250),
    )
    xi = 250  # x increment
    xl = x + xi  # x left
    xr = w - xi  # x right

    yi = get_on_a(x=xl)  # y increment
    yt = y + yi  # y top
    yb = h - yi  # y left

    font_b = ("Arial", 60)
    canvas.create_text(xl, yt, text=rl(), font=font_b)
    canvas.create_text(xc, yt, text=rl(), font=font_b)
    canvas.create_text(xr, yt, text=rl(), font=font_b)

    canvas.create_text(xl, yc, text=rl(), font=font_b)
    canvas.create_text(xr, yc, text=rl(), font=font_b)

    canvas.create_text(xl, yb, text=rl(), font=font_b)
    canvas.create_text(xc, yb, text=rl(), font=font_b)
    canvas.create_text(xr, yb, text=rl(), font=font_b)

    font = ImageFont.truetype(r"C:\Users\System-Pc\Desktop\arial.ttf", 60)
    draw.text((xl, yt), text=rl(), font=font, anchor="mm")
    draw.text((xc, yt), text=rl(), font=font, anchor="mm")
    draw.text((xr, yt), text=rl(), font=font, anchor="mm")
    draw.text((xl, yc), text=rl(), font=font, anchor="mm")
    draw.text((xr, yc), text=rl(), font=font, anchor="mm")
    draw.text((xl, yb), text=rl(), font=font, anchor="mm")
    draw.text((xc, yb), text=rl(), font=font, anchor="mm")
    draw.text((xr, yb), text=rl(), font=font, anchor="mm")

    # rectangle C
    canvas.create_rectangle(
        470,
        get_on_a(x=470),
        w - 470,
        get_on_a(x=w - 470),
    )
    xi = 470  # x increment
    xl = x + xi  # x left
    xr = w - xi  # x right

    yi = get_on_a(x=xl)  # y increment
    yt = y + yi  # y top
    yb = h - yi  # y left

    font_c = ("Arial", 35)
    canvas.create_text(xl, yt, text=rl(), font=font_c)
    canvas.create_text(xr, yt, text=rl(), font=font_c)
    canvas.create_text(xl, yb, text=rl(), font=font_c)
    canvas.create_text(xr, yb, text=rl(), font=font_c)

    font = ImageFont.truetype(r"C:\Users\System-Pc\Desktop\arial.ttf", 35)
    draw.text((xl, yt), text=rl(), font=font, anchor="mm")
    draw.text((xr, yt), text=rl(), font=font, anchor="mm")
    draw.text((xl, yb), text=rl(), font=font, anchor="mm")
    draw.text((xr, yb), text=rl(), font=font, anchor="mm")

    # d = 2r
    # (x – h)^2 + (y – k)^2 = r^2
    # (x - 550)^2 + (y - 425)^2 =  r^2
    r = 165
    canvas.create_oval(w / 2 - r, h / 2 - r, w / 2 + r, h / 2 + r, width=2)

    # coords 1 and 5
    x, y = sympy.symbols("x y")
    eq1 = (x - 550) ** 2 + (y - 425) ** 2 - r**2
    eq2 = x - 550
    solutions = sympy.solve([eq1, eq2], (x, y))
    for s in solutions:
        canvas.create_text(s[0], s[1], text=rl(), font=font_c)
        draw.text((s[0], s[1]), text=rl(), font=font, anchor="mm")

    # coords 2 and 6
    x, y = sympy.symbols("x y")
    eq1 = (x - 550) ** 2 + (y - 425) ** 2 - r**2
    eq2 = y + x - 975
    solutions = sympy.solve([eq1, eq2], (x, y))
    for s in [(s[0].evalf(), s[1].evalf()) for s in solutions]:
        canvas.create_text(s[0], s[1], text=rl(), font=font_c)
        draw.text((s[0], s[1]), text=rl(), font=font, anchor="mm")

    # coords 3 and 7
    x, y = sympy.symbols("x y")
    eq1 = (x - 550) ** 2 + (y - 425) ** 2 - r**2
    eq2 = y - 425
    solutions = sympy.solve([eq1, eq2], (x, y))
    for s in solutions:
        canvas.create_text(s[0], s[1], text=rl(), font=font_c)
        draw.text((s[0], s[1]), text=rl(), font=font, anchor="mm")

    # coords 8 and 4
    x, y = sympy.symbols("x y")
    eq1 = (x - 550) ** 2 + (y - 425) ** 2 - r**2
    eq2 = y - x + 125
    solutions = sympy.solve([eq1, eq2], (x, y))
    for s in [(s[0].evalf(), s[1].evalf()) for s in solutions]:
        canvas.create_text(s[0], s[1], text=rl(), font=font_c)
        draw.text((s[0], s[1]), text=rl(), font=font, anchor="mm")

    image.save(
        "peripheral_awareness\peripheral_awareness.png",
    )

    # image.show()
    # oot.mainloop()
