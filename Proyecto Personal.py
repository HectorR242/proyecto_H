from os import system
system('cls')

Precios = ["1800","1800","2000","2000","800","800","800","800","800","800","800","800","800","800","1500","800","1800","1800","2500","1500"]
Máquina_Expendedora = {"A1": "Papas Sabritas Sabor Pollo: Precio: " + Precios[0],"A2": "Papas Sabritas Sabor BBQ: Precio: 1800","A3": "Doritos Nacho: Precio: 2000","A4": "Doritos Diablo: Precio: 2000","A5": "Choclitos Limon: Precio: 800","A6": "Ponque Bimbo Chocoso: Precio: 800","A7": "Ponque Vainilla Bimbo: Precio: 800","A8": "Ponque Bimbo Submarino Arequipe: Precio: 800","A9": "Ponque Bimbo Chocolate: Precio: 800","A10": "Galleta Oreo: Precio: 800","A11": "Galleta Festiva Chocolate: Precio: 800","A12": "Galleta Festiva Vainilla: Precio: 800","A13": "Galleta Festiva Limon: Precio: 800","A14": "Galleta Festiva Recreo: Precio: 800","A15": "Festiva MiniChips: Precio: 1500","A16": "Galleta Festiva Vainilla: Precio: 800","A17": "Gaseosa Coca-Cola Personal: Precio: 1800","A18": "Gaseosa Pepsi Personal: Precio: 1800","A19": "Agua Cristal: Precio: 2500","A20": "PonyMalta: Precio: 1500"}


print("-----------------------------------------------------------------------------------------------------------------")
print("MAQUINA EXPENDEDORA:")
print("")
for Clave, Valor in Máquina_Expendedora.items():                                                                        
    print(Clave + ". " + Valor)
print("")
print("-----------------------------------------------------------------------------------------------------------------")


def Menu():
    print("Selecciones Del Menu \n\t 1. Opciones\n\t 2. Precios")
    print("-----------------------------------------------------------------------------------------------------------------")
    Menu = input("Seleccione Menu: ")
    if Menu=="1":
        Opciones()
    elif Menu=="2":
        Precio()

def Opciones():
    Opciones = input("Ingrese su producto: ")
    if Máquina_Expendedora.get(Opciones):
        print("-----------------------------------------------------------------------------------------------------------------")
        print(Máquina_Expendedora[Opciones])
        Precio = 1800
        Pago= int(input("Ingrese su pago: "))
        print("-----------------------------------------------------------------------------------------------------------------")
        if Pago >= Precio:
            print("El cambio es: $",Pago - Precio)
        else:
            print("Te falta $",Precio-Pago,"no puedes hacer la compra")
    else:
        print("Error")

def Precio():
    Cambio = input("Que precio desear cambiar: ")
    Posicion = int(input("Elija la posicion del precio: "))
    Precios[Posicion] = Cambio


Menu()