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
# doing for 7 days or a week
#------------------------------------
def fitness():
    total = 0  # Set total push up of whole week to 0
    total_2()
    count_push_up = 0 # Set push up in each day to 0
    each_day = []  # List that will store how many push up doing in a day
    each_day.append(count_push_up)
    for count_push_up in range(1,8):  # If the input not error the loop will go for 8 times
        while True:  # Check how many push up been doing
            try:  
                count_push_up = int(input("How many push up have you done toady: "))
                if(count_push_up >= 80):
                    print("Nice you are very strong keep workinghard!")
                elif(count_push_up >= 50):
                    print("You are strong keep working hard!")
                elif(count_push_up >= 30):
                    print("You are average keep working hard!")
                elif(count_push_up >= 10):
                    print("Not bad, don't give up keep working hard!")
                elif(count_push_up <= 9 and count_push_up >0):
                    print("Come on you can do better than this!")
                else:
                    print("Are you kidding me?")
                     
                total += count_push_up  # Add all amount of push up that store in list together to get a total push up       
                total_2 = max   

                break
                
            except:  # If user enter alphabet it will print this
                print("Error, please enter with a number")                  
    
    print(f"Nice {name} you did {total} push up for this week {total_2}")


#---------------------main routine---------------------------
Min = 2  # Minimum of letter for user name
Max = 20  # Maximum of letter for user name
while True:  #Check if user name between Min and Max
    name = str(input("Enter your name: "))
    if(len(name) > Min and len(name) < Max and name.isalpha): 
        print(f"Hi {name}! Welcome to Y11 Fitness Trcker!")  #greeting!!
        break
    else:
        print("Please try again")


while True: 
    try:
        age = int(input("Enter your age betwee 14-17: "))
        if(14 <= age <= 17):
            break
        else:
            print("Sorry, age must be between 14 and 17.")
    except:
        print("Please enter with a number.")

fitness()