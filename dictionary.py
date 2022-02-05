temp = {"BR1097":14, "BR2564":17}

locatie = input(str("Type de locatie van de sensor: "))

if locatie in temp:
    print("Locatie:", input, "Temperatuur:", temp[input])

else:
    print("Locatie unknown")

    answer = input(str("Wil je deze locatie opslaan? (ja of nee): "))

    if answer == "ja":

        temp[locatie] = 0
        print("Sluit alsjeblieft de sensor aan!")
        print(temp)

    else:
        pass
