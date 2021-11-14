import PySimpleGUI as sg

sg.Window(title="Hello World", layout=[[]], margins=(300, 500)).read()

lol = input("What do you want to do?")

if lol == "add":
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    sum = a + b
    print("sum:", sum)
    
if lol == "minus":
    aminus = int(input("enter first number: "))
    bminus = int(input("enter second number: "))
    summinus = aminus - bminus
    print("sum:", summinus)

if lol == "multiply":
    amul = int(input("enter first number: "))
    bmul = int(input("enter second number: "))
    summul = amul * bmul
    print("sum:", summul)

if lol == "division":
    adiv = int(input("enter first number: "))
    bdiv = int(input("enter second number: "))
    sumdiv = adiv / bdiv
    print("sum:", sumdiv)
