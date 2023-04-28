import datetime
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement

class TimeLogicAdapter(LogicAdapter):
    """
    Adaptador de lógica que responde a perguntas relacionadas ao tempo.
    """
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['bom dia', 'boa tarde', 'boa noite']
        return any(word in statement.text.lower() for word in words)

    def process(self, statement, additional_response_selection_parameters=None):
    
        hour = datetime.datetime.now().hour
        if 'bom dia' in statement.text.lower():
            if 5 <= hour < 12:
                response = "Bom dia para você também!"
            elif 12 <= hour < 18:
                response = "Já é tarde para desejar bom dia, mas tudo bem. Como posso ajudar?"
            else:
                response = "Já é noite, mas mesmo assim: bom dia!"
        elif 'boa tarde' in statement.text.lower():
            if 12 <= hour < 18:
                response = "Boa tarde! Em que posso ajudar?"
            else:
                response = "Já é noite, mas mesmo assim: boa tarde!"
        elif 'boa noite' in statement.text.lower():
            if 18 <= hour < 24:
                response = "Boa noite! Em que posso ajudar?"
            elif 0 <= hour < 5:
                response = "Ainda é madrugada, mas mesmo assim: boa noite!"
            else:
                response = "Já é tarde para desejar boa noite, mas tudo bem. Como posso ajudar?"
        else:
            response = "Desculpe, eu não entendi. Poderia reformular a sua pergunta?"
        
        output_statement = Statement(text=response)
        
        output_statement.confidence = 1
        
        return output_statement
