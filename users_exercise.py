users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users["Jonathan"]["twitter"])


# 2. Get Erik's hometown
print(users["Erik"]["home_town"])


# 3. Get the list of Erik's lottery numbers
print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"])


# 5. Get the smallest of Erik's lottery numbers
smallest_number = min(users["Erik"]["lottery_numbers"])
print(smallest_number)

# 6. Return an list of Avril's lottery numbers that are even
avril_lottery_numbers = users["Avril"]["lottery_numbers"]
avril_even_numbers = [num for num in avril_lottery_numbers if num % 2 == 0]
print(avril_even_numbers)
                               


# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
erik_lottery_numbers = users["Erik"]["lottery_numbers"]
erik_lottery_numbers.append(7)
print(erik_lottery_numbers)


# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "fluffy"
new_pet = {
    "name": "fluffy",
    "species": "dog"
}

users["Erik"]["pets"].append(new_pet)
print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary
users["Tommy"] = {
    "twitter": "Tommy123",
    "lottery_numbers": [1, 2, 3, 4, 5, 6],
    "home_town": "Edinburgh",
    "pets": [
        {
            "name": "luna",
            "species": "dog"
        },
        {   
            "name": "juno",
            "species": "dog"

        }
    ]
}

print(users)