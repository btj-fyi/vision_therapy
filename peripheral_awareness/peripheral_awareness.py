import sympy
from PIL import Image, ImageDraw, ImageFont
from random import shuffle

letters: list = []
count: int = 0


def rl() -> str:
    global letters
    global count
    alphabet: list[str] = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    if count > 27:
        count = 0
        letters = alphabet
    if len(letters) == 0:
        print(letters)
        letters = alphabet
    shuffle(letters)
    if len(letters) > 0:
        l: str = letters.pop()
    print(f"{l}: count = {count}")
    count += 1
    return l


def peripheral_awareness():
    w = 1100
    h = 850
    image = Image.open("peripheral_awareness/peripheral_awareness_blank.png")
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

    font = ImageFont.truetype(r"/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 60)
    draw.circle((w / 2, h / 2), 30, fill="red")

    x = 0
    y = 0
    xc = w / 2
    yc = h / 2

    # rectangle A
    xi = 110  # x increment
    xl = x + xi  # x left
    xr = w - xi  # x right

    yi = get_on_a(x=xl)  # y increment
    yt = y + yi  # y top
    yb = h - yi  # y left
    font = ImageFont.truetype(r"/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 85)
    draw.text((xl, yt), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xc, yt), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xr, yt), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xl, yc), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xr, yc), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xl, yb), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xc, yb), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xr, yb), text=rl(), font=font, anchor="mm", fill="black")

    # rectangle B
    xi = 250  # x increment
    xl = x + xi  # x left
    xr = w - xi  # x right

    yi = get_on_a(x=xl)  # y increment
    yt = y + yi  # y top
    yb = h - yi  # y left
    font = ImageFont.truetype(r"/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 60)
    draw.text((xl, yt), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xc, yt), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xr, yt), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xl, yc), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xr, yc), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xl, yb), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xc, yb), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xr, yb), text=rl(), font=font, anchor="mm", fill="black")

    # rectangle C
    xi = 470  # x increment
    xl = x + xi  # x left
    xr = w - xi  # x right

    yi = get_on_a(x=xl)  # y increment
    yt = y + yi  # y top
    yb = h - yi  # y left
    font = ImageFont.truetype(r"/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 35)
    draw.text((xl, yt), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xr, yt), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xl, yb), text=rl(), font=font, anchor="mm", fill="black")
    draw.text((xr, yb), text=rl(), font=font, anchor="mm", fill="black")

    # d = 2r
    # (x – h)^2 + (y – k)^2 = r^2
    # (x - 550)^2 + (y - 425)^2 =  r^2
    r = 165

    # coords 1 and 5
    x, y = sympy.symbols("x y")
    eq1 = (x - 550) ** 2 + (y - 425) ** 2 - r**2
    eq2 = x - 550
    solutions = sympy.solve([eq1, eq2], (x, y))
    for s in solutions:
        draw.text((s[0], s[1]), text=rl(), font=font, anchor="mm", fill="black")

    # coords 2 and 6
    x, y = sympy.symbols("x y")
    eq1 = (x - 550) ** 2 + (y - 425) ** 2 - r**2
    eq2 = y + x - 975
    solutions = sympy.solve([eq1, eq2], (x, y))
    for s in [(s[0].evalf(), s[1].evalf()) for s in solutions]:
        draw.text((s[0], s[1]), text=rl(), font=font, anchor="mm", fill="black")

    # coords 3 and 7
    x, y = sympy.symbols("x y")
    eq1 = (x - 550) ** 2 + (y - 425) ** 2 - r**2
    eq2 = y - 425
    solutions = sympy.solve([eq1, eq2], (x, y))
    for s in solutions:
        draw.text((s[0], s[1]), text=rl(), font=font, anchor="mm", fill="black")

    # coords 8 and 4
    x, y = sympy.symbols("x y")
    eq1 = (x - 550) ** 2 + (y - 425) ** 2 - r**2
    eq2 = y - x + 125
    solutions = sympy.solve([eq1, eq2], (x, y))
    for s in [(s[0].evalf(), s[1].evalf()) for s in solutions]:
        draw.text((s[0], s[1]), text=rl(), font=font, anchor="mm", fill="black")

    image.save(
        "static/peripheral_awareness.png",
    )

    # image.show()
    # oot.mainloop()
