from langchain_ai21 import AI21LLM
from langchain_core.pydantic_v1 import Field

from lwe.core.provider import Provider, PresetValue

AI21_DEFAULT_MODEL = 'j2-jumbo-instruct'


class CustomAI21LLM(AI21LLM):

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
        return {
            'models': {
                'j2-large': {
                    'max_tokens': 8192,
                },
                'j2-grande': {
                    'max_tokens': 8192,
                },
                'j2-jumbo': {
                    'max_tokens': 8192,
                },
                'j2-large-instruct': {
                    'max_tokens': 8192,
                },
                'j2-grande-instruct': {
                    'max_tokens': 8192,
                },
                'j2-jumbo-instruct': {
                    'max_tokens': 8192,
                },
            }
        }

    @property
    def default_model(self):
        return AI21_DEFAULT_MODEL

    def llm_factory(self):
        return CustomAI21LLM

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
