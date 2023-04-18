from os import system
system('cls')

Máquina_Expendedora = {"A1": "Papas Sabritas Sabor Pollo: Precio: 1800","A2": "Papas Sabritas Sabor BBQ: Precio: 1800","A3": "Doritos Nacho: Precio: 2000","A4": "Doritos Diablo: Precio: 2000","A5": "Choclitos Limon: Precio: 800","A6": "Ponque Bimbo Chocoso: Precio: 800","A7": "Ponque Vainilla Bimbo: Precio: 800","A8": "Ponque Bimbo Submarino Arequipe: Precio: 800","A9": "Ponque Bimbo Chocolate: Precio: 800","A10": "Galleta Oreo: Precio: 800","A11": "Galleta Festiva Chocolate: Precio: 800","A12": "Galleta Festiva Vainilla: Precio: 800","A13": "Galleta Festiva Limon: Precio: 800","A14": "Galleta Festiva Recreo: Precio: 800","A15": "Festiva MiniChips: Precio: 1500","A16": "Galleta Festiva Vainilla: Precio: 800","A17": "Gaseosa Coca-Cola Personal: Precio: 1800","A18": "Gaseosa Pepsi Personal: Precio: 1800","A19": "Agua Cristal: Precio: 2500","A20": "PonyMalta: Precio: 1500"}

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
    Menu=input("Seleccione Menu: ")
    if Menu=="1":
        Maquina()
    elif Menu=="2":
        print()

def Maquina():
    Opciones=input("Ingrese su producto: ").upper()
    for Clave in Máquina_Expendedora:
        if Opciones == Clave:
            print("-----------------------------------------------------------------------------------------------------------------")
            print(Máquina_Expendedora[Opciones])
            Precio = 1800
            Pago= int(input("Ingrese su pago: "))
            print("-----------------------------------------------------------------------------------------------------------------")
            if Pago >= Precio:
                print("El cambio es: $",Pago - Precio)
            else:
                print("Te falta $",Precio-Pago,"no puedes hacer la compra")
      
Menu()
