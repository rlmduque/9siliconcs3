class Vehicle:
  def move(self):
    pass

  def start_trip(self, vehicle):
    vehicle.move

class Car(Vehicle):
  def move(self):
    print("The car drives on the road.")

class Boat(Vehicle):
  def move(self):
    print("The boat sails on water.")

class Drone(Vehicle):
  def move(self):
    print("The drone flies in the sky.")

car = Car()
boat = Boat()
drone = Drone()

car.move()
boat.move()
drone.move()

car.start_trip(car)
boat.start_trip(boat)
drone.start_trip(drone)
