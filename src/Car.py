class Car:
    def __init__(self):
        self.engine = Engine()
        self.pedals = Pedals()
        self.steering_wheel = SteeringWheel()

class Engine:
    def __init__(self):
        self.is_running: bool = False
    
    def start(self):
        self.is_running = True
    
    def stop(self):
        self.is_running = False

class Pedals:
    def __init__(self):
        self.go: bool = False
        self.brake: bool = True
    
    def press_gas(self):
        self.go = True
        self.brake = False
    
    def press_brake(self):
        self.go = False
        self.brake = True

class SteeringWheel:
    def __init__(self):
        self.direction = 'straight'
    
    def turn_left(self):
        self.direction = 'left'
    
    def turn_right(self):
        self.direction = 'right'

