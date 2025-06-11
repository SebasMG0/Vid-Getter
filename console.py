import link_download
import clipboard_manager
import os

TITLE= """
**************************************************************
    
    ░█▀▄░█░█░█░░░█░░░█▀▀░▀█▀░░░█▀▀░█▀█░█░█░█▀▀░█▀▄
    ░█▀▄░█░█░█░░░█░░░█▀▀░░█░░░░▀▀█░█▀█░▀▄▀░█▀▀░█▀▄
    ░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░▀░░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀  

                                        by: @SebasMG0
**************************************************************"""

OPTIONS= """**************************************************************
    [1] - Pegar Enlace
    [2] - Serie de Copiado
    [3] - Salir
**************************************************************"""

MSG=""
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n".join([TITLE, OPTIONS]))

    try:
        option = int(input("Seleccione una opción: "))
        if option == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pegue el enlace de YouTube:")

            downloaded_title= link_download.download_m4a(input("Enlace: ").strip())

            print("\t¡Descarga completada!\n")
            print("_"*63)
            
        elif option == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-"*80)
            print("\t¡Empiece a copiar enlaces de YouTube!")
            print("\tPresione Ctrl+C dentro de la aplicación para detener el proceso.")
            print("-"*80)

            serie = clipboard_manager.copy_series()
            link_download.download_serie(serie)
            print("_"*63)
            
        elif option == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-"*63)
            print("\tSaliendo del programa...")
            print("-"*63)
            break

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-"*63)
            print("\tOpción no válida, por favor intente de nuevo.")
            print("-"*63)

    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Entrada no válida, por favor ingrese un valor correcto número.")

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n\tSaliendo del programa...")
        break