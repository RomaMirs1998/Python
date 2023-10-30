import random

import uuid

from faker import Faker



fake = Faker()



sql_commands = []



for _ in range(100000):

    vorname = fake.first_name()

    nachname = fake.last_name()

    firmenname = f"{vorname} {nachname} GmbH"

    passwort = fake.password(length=12)

    hauptkategorieId = random.randint(1, 10)

    email = f"{vorname}.{nachname}@example.com".lower()

    email = email+str(uuid.uuid4())

    telefon = fake.phone_number()

    telefon = telefon+str(uuid.uuid4())

    bundesland = fake.state()

    strasse = fake.street_name()

    hausnummer = fake.building_number()

    plz = fake.postcode()

    stadt = fake.city()

    gisa = str(uuid.uuid4())

    land = "AT"



    # Erstellen des SQL-Befehls

    sql_command = f"INSERT INTO \"ABC\" (\"anmeldeDatum\", \"vorname\", \"nachname\", \"firmenname\", \"passwort\", \"hauptkategorieId\", \"email\", \"telefon\", \"bundesland\", \"strasse\", \"hausnummer\", \"plz\", \"stadt\", \"gisa\", \"land\") VALUES (CURRENT_TIMESTAMP, '{vorname}', '{nachname}', '{firmenname}', '{passwort}', {hauptkategorieId}, '{email}', '{telefon}', '{bundesland}', '{strasse}', '{hausnummer}', '{plz}', '{stadt}', '{gisa}', '{land}');"

    sql_commands.append(sql_command)





for command in sql_commands[:10]:

    print(command)




with open('create_companies.sql', 'w') as file:

    for command in sql_commands:

        file.write(command + "\n")
