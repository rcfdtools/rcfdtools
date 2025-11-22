import arrr
from pyscript import document


def translate_english(event):
    input_text_a= document.querySelector("#a")
    input_text_b= document.querySelector("#b")
    a = input_text.a
    b = input_text.b
    output_div = document.querySelector("#output")
    output_div.innerText = a+b
