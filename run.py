# -*- coding: utf-8 -*-
from form.logo import LogoOne, LogoCero, LogoTwo
from colorama import Back, Fore, init
from tqdm import tqdm
import os
#iniciamos colores
from time import sleep
init()


def Carga():
    loop = tqdm(total=50000, position=0, leave=False)
    for k in range(50000):
        loop.set_description(Fore.BLUE + "Loading .....".format(k) + Fore.RESET)
        loop.update(1)
    loop.close()


def MenuInicial():
    os.system('clear')
    LogoCero()
    sleep(0.7)
    os.system('clear')
    sleep(0.3)
    LogoCero()
    sleep(0.3)
    os.system('clear')
    sleep(0.3)
    LogoOne()
    sleep(0.3)
    os.system('clear')
    sleep(0.3)
    LogoCero()
    sleep(1.5)
    sleep(0.60)
    Carga()
    print(Fore.GREEN + "\t\tBienvenido a Check Mail BY OPERS LINUX\t\t")
    print("\t\t__________________________\t\t")


def main():
    MenuInicial()
    try:
        txt = open("div.txt", "r")
        for i, linea in enumerate(txt):

            #print("La Linea seleccionada es: ", linea)
            #print("La enumeracion es: ", i)
            print("{} [ {} + {} ] {} < Correo numero: > {}".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.RESET) + str(i))
            dividir = linea.split(">> ")
            print(dividir[1])
            f = open("list.txt", "a")
            f.write(dividir[1])
            f.close()

    except NameError:
        LogoTwo()
        print("Hay un caracter mal en el archivo")
    except IOError:
        LogoTwo()
        print("Coloque el archivo txt llamado div con nombres y correos")
    except IndexError:
        
        print("La linea no coincide con el acomodo que se requiere, revise el numero de linea en el archivo DIV")






if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
