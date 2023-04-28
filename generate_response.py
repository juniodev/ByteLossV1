from chatterbot import ChatBot
from chatterbot import comparisons
from chatterbot.response_selection import get_first_response
import spacy
from chatterbot import filters
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
from data_trainer import agrupa_perguntas_respostas

nlp = spacy.load("pt_core_news_sm")

class ISO_639_1:
    ISO_639_1 = 'pt_core_news_sm'
    ISO_639 = 'por'
    EN = 'Portuguese'

class Chat:
    def __init__(self):
        self.name = None
        self.chatbot = self.init_bot()

    def set_name(self, name):
        self.name = name
        self.update_adapter_name()

    def update_adapter_name(self):
        self.chatbot.logic_adapters[1].name = self.name   
    
    def init_bot(self):

        bot = ChatBot(
            'ByteLoss',
            tagger_language=ISO_639_1,
            logic_adapters=[
            {
                'import_path': 'adapters.time_adapter.TimeLogicAdapter'
            },
            {
                'import_path': 'adapters.user_adapter.UserLogicAdapter',
                'name': self.name
            },
            {
                "import_path": "chatterbot.logic.BestMatch",
                "statement_comparison_function": comparisons.LevenshteinDistance,
                "response_selection_method": get_first_response,
                'nlp': nlp
            }
            ],
            preprocessors=[
                'chatterbot.preprocessors.clean_whitespace',
                'chatterbot.preprocessors.unescape_html',
                'chatterbot.preprocessors.convert_to_ascii',
                'chatterbot.preprocessors.clean_whitespace'
            ],
            filters=[
                filters.get_recent_repeated_responses
            ],
            input_adapter="chatterbot.input.VariableInputTypeAdapter",
            output_adapter="chatterbot.output.OutputAdapter",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            database_uri="sqlite:///database.sqlite3"
        )

        list_tainer = agrupa_perguntas_respostas('data.csv')
        trainer = ListTrainer(bot)
        for conversation in list_tainer:
            trainer.train(conversation)

        return bot

    def processar_pergunta(self, pergunta):
        
        text = pergunta.encode('utf-8').decode('utf-8')

        bot = self.chatbot

        statement = Statement(text=text, search_text=text)

        response = bot.get_response(statement)

        return response.text
