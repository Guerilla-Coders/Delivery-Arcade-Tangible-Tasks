import time
from typing import List

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


class StepperController:
    coil_delay = 0.001
    steps_per_revolution = 2048
    seq_full_step = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
    seq_half_step = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1],
    ]

    def __init__(self, enable_pin: int, coil_pins: List[int]):
        self.enable_pin = enable_pin
        self.coil_pins = coil_pins
        self.seq = self.seq_half_step
        self.num_seq = len(self.seq)

        for pin in [self.enable_pin] + self.coil_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

    def enable_motor(self):
        GPIO.output(self.enable_pin, True)
        print("Enabled motor")
        time.sleep(self.coil_delay)

    def disable_motor(self):
        GPIO.output(self.enable_pin, False)
        print("Disabled motor")
        time.sleep(self.coil_delay)

    def steps(self, num_steps):
        print(f"{num_steps} steps in {'CCW' if num_steps < 0 else 'CW'} direction")

        counter = range(num_steps) if num_steps >= 0 else range(-num_steps, 0)
        for i in counter:
            step_pointer = i % self.num_seq
            for j, pin in enumerate(self.coil_pins):
                GPIO.output(pin, self.seq[step_pointer][j] == 1)
            time.sleep(self.coil_delay)


if __name__ == '__main__':
    stepper = StepperController(18, [24, 25, 8, 7])

    stepper.enable_motor()
    stepper.steps(stepper.steps_per_revolution)
    stepper.steps(-stepper.steps_per_revolution)
    stepper.disable_motor()

