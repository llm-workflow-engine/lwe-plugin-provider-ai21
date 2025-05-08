from langchain_ai21.chat_models import ChatAI21
from pydantic import Field

from lwe.core.provider import Provider, PresetValue

AI21_DEFAULT_MODEL = 'jamba-large'


class CustomChatAI2(ChatAI21):

    model: str = Field(default=AI21_DEFAULT_MODEL)
    """Model name to use."""


class ProviderAi21(Provider):
    """
    Access to AI21 models
    """

    @property
    def model_property_name(self):
        return 'model'

    @property
    def capabilities(self):
        return {}

    @property
    def default_model(self):
        return AI21_DEFAULT_MODEL

    @property
    def static_models(self):
        return {
            'jamba-mini': {
                'max_tokens': 262144,
            },
            'jamba-large': {
                'max_tokens': 262144,
            },
        }

    def llm_factory(self):
        return CustomChatAI2

    def customization_config(self):
        return {
            'model': PresetValue(str, options=self.available_models),
            'temperature': PresetValue(float, min_value=0.0, max_value=1.0),
            'maxTokens': PresetValue(int, min_value=1),
            'minTokens': PresetValue(int, min_value=0),
            'topP': PresetValue(float, min_value=0.0, max_value=1.0),
            'numResults': PresetValue(int, min_value=1),
            'presencePenalty': {
                'scale': PresetValue(float, min_value=0.0, max_value=5.0),
                'applyToWhitespaces': PresetValue(bool),
                'applyToPunctuations': PresetValue(bool),
                'applyToNumbers': PresetValue(bool),
                'applyToStopwords': PresetValue(bool),
                'applyToEmojis': PresetValue(bool)
            },
            'countPenalty': {
                'scale': PresetValue(float, min_value=0.0, max_value=5.0),
                'applyToWhitespaces': PresetValue(bool),
                'applyToPunctuations': PresetValue(bool),
                'applyToNumbers': PresetValue(bool),
                'applyToStopwords': PresetValue(bool),
                'applyToEmojis': PresetValue(bool)
            },
            'frequencyPenalty': {
                'scale': PresetValue(float, min_value=0.0, max_value=5.0),
                'applyToWhitespaces': PresetValue(bool),
                'applyToPunctuations': PresetValue(bool),
                'applyToNumbers': PresetValue(bool),
                'applyToStopwords': PresetValue(bool),
                'applyToEmojis': PresetValue(bool)
            },
        }
