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
    iterat = float(input_iterat.value)
    results = '\nResults:\n'
    area = area_trapezoid(b, z1, z2, Y)
    results += f'Area: {area}\n'
    output_div = document.querySelector("#output")
    output_div.innerText = results

def area_trapezoid(b, z1, z2, Y):
    area = b * Y + ((Y ^ 2) / 2) * (z1 + z2)
    return area