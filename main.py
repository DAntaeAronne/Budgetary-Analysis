import csv

# Opening the csv file
with open('city-of-seattle-2012-expenditures-dollars.csv', "r", newline='') as file:
    # Storing the data as a dictionary {Department : Funds}
    DepTot = {}

    # Reader of the file
    csv_reader = csv.reader(file, delimiter=",")

    # Skipping the headers
    next(csv_reader)

    # Going through each row and adding the funds to each department
    for row in csv_reader:

        # Setting the key to the department name
        key = row[0]

        # Setting the value to the data in the "2012  Actual" column
        # If there was nothing in the '2012 Actual' column
        #   Then set the value to 0
        # Else
        #   Set the value to whatever number is there
        if row[3] == '':
            val = 0
        else:
            val = int(row[3])

        # Updating the funds of the departments
        # If the department is not added
        #   Then add the department to the dictionary
        # Else
        #   Update the value of the department
        if not DepTot.get(key):
            DepTot.update({key: val})
        else:
            DepTot[key] += val

# Converting the funds into proper dollar format
for Dep in DepTot:

    # Turn the value in that department into a string
    Funds = str(DepTot[Dep])
    ConvFunds = ""
    DigCount = 1

    # Starting from the back of the string, add the digits one at a time
    for i in reversed(range(0, len(Funds))):
        ConvFunds = Funds[i] + ConvFunds

        # Every 3 digits add a comma to denote hundreds, thousands, millions, etc.
        if DigCount % 3 == 0 and i != 0:
            ConvFunds = "," + ConvFunds
        DigCount += 1

    # Place $ at start of Funds
    ConvFunds = "$" + ConvFunds + ".00"
    DepTot[Dep] = ConvFunds

print(DepTot)
