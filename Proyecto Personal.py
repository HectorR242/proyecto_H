from os import system
system('cls')
import time

Usuario = {"1": "242"}
Contraseña = {"2": 2427}
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
            ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅\n\t    █ 1. Productos      █\n\t    █ 2. Configuracion █\n\t    █ 3. Apagar        █
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
                Verificacion()
            elif Menu1==3:
                print("Apagando...")
                time.sleep(2)
                system("cls")
                exit()
            else:
                print("Error, opcion incorrecta")
                print("Intentalo De Nuevo")
                time.sleep(3)
                system("cls")
                print("-----------------------------------------------------------------------------------------------------------------")
        except ValueError:
            print("-----------------------------------------------------------------------------------------------------------------")
            print("Error, el dato solo puede ser tipo numerico ✘")
            print("Intentalo De Nuevo")
            time.sleep(3)
            system("cls")
            print("-----------------------------------------------------------------------------------------------------------------")

def Verificacion():
    Contador=0
    while True:
        try:
            print("Antes de acceder a la configuración, confirme que es el propietario de la máquina.")
            Usuario1 = input("Digite su usuario: ")
            Contraseña1 = int(input("Digite su contraseña: "))
            if Usuario1 == Usuario["1"] and Contraseña1 == Contraseña["2"]:
                Configuracion()
            else:
                print("El nombre de usuario o la contraseña son incorrectos")
                Contador+=1
                print("Intentos disponibles: 3")
                print(Contador)
                time.sleep(3)
                system("cls")
                if Contador==3:
                    print("-----------------------------------------------------------------------------------------------------------------")
                    return Menu()
                else:
                    print("")
        except ValueError:
            print("El nombre de usuario o la contraseña son incorrectos")
            Contador+=1
            print("Intentos disponibles: 3")
            print(Contador)
            time.sleep(3)
            system("cls")
            if Contador==3:
                print("-----------------------------------------------------------------------------------------------------------------")
                return Menu()
            else:
                print("")
    
def Administrador():
    while True:
        Verificacion=int(input("Confirmar la contraseña actual: "))
        if Verificacion == Contraseña["2"]:
            UsuarioN=input("Ingrese su nuevo nombre de usuario: ")
            Nueva=int(input("Ingrese su nueva contraseña: "))
            Usuario["1"]=UsuarioN
            Contraseña["2"]=Nueva
            print("Su nombre de usuario y su contraseña a sido cambiada exictosamente")   
            break
        else: 
            print("Error, contraseña incorrecta")
            Contador+=1
            print("Intentos disponibles: 3")
            print(Contador)
            if Contador==3:
                print("-----------------------------------------------------------------------------------------------------------------")
                return Menu()
            else:
                print("")

def Opciones():
    Contador=0
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
            print("Cargando, Por Favor Espere....")
            time.sleep(2)
            system("cls")     
        except ValueError:
            print("-----------------------------------------------------------------------------------------------------------------")
            print("Error, el dato solo puede ser tipo numerico ✘")
            print("Intentalo De Nuevo")
        else:
            if Máquina_Expendedora.get(Productos):
                print("-----------------------------------------------------------------------------------------------------------------")
                print(Máquina_Expendedora[Productos]+CopiaM[Productos])
                Pago = int(input("Ingrese su pago: "))
                Precio = CopiaP[Productos]
                print("-----------------------------------------------------------------------------------------------------------------")
                if Pago >= Precio:
                    print("El cambio es: $",Pago - Precio)
                    print("Su compra ha sido un éxito, por favor recoja su producto en la bandeja de la máquina.")
                    time.sleep(3)
                    system("cls")
                else:
                    print("Te falta $",Precio-Pago,"no puedes hacer la compra")
            else:
                print("Error, producto no encontrado")
                Contador+=1
                print("Intentos disponibles: 3")
                print(Contador)
                print("-----------------------------------------------------------------------------------------------------------------")
                if Contador==3:
                    time.sleep(3)
                    return Menu()
                    print("-----------------------------------------------------------------------------------------------------------------")
                else:
                    print("")
            print("-----------------------------------------------------------------------------------------------------------------")

