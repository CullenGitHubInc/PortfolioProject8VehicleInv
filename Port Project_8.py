class Automobile:
    def __init__(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage

    # Method to get vehicle details as a string
    def get_vehicle_details(self):
        return f"{self.__year} {self.__make} {self.__model} ({self.__color}) with {self.__mileage} miles"

    # Method to update vehicle attributes
    def update_vehicle(self, make=None, model=None, color=None, year=None, mileage=None):
        if make:
            self.__make = make
        if model:
            self.__model = model
        if color:
            self.__color = color
        if year:
            self.__year = year
        if mileage:
            self.__mileage = mileage

class Inventory:
    def __init__(self):
        self.vehicles = []

    # Method to add a new vehicle
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    # Method to remove a vehicle
    def remove_vehicle(self, index):
        if 0 <= index < len(self.vehicles):
            del self.vehicles[index]

    # Method to update a vehicle
    def update_vehicle(self, index, make=None, model=None, color=None, year=None, mileage=None):
        if 0 <= index < len(self.vehicles):
            self.vehicles[index].update_vehicle(make, model, color, year, mileage)

    # Method to list all vehicles
    def list_vehicles(self):
        for i, vehicle in enumerate(self.vehicles):
            print(f"Vehicle {i+1}: {vehicle.get_vehicle_details()}")

    # Method to save inventory to a file
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for vehicle in self.vehicles:
                file.write(vehicle.get_vehicle_details() + '\n')

# Main function to manage inventory
def main():
    inventory = Inventory()

    # Add some vehicles to the inventory
    inventory.add_vehicle(Automobile("Honda", "Civic", "Black", 2015, 17000))
    inventory.add_vehicle(Automobile("Ford", "Escort", "Blue", 2021, 24000))
    inventory.add_vehicle(Automobile("Toyota", "Tacoma", "White", 2022, 7000))

    # List all vehicles
    print("Current inventory:")
    inventory.list_vehicles()

    # Update a vehicle's details
    inventory.update_vehicle(1, mileage=32000)
    print("\nInventory after update:")
    inventory.list_vehicles()

    # Remove a vehicle
    inventory.remove_vehicle(0)
    print("\nInventory after removal:")
    inventory.list_vehicles()

    # Save inventory to file
    inventory.save_to_file("vehicle_inventory.txt")

# Run the main function
if __name__ == "__main__":
    main()
