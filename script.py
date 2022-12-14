# Scott Schumacker
# Script for creating a password

# Importing libraries
import random

# Initializing a function to create a new password
def newPassword():
    # Creating a list of words to choose from
    word_choices = ['apple', 'banana', 'orange', 'cool', 'science', 'scholar', 'chef', 'cook', 'master', 'carpenter', 'scientist', 'math', 'statistics',
                'structure', 'alaska', 'usa', 'russia', 'wyoming', 'maine', 'utah', 'china', 'germany']
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    # Creating loop for adding words
    combo = []
    for i in [1,2]:
        combo = combo + [random.choice(word_choices)]
    
    # Creating loop for adding numbers
    numberCombo = []
    for number in [3,4]:
        numberCombo = numberCombo + [random.choice(numbers)]
    
    # Creating loops for adding words and adding numbers
    password = ""
    for word in combo:
        password = password + str(word)
    
    for x in numberCombo:
        password = password + str(x)
    
    return(password)

print(newPassword())