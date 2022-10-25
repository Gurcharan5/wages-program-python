import tkinter as tk

root = tk.Tk()

name = tk.Entry(root, width="60")
role = tk.Entry(root, width="60")
hours = tk.Entry(root, width="60")

name.grid(row=0, column=1)
role.grid(row=1, column=1)
hours.grid(row=2, column=1)

inputNameText = tk.Label(root, text="Enter your name: ", padx=80, pady=20)
inputRoleText = tk.Label(root, text="Enter your job role: ", padx=80, pady=20)
inputHoursText = tk.Label(root, text="Input how many hours you have worked this month: ", padx=80, pady=20)

inputNameText.grid(row=0, column=0)
inputRoleText.grid(row=1, column=0)
inputHoursText.grid(row=2, column=0)

def workOutHours():
    global hours
    totalHours = int(hours.get())

    overtimeHours = 0
    regularHours = totalHours

    if totalHours > 160:
        overtimeHours = totalHours - 160
        regularHours = totalHours - overtimeHours

 
    calculatePay(overtimeHours, regularHours)
    

def calculatePay(overtimeHours, regularHours):
    global role
    role = str(role.get()).upper()
    
    
    if role == "MANAGER":
        regularRate = 15.38
        overtimeRate = 20.38
    elif role == "LABOURER":
        regularRate = 10.56
        overtimeRate = 15.56
    elif role == "DESIGNER":
        regularRate = 20.87
        overtimeRate = 25.87
    elif role == "DRIVER":
        regularRate = 4.50
        overtimeRate = 9.50
        

    calculateGrossPay(regularRate, overtimeRate, overtimeHours, regularHours)
   

def calculateGrossPay(regularRate, overtimeRate, overtimeHours, regularHours):
    normalWagePay = regularHours * regularRate
    overtimeWagePay = overtimeHours * overtimeRate
    grossPay = normalWagePay + overtimeWagePay
    
    if grossPay > 12500:
        nationalInsurance = 0.965
        taxAmount = 0.65
        
        
    elif grossPay > 4189:
        nationalInsurance = 0.965
        taxAmount = 0.6
        
        
    elif grossPay > 1000:
        nationalInsurance = 0.8675
        taxAmount = 0.8
        
    
    finalPay = grossPay * nationalInsurance * taxAmount
    printResults(finalPay)
    

def printResults(finalPay):
    results = tk.Label(root, text="Your final pay " + str(name.get()) +  " is: £" + str(finalPay))
    results.grid(row=2, column=3)
    print(finalPay)


submit = tk.Button(root, text="Submit your data and see how much you made this month", padx=60, pady=10, command=workOutHours)

submit.grid(row=1, column=3)



root.mainloop()