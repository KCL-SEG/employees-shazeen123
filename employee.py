"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    def __init__(self, name, salaryContract, hourlyContract, bonusCommission, contractCommission):
        self.name = name
        self.bonusCommission = bonusCommission
        self.salaryContract = salaryContract
        self.numberOfContracts = 0
        self.hours = 0
        self.hourlyContract = hourlyContract
        self.contractCommission = contractCommission
        
        
    def get_pay(self):
        if self.salaryContract > 0:
            return self.salaryContract + (self.numberOfContracts * self.contractCommission) + self.bonusCommission
        else:
            return self.hourlyContract * self.hours + (self.numberOfContracts * self.contractCommission) + self.bonusCommission
        pass

    def set_contracts(self, contractTotal):
        self.numberOfContracts = contractTotal
    
    def set_hours(self, workingHours):
        self.hours = workingHours

    def __str__(self):
        if self.salaryContract > 0:
            if self.bonusCommission == 0 and self.contractCommission == 0:
                return f'{self.name} works on a monthly salary of {self.salaryContract}. Their total pay is {self.get_pay()}.'
            elif self.bonusCommission == 0:
                return f'{self.name} works on a monthly salary of {self.salaryContract} and receives a commission for {self.numberOfContracts} contract(s) at {self.contractCommission}/contract. Their total pay is {self.get_pay()}.'
            else:
                return f'{self.name} works on a monthly salary of {self.salaryContract} and receives a bonus commission of {self.bonusCommission}. Their total pay is {self.get_pay()}.'
        else:
            if self.bonusCommission == 0 and self.contractCommission == 0:
                return f'{self.name} works on a contract of {self.hours} hours at {self.hourlyContract}/hour. Their total pay is {self.get_pay()}.'
            elif self.bonusCommission == 0:
                return f'{self.name} works on a contract of {self.hours} hours at {self.hourlyContract}/hour and receives a commission for {self.numberOfContracts} contract(s) at {self.contractCommission}/contract. Their total pay is {self.get_pay()}.'
            else:
                return f'{self.name} works on a contract of {self.hours} hours at {self.hourlyContract}/hour and receives a bonus commission of {self.bonusCommission}. Their total pay is {self.get_pay()}.'



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 25, 0, 0)
charlie.set_hours(100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 200)
renee.set_contracts(4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 25, 0, 220)
jan.set_hours(150)
jan.set_contracts(3)
print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 1500, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 30, 600, 0)
ariel.set_hours(120)
