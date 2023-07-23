#Zakoduj tajną wiadomość

# PYTHON JEST SUPER

# - stwórz plik zaawierający algorytm, który zmieni powyższą wiadomość w ciąg ”RZUIPO-KFTU-TWRFS”
#algorytm nie uwzględnia polskich znaków

def coded_message(message):
    cypher = ""
    code = {
        "A": "B",
        "B": "C",
        "C": "D",
        "D": "E",
        "E": "F",
        "F": "G",
        "G": "H",
        "H": "I",
        "I": "J",
        "J": "K",
        "K": "L",
        "L": "M",
        "M": "N",
        "N": "O",
        "O": "P",
        "P": "R",
        "R": "S",
        "S": "T",
        "T": "U",
        "U": "W",
        "W": "X",
        "X": "Y",
        "Y": "Z",
        "Z": "A",
        " ": "-",
      }
    for i in range(len(message)):
        cypher += code[(message[i])]
    return cypher

message = (input('Podaj wiadomość, którą chcesz zakodować:')).upper()
message_2= coded_message(message)
print(f"Twoja zakodowana wiadomość to {message_2}")

