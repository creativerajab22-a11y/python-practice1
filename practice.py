class EChallanSystem:
    def __init__(self, city):
        self.city = city
        self.violations = {
            "not wearing seat belts": 1535,
            "red-light violations": 3416,
            "driving without a helmet": 507,
            "wrong parking": 7.32,  # percentage
            "missing U-turns": 5.5   # percentage
        }
        self.total_challans = 6662
        self.total_amount_in_rupees = 1.25 * 10**7  # 1.25 crore rupees
    def show_summary(self):
        print(f"E-Challan System in {self.city}")
        print(f"Total Challans issued in 6 hours: {self.total_challans}")
        print(f"Total amount collected: Rs. {self.total_amount_in_rupees:,}")
        print("\nBreakdown of violations:")
        for violation, count in self.violations.items():
            if isinstance(count, int):
                print(f"- {count} challans for {violation}")
            else:
                print(f"- {count}% for {violation}")
    def calculate_amount_per_challan(self):
        return self.total_amount_in_rupees / self.total_challans
    def display_accountability_message(self):
        print("\nAccountability should be two-way for the drivers and for those responsible for the city's infrastructure.")
        print("When basic infrastructure doesn’t exist, no proper lanes, no clear signs, no proper parking how can citizens be expected to follow the rules?")
        print("It's time to fix the system too.")
# Usage example:
karachi_echallan = EChallanSystem("Karachi")
karachi_echallan.show_summary()
print(f"\nAverage amount per challan: Rs. {karachi_echallan.calculate_amount_per_challan():,.2f}")
karachi_echallan.display_accountability_message()
