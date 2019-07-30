from mycroft import MycroftSkill, intent_file_handler


class RecipeCake(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('cake.recipe.intent')
    def handle_cake_recipe(self, message):
        self.speak_dialog('cake.recipe')


def create_skill():
    return RecipeCake()

