# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
    # ```sh
    # Enter your age: 30
    # You are old enough to learn to drive.
    # Output:
    # Enter your age: 15
    # You need 3 more years to learn to drive.


Age = int(input(' enter your age '))
diff = 18 - Age

if Age   >= 18:
    print("You are old enough to drive")
else:
     print(f'"You need {diff} more years to learn to drive')


# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to 
# get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' 
# for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
#     You are 5 years older than me.
#     ```

my_age = 20
clients_age = int(input("Enter your age  "))
if clients_age > my_age:
  diff = clients_age-my_age
  if diff == 1:
    print("you are one year older")
  else:
    print(f' you are {diff} years older')
elif my_age > clients_age:
    diff2= my_age - clients_age
    if diff2==1:
        print("i am one year older")
    else:
        print(f'i am {diff2} years older')
else:
    print("we are the same age ")


# Write a code which gives grade to students according to theirs scores:

#    ```sh
#    80-100, A
#    70-89, B
#    60-69, C
#    50-59, D
#    0-49, F
#    ```

result = int(input("enter your score "))
if result <= 49:
    print('your grade is F')

elif result >= 50  and result <= 59:
    print("your grade is D")

elif result >= 60 and result <= 69:
    print("your grade is C")

elif result >= 70 and result <= 89:
    print('your grade is B')
else: 
    print("your grade is A")


#  Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
#  if a is less b return a is smaller than b, else a is equal to b. Output:

# ```sh
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# ```

user1 = int(input("Enter your number "))
user2 = int(input("Enter your second number"))
if user1 > user2:
    print("a is greater than b")
elif user1 < user2:
    print("a is less than b")
else:
    print("a is equal to b")   

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
#    September, October or November, the season is Autumn.
#    December, January or February, the season is Winter.
#    March, April or May, the season is Spring
#    June, July or August, the season is Summer

season =input("Enter season  ")
if season == "september" and "October" and "November":
    print("Autumn")
elif season =="December" and "January" and "February":
    print("Winter")
elif season == "March" and "April" and "May":
    print("Spring")
else:
    print("Summer")


#     The following list contains some fruits:

#    ```sh
#    fruits = ['banana', 'orange', 'mango', 'lemon']
#    ```

#    If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append("Guava")
print(fruits)
fruits = input("Enter your fruits ")
if fruits == 'banana' and 'orange'and 'mango'and 'lemon':
    print('That fruit already exist in the list')
else:
    print("fruit not found")

#     Here we have a person dictionary. Feel free to modify it!

# ```py
#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
# ```

#      * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#      * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#      * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#      * If the person is married and if he lives in Finland, print the information in the following format:

# ```py
#     Asabeneh Yetayeh lives in Finland. He is married.
# ```
 

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
   }

for key in person:
    print(key)

print(person["skills"][2])
print("Python" in person["skills"] )


skills=person["skills"]
if "Node" in skills and "React" in skills and "MongoDB" in skills:
    print("He is a Fullstack")
elif "Node" in skills and "Python" in skills and "MongoDB" in skills:
    print("He is a backend developer")
elif "Javascript" in  skills and "React" in skills:
    print("He is a frontend developer")
else:
    print("Unknown title")

marriage=person["is_married"]
country=person ['country']
firstname = "Lucy"
lastname = "Obahor"
if marriage ==True and country == "Finland":
    print(f'{firstname} {lastname} lives in {country}. She is married')



Education ="O level", "BSC", "MSC", "PHD"
if "O level" in Education and "BSC" in Education and "MSC" in Education and "PHD" in Education:
    print("She is a PHD holder.")
elif 'O level' in Education and "BSC" in Education:
    print("She has completed her BSC")
elif "O level in Education":
    print("She is an undergraduate ")
elif "O level" in Education and 'BSC' in Education and "MSC" in Education:
    print("She has completed Masters ")
else:
    print('She is not in school yet')




