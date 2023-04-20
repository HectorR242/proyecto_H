from os import system
system('cls')

Precios = ["3800","1800","2000","2000","800","800","800","800","800","800","800","800","800","800","1500","800","1800","1800","2500","1500"]
CopiaH = {"A1":3800,"A2": 1800,"A3": 2000,"A4": 2000,"A5": 800,"A6": 800,"A7": 800,"A8": 800,"A9": 800,"A10": 800,"A11": 800,"A12": 800,"A13": 800,"A14": 800,"A15": 1500,"A16": 800,"A17": 1800,"A18": 1800,"A19": 2500,"A20": 1500}
CopiaR = {"A1":"3800","A2": "1800","A3": "2000","A4": "2000","A5": "800","A6": "800","A7": "800","A8": "800","A9": "800","A10": "800","A11": "800","A12": "800","A13": "800","A14": "800","A15": "1500","A16": "800","A17": "1800","A18": "1800","A19": "2500","A20": "1500"}
Máquina_Expendedora = {"A1": "Papas Sabritas Sabor Pollo: Precio: " ,"A2": "Papas Sabritas Sabor BBQ: Precio: ","A3": "Doritos Nacho: Precio: ","A4": "Doritos Diablo: Precio: ","A5": "Choclitos Limon: Precio: ","A6": "Ponque Bimbo Chocoso: Precio: ","A7": "Ponque Vainilla Bimbo: Precio: ","A8": "Ponque Bimbo Submarino Arequipe: Precio: ","A9": "Ponque Bimbo Chocolate: Precio: ","A10": "Galleta Oreo: Precio: ","A11": "Galleta Festiva Chocolate: Precio: ","A12": "Galleta Festiva Vainilla: Precio: ","A13": "Galleta Festiva Limon: Precio: ","A14": "Galleta Festiva Recreo: Precio: ","A15": "Festiva MiniChips: Precio: ","A16": "Galleta Festiva Vainilla: Precio: ","A17": "Gaseosa Coca-Cola Personal: Precio: ","A18": "Gaseosa Pepsi Personal: Precio: ","A19": "Agua Cristal: Precio: ","A20": "PonyMalta: Precio: "}

def Opciones1():
        print("-----------------------------------------------------------------------------------------------------------------")
        print("MAQUINA EXPENDEDORA:")
        print("")
        Num=0
        for Clave, Productos in Máquina_Expendedora.items():
            print(Clave + ". " + Productos +" "+ Precios[Num])
            Num=Num+1    
        print("")
        print("-----------------------------------------------------------------------------------------------------------------")
        
        Opciones = input("Ingrese su producto: ").upper()

        if Máquina_Expendedora.get(Opciones):
            print("-----------------------------------------------------------------------------------------------------------------")
            print(Máquina_Expendedora[Opciones])
            Pago= int(input("Ingrese su pago: "))
            Precio=CopiaH[Opciones]
            print("-----------------------------------------------------------------------------------------------------------------")
            if Pago >= Precio:
                print("El cambio es: $",Pago - Precio)
            else:
                print("Te falta $",Precio-Pago,"no puedes hacer la compra")
        else:
            print("Error")

def Precio():
    print("-----------------------------------------------------------------------------------------------------------------")
    Posiciones=["A1=0","A2=1","A3=2","A4=3","A5=4","A6=5","A7=6","A8=7","A9=8","A10=9","A11=10","A12=11","A13=12","A14=13","A15=14","A16=15","A17=16","A18=17","A19=18","A20=19"]
    for i in Posiciones:
        print(i)
    print("-----------------------------------------------------------------------------------------------------------------")
    Posicion=int(input("Seleccione el numero del producto: "))
    Posicion1 = input("Seleccion el codigo del producto: ")
    Cambio = int(input("Coloquere el precio: "))
    Cambio2 = input("Coloquere el precio: ")
    Precios[Posicion]=Cambio2
    CopiaH[Posicion1]=Cambio
    Opciones1()


def Menu():
    while True:
        print("Selecciones Del Menu \n\t 1. Opciones\n\t 2. Precios")
        print("-----------------------------------------------------------------------------------------------------------------")
        Menu1 = input("Seleccione Menu: ")
        if Menu1=="1":
            Opciones1()
        elif Menu1=="2":
            Precio()  

Menu()
 
 

 