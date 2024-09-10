# Internet verbinding selectie
connections = ["4G", "5G", "WIFI OPEN"]

connection_choice = input('Welke verbinding wilt U gebruiken [4G, 5G, Wifi open]: ').upper()

if connection_choice in connections:
    print(f"U bent verbonden via {connection_choice}!")
elif connection_choice == "WIFI OPEN":
    print(f"U heeft de voor de Wifi open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.")
    confermation = input("Wilt u nog steeds een verbinding maken? [ja/nee]: ").lower()
    if confermation == "ja":
        print(f"U bent verbonden via {connection_choice}!")
    else:
        print("U bent niet verbonden!")
else:
    print("Onbekende invoer, er wordt geen verbinding tot stand gebracht.")

# Flowchart 1
print("Patient exposed to TB")

question_1 = input("Is the patient an adult or a child? [Adult/Child]: ").lower()
if question_1 == "adult":
    print("Adult")
    question_2= input("Has common TB symptoms? [Yes/No]: ").lower()

    if question_2 == "yes":
        print("Treat as likely TB patient and perform full TB exam.")

    elif question_2 == "no":
        print("Have patient report back if unwell, return in 1 month for checkup.")

    else:
        print("Abort, unknown input.")

elif question_1 == "CHILD":
    print("Child")
    question_3 = input("Can TB test be given? [Yes/No]: ").lower()

    if question_3 == "yes":
        print("Administer TB test.")
        print("Assess TB test results and child's condition.")

    elif question_3 == "no":
        question_4 = input("Child well? [Yes/No]: ").lower()

        if question_4 == "yes":
            print("6 months preventive isoniazid.")
            print("Have parent bring in if child shows any symptoms.")

        elif question_4 == "no":
            print("Take full history.Examine for TB.")
            print("If TB likely diagnosis, treat for TB.")
            print("If other diagnosis more likely, treat as needed and watch for TB symptoms.")
        else:
            print("Abort, unknown input.")
    else:
        print("Abort, unknown input.")
else:
    print("Abort, unknown input.")

#flowchart 2

print("Shopping Cart")

question_1 = input("Payment method? [Online/Offline]: ").lower()

if question_1 == "online":
    print("Online, place purchase order")
    question_2 = input("Admin User? [Yes/No]: ").lower()
    
    if question_2 == "yes":
        print("Enter payment details.")
        print("Place order.")

    elif question_2 == "no":
        question_3 = input("Approvel rules? [Approved/Rejected]: ").lower()

        if question_3 == "approved":
            print("Enter payment details.")
            print("Place order.")

        elif question_3 == "rejected":
            print("Purchase order rejected.")
            
        else:
            print("Abort, unknown input.")

    else:
        print("Abort, unknown input.")

elif question_1 == "offline":
    print("Offline, place purchase order")
    question_4 = input("Admin User? [Yes/No]: ").lower()

    if question_4 == "yes":
        print("Order created automatically.")

    elif question_4 == "no":
        question_5 = input("Approvel rules? [Approved/Rejected]: ").lower()

        if question_5 == "approved":
            print("Order created automatically.")

        elif question_5 == "rejected":
            print("Purchase order rejected.")

        else:
            print("Abort, unknown input.")

    else:
        print("Abort, unknown input.")

else:
    print("Abort, unknown input.")

# Bestellen
burgers = ["hamburger", "cheeseburger", "bic mac", "quarter pounder"]
warme_drankjes = ["koffie", "cappucino", "chocolademelk"]
koude_drankjes = ["coca cola", "cola zero", "7-up", "fanta", "fristi"]

dine_in = False

print("Welkom bij de Mac Donald's")
question_1 = input("Hier opeten of meenemen? [Opeten/Meenemen]: ").lower()

if question_1 == "meenemen":
    print("Meenemen")
    eat_in = False

elif question_1 == "opeten":
    print("Hier opeten")
    eat_in = True

else:
    print("Abort, unkown input.")

question_2 = input("Burgers of drankjes? [Burgers/Drankjes]: ").lower()

if question_2 == "burgers":
    question_3 = input("Burgers [Hamburger, Cheeseburger, Bic Mac, Quarter Pounder]: ").lower()

    if question_3 == "hamburger":
        print(question_3)

    else:
        print("Abort, unkown input.")

elif question_2 == "drankjes":
    question_4_str = input("Drankjes [Warme/Koude]: ").lower()

    if question_4 == "warme":
        question_5 = input("Warme drank: [Koffie, Cappucino, Chocolademelk]: ").lower()

        if question_5 in warme_drankjes:
            print(question_5)

        else:
            print("Abort, unkown input.")

    elif question_4 == "koude":
        question_6_str = input("Koude drank: [Coca Cola, Cola Zero, 7-Up, Fanta, Fristi]: ").lower()
        if question_5 in koude_drankjes:
            print(question_5)

        else:
            print("Abort, unkown input.")
    else:
        print("Abort, unkown input.")
else:
    print("Abort, unkown input.")

if eat_in:
    print("Bedankt voor uw bestelling en eet smakelijk in ons restaurant.")
else:
    print("Bedankt voor uw bestelling, goede reis en eet smakelijk.")

