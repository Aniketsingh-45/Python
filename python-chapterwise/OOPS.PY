#ENCAPSULATION
class car:
  brand=None
  model=None

  def __init__(self, car_brand, car_model):# SELF IS NECCESSARY 
    self.brand=car_brand
    self.model=car_model

  def full_name(self):
    print(f"the brand is {self.brand} and model is {self.model}")

first_car=car("toyato", "supra")
first_car.full_name()