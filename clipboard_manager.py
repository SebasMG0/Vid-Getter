import os
import time
import pyperclip

def copy_series():
    serie= []
    actual_str= pyperclip.paste()

    try:
        while True:
            current_clipboard = pyperclip.paste()
            
            if current_clipboard != actual_str:
                actual_str = current_clipboard
                serie.append(actual_str)

            time.sleep(1)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-"*63)
        
        print("\tSerie de copiado finalizada.")
        return serie