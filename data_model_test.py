import unittest
from data_model import DataModel


class DataModelTest(unittest.TestCase):
    test_model = DataModel()
    test_model.get_organization_structure("organization_structure_data.txt", "structure")
    test_model.save_configuration('structure_config.json')

    # Test fetching and saving data from organization_structure_data file
    def test_organization_structure_persistence(self):
        assert self.test_model.branches["branch_a"].parent_name == "area_a"
        assert self.test_model.branches["branch_m"].parent_name == "area_d"
        assert self.test_model.areas["area_a"].parent_name == "division_a"
        assert self.test_model.divisions["division_a"].parent_name == "client"

    # Test fetching and saving data from structure_config file
    def test_data_save_persistence(self):
        assert len(self.test_model.branches.keys()) == 16
        assert len(self.test_model.areas.keys()) == 4
        assert len(self.test_model.divisions.keys()) == 2
        assert len(self.test_model.clients.keys()) == 1

    # Test calculation of membership fee for different cases
    def test_membership_fee_calculation(self):
        assert self.test_model.calculate_membership_fee("week", 300, "branch_a") == 450.0
        assert self.test_model.calculate_membership_fee("month", 3600, "branch_b") == 1080.0
        assert self.test_model.calculate_membership_fee("week", 360, "branch_k") == 250.0
