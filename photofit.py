##    photofit - Draws face from description
##    Copyright (C) 2024 Oliver Nguyen
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import turtle

def draw_eye(turtle_color, x, y, current_turtle):
    t = current_turtle

    t.pu()
    t.goto(x, y)
    t.pd()
    t.seth(0)

    t.color("black", "white")
    t.begin_fill()
    t.circle(25)
    t.end_fill()

    t.pu()
    t.seth(90)
    t.fd(10)
    t.pd()
    t.seth(0)

    t.color(turtle_color)
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.seth(0)

    t.pu()
    t.seth(90)
    t.fd(7.5)
    t.pd()
    t.seth(0)

    t.color("black")
    t.begin_fill()
    t.circle(7.5)
    t.end_fill()

def draw_eyes(color, current_turtle):
    """Draws both eyes on face"""
    COLORS = {"black": "black",
              "brown": "#634e34",
              "blue": "#2e536f",
              "green": "#3d671d"}

    turtle_color = COLORS[color]
    t = current_turtle

    draw_eye(turtle_color, 75, 75, t)
    draw_eye(turtle_color, -75, 75, t)

def draw_lips(gender, current_turtle):
    """Draws lips"""
    t = current_turtle

    LIP_WIDTHS = {"": 12.5,
                  "male": 10,
                  "female": 15}
    lip_width = LIP_WIDTHS[gender]
    
    t.color("#e76a6a")

    t.pu()
    t.goto(-50, 0)
    t.pd()
    t.begin_fill()
    t.goto(-30, lip_width)
    t.goto(30, lip_width)
    t.goto(50, 0)
    t.goto(30, -lip_width)
    t.goto(-30, -lip_width)
    t.goto(-50, 0)
    t.end_fill()

    t.color("black")
    t.seth(0)
    t.fd(100)

def draw_glasses_lens(current_turtle):
    t = current_turtle
    # Positions turtle
    t.pu()
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.seth(0)
    t.pd()
    # Draws lens
    t.circle(50)
    # Re-positions turtle for further drawing
    t.pu()
    t.fd(50)
    t.lt(90)
    t.fd(50)
    t.seth(0)
    t.pd()

def draw_glasses(current_turtle):
    """Draws glasses on face"""
    t = current_turtle
    t.pu()
    t.goto(-200, 100)
    t.pd()
    t.seth(0)

    t.fd(75)
    draw_glasses_lens(t)
    t.fd(50)
    draw_glasses_lens(t)
    t.fd(75)

def draw_mustache(color):
    pass

def draw_beard(color):
    pass

def draw_forehead(skin_color, current_turtle):
    """Draws forehead to reduce size of hair"""
    COLORS = {"white": "wheat",
              "brown": "peru",
              "black": "saddle brown"}

    turtle_color = COLORS[skin_color]
    t = current_turtle

    t.pu()
    t.goto(150, 100)
    t.pd()

    t.color(turtle_color)
    t.seth(90)
    t.begin_fill()
    t.circle(150, 180)
    t.end_fill()

def draw_hair(color, style, current_turtle):
    """Draws upper part of hair"""
    COLORS = {"black": "black",
              "brown": "#341f0a",
              "blonde": "#d7d67c",
              "gray": "gray"}

    turtle_color = COLORS[color]
    t = current_turtle

    t.pu()
    t.goto(200, 100)
    t.pd()

    t.color(turtle_color)
    t.seth(90)
    t.begin_fill()
    t.circle(200, 180)
    t.end_fill()

def draw_long_hair(color, current_turtle):
    """Draws lower part of long hair"""
    COLORS = {"black": "black",
              "brown": "#341f0a",
              "blonde": "#d7d67c",
              "gray": "gray"}

    turtle_color = COLORS[color]
    t = current_turtle

    current_turtle.pu()
    current_turtle.goto(-200, -100)
    current_turtle.pd()

    current_turtle.color(turtle_color)
    current_turtle.seth(0)
    current_turtle.begin_fill()

    for i in range(2):
        current_turtle.fd(400)
        current_turtle.lt(90)
        current_turtle.fd(200)
        current_turtle.lt(90)

    current_turtle.end_fill()

def draw_face(skin_color, current_turtle):
    COLORS = {"white": "wheat",
              "brown": "peru",
              "black": "saddle brown"}

    skin_turtle_color = COLORS[skin_color]

    current_turtle.pu()
    current_turtle.goto(0, -100)
    current_turtle.pd()

    current_turtle.color(skin_turtle_color)
    current_turtle.begin_fill()
    current_turtle.circle(200)
    current_turtle.end_fill()

def main_loop():
    print("Setting up turtle...")

    # Sets up turtle. Speed 0 = instant. Turtle hidden for further speed.
    window = turtle.Screen()
    t = turtle.Turtle()
    t.ht()
    t.speed(0)

    print("Enter gender")
    print("(male, female) [leave blank for other]")
    gender = input("> ").lower()
    
    print("Enter colour of skin")
    print("(white, brown, black)")
    skin_color = input("> ").lower()

    print("Bald? [y/n]")
    bald = input("> ").lower()

    if not bald:
        print("Enter colour of hair")
        print("(black, brown, blonde, gray)")
        hair_color = input("> ").lower()

        print("Enter style of hair")
        print("(short, long)")
        hair_style = input("> ").lower()

    print("Enter colour of eyes")
    print("(black, brown, blue, green)")
    eye_color = input("> ").lower()

    print("Glasses? [y/n]")
    glasses = input("> ").lower()

    print("Drawing...")

    if (not bald) and (hair_style == "long"):
        draw_long_hair(hair_color, t)

    draw_face(skin_color, t)
    
    if not bald:
        draw_hair(hair_color, hair_style, t)
        draw_forehead(skin_color, t)
    
    draw_eyes(eye_color, t)
    draw_lips(gender, t)

    if glasses == "y":
        draw_glasses(t)

    print("Finished")
    input("Press [ENTER] to draw another face or [Ctrl-C] to quit...")

    t.reset()

def main():

    NOTICE = """photofit Copyright (c) 2024 Oliver Nguyen 
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions. See <gnu.org/licenses/>."""
    
    print("Welcome to photofit (v0.1.1:9e747ae, 26 Apr 2024)")
    print()
    print(NOTICE)
    print()
    print("Please report bugs to the GitHub repository")
    print("<github.com/estella144/photofit/issues>")
    print()
    input("Press [ENTER] to start or [Ctrl-C] to quit")

    while True:
        main_loop()

if __name__ == "__main__":
    main()
