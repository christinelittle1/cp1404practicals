TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator")
tariff = int(input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use in kWh: "))
number_of_days = float(input("Enter number of billing days: "))

if tariff == 11:
    estimated_bill = daily_use * number_of_days * TARIFF_11
    print("Estimated bill: ${:.2f}".format(estimated_bill))

if tariff == 31:
    estimated_bill = daily_use * number_of_days * TARIFF_31
    print("Estimated bill: ${:.2f}".format(estimated_bill))
