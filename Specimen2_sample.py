######## CREATE PATIENT ARRAYS FOR TESTING ########
from random import randint
patient = []
for i in range(1000):
    # make random name
    patient.append(chr(randint(65,91)) + chr(randint(97, 113)) + chr(randint(97,113)))
#make random readings
readings = [[randint(300, 380)/100, randint(400,1200)/10] for _ in range(1000)]
############  THE ABOVE IS JUST TO MAKE MY CODE WORK DON'T DO IT IN THE EXAM #########


# Write a procedure that takes a patient ID as 
def checkPatient(id):
    if id < 1 or id > 1000: # check to see if patient id is valid
        print("Patient ID out of range") # error message if incorrect
        return #end procedure
    
    # change id from 1 - 1000 to 0 - 999 for Python
    id = id - 1

    # Print patient name
    print(patient[id])

    # Get the temperature and pulse from the 2D array
    temp = readings[id][0]
    pulse = readings[id][1]

    # check if both readings are out
    if (temp < 31.6 or temp > 37.2) and (pulse < 55.0 or pulse > 100.0):
        print("Severe warning: Pulse and Temp")

    # check if temp is out
    elif temp < 31.6 or temp > 37.2:
        print("Warning temp")

    # check if pulse is out
    elif pulse < 55.0 or pulse > 100.0:
        print("Warning pulse")
    
    # otherwise normal
    else:
        print("Normal readings")

    return # not strictly necessary
