
bill = float(input("What was the bill? "))
numberPeople = int(input("What is the number of people? "))
tip = int(input("How much tip you want to give? 10, 12 or 15?"))

tipPercent = tip / 100
totalTip = bill * tipPercent
totalBill = bill + totalTip
billPerPerson = totalBill / numberPeople

finalSum = round(billPerPerson,2)
print(f"One person should pay: PLN{finalSum}")
