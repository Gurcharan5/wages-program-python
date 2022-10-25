from tkinter import *

root = Tk()

name = Entry(root, width="60")
role = Entry(root, width="60")
hours = Entry(root, width="60")

name.grid(row=0, column=1)
role.grid(row=1, column=1)
hours.grid(row=2, column=1)

inputNameText = Label(root, text="Enter your name: ", padx=80, pady=20)
inputRoleText = Label(root, text="Enter your job role: ", padx=80, pady=20)
inputHoursText = Label(root, text="Input how many hours you have worked this month: ", padx=80, pady=20)

inputNameText.grid(row=0, column=0)
inputRoleText.grid(row=1, column=0)
inputHoursText.grid(row=2, column=0)

def workOutHours():
    global hours
    totalHours = int(hours.get())

    if totalHours > 160:
        overtimeHours = totalHours - 160
        regularHours = totalHours - overtimeHours
    else:
        overtimeHours = 0
        regularHours = totalHours
    
    return overtimeHours, regularHours
    calculatePay(overtimeHours, regularHours)
    #print(overtimeHours + regularHours)

def calculatePay(overtimeHours, regularHours):
    overtimeHours = overtimeHours
    regularHours = regularHours
    role = str(role.get()).capitalize
    while role == "MANAGER":
        regularRate = float(15.38)
        overtimeRate = float(20.38)
        break
    while role == "LABOURER":
        regularRate = float(10.56)
        overtimeRate = float(15.56)
        break
    while role == "DESIGNER":
        regularRate = float(20.87)
        overtimeRate = float(25.87)
        break
    while role == "DRIVER":
        regularRate = float(4.50)
        overtimeRate = float(9.50)
        break
    return regularRate, overtimeRate, overtimeHours, regularHours
    calculateGrossPay(regularRate, overtimeRate, overtimeHours, regularHours)
    #print(regularRate + overtimeRate + overtimeHours + regularHours)

def calculateGrossPay(regularRate, overtimeRate, overtimeHours, regularHours):
    normalWagePay = regularHours * regularRate
    overtimeWagePay = overtimeHours * overtimeRate
    grossPay = normalWagePay + overtimeWagePay
    global finalPay
    while grossPay > 12500:
        nationalInsurance = 0.965
        taxAmount = 0.65
        finalPay = grossPay * nationalInsurance * taxAmount
        break
    while grossPay > 4189:
        nationalInsurance = 0.965
        taxAmount = 0.6
        finalPay = grossPay * nationalInsurance * taxAmount
        break
    while grossPay > 1000:
        nationalInsurance = 0.8675
        taxAmount = 0.8
        finalPay = grossPay * nationalInsurance * taxAmount
        break
    printResults(finalPay)
    #print(finalPay)

def printResults(finalPay):
    results = Label(root, text="Your final pay " + str(name.get()) +  " is: £" + str(finalPay))
    results.grid(row=2, column=3)
    print(finalPay)


submit = Button(root, text="Submit your data and see how much you made this month", padx=60, pady=10, command=workOutHours)

submit.grid(row=1, column=3)



root.mainloop()