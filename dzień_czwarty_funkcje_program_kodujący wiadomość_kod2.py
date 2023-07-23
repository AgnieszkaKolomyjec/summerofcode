
# - wymyśl własny algorytm kodujący (możesz skorzystać z istniejących np. klasyczne/harcerskie)
#bez polskich znaków

def coded_message(message):
    cypher = ""
    code = {
        "A": "5",
        "B": "%",
        "C": "6",
        "D": "^",
        "E": "7",
        "F": "&",
        "G": "8",
        "H": "*",
        "I": "9",
        "J": "(",
        "K": "0",
        "L": ")",
        "M": "1",
        "N": "!",
        "O": "2",
        "P": "@",
        "R": "3",
        "S": "#",
        "T": "4",
        "U": "$",
        "W": "<",
        "X": ">",
        "Y": "?",
        "Z": "+",
        " ": "-",
      }
    for i in range(len(message)):
        cypher += code[(message[i])]
    return cypher

message = (input('Podaj wiadomość, którą chcesz zakodować:')).upper()
message_2= coded_message(message)
print(f"Twoja zakodowana wiadomość to {message_2}")

