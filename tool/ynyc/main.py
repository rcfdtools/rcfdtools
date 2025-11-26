import arrr
from pyscript import document

def run(event):

    # read fields from html page
    input_UnitSys = document.querySelector("#UnitSys")
    input_q = document.querySelector("#q") # q total, not unitary value
    input_g = document.querySelector("#g")
    input_b = document.querySelector("#b")
    input_z1 = document.querySelector("#z1")
    input_z2 = document.querySelector("#z2")
    input_sf = document.querySelector("#z2")
    input_n = document.querySelector("#n")
    input_alpha = document.querySelector("#alpha")
    input_y2 = document.querySelector("#y2")
    input_y1 = document.querySelector("#y1")
    input_iterat = document.querySelector("#iterat")

    # read fields values
    UnitSys = input_UnitSys.value
    q = float(input_q.value)
    g = float(input_g.value)
    b = float(input_b.value)
    z1 = float(input_z1.value)
    z2 = float(input_z2.value)
    sf = float(input_sf.value)
    n = float(input_n.value)
    alpha = float(input_alpha.value)
    alpha = float(input_alpha.value)
    y1 = float(input_y1.value)
    y2 = float(input_y2.value)
    iterat = float(input_iterat.value)
    results = '\nResults:\n'
    area = area_trapezoid(b, z1, z2, y2)
    results += f'Area: {area}\n'
    output_div = document.querySelector("#output")
    output_div.innerText = results

    # pre validations
    # units system eval
    if UnitSys == 'SI':
        c = 1
        c_unit_text = "m"
    else:
        c = 1.486
        c_unit_text = "ft"
    # alpha validation
    if alpha == 0: alpha = 1
    # eval y2 > y1
    y1a = y1
    if y2 < y1:
        y1 = y2
        y2 = Y1a
    # eval # iterations > 0
    if iterat <= 0: iterat = 32
    y1a = y1
    y2b = y2

# Yc Calculations
inc = 0
for inc in iterat:
    y2a = (y2 + y1) / 2
    q1 = f_yc_calc(q, g, b, z1, z2, y2, alpha)
    q2 = f_yc_calc(Q, g, b, z1, z2, Y2a, alpha)
    y1 = y2 # xxxx check zero difference validation
    y2 = y2a

def area_trapezoid(b, z1, z2, y):
    area = b * y + ((y ** 2) / 2) * (z1 + z2)
    return area