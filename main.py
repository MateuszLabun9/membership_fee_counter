from data_model import DataModel
import input_validation


def main():
    m1 = DataModel()  # Creating DataModel object
    m1.get_organization_structure("organization_structure_data.txt", "structure")  # Fetching organization structure
    m1.save_configuration('structure_config.json')  # Fetching organization config
    while True:
        time_period = input_validation.rent_period_validation()  # User input validation
        rent_amount = input_validation.rent_amount_validation(time_period)  # User input validation
        organization_unit = input_validation.organization_unit_validation(m1)  # User input validation
        calculation_result = m1.calculate_membership_fee(time_period, rent_amount, organization_unit)  # Calculation
        print("Calculation result: ", calculation_result, "\n")


if __name__ == "__main__":
    main()
