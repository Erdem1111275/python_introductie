# populaire games

# List of Games
games = ["Player’s Unknown Battle Ground (PUBG) 50 Million 2018",
                 "Fortnite Battle Royale 39 Million 2017",
                 "Apex Legends 50 Million (1 Month) 2019",
                 "Leauge of Legends (LOL) 27 Million 2009",
                 "Counter Strike; Global Offensive 32 Million 2014",
                 "Heartstone 29 Million 20120",
                 "Minecraft 91 Million 2011",
                 "DOTA 2 5 million 2015",
                 "The Division 2 N/A 2019",
                 "The Splatoon 2"]

print(f"{games}\n")

# a
print(f"5] {games[4]}")
print(f"{games}\n")

# b
dota = games[7]
chars_in_name = len(dota)
print(f"The game {dota} has {chars_in_name} characters.")
print(f"{games}\n")


# c
number_of_games = len(games)
print(f"Er zitten {number_of_games} games in de lijst.")
print(f"games\n")

# d
games.insert(1, "Snake")
print(f"games\n")

# e
index_of_splatoon = games.index("The Splatoon 2")
splatoon = games.pop(index_of_splatoon)
print(f"Helaas heeft de game {splatoon} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van {splatoon}.\n")

# f
index_of_heartstone = games.index("Heartstone 29 Million 20120")
games[index_of_heartstone] = "Heartstone 29 Million 2012"
print(games)


# computer leveranciers
suppliers = (   "Apple",
                "Asus",
                "Dell",
                "Lenovo",
                "Acer",
                "Samsung",
                "MSI",
                "Hewlett-Packard (HP)",
                "Toshiba",
                "Microsoft",
                "Chuwi",
                "Sony")

print(f"suppliers\n")

# a
number_of_suppliers = len(suppliers)
print(f"De tuple bevat {number_of_suppliers} computer leveranciers.")
print(f"suppliers\n")

# b
supplier = suppliers[7]
characters_in_name = len(supplier)
print(f"De naam van {supplier} bestaat uit {characters_in_name} karakters.\n")

# c
index_of_supplier = suppliers.index("Samsung")
print(f"De index van computer leverancier {suppliers[index_of_supplier]} is {index_of_supplier}.")


# Telefoonnummers uit films

phone_numbers = {   "The Simpsons": "636-555-3226",
                    "Vegas Vacation": "555-0100",
                    "Ghostbusters": "555-23678",
                    "Billy Madison": "555-0840",
                    "Swingers": "213-555-4679",
                    "Bruce Almighty": "555-0123",
                    "Seinfeld": "555-FILK",
                    "Arrested Development": "555-0113",
                    "Die Hard With a Vengeance": "555-0001",
                    "The A-Team": "555-6162",}

print(f"phone_numbers\n")

# a]
print(f"Het telefoonnummer van Bruce Almighty is {phone_numbers['Bruce Almighty']}.")
print(f"phone_numbers\n")

# b]
phone_numbers["Harry Potter"] = "605-475-6961"
print(f"phone_numbers\n")

# c]
old_phone_number = phone_numbers["Ghostbusters"]
new_phone_number = "555-2368"
phone_numbers["Ghostbusters"] = new_phone_number
print(f"Het telefoonnummr {old_phone_number} van de Ghostbusters is gewijzigd naar {new_phone_number}.")
print(f"phone_numbers")

# d]
phone_number = phone_numbers.pop("Seinfeld")
print(f"Telefoonnummer {phone_number} van Sienfeld is verwijderd.")
print(f"phone_numbers\n")

# e]
number_of_phone_numbers = len(phone_numbers)
print(f"In de dictionary zitten {number_of_phone_numbers} telefoonnummers.")
print(f"phone_numbers")

