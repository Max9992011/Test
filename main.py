# Создать программу которая берет любой текстовый инпут и переделывает текст в код Морза

#функция которая содержит азбуку морезе

MorseCode= {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.','Q': '--.-', 'R': '.-.', 'S': '...',
'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-','Y': '-.--', 'Z': '--..'}

#функция которая создаёт инпут

user_input = input("Введите текст для перевода в азбуку Морзе: ")
