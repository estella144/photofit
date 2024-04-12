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

def draw_eye(color, x, y):
    pass

def draw_eyes(color):
    pass

def draw_glasses():
    pass

def draw_mustache(color):
    pass

def draw_beard(color):
    pass

def draw_hair(color, style):
    pass

def draw_face(skin_color):
    pass

def main():
    print("Welcome to photofit")
    input("Press [ENTER] to start or [Ctrl-C] to quit")
    print("[*] Setting up turtle...")
    
    window = turtle.Screen()
    t = turtle.Turtle()

    print("[-] Enter colour of skin")
    print("    Available: None")
    skin_color = input("  > ")

    print("[-] Enter colour of hair")
    print("    Available: black, brown, blonde")
    hair_color = input("  > ")

    print("[-] Enter style of hair")
    print("    Available: short, long")
    hair_style = input("  > ")
    
    print("[-] Enter colour of eyes")
    print("    Available: black, brown, blue, green")
    eye_color = input("  > ")

if __name__ == "__main__":
    main()

