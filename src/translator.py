from vertexai.preview.language_models import ChatModel, InputOutputTextPair
from stopit import threading_timeoutable as timeoutable

chat_model = ChatModel.from_pretrained("chat-bison@001")

def get_translation(post: str) -> str:
    parameters = {
        "temperature": 0.7,
        "max_output_tokens": 256,
    }

    context = "You are translating queries from other languages into English"
    chat = chat_model.start_chat(context=context)
    response = chat.send_message(post, **parameters)
    return response.text

def get_language(post: str) -> str:
    parameters = {
        "temperature": 0.7,
        "max_output_tokens": 256,
    }

    context = "You are identifying the language of the given query"
    chat = chat_model.start_chat(context=context)
    response = chat.send_message(post, **parameters)
    return response.text

def translate_content(content: str) -> tuple[bool, str]:
  result = translate_content_helper(content, timeout=10)
  if result == None:
    return (True, content)
  return result

@timeoutable()
def translate_content_helper(content: str):
  lang = get_language(content)
  translation = get_translation(content)

  if lang == None or translation == None:
    return None
  if not isinstance(lang, str) or not isinstance(translation, str):
    return None
  if len(lang) == 0 or len(translation) == 0:
    return None

  langs = lang.split(" ")
  if len(langs) >= 5:
    return None

  if langs[0].lower() == "English".lower():
    return (True, content)
  return (False, translation)
