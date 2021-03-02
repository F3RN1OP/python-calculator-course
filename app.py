from tkinter import *

# modulo parser permite tomar una expresion y empezar a ejecutarla o evaluarla
import parser

# instancia raiz de la app
root = Tk()

# titulo
root.title("Calculator")

# entrada de texto ubicado en la fila 1 que se extiende de oeste a este ocupando 6 columnas
# definicion
display = Entry(root)
# hubicacion en la grilla
display.grid(row=1, columnspan=6, sticky=W+E)

# acumulador para pintar digitos 1 al lado del otro
i = 0


####FUNCIONES####
# funcion para pintar numeros en el input
def get_numbers(n):
    # se declara como global por que no pertenece a esta funcion, y permita que se incremente
    global i
    # inserta 1 caracter en la pantalla 2 argumentos 1 indice, 2 caracter a pintar
    display.insert(i, n)
    i += 1

    # funcion para pintar operadores matematicos


def get_operations(operator):
    global i
    # obtiene la longuitud del operador
    operator_lenght = len(operator)
    display.insert(i, operator)
    i += operator_lenght

    # funcion para limpiar el input


def clear_display():
    # elimina todo 1 vueve al inicio, 2 declara el final en el indice 0
    display.delete(0, END)
    # funcion para eliminar caracteres del input


def undo():
    # obtiene el estado de la pantalla
    display_state = display.get()
    # si hay 1 elemto en la pantalla elimina el ultimo
    if len(display_state):
        # elimina el ultimo elemento de la pantalla
        display_new_state = display_state[:-1]
        # limpia la pantalla
        clear_display()
        # y pinta el nuevo estado en el indice 0
        display.insert(0, display_new_state)
    else:
        # limpia la pantalla
        clear_display()
        # inserta un texto de error en caso de que no haya nada
        display.insert(0, 'Error')


def calculate():
    # obtiene el estado de la pantalla
    display_state = display.get()
    # expresion para interpretar el contenido de la pantalla
    try:
        # se pasa a parser el estado de la pantalla para que lo interprete y devuelve una expresion matematica
        math_expression = parser.expr(display_state).compile()
        # evalua la expresion
        result = eval(math_expression)
        # limpia la pantalla
        clear_display()
        # y pinta el resultado
        display.insert(0, result)
    except expression as identifier:
        # en caso de haber una expresion erronea limpia la pantalla
        clear_display()
        # y muestra 1 error
        display.insert(0, 'Error')

# Numeric Buttons
    # command=lambda:get_numbers(1) define un evento y ejecuta la funcion get_numbers al recibir un click
Button(root, text="1", command=lambda: get_numbers(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: get_numbers(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: get_numbers(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda: get_numbers(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_numbers(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_numbers(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda: get_numbers(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_numbers(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_numbers(9)).grid(row=4, column=2)

Button(root, text="0", command=lambda: get_numbers(0)).grid(
    row=5, columnspan=2, sticky=W+E)

# Control Buttons
Button(root, text="AC", command=lambda: clear_display()).grid(row=2, column=5)
Button(root, text="⟵", command=lambda: undo()).grid(
    row=2, column=4, sticky=W+E)

# Basic operations buttons
Button(root, text="+", command=lambda: get_operations("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda: get_operations("-")
       ).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", command=lambda: get_operations("*")
       ).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", command=lambda: get_operations("/")
       ).grid(row=5, column=3, sticky=W+E)

# More operations buttons
Button(root, text="exp", command=lambda: get_operations(
    "**")).grid(row=3, column=4)
Button(root, text="^2", command=lambda: get_operations(
    "^2")).grid(row=3, column=5, sticky=W+E)

Button(root, text="(", command=lambda: get_operations(
    "(")).grid(row=4, column=4, sticky=W+E)
Button(root, text=")", command=lambda: get_operations(
    ")")).grid(row=4, column=5, sticky=W+E)

Button(root, text="=", command= lambda: calculate()).grid(row=5, column=4, sticky=W+E, columnspan=2)

Button(root, text="%", command=lambda: get_operations("%")).grid(row=5, column=2)

# al ejecutar inicia la aplicacion
root.mainloop()
