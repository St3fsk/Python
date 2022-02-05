import json

aStudenten = '[{"voornaam":"Floris", "achternaam":"Ruysdaal"}, {"voornaam":"Julia", "achternaam":"Gomez"}, {"voornaam":"Anusha", "achternaam":"Verberge"}]'
data_Studenten = json.loads(aStudenten)

data_Studenten[0]["eerstestudiejaar"] = "2019"
data_Studenten[0]["vakken"] = "Natuurkunde, Scheikunde"
data_Studenten[1]["vakken"] = "Nederlands"
data_Studenten[2]["vakken"] = "Russische, Chinees"

print(data_Studenten)
print()
name = input("Enter name: ")

for student in data_Studenten:

    if student["voornaam"] == name:

        print()

        try:

            print("Voornaam: ", student["voornaam"])
            print("Achternaam: ", student["achternaam"])
            print("Eerste studiejaar: ", student["eerstestudiejaar"])
            print("Vakken: ", student["vakken"])

        except:

            print("Vakken: ", student["vakken"])