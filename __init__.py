from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'alex'

LOGGER = getLogger(__name__)


class HelloWorldSkill(MycroftSkill):

    def __init__(self):
        super(HelloWorldSkill, self).__init__(name="HelloWorldSkill")

	def initialize(self):
        hello_world_intent = IntentBuilder("HelloWorldIntent"). \
			require("HelloWorldKeyword").build()
        self.register_intent(Hello_world_intent, self.handle_hello_world_intent)

    def handle_hello_world_intent(self, message):
        self.speak_dialog("wake.up")

    def stop(self):
        pass


def create_skill():
return HelloWorldSkill()
