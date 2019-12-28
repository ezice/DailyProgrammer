'''
Created on Dec 27, 2019

@author: rick
'''

if __name__ == '__main__':
    name = input("What is your name: ");
    age = input("What is your age: ");
    userName = input("What is your Reddit username: ");
    outputString = "your name is {}, you are {} years old, and your username is {}\n"
    outputString = outputString.format(name, age, userName)
    print(outputString);
    logfile = open("logfile.txt", "a")
    logfile.write(outputString);
    logfile.close()