from os import system
system('cls')
import time

UsuarioAdministrado = ["Hec242", 2427]
Máquina_Expendedora = {"A1": "Papas Sabritas Sabor Pollo: Precio: ","A2": "Papas Sabritas Sabor BBQ: Precio: ","A3": "Doritos Nacho: Precio: ","A4": "Doritos Diablo: Precio: ","A5": "Choclitos Limon: Precio: ","A6": "Ponque Bimbo Chocoso: Precio: ","A7": "Ponque Vainilla Bimbo: Precio: ","A8": "Ponque Bimbo Submarino Arequipe: Precio: ","A9": "Ponque Bimbo Chocolate: Precio: ","A10": "Galleta Oreo: Precio: ","A11": "Galleta Festiva Chocolate: Precio: ","A12": "Galleta Festiva Vainilla: Precio: ","A13": "Galleta Festiva Limon: Precio: ","A14": "Galleta Festiva Recreo: Precio: ","A15": "Festiva MiniChips: Precio: ","A16": "Galleta Festiva Vainilla: Precio: ","A17": "Gaseosa Coca-Cola Personal: Precio: ","A18": "Gaseosa Pepsi Personal: Precio: ","A19": "Agua Cristal: Precio: ","A20": "PonyMalta: Precio: ","B21": "7UP: Precio: ","B22": "Fanta: Precio: ","B23": "Sprite: Precio: ","B24": "Tropical: Precio: ","B25": "Dr.Pepper: Precio: ","B26": "Postobon Manzana: Precio: ","B27": "Postobon Colombiana: Precio: ","B28": "Postobon Uva: Precio: ","B29": "Chocoramo: Precio: ","B30": "Chocoso: Precio: ","B31": "Bon Yurt Zucaritas: Precio: ","B32": "Bon Yurt Choco Crispis: Precio: ","B33": "Bon Yurt MiniChips: Precio: ","B34": "Bon Yurt Froot Loopso: Precio: ","B35": "Leche Alpina Chocolate: Precio: ","B36": "Leche Alpina Vainilla: Precio: ","B37": "Leche Alpina Fresa: Precio: ","B38": "DeTodito Paketon Original: Precio: ","B39": "DeTodito Paketon BBQ: Precio: ","B40": "DeTodito Paketon Mix: Precio: "}
CopiaP = {"A1":3800,"A2": 1800,"A3": 2000,"A4": 2000,"A5": 800,"A6": 800,"A7": 800,"A8": 800,"A9": 800,"A10": 800,"A11": 800,"A12": 800,"A13": 800,"A14": 800,"A15": 1500,"A16": 800,"A17": 1800,"A18": 1800,"A19": 2500,"A20": 1500,"B21": 1800,"B22": 2000,"B23": 1800,"B24": 1500,"B25": 2000,"B26": 1800,"B27": 1800,"B28": 1800,"B29": 2500,"B30": 2300,"B31": 3500,"B32": 3500,"B33": 3500,"B34": 3500,"B35": 2500,"B36": 2500,"B37": 2500,"B38": 6500,"B39": 6500,"B40": 6500}
CopiaM = {"A1":"3800","A2": "1800","A3": "2000","A4": "2000","A5": "800","A6": "800","A7": "800","A8": "800","A9": "800","A10": "800","A11": "800","A12": "800","A13": "800","A14": "800","A15": "1500","A16": "800","A17": "1800","A18": "1800","A19": "2500","A20": "1500","B21": "1800","B22": "2000","B23": "1800","B24": "1500","B25": "2000","B26": "1800","B27": "1800","B28": "1800","B29": "2500","B30": "2300","B31": "3500","B32": "3500","B33": "3500","B34": "3500","B35": "2500","B36": "2500","B37": "2500","B38": "6500","B39": "6500","B40": "6500"}
Precios = ["3800","1800","2000","2000","800","800","800","800","800","800","800","800","800","800","1500","800","1800","1800","2500","1500","1800","2000","1800","1500","2000","1800","1800","1800","2500","2300","3500","3500","3500","3500","2500","2500","2500","6500","6500","6500"]

def Menu():
    while True:
        try:
            print("                  ***MAQUINA EXPENDEDORA***")
            print("""
            ████████████████████████████████████ 
            █    Súper Expendedor   █          █
            █████████████████████████          █
            █[A1]  [A2]  [A3]   [A4]█          █
            █[A5]  [A6]  [A7]   [A8]█          █
            █[A9]  [A10] [A11] [A12]█          █
            █[A13] [A14] [A15] [A16]█  ██████  █
            █[A17] [A18] [A19] [A20]█          █
            █[B21] [B22] [B23] [B24]█ * * * *  █           
            █[B25] [B26] [B27] [B28]█ * * * *  █
            █[B29] [B30] [B31] [B32]█ * * * *  █
            █[B33] [B34] [B35] [B36]█ * * * *  █
            █[B37] [B38] [B39] [B40]█          █
            █████████████████████████          █
            █                       █          █
            █     █████████████     █          █
            █     █           █     █          █
            █     █████████████     █          █
            █                       █          █                             
            ████████████████████████████████████ 
            """)
            print("-----------------------------------------------------------------------------------------------------------------")
            print("""Selecciones Del Menu:
            ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅\n\t    █ 1. Opciones      █\n\t    █ 2. Configuracion █\n\t    █ 3. Apagar        █
            ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
            """)
            print("""
            ███████████████████
            █ [1] [2] [3] [↑] █
            █ [4] [5] [6] [↓] █
            █ [7] [8] [9] [→] █
            █ [A] [0] [B] [←] █
            ███████████████████
            """)
            print("-----------------------------------------------------------------------------------------------------------------")
            Menu1 = int(input("Elija una opcion: "))
            if Menu1==1:
                print("Cargando, Por Favor Espere....")
                time.sleep(2)
                system("cls")
                Opciones()
            elif Menu1==2:
                print("Cargando, Por Favor Espere....")
                time.sleep(2)
                system("cls")
                Seguridad()
            elif Menu1==3:
                print("Apagando...")
                time.sleep(2)
                system("cls")
                exit()
        except ValueError:
            print("-----------------------------------------------------------------------------------------------------------------")
            print("Error, el dato solo puede ser tipo numerico ✘")
            print("Intentalo De Nuevo")
            print("-----------------------------------------------------------------------------------------------------------------")

