# I am going to write a program about dictionaries (printing out people's information)

person_info = {
    "name": "Ryan Thomas",
    "age": 24,
    "favorite food": "carrots",
    "favorite place": "Disneyland",
    "favorite music": "Country",
    "favorite song": "Wake me Up before you go go",
    "is_tall": True

}

# printing out values in the dictionary

print(person_info["name"])
print(person_info["age"])
print(person_info["favorite food"])
print(person_info["favorite place"])
print(person_info["favorite music"])
print(person_info["favorite song"])
print(person_info["is_tall"])

# adding new key values and printing them out
person_info["favorite food"] = "blueberries"

print(person_info["favorite food"])

person_info_2 = {
    "name": "Justin Thomas",
    "age": 21,
    "favorite food": "carrots",
    "favorite place": "Disneyland",
    "favorite music": "Pop",
    "favorite song": "We Belong",
    "is_tall": True
}

# printing out values in the dictionary

print(person_info_2["name"])
print(person_info_2["age"])
print(person_info_2["favorite food"])
print(person_info_2["favorite place"])
print(person_info_2["favorite music"])
print(person_info_2["favorite song"])
print(person_info_2["is_tall"])

# adding new key values and printing them out
person_info_2["favorite place"] = "Great America"

print(person_info_2["favorite place"])

# creating a dictionary (from english to spanish
translations = {"you're welcome": "de nada", "blue": "azul", "green": "verde", "thank you": "gracias", "grey": "gris",
                "black": "negro", "red": "rojo"}

# adding new keys to the person_info dictionary
person_info["favorite color"] = "blue"

person_info["favorite video game"] = "Ninja turtles"

# printing out the dictionary
print(person_info)

# adding new keys to the person_info_2 dictionary
person_info_2["favorite color"] = "red"

person_info_2["favorite video game"] = "Nerf arcade"

# printing out the dictionary
print(person_info_2)

# adding multiple new keys to the person_info dictionary
person_info.update({"favorite movie": "High School Musical", "favorite TV show": "Masterchef",
                    "favorite animal": "zebra"})

# printing out the dictionary
print(person_info)

# adding multiple new keys to the person_info_2 dictionary
person_info_2.update({"favorite movie": "Shrek", "favorite TV show": "Spongebob Squarepants",
                      "favorite animal": "penguins"})

# printing out the dictionary
print(person_info_2)
