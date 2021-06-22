from pyramid.view import (
    view_config,
    view_defaults
    )
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='192.168.0.10')
led = LED(17, pin_factory=factory)

@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='button')
    def home(self):
        return {}
    @view_config(route_name='ledon')
    def ledon(self):
        led.on()
        return {}
    @view_config(route_name='ledoff')
    def ledoff(self):
        led.off()
        return {}
