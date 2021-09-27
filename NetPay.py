""" Ask for employee name
    Ask for amount of hours worked
    Separate regular OT from reg hours
    Display gross pay for normal hours
    Display gross pay for OT
    Display net pay """

pay_rate = 10
tax_rate = .10

#Ask for employees name
print("Hello, what is your name?")
name = input("")
print("Hello", name)

#Ask for how many hours they worked
print("How many hours did you work this week,", name,"?")
total_hours = input("")
print(name + ", you worked " + total_hours + " hours at $" + str(pay_rate) + " per hour.")

#Separate OT from reg hours
if float(total_hours) > 40:
    over_time = float(total_hours) - 40
    print(name + ", you worked", over_time, "hour(s) in over time at $" + str((float(pay_rate)/2) + (float(pay_rate))) + " per hour.")

#Display gross pay for normal hours
regular_hrPay = float(total_hours) * float(pay_rate)

if float(total_hours) <= 40:
    print(name + ", your gross pay is $" + str(regular_hrPay))

#Display gross pay for OT
elif float(total_hours) > 40:
    OT_pay = (float(over_time) * (float(pay_rate)/2)) + (float(regular_hrPay))
    print(name + ", your gross pay is $" + str(OT_pay))

#Display net pay
if float(total_hours) <= 40:
    print(name + ", you paid $" + str(float(regular_hrPay) * (float(tax_rate))) + " in tax.")
    print(name + ", your net pay is $" + str(float(regular_hrPay - ((float(regular_hrPay) * (float(tax_rate)))))))

elif float(total_hours) > 40:
    print(name + ", you paid $" + str(float(OT_pay) * (float(tax_rate))) + " in tax.")
    print(name + ", your net pay is $" + str(float(OT_pay) - (float(OT_pay) * (float(tax_rate)))))

print("Type any key to end")
input("")
