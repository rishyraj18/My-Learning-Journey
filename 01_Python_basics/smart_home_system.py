from abc import ABC , abstractmethod

class SmartHome(ABC):
    
    def __init__(self, location):
        self.location = location

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def display_status(self):
        pass
    

class fan(SmartHome):

    def __init__(self,location, status = "off"):
        super().__init__(location)
        self.status = status
        print(f"Fan in {self.location} added")

    def turn_off(self):
        print(f"Fan in {self.location} Tunned Off!")
        self.status = "Off"

    def turn_on(self):
        print(f"Fan in {self.location} Tunned On!")
        self.status = "On"
        
    def power_saver(self):
        print("Fan is set to power saver mode")
        self.status = "Power Saver, On"
    
    def display_status(self):
        print(f"Status : {self.status}")

class Light(SmartHome):

    def __init__(self,location, status = "off"):
        super().__init__(location)
        self.status = status
        print(f"Light in {location} added")

    def turn_off(self):
        print(f"Light in {self.location} Tunned Off!")
        self.status = "Off"

    def turn_on(self):
        print(f"Light in {self.location} Tunned On!")
        self.status = "On"
        
    def power_saver(self):
        print(f"Light in {self.location} is set to Power saver mode")
        self.status = "Power Saver, On"
    
    def display_status(self):
        print(f"Status : {self.status}")

class AC(SmartHome):

    def __init__(self,location, status = "off"):
        super().__init__(location)
        self.status = status
        print(f"AC in {self.location} added")

    def turn_off(self):
        print(f"AC in {self.location} Tunned Off!")
        self.status = "Off"

    def turn_on(self):
        print(f"AC in {self.location} Tunned On!")
        self.status = "On"
        
    def power_saver(self):
        print("AC is set to power saver mode")
        self.status = "Power Saver, On"
    
    def display_status(self):
        print(f"Status : {self.status}")

ac1 = AC("Grd_bedroom")
