'''
    author: Plawan NIlsakorn
    date: 25/08/2025
    version: 1
    description: 1.1 assesment - Fitness Tracker
'''
    
def fitness():
        count_push_up = 0
        for i in range(7):
            while True:
                  count_push_up = int(input("How many push up have you done toady: "))
                  if(count_push_up >= 80):
                        print("Nice you are strong keep workinghard!")
                  elif(count_push_up >= 50):
                        print("You are average keep working hard")
                  
                



fitness()

#------------------main routine------------------------------
print("Welcome to Y11 Fitness Trcker!")
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

