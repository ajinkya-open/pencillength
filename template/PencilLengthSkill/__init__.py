from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler


class PencilLengthSkill(MycroftSkill):
    def __init__(self):
        super(PencilLengthSkill, self).__init__(name="PencilLengthSkill")
        self.already_said_hello = False
        self.be_friendly = True
        self.hello_phrases = ['Hello']

    def initialize(self):
        thank_you_intent = IntentBuilder("ThankYouIntent").require("PencilKeyword").build()
        self.register_intent(thank_you_intent, self.handle_thank_you_intent)

    def handle_hello_world_intent(self, message):
        self.speak_dialog("length.of.pencil")
