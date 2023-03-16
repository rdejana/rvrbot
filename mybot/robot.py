import traitlets
from traitlets.config.configurable import SingletonConfigurable
from .motor import Motor
class Robot(SingletonConfigurable):
    left_motor = traitlets.Instance(Motor)
    right_motor = traitlets.Instance(Motor)

    def __init__(self, *args, **kwargs):
        super(Robot, self).__init__(*args, **kwargs)
        self.left_motor = Motor()
        self.right_motor = Motor()

    def set_motors(self, left_speed, right_speed):
        self.left_motor.value = left_speed
        self.right_motor.value = right_speed

    def forward(self, speed=1.0, duration=None):
        self.left_motor.value = speed
        self.right_motor.value = speed

    def backward(self, speed=1.0):
        self.left_motor.value = -speed
        self.right_motor.value = -speed

    def left(self, speed=1.0):
        self.left_motor.value = -speed
        self.right_motor.value = speed

    def right(self, speed=1.0):
        self.left_motor.value = speed
        self.right_motor.value = -speed

    def stop(self):
        self.left_motor.value = 0
        self.right_motor.value = 0