import random

collection = ['red','red','orange','pink','pink','pink','yellow','yellow'] #current marbles 
secret_bag = ['blue','blue','blue','green','green','green','green','orange','purple','purple','yellow','yellow','pink','pink','red','red','red','red'] #potential marbles
marbles_chose = [] #empty list that can be added to
tries_remaining = 5 

attempt = input("Enter the key 'x' if you want to attempt to get a green marble. ")
for x in range(6):
    if attempt == "x" and tries_remaining > 0: #This will determine if the user put the correct input and if the user has enough tries
        selection = random.choice(secret_bag) #this grabs a random value or marble from the secret bag list
        marbles_chose.append(selection) #this adds the random marble to the list of marbles already grabbed
        tries_remaining -=1 #this removes one a try
        if selection == 'green': #an if statment inside an if statment is called nesting
            collection.append(selection) #moves the green marble to collection
            secret_bag.remove(selection) #removes the green marble from the potential marbles
            if ('green' in collection): #if a green marble is chosen
                print(f'You found a green marble. you have {tries_remaining} tries remaining.')
                break
    else:
        print('sorry, you are out of tires.')
print(f'Here are all the marbles that were chosen {marbles_chose}')
#This program will loop until a green is found.
            
