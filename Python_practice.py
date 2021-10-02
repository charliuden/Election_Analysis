print("Hello World")

#Lists
counties = ["Arapahoe", "Denver", "Jefferson"]
counties.insert(1,"El Paso")
counties.remove("Arapahoe")
counties.remove("Denver")
counties.insert(2,"Denver")
counties.append("Arapahoe")
print(counties)

#Tuples
my_tuple = ()
my_tuple = tuple()

#Dictionaries
counties_dict = {}
#add arapahoe county and number of voters
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
len(counties_dict)
counties_dict.items()#gives you contents of dictionary
counties_dict.keys() #gives you all the keys
counties_dict.values() #gives you all the values
#get values based on key
counties_dict.get("Denver")

#these all give the same answer:
print(counties_dict['Arapahoe'])
counties_dict.get("Arapahoe")
print(counties_dict['Arapahoe'])
print(counties_dict.get("Arapahoe"))


#make a list of dictionaries:
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
#add "El Paso" and number of registered voters
voting_data.append({"county":"El Paso", "registered_voters": 461149})
print(voting_data)
#remove arapahoe and its registered voters

#make denver and voters third item, keep jevverson and voters second
#counties.remove("Denver")
#counties.insert(2,"Denver")

print(voting_data)


# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")




# IF STATEMENTS
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

# IF-ELSE STATEMENTS
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

# NESTED IF-ELSE STATEMENTS
#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

# ELIF STATEMENTS
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

# MEMBERSHIP OPERATORS
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# LOGICAL OPERATORS
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
