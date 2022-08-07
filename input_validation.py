# Validation of user input

# Validation of rent period input, this method makes sure user input is 'week' or 'month'
# Keep asking for this 2 key words until receives one of them
def rent_period_validation():
    period = ""
    while True:
        try:
            period = str(input("Please type rent period, use 'month' or 'week': "))
        except ValueError:
            return rent_period_validation()
        if period != "month" and period != "week":
            return rent_period_validation()
        else:
            break
    return period


# Validation of rent amount based on cases listed in description
def rent_amount_validation(rent_period):
    amount = 0.0
    while True:
        try:
            amount = float(input("Enter rent for one " + rent_period + " "))
        except ValueError:
            print("\nPlease enter value with comma as a separator")
        else:
            if rent_period == "week" and (amount < 25.0 or amount > 2000.0):
                print("Weekly rent can not be lower than £25 and higher than £2000")
            elif rent_period == "month" and (amount < 110.0 or amount > 8660.0):
                print("Monthly rent can not be lower than £110 and higher than £8660")
            else:
                break
    return amount


# Validation of organization unit, after user provides input, it is checked if given unit exist in fetched data
def organization_unit_validation(model):
    while True:
        try:
            unit_name = str(input("Please type organization name: "))
        except ValueError:
            print("\nPlease enter proper name")
        else:
            if unit_name in model.branches.keys() or unit_name in model.areas.keys() or unit_name in model.divisions.keys() \
                    or unit_name in model.clients.keys():
                break
            else:
                print("Organization name not found!")
    return unit_name
