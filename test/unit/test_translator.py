from src.translator import translate_content
from mock import patch
import ipytest


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息.")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_llm_normal_response():
    is_english, translated_content = translate_content("This is an English message.")
    assert is_english == True
    assert translated_content == "This is an English message."

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("askdfalkjwejf klwqj.")
    assert is_english == True
    assert translated_content == "askdfalkjwejf klwqj."

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_unexpected_language(mocker):
    mocker.return_value.text = "I don't understand your request"
    is_english, translated_content = translate_content("Aquí está su primer ejemplo.")
    assert is_english == True
    assert translated_content == "Aquí está su primer ejemplo."

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_return_none(mocker):
    mocker.return_value.text = None
    is_english, translated_content = translate_content("Aquí está su primer ejemplo.")
    assert is_english == True
    assert translated_content == "Aquí está su primer ejemplo."

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_return_nonstring(mocker):
    mocker.return_value.text = []
    is_english, translated_content = translate_content("Aquí está su primer ejemplo.")
    assert is_english == True
    assert translated_content == "Aquí está su primer ejemplo."

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_return_empty(mocker):
    mocker.return_value.text = ""
    is_english, translated_content = translate_content("Aquí está su primer ejemplo.")
    assert is_english == True
    assert translated_content == "Aquí está su primer ejemplo."