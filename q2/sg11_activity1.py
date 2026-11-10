class Patient:
  def __init__(self, name, bill_amount):
    self._name = name
    self._bill_amount = bill_amount

  def get_name(self):
    return self._name

  def set_name(self):
    self._name = name

  def get_bill_amount(self):
    return self._bill_amount

  def set_bill_amount(self, bill_amount):
    if bill_amount >= 0:
      self._bill_amount = bill_amount
    else:
      return "Bill amount must not be negative."

  def calculate_bill(self):
    return self._bill_amount

  def display_patient_type(self):
    return "Regular Patient"

class SeniorPatient(Patient):
  def calculate_bill(self):
    new_bill = (self._bill_amount)*0.2
    return new_bill

  def display_patient_type(self):
    return "Senior Patient"

class PhilHealthPatient(Patient):
  def calculate_bill(self):
    new_bill = (self._bill_amount)*0.15
    return new_bill
    
  def display_patient_type(self):
    return "PhilHealth Patient"

patient = Patient("Juan Dela Cruz", 15000)

print("")
print("Hospital Billing System")
print("-----------------------")
print(f"Patient name: {patient._name}")
print(f"Patient type: ", patient.display_patient_type())
print(f"Original Bill: ₱{patient._bill_amount:,.2f}")
print(f"Final Bill: ₱{patient.calculate_bill():,.2f}")