def validar_usuario(Admin_Lista:list):
    Admin = False
    print("Antes de acceder a la configuración, confirme que es el propietario de la máquina.")
    Usuario = input("Digite su usuario: ")
    Contraseña = int(input("Digite su contraseña: "))
    if Usuario in Admin_Lista:
        if Contraseña == Admin_Lista[1]:
            Admin = True
            return Admin, 1
        else:
            return Admin, 1
    return False, 0

def Seguridad():
    while (True):
        UsuarioDefinido, Roles = validar_usuario(UsuarioAdministrado)
        if UsuarioDefinido == True and Roles == 1:
            Configuracion()
        else:
            print ("Los datos no pudieron ser comprobados")

def Opciones():
    while True:
        try:
            print("-----------------------------------------------------------------------------------------------------------------")
            print("***PRODUCTOS DISPONIBLES***")
            print("")
            Num=0
            for Clave, Productos in Máquina_Expendedora.items():
                print(Clave + ". " + Productos +" "+ Precios[Num])
                Num=Num+1    
            print("")
            print("-----------------------------------------------------------------------------------------------------------------")

            Productos = input("Ingrese su producto: ").upper()

            if Máquina_Expendedora.get(Productos):
                print("-----------------------------------------------------------------------------------------------------------------")
                print(Máquina_Expendedora[Productos]+CopiaM[Productos])
                Pago = int(input("Ingrese su pago: "))
                Precio = CopiaP[Productos]
                print("-----------------------------------------------------------------------------------------------------------------")
                if Pago >= Precio:
                    print("El cambio es: $",Pago - Precio)
                    print("Su compra ha sido un éxito, por favor recoja su producto en la bandeja de la máquina.")
                else:
                    print("Te falta $",Precio-Pago,"no puedes hacer la compra")
            else:
                print("Error")
            print("-----------------------------------------------------------------------------------------------------------------")
            return Menu()

        except ValueError:
            print("-----------------------------------------------------------------------------------------------------------------")
            print("Error, el dato solo puede ser tipo numerico ✘")
            print("Intentalo De Nuevo")

def Configuracion():
    print("-----------------------------------------------------------------------------------------------------------------")
    print("*****CONFIGURACION DE LA MAQUINA*****")
    print("Seleccione Menu:")
    print("""\n\t 1.Cambiar Productos\n\t 2.Cambiar Precios\n\t 3.Temperatura\n\t 4.Salir
    """)
    Opciones = input("Seleccione: ")
    if Opciones=="1":
        Producto()
    elif Opciones=="2":
        Precio()

def Producto():
    while True:
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Seleccione el código del producto y luego agregue el nombre que desea cambiar correspondiente al producto que eligió: ")
        print("Ejemplo: \n\t 1.Codigo = A1 ✔ \n\t 2.Nombre = Galletas Noel ✔ ")
        print("-----------------------------------------------------------------------------------------------------------------")
        Posiciones=["A1=0","A2=1","A3=2","A4=3","A5=4","A6=5","A7=6","A8=7","A9=8","A10=9","A11=10","A12=11","A13=12","A14=13","A15=14","A16=15","A17=16","A18=17","A19=18","A20=19"]
        print("Lista De Los Codigos: ")
        for i in Posiciones:
            print("————————————————")
            print("⌨  "+"Codigo:"+i)
            print("————————————————")
        print("-----------------------------------------------------------------------------------------------------------------")
        Codigo = input("Digite el codigo del producto: ")
        Cambio = input("Nombre su producto: ")
        Máquina_Expendedora[Codigo] = Cambio + ":" + " Precio: "
        Opciones()

def Precio():
    while True:
        try:
            print("-----------------------------------------------------------------------------------------------------------------")
            print("Seleccione el codigo del producto y agregue su numero correspondiente para hacer el cambio del precio: ")
            print("Ejemplo: \n\t 1.Codigo = A1 ✔ \n\t 2.Numero = 0 ✔ ")
            print("-----------------------------------------------------------------------------------------------------------------")
            Posiciones=["A1=0","A2=1","A3=2","A4=3","A5=4","A6=5","A7=6","A8=7","A9=8","A10=9","A11=10","A12=11","A13=12","A14=13","A15=14","A16=15","A17=16","A18=17","A19=18","A20=19"]
            print("Lista De Los Codigos: ")
            for i in Posiciones:
                print("————————————————")
                print("⌨  "+"Codigo:"+i)
                print("————————————————")
            print("-----------------------------------------------------------------------------------------------------------------")
            Codigo = input("Digite el codigo del producto: ")
            if Codigo == Máquina_Expendedora:
                Codigo2 =int(input("Digite el numero del producto: "))
                Cambio = int(input("Coloquere el precio: "))
                Cambio2 = input("Coloquere el precio: ")
                Precios[Codigo2]=Cambio2
                CopiaP[Codigo]=Cambio
                CopiaM[Codigo]=Cambio2
                Opciones()
        except KeyError(Máquina_Expendedora):
            print("Error, el dato solo puede ser tipo numerico ✘")
            print("Intentalo De Nuevo")

def Temperatura():
    pass

if __name__ == "__main__":
    Precio()

 