def Configuracion():
    Contador=0
    while True:
        try:
            print("-----------------------------------------------------------------------------------------------------------------")
            print("*****CONFIGURACION DE LA MAQUINA*****")
            print("Seleccione Menu:")
            print("""\n\t 1.Cambiar Productos\n\t 2.Cambiar Precios\n\t 3.Agregar\n\t 4.Cambiar administrador\n\t 5.Salir
            """)
            Opciones = int(input("Seleccione: "))
            if Opciones==1:
                Producto()
            elif Opciones==2:
                Precio()
            elif Opciones==3:
                Añadir()
            elif Opciones==4:
                Administrador()
            elif Opciones==5:
                system("cls")
                return Menu()
        except ValueError:
            print("Error, el dato solo puede ser tipo numerico ✘")
            Contador+=1
            print("Intentos disponibles: 3")
            print(Contador)
            if Contador==3:
                print("-----------------------------------------------------------------------------------------------------------------")
                return Menu()
            else:
                print("")

def Producto():
    Contador=0
    while True:
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Seleccione el código del producto y luego agregue el nombre que desea cambiar correspondiente al producto que eligió: ")
        print("Ejemplo: \n\t 1.Codigo = A1 ✔ \n\t 2.Nombre = Galletas Noel ✔ ")
        print("-----------------------------------------------------------------------------------------------------------------")
        Posiciones=["A1=0","A2=1","A3=2","A4=3","A5=4","A6=5","A7=6","A8=7","A9=8","A10=9","A11=10","A12=11","A13=12","A14=13","A15=14","A16=15","A17=16","A18=17","A19=18","A20=19","B21=20","B22=21","B23=22","B24=23","B25=24","B26=25","B27=26","B28=27","B29=28","B30=29","B31=30","B32=31","B33=32","B34=33","B35=34","B36=35","B37=36","B38=37","B39=38","B40=39"]
        print("Lista De Los Codigos: ")
        for i in Posiciones:
            print("————————————————")
            print("⌨  "+"Codigo:"+i)
            print("————————————————")
        print("-----------------------------------------------------------------------------------------------------------------")
        Codigo = input("Digite el codigo del producto: ")
        if Máquina_Expendedora.get(Codigo):
            Cambio = input("Nombre su producto: ")
            if Cambio.isalnum()== False:    
                Máquina_Expendedora[Codigo] = Cambio + ":" + " Precio: "
                Opciones()
            else:
                print("Error, el dato solo puede ser tipo texto ✘")
                Contador+=1
                print("Intentos disponibles: 3")
                print(Contador)
                if Contador==3:
                    print("-----------------------------------------------------------------------------------------------------------------")
                    return Menu()
                else:
                    print("")
        else:
            print("Error, la clave no existe")
            Contador+=1
            print("Intentos disponibles: 3")
            print(Contador)
            if Contador==3:
                print("-----------------------------------------------------------------------------------------------------------------")
                return Menu()
            else:
                print("")

