from src.translator import translate_content


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_llm_normal_response():
    is_english, translated_content = translate_content("This is an English message")
    assert is_english == True
    assert translated_content == "This is an English message"

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("askdfalkjwejf klwqj")
    assert is_english == True
    assert translated_content == "askdfalkjwejf klwqj"

# @patch('vertexai.preview.language_models._PreviewChatSession.send_message')
# def test_unexpected_language(mocker):
#   mocker.return_value.text = "I don't understand your request"
#   assert translate_content("Aquí está su primer ejemplo.") == (True, "Aquí está su primer ejemplo.")

# @patch('vertexai.preview.language_models._PreviewChatSession.send_message')
# def test_return_none(mocker):
#   mocker.return_value.text = None
#   assert query_llm_robust("Aquí está su primer ejemplo.") == (True, "Aquí está su primer ejemplo.")

# @patch('vertexai.preview.language_models._PreviewChatSession.send_message')
# def test_return_nonstring(mocker):
#   mocker.return_value.text = []
#   assert query_llm_robust("Aquí está su primer ejemplo.") == (True, "Aquí está su primer ejemplo.")

# @patch('vertexai.preview.language_models._PreviewChatSession.send_message')
# def test_return_empty(mocker):
#   mocker.return_value.text = ""
#   assert query_llm_robust("Aquí está su primer ejemplo.") == (True, "Aquí está su primer ejemplo.")