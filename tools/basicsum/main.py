import arrr
from pyscript import document

def run(event):
    input_a = document.querySelector("#a")
    input_b = document.querySelector("#b")
    a = input_a.value * 1
    b = input_b.value * 1
    output_div = document.querySelector("#output")
    output_div.innerText = a+b
