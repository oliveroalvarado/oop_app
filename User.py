class Info:
    def __init__(self, name, email_address, driver_license, number):
        self.name = name
        self.email_address = email_address
        self.driver_license = driver_license
        self.number = number

    def new_user(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email_address}")
        print(f"Driver's License: {self.driver_license}")
        print(f"Phone number: {self.number}")


oliver = Info("Oliver", "oliver@gmail.com", "E3092AS", "2094839347")
kao = Info("Kao", "kao@gmail.com", "E93734", "2948502984")

oliver.new_user()
kao.new_user()

