'''
Created on Dec 27, 2019

@author: rick
'''

if __name__ == '__main__':
    valid = False
    while valid is not True:
        print("Please answer two of the three following questions.  Enter 0 to calculate.\n")
        rate = int(input("What is your hourly pay rate? "))
        hoursPerWeek = int(input("How many hours per week do you work? "))
        salary = int(input("What is your expected annual salary? "))

        answered = 0    
            
        if (rate != 0):
            answered += 1
             
        if (hoursPerWeek != 0):
            answered += 1
             
        if (salary != 0): 
            answered += 1
        
        if (answered > 2):
            print("Please answer only two of the questions.\n\n")                
        elif (answered < 2):
            print("You must answer two of the questions.\n\n")
        else:
            valid = True
        
    if (salary == 0):
        salary = rate * hoursPerWeek * 52
        outputString = "At ${0}/hr, working {1} hours per week, your annual salary is ${2}"
    elif (rate == 0):
        rate =  salary / (hoursPerWeek * 52)
        outputString = "working {1} hours per week, to make {2}, you''ll need to make {0} per hour"
    else:
        hoursPerWeek = salary / (rate * 52)
        outputString = "working at {0}/hr, to make {2}, you'll need to work {1} per week"
    
    outputString = outputString.format(rate, hoursPerWeek, salary)
    print(outputString)
    