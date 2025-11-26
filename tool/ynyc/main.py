import arrr
from pyscript import document

def run(event):
    # read fields from html page
    input_UnitSys = document.querySelector("#UnitSys")
    input_Q = document.querySelector("#Q")
    input_g = document.querySelector("#g")
    input_b = document.querySelector("#b")
    input_z1 = document.querySelector("#z1")
    input_z2 = document.querySelector("#z2")
    input_n = document.querySelector("#n")
    input_alpha = document.querySelector("#alpha")
    input_iterat = document.querySelector("#iterat")
    # read fields values
    UnitSys = input_UnitSys.value
    Q = float(input_Q.value)
    g = float(input_g.value)
    b = float(input_b.value)
    z1 = float(input_z1.value)
    z2 = float(input_z2.value)
    n = float(input_n.value)
    alpha = float(input_alpha.value)
    iterat = float(input_iterat.value)
    xxx = (Q + g + b + z1 + z2 + n + alpha + iterat)
    output_div = document.querySelector("#output")
    output_div.innerText = xxx

