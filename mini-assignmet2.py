class Vehicle:
    def __init__(self, color, number_of_doors, gas_powered):
        self.__color = color
        self.__number_of_doors = number_of_doors
        self.__gas_powered = gas_powered

        # Property for color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        allowed_colors = ['red', 'blue', 'green', 'black', 'white']
        if isinstance(value, str) and value.lower() in allowed_colors:
            self.__color = value
        else:
            raise ValueError(f"{value} is not an allowed color. Choose from {allowed_colors}.")

    # Property for number of doors
    @property
    def number_of_doors(self):
        return self.__number_of_doors

    @number_of_doors.setter
    def number_of_doors(self, value):
        allowed_doors = [2, 4, 5]
        if isinstance(value, int) and value in allowed_doors:
            self.__number_of_doors = value
        else:
            raise ValueError("Number of doors must be 2, 4, or 5.")

    # Property for gas-powered
    @property
    def gas_powered(self):
        return self.__gas_powered

    @gas_powered.setter
    def gas_powered(self, value):
        if isinstance(value, bool):
            self.__gas_powered = value
        else:
            raise ValueError("Gas powered must be a Boolean value (True or False).")

    # Method to check if the vehicle is eco-friendly
    def is_eco_friendly(self):
        return self.__number_of_doors == 2 and not self.__gas_powered

    # Override toString
    def __str__(self):
        gas_status = "gas-powered" if self.__gas_powered else "not gas-powered"
        return f"Vehicle: {self.__color}, {self.__number_of_doors} doors, {gas_status}."


# Truck class inheriting from Vehicle
class Truck(Vehicle):
    def __init__(self, color, number_of_doors, gas_powered, seats, trunk_space):
        super().__init__(color, number_of_doors, gas_powered)
        self.__seats = seats  # Private attribute
        self.__trunk_space = trunk_space  # Private attribute

    # Property for seats
    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, value):
        if isinstance(value, int) and value > 0:
            self.__seats = value
        else:
            raise ValueError("Seats must be a whole number greater than zero.")

    # Property for trunk space
    @property
    def trunk_space(self):
        return self.__trunk_space

    @trunk_space.setter
    def trunk_space(self, value):
        if isinstance(value, int) and value > 0:
            self.__trunk_space = value
        else:
            raise ValueError("Trunk space must be a whole number greater than zero.")

    # Override is_eco_friendly to include Truck-specific rules
    def is_eco_friendly(self):
        return super().is_eco_friendly() and self.__seats <= 2 and self.__trunk_space == 0

