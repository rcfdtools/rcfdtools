from pyscript import document

def run(event):
    input_a = document.querySelector("#a")
    input_b = document.querySelector("#b")
    a = input_a.value
    b = input_b.value
    output_div = document.querySelector("#output")
    output_div.innerText = a+b
