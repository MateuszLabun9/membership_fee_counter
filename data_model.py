import unittest
from organization_unit import OrganizationUnit
import json


# Method used to save configuration fetched from configuration file
def save_config(configurable_object, data_object):
    # Save configuration from file to proper dictionary
    configurable_object[data_object["name"]].config = data_object["config"]


# Method used to calculate rent amount with 20% Vat
def calculate_vat(rent_amount):
    fee = rent_amount + rent_amount * 0.2
    return fee


class DataModel:  # DataModel class with dictionaries for each type of organization
    def __init__(self):
        self.clients = {}  # Saved clients dictionary
        self.divisions = {}  # Saved divisions dictionary
        self.areas = {}  # Saved areas dictionary
        self.branches = {}  # Saved branches dictionary

    # Get organization structure saved in txt file
    def get_organization_structure(self, file_path, data_type):
        structure_file = open(file_path, "r")
        fetched_data = structure_file.readlines()
        for line in fetched_data:
            match data_type:
                case "structure":  # If file type is structure
                    self.save_fetched_data(line.strip())
                case "configuration":  # If file type is configuration
                    self.save_configuration(line.strip())
        structure_file.close()

    # Saving fetched structure data in proper dictionaries
    def save_fetched_data(self, line):
        split_data = []
        for arg in line.split():
            split_data.append(arg.replace(",", "").replace("{", "").replace("}", "").replace("[", "").replace("]", ""))
        # saving branches
        if "area" in split_data[0]:
            for branch in split_data[1:]:
                self.branches[branch] = OrganizationUnit(split_data[0])
        # saving areas
        elif "division" in split_data[0]:
            for area in split_data[1:]:
                self.areas[area] = OrganizationUnit(split_data[0])
        # saving divisions
        elif "client" in split_data[0]:
            for division in split_data[1:]:
                self.clients[split_data[0]] = OrganizationUnit(None)  # saving client
                self.divisions[division] = OrganizationUnit(split_data[0])

    # Saving proper configuration from configuration file
    def save_configuration(self, file_path):
        with open('structure_config.json') as config_file:
            data = json.load(config_file)
        for configuration in data:
            if "branch" in configuration["name"]:
                if configuration["config"] is not None:
                    save_config(self.branches, configuration)
            elif "area" in configuration["name"]:
                if configuration["config"] is not None:
                    save_config(self.areas, configuration)
            elif "division" in configuration["name"]:
                if configuration["config"] is not None:
                    save_config(self.divisions, configuration)
            elif "client" in configuration["name"]:
                if configuration["config"] is not None:
                    save_config(self.clients, configuration)
        config_file.close()

    # Calculating membership fee for specific organization structure
    def calculate_membership_fee(self, rent_period, rent_amount, organization_unit):
        membership_fee = 0.0
        # Check if period is month, if so divide amount by 4 -> 1 month is 4 weeks approx
        if rent_period == "month":
            rent_amount = rent_amount / 4
        if "branch" in str(organization_unit):
            membership_fee = self.search(self.branches, organization_unit, rent_amount)
        elif "area" in str(organization_unit):
            membership_fee = self.search(self.areas, organization_unit, rent_amount)
        elif "division" in str(organization_unit):
            membership_fee = self.search(self.divisions, organization_unit, rent_amount)
        elif "client" in str(organization_unit):
            membership_fee = self.search(self.clients, organization_unit, rent_amount)
        return membership_fee

    # Search for configuration data from object or parent structure
    def search(self, organization_name, organization_unit, rent_amount):
        if organization_name[organization_unit].config is not None:
            if organization_name[organization_unit].config["has_fixed_membership_fee"] is not False:
                membership_fee = organization_name[organization_unit].config["fixed_membership_fee_amount"] / 100
                return membership_fee
            else:
                return calculate_vat(rent_amount)
        else:
            if organization_name[organization_unit].parent_name is not None:
                if "area" in organization_name[organization_unit].parent_name:
                    return self.search(self.areas, organization_name[organization_unit].parent_name, rent_amount)
                elif "division" in organization_name[organization_unit].parent_name:
                    return self.search(self.divisions, organization_name[organization_unit].parent_name, rent_amount)
                elif "client" in organization_name[organization_unit].parent_name:
                    return self.search(self.clients, organization_name[organization_unit].parent_name, rent_amount)
            else:
                membership_fee = calculate_vat(rent_amount)
                return membership_fee
