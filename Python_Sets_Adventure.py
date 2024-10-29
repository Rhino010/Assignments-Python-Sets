"""
1. Python Sets Adventure
Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

Task 1: Flight Route Comparison Imagine you work for an airline and 
need to compare the flight routes of your airline with a competitor. 
You have two sets of flight destinations, one for each airline. Write a Python program to find out:

1. Destinations that both airlines fly to.

2. Destinations unique to your airline.

3. Whether there are any destinations that neither airline shares.
"""

airline1_destinations = {"Toronto", "San Francisco", "Chicago", "New York"}
airline2_destinations = {"Austin", "Scottsdale", "Milwaukee", "Chicago", "Tampa Bay"}





def show_shared(dest1, dest2):
    shared_destinations = dest1.intersection(dest2)
    print(shared_destinations)
def show_unique(dest1, dest2):
    while True:
        print("\n1. Unique destinations of Airline 1\n2. Unique destinations of Airline 2\n3. Go to main menu")
        selection = input("Please make your selection:\n")
        if selection == '1':
            air1_unique = dest1.difference(dest2)
            print(f"The destination(s) unique to Airline 1 is(are) {air1_unique}.")
            break
        elif selection == '2':
            air2_unique = dest2.difference(dest1)
            print(f"The destination(s) unique to Airline 2 is(are) {air2_unique}.")
            break
        elif selection == '3':
            break
        else:
            print("Invalid selection.")
def show_unshared(dest1, dest2):
    unshared_destinations = dest1.symmetric_difference(dest2)
    print(f"These destinations are unshared destinations: {unshared_destinations}")

while True:

    print("Main Menu\n")
    print("\n1. Show shared destinations\n2. Show unique destinations\n3. Show destinations not shared by the airlines\n4. Exit")
    choice = input("Please make a selection.")
    
    if choice == "1":
        show_shared(airline1_destinations, airline2_destinations)
    elif choice == '2':
        show_unique(airline1_destinations, airline2_destinations)
    elif choice == '3':
        show_unshared(airline1_destinations, airline2_destinations)
    elif choice == '4':
        print("Exiting....")
        break
    else:
        print("Try again.")