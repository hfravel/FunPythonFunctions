from FunFuncs import *

def testAll():
    testNames = {"uniqStrings" : uniqStringTest}
    cont = True
    
    while cont:
        userInput = input("Please type what you want to Test (q to quit, l to list the tests, and a to test everything: ")
        if userInput == "q":
            cont = False
        elif userInput == "l":
            for test in testNames:
                print(test)
        elif userInput == "a":
            for test in testNames:
                testNames[test]()
        elif userInput in testNames:
            testNames[userInput]()
        else:
            print("Try again.")
    

def uniqStringTest():
    dashes = "---------------------\n"
    print("Running Tests for uniqString\n", end = dashes)
    
    testStrs = ["Hello", "hey", "RaceCAr", "heHE", "String", "", " ", "!!"]
    i = 1
    for x in testStrs:
        print("Test {} ... \"{}\"\t is unique: {}.".format(i, x, uniqString(x)))
        i += 1
    print("", end = dashes)

testAll()