def Precio():
    Contador=0
    while True:
        try:
            print("-----------------------------------------------------------------------------------------------------------------")
            print("Seleccione el codigo del producto y agregue su numero correspondiente para hacer el cambio del precio: ")
            print("Ejemplo: \n\t 1.Codigo = A1 ✔ \n\t 2.Numero = 0 ✔ ")
            print("-----------------------------------------------------------------------------------------------------------------")
            Posiciones=["A1=0","A2=1","A3=2","A4=3","A5=4","A6=5","A7=6","A8=7","A9=8","A10=9","A11=10","A12=11","A13=12","A14=13","A15=14","A16=15","A17=16","A18=17","A19=18","A20=19","B21=20","B22=21","B23=22","B24=23","B25=24","B26=25","B27=26","B28=27","B29=28","B30=29","B31=30","B32=31","B33=32","B34=33","B35=34","B36=35","B37=36","B38=37","B39=38","B40=39"]
            print("Lista De Los Codigos: ")
            for i in Posiciones:
                print("————————————————")
                print("⌨  "+"Codigo:"+i)
                print("————————————————")
            print("-----------------------------------------------------------------------------------------------------------------")
            Codigo = input("Digite el codigo del producto: ")
            if Máquina_Expendedora.get(Codigo):
                Codigo2 =int(input("Digite el numero del producto: "))
                Cambio = int(input("Coloquere el precio: "))
                Cambio2 = input("Coloquere el precio: ")
                if Cambio2.isalpha()== False:
                    Precios[Codigo2]=Cambio2
                    CopiaP[Codigo]=Cambio
                    CopiaM[Codigo]=Cambio2
                    Opciones()
                else:
                    print("Error, el dato solo puede ser tipo numerico ✘")
                    Contador+=1
                    print("Intentos disponibles: 3")
                    print(Contador)
                    if Contador==3:
                        print("-----------------------------------------------------------------------------------------------------------------")
                        return Menu()
                    else:
                        print("")
            else:
                print("Error, la clave no existe")
                Contador+=1
                print("Intentos disponibles: 3")
                print(Contador)
                if Contador==3:
                    print("-----------------------------------------------------------------------------------------------------------------")
                    return Menu()
                else:
                    print("")
        except ValueError:
            print("Error, el dato solo puede ser tipo numerico ✘")
            Contador+=1
            print("Intentos disponibles: 3")
            print(Contador)
            if Contador==3:
                print("-----------------------------------------------------------------------------------------------------------------")
                return Menu()
            else:
                print("")

def Añadir():
    Contador=0
    while True:
        try:
            print("-----------------------------------------------------------------------------------------------------------------")
            print("Añade el nuevo código de producto y su nombre y precio correspondiente.")
            print("Ejemplo: \n\t 1.Codigo = A1 ✔ \n\t 2.Precio = 1500 ✔ ")
            print("-----------------------------------------------------------------------------------------------------------------")
            Posiciones=["A1=0","A2=1","A3=2","A4=3","A5=4","A6=5","A7=6","A8=7","A9=8","A10=9","A11=10","A12=11","A13=12","A14=13","A15=14","A16=15","A17=16","A18=17","A19=18","A20=19","B21=20","B22=21","B23=22","B24=23","B25=24","B26=25","B27=26","B28=27","B29=28","B30=29","B31=30","B32=31","B33=32","B34=33","B35=34","B36=35","B37=36","B38=37","B39=38","B40=39"]
            print("Solo puedes añadir codigos que sean diferentes de los ya disponibles")
            print("Lista De Los Codigos Actuales: ")
            for i in Posiciones:
                print("————————————————")
                print("⌨  "+"Codigo:"+i)
                print("————————————————")
            print("-----------------------------------------------------------------------------------------------------------------")
            Agregar = input("Agregue el nuevo codigo: ")
            Num4=0
            for Clave1, Objeto1 in Máquina_Expendedora.items():
                Num5=Num4+1    
                if Agregar == Clave1:
                    print("Error, el codigo introducido ya se encuentra en uso")
                    time.sleep(3)
                    system("cls")
                    Añadir()
        except ValueError:
            print("Error, el dato solo puede ser tipo numerico ✘")
            Contador+=1
            print("Intentos disponibles: 3")
            print(Contador)
            if Contador==3:
                print("-----------------------------------------------------------------------------------------------------------------")
                return Menu()
            else:
                print("")
        else:
            Cambio = input("Agregue su nuevo producto: ")
            Cambio2 = input("Agregue el precio del producto: ")
            Cambio3 = int(input("Verifique nuevamente el precio: "))
            Máquina_Expendedora[Agregar]=Cambio + ":" + " Precio: "
            Precios.append(Cambio2)
            CopiaP[Agregar]=Cambio3
            CopiaM[Agregar]=Cambio2
            Opciones()     

if __name__ == "__main__":
    Menu()