import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Define question-answer pairs
pairs = [
    ["hello", ["Hi there!", "Hello! How can I help you?", "Hey! Nice to meet you!"]],
    ["how are you?", ["I'm a bot, but I'm doing great! How about you?"]],
    ["what is your name?", ["I am AI-Chatbot.", "You can call me Chatbot."]],
    ["bye", ["Goodbye!", "See you next time!", "Take care!"]],
    ["مرحباً", ["مرحباً بك! كيف يمكنني مساعدتك؟"]],
    ["كيف حالك؟", ["أنا روبوت وأقوم بعملي على أكمل وجه!"]],
    ["ما اسمك؟", ["اسمي هو AI-Chatbot.", "يمكنك مناداتي بـ Chatbot."]],
    ["وداعاً", ["إلى اللقاء!", "أتمنى لك يومًا سعيدًا!"]],
]

# Create chatbot model
chat = Chat(pairs, reflections)

# Define a default response
DEFAULT_RESPONSE = "I am sorry, I didn't understand that. Could you rephrase it?" \
                   " | عذرًا، لم أفهم ما قلت. هل يمكنك إعادة صياغته؟"

# Chatbot response function
def chatbot_response(user_input):
    response = chat.respond(user_input)
    if response:
        return response
    return DEFAULT_RESPONSE  # Use the default response for unmatched inputs
