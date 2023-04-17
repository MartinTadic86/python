import random

if not filename:
    print("Název souboru musí být zadaný.")
    exit()

text = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Pellentesque vitae lectus in mauris sollicitudin ornare.",
        "Quisque sed augue sit amet odio ullamcorper efficitur.",
        "Vivamus interdum, libero sed vehicula ullamcorper, massa velit suscipit magna, vel molestie est erat id nunc.",
        "Fusce eget ex id nisl pretium lacinia a a augue."]

try:
    with open(filename, "w") as file:
        for i in range(5):
            file.write(random.choice(text) + "\n")

except OSError as error:
    print("Nepodařilo se vytvořit soubor:", error)
    exit()

except Exception as error:
    print("Nastala neočekávaná chyba:", error)
    exit()

print("Soubor byl úspěšně vytvořen a zaplněn náhodnými řádky textu.")
