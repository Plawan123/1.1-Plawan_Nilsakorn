'''
    author: Plawan NIlsakorn
    date: 25/08/2025
    version: 1
    description: 1.1 assesment - Fitness Tracker
'''


#---------------------intro---------------------------------
print("Welcome to Y11 Fitness Trcker!")
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))


#-----------------function-----------------------------------
def fitness():
    count_push_up = 0
    for i in range(1,8):
        while True:
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

                break
                
            except:
                print("Error, please enter with a number")
                  
                

fitness()


