from mycroft import MycroftSkill, intent_file_handler


class DrillPressVise(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('vise.press.drill.intent')
    def handle_vise_press_drill(self, message):
        self.speak_dialog('vise.press.drill')
        self.speak("Drill Press Vise")


def create_skill():
    return DrillPressVise()
