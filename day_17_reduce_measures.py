'''This program expresses an imperial volume using the largest units possible
between cups, tablespoon and teaspoon'''

# Ask user to enter the unit of measurement and number of units
unit_of_measurement = str(input("Please enter the unit of measurement: ")).strip(' ').lower()
number_of_units = int(input("Please enter the number of units for the measurement: "))


def reduce_measures(number_of_units,unit_of_measurement):
    '''This function converts the number of units from the unit of measurement to the highest
    possible unit'''

    # Name the unit_of_measurement variable
    cup = 0
    tablespoon = 0
    teaspoon = 0

    # Assign number_of_units to cup if unit_of_measurement is cup
    if unit_of_measurement in ("cups","cup"):
        cup = number_of_units

    # If unit_of_measurement is tablespoon
    elif unit_of_measurement in ("tablespoons", "tablespoon"):

        # If number_of_units is greater than 15
        # Convert number_of_units to cup unit_of_measurement equivalent and compute
        while number_of_units-16 >= 0:
            cup += 1
            number_of_units -= 16
        
        # If number_of_units is less than 16
        # Assign number_of_units to tablespoon
        else:
            tablespoon = number_of_units
    
    # If unit_of_measurement is teaspoon
    elif unit_of_measurement in ("teaspoons", "teaspoon"):

        # If number_of_units is greater than 47
        # Convert number_of_units to cup unit_of_measurement equivalent and compute
        while number_of_units-(16*3) >= 0:
            cup += 1
            number_of_units -= (16*3)

        # If number_of_units is greater than 2
        # Convert number_of_units to tablespoon unit_of_measurement equivalent and compute
        while number_of_units > 2:
            tablespoon += 1
            number_of_units -= 3

        # If number_of_units is less than 3
        # Assign number_of_units to teaspoon
        while number_of_units > 0:
            teaspoon += number_of_units
            number_of_units = 0

    # Call the plurality function and pass in the parameters
    plurality(cup,tablespoon,teaspoon)


def plurality(cup,tablespoon,teaspoon):
    '''This function checks the number of units for the unit_of_measure
    and classifies the unit_of_measurement either as singular or plural
    while addind the right punctuation
    '''

    # Name a list to contain the number of units of cup, tablespoon and teaspoon
    measures = [cup, tablespoon, teaspoon]

    # Name an empty list for later use
    list_measures = []

    # Name an empty string spoon_f, tablespoon_f, cup_f, cup_, tablespoon_ and teaspoon_ for later use
    spoon_f, tablespoon_f, cup_f = "", "", ""
    cup_, tablespoon_, teaspoon_ = "", "",""

    # iterate over the elements in list measures
    for i in measures:

        # Append the element to list_measures
        # If the element of list is greater than 0
        if i > 0:
            list_measures.append(i)

    # If an element is in list_measures
    # get the index of the element for later use
    if cup in list_measures:
        cup_index = list_measures.index(cup)
    if tablespoon in list_measures:
        tablespoon_index = list_measures.index(tablespoon)
    if teaspoon in list_measures:
        teaspoon_index = list_measures.index(teaspoon)

    # If cup is in list_measures
    if cup in list_measures:

        # Check the value at the index of cup in list_measures
        # And assign the appropriate form to cup
        if list_measures[cup_index] > 1:
            cup_ = "cups"
        else:
            cup_ = "cup"

        # Check the number of items in list_measures and assign
        # The appropriate punctuation
        if len(list_measures)==2:
            cup_ = str(cup_) + " and"
        elif len(list_measures)==3:
            cup_ = str(cup_) + ","
        
        # Format the output of cup values
        # cup is the cup value while cup_ is the right punctuation
        cup_f = f"{cup} {cup_}"

    # If tablespoon is in list_measures
    if tablespoon in list_measures:

        # Check the value at the index of tablespoon in list_measures
        # And assign the appropriate form to tablespoon
        if list_measures[tablespoon_index] > 1:
            tablespoon_ = "tablespoons"
        else:
            tablespoon_ = "tablespoon"

        # Check the number of items in list_measures and assign
        # The appropriate punctuation
        if len(list_measures) == 3 or (len(list_measures) == 2 and teaspoon in list_measures):
            tablespoon_ = str(tablespoon_) + " and"

        # Format the output of cup values
        # cup is the tablespoon value while tablespoon_ is the right punctuation
        tablespoon_f = f"{tablespoon} {tablespoon_}"

    # If teaspoon is in list_measures
    if teaspoon in list_measures:

        # Check the value at the index of teaspoon in list_measures
        # And assign the appropriate form to teaspoon
        if list_measures[teaspoon_index] > 1:
            teaspoon_ = "teaspoons"
        else:
            teaspoon_ = "teaspoon"
        spoon_f = f"{teaspoon} {teaspoon_}"

    # Teaspoon is always the last in the list hence needs no punctuation

    # Check whether there is nothing in list_measures to display and display
    # An error message
    # This can occur when all items in the measures list is 0 or when
    # The selected unit_of_measurement is invalid
    if list_measures == []:
        print("Invalid entry")
    else:

        # Display the formatted output
        # cup_f, tablespoon_f and teaspoon_f is the formatted output of the respective values
        print(f"{cup_f} {tablespoon_f} {spoon_f}")

# Call the reduced measures function
reduce_measures(number_of_units,unit_of_measurement)