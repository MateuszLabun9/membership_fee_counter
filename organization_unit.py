
class OrganizationUnit:  # Organization unit model
    def __init__(self, parent_name):
        self.config = None  # Default configuration is None
        self.parent_name = parent_name  # Parent name used when recursively looking for configuration
        self.has_fixed_membership_fee = False  # Default fee state is False
        self.fixed_membership_fee_amount = 0  # Default fee is 0

