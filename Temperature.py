#! /usr/bin/python3.8
import tkinter as tk
from random import choice, randint
from math import pi


def kelvin(temp):
    return temp + 273.15


def rankine(temp):
    temp += 273.15
    return temp * 9 / 5


def delisle(temp):
    temp = 100 - temp
    return temp * 3 / 2


def newton(temp):
    return temp * 33 / 100


def reaumur(temp):
    return temp * 4 / 5


def romer(temp):
    temp = temp * 21 / 40
    return temp + 7.5


def radians(temp):
    return temp * pi / 180


def average_energy(temp):
    boltzmann_constant = 1.380649e-23
    temp = kelvin(temp)
    energy = 1.5 * boltzmann_constant * temp
    conversion_constant = 6.242e18
    return energy * conversion_constant


def random_unit(temp):
    units = choice(list(scales.keys()))
    new_temp = scales[units](temp)
    if units == "Radians":
        lbl_text = f"{new_temp:.2f} Radians"
    elif units == "eV":
        lbl_text = f"{new_temp:.2f} eV"
    else:
        lbl_text = f"{new_temp:.2f} degrees {units}"
    lbl.configure(text=lbl_text)


scales = {
    "Kelvin": kelvin,
    "Rankine": rankine,
    "Delisle": delisle,
    "Newton": newton,
    "Reaumur": reaumur,
    "Romer": romer,
    "Radians": radians,
    "eV": average_energy,
}

window = tk.Tk()

window.title("Temperature")
window.geometry("250x100")

temp = randint(5, 40)

lbl = tk.Label(window)
lbl.pack(ipady=15)
random_unit(temp)

btn_units = tk.Button(window, text="Change units", command=lambda: random_unit(temp))
btn_units.pack()

window.mainloop()
