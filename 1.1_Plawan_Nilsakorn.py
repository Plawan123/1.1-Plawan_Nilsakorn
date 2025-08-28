'''
    author: Plawan NIlsakorn
    date: 25/08/2025
    version: 1
    description: 1.1 assesment - Fitness Tracker
'''


#-----------------function-----------------------------------

#------------------------------------
# To check how many push up user been doing
# and tell them how stong they are. 
# Also add all total push up that user been
# doing for 7 days or a week.
#------------------------------------


def fitness():
    total = 0  # Set total push up of whole week to 0
    count_push_up = 0 # Set push up in each day to 0
    each_day = []  # List that will store how many push up doing in a day

    for count_push_up in range(1,8):  # If the input not error the loop will go for 8 times
        while True: # Check how many push up been doing
            try:  # This is to make sure that the code won't be crash if user input a alphabet etc  Give user a feed back of how strong they are from many push they do
                count_push_up = int(input("How many push up have you done toady: "))
                if(count_push_up >= 80):
                    print("Nice you are very strong keep working hard!")
                elif(count_push_up >= 50):
                    print("You are strong keep working hard!")
                elif(count_push_up >= 30):
                    print("You are average keep working hard!")
                elif(count_push_up >= 10):
                    print("Not bad, don't give up keep working hard!")
                elif(count_push_up <= 9 and count_push_up >0):
                    print("Come on you can do better than this!")


                else:  # If enter any other thing else that is a number and lower than 0 
                    print("Are you kidding me?")  

                    break  # Stop loop if no error or negative number

                each_day.append(count_push_up)     
                total += count_push_up  # Add all amount of push up that store in list together to get a total push up       

    
                
            except:  # If user enter alphabet it will print this
                print("Error, please enter with a number")  

    best = max(each_day)  # Get the best result that store in the list
    print(f"Nice {name} you did {total} push up for this week!")
    print(f"Your best result was {best}!")


#---------------------main routine---------------------------
Min = 2  # Minimum of letter for user name
Max = 20  # Maximum of letter for user name
while True:  #Check if user name between Min and Max
    name = str(input("Enter your name: "))  # Force user to enter between 2-20 alphabet
    if(len(name) > Min and len(name) < Max and name.isalpha): 
        print(f"Hi {name}! Welcome to Y11 Fitness Trcker!")  #greeting!!
        break
    else:  # If user enter any other letter more or less than the limits will print this
        print("Please try again your name must be between 2-20 letters")

# User can only go in the the quest if there age is 14-17
while True: 
    # Don't let the code crash if user enter with alphabet
    try:
        age = int(input("Enter your age between 14-17: "))
        if(14 <= age <= 17):
            break
        else:
            print("Sorry, age must be between 14-17.")
    except:  
        print("Please enter with a number.")

fitness()