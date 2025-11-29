# Yn Yc: solved with Bisection Method
# Developers: github.com/rcfdtools, github.com/frankv13, github.com/juanrodace

# Libraries
from datetime import datetime
import dictionary as dictionary
import functions as funcs
from pyscript import document

def run(event):

    # read fields from html page
    input_unit_sys = document.querySelector("#unit_sys")
    input_q = document.querySelector("#q") # q total, not unitary value
    input_g = document.querySelector("#g")
    input_b = document.querySelector("#b")
    input_z1 = document.querySelector("#z1")
    input_z2 = document.querySelector("#z2")
    input_so = document.querySelector("#so")
    input_n = document.querySelector("#n")
    input_alpha = document.querySelector("#alpha")
    input_rho = document.querySelector("#rho")
    input_y1 = document.querySelector("#y1")
    input_y2 = document.querySelector("#y2")
    input_steps = document.querySelector("#steps")

    # read fields values
    unit_sys = input_unit_sys.value # SI - International, US - Imperial/US
    q = float(input_q.value) # Flow
    g = float(input_g.value) # Gravity acceleration
    b = float(input_b.value) # Channel base
    z1 = float(input_z1.value) # Left side slope
    z2 = float(input_z2.value) # Right side slope
    so = float(input_so.value) # Channel slope
    n = float(input_n.value) # Channel roughness
    alpha = float(input_alpha.value) # Kinetic correction factor
    rho = float(input_rho.value) # ρ: fluid density
    y1 = float(input_y1.value) # Numerical method, low elevation seed
    y2 = float(input_y2.value) # Numerical method, high elevation seed
    steps = int(input_steps.value) # Numerical method, steps

    # Pre validations
    dicts = dictionary.dicts
    if unit_sys.upper() == 'SI':  # Units system eval
        units = dictionary.units_si
    else:
        units = dictionary.units_us
    if alpha == 0: alpha = 1  # alpha validation
    y1aux, y2aux = y1, y2
    y1a = y1
    if y2 < y1:  # eval y2 > y1
        y1, y2 = y2, y1a
    if steps <= 0: steps = 64  # eval # step iterations > 0
    y1a, y2b = y1, y2

    # Yc Calculation
    y2 = funcs.yc(steps, q, g, b, z1, z2, y2, y1, alpha)

    # Yn Calculation
    y2b = funcs.yn(steps, q, b, z1, z2, y2b, y1a, so, n, units['c'])

    # Print results in console
    results = funcs.results(dict['app_version'], datetime.now(), q, g, b, z1, z2, so, n, alpha, rho, y1aux, y2aux,
                            steps, y2b, y2, funcs.shape_type(b, z1, z2), unit_sys, dicts, units)
    output_div = document.querySelector("#output")
    output_div.innerText = results

