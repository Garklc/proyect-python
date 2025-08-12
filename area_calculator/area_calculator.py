
import math

def calculate_area(shape, *args):
    if shape.lower() == 'circle':
        radius = args[0]
        return math.pi * radius ** 2
    elif shape.lower() == 'rectangle':
        length, width = args
        return length * width
    elif shape.lower() == 'triangle':
        base, height = args
        return 0.5 * base * height
    else:
        return "Figura no soportada"

if __name__ == "__main__":
    print("Calculadora de Áreas")
    print("1. Círculo")
    print("2. Rectángulo")
    print("3. Triángulo")
    choice = input("Elige una figura: ")

    if choice == '1':
        radius = float(input("Ingresa el radio: "))
        area = calculate_area('circle', radius)
        print(f"Área del círculo: {area}")
    elif choice == '2':
        length = float(input("Ingresa el largo: "))
        width = float(input("Ingresa el ancho: "))
        area = calculate_area('rectangle', length, width)
        print(f"Área del rectángulo: {area}")
    elif choice == '3':
        base = float(input("Ingresa la base: "))
        height = float(input("Ingresa la altura: "))
        area = calculate_area('triangle', base, height)
        print(f"Área del triángulo: {area}")
    else:
        print("Figura no válida")
