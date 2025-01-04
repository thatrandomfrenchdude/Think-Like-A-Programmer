class Car:
    '''
    Car class
    
    Attributes:
        engine (Engine): Engine object
        pedals (Pedals): Pedals object
        steering_wheel (SteeringWheel): SteeringWheel object
    '''
    def __init__(self):
        self.engine: Engine = Engine()
        self.pedals: Pedals = Pedals()
        self.steering_wheel: SteeringWheel = SteeringWheel()

class Engine:
    '''
    Engine class
    
    Attributes:
        is_running (bool): Engine status
    '''
    def __init__(self):
        self.is_running: bool = False
    
    def start(self):
        self.is_running = True
    
    def stop(self):
        self.is_running = False

class Pedals:
    '''
    Pedals class
    
    Attributes:
        go (bool): Gas pedal status
        brake (bool): Brake pedal status
    '''
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
    '''
    SteeringWheel class

    Attributes:
        direction (str): Steering direction
    '''
    def __init__(self):
        self.direction = 'straight'
    
    def turn_left(self):
        self.direction = 'left'
    
    def turn_right(self):
        self.direction = 'right'