from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement

class UserLogicAdapter(LogicAdapter):
    """
    Adaptador de lógica que nome do usuario
    """
    def __init__(self, chatbot, **kwargs):
        self.name = kwargs.get('name')
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['você sabe meu nome?', 'quem eu sou', 'você me conhece', 'qual meu nome?', 'quem sou eu?', 'voce me conhece?', 'qual meu nome?']
        return any(word in statement.text.lower() for word in words)

    def process(self, statement, additional_response_selection_parameters=None):
        
        output_statement = Statement(text="Eu sei quem você é, seu nome é {}, estou certo?".format(self.name))
        
        output_statement.confidence = 1
        
        return output_statement
