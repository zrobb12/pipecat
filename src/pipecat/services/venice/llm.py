from pipecat.services.openai.llm import OpenAILLMService

class VeniceLLMService(OpenAILLMService):
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = "https://api.venice.ai/v1",  # Replace if Venice uses a different endpoint
        model: str = "your-venice-model",            # Replace with your actual Venice model name
        **kwargs,
    ):
        """
        Initialize the Venice LLM service.

        Args:
            api_key: Venice API key.
            base_url: Venice API endpoint.
            model: Model name for Venice.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(api_key=api_key, base_url=base_url, model=model, **kwargs)
