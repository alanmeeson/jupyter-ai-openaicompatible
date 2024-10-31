import os
import json
from typing import ClassVar, List

from langchain_openai import (
    ChatOpenAI,
    OpenAI,
    OpenAIEmbeddings
)

from jupyter_ai_magics.providers import BaseProvider, Field, AuthStrategy, EnvAuthStrategy, TextField
from jupyter_ai_magics.embedding_providers import BaseEmbeddingsProvider


class OpenAICompatibleProvider(BaseProvider, OpenAI):
    """
    A JupyterAI model registry provider for OpenAI compatible APIs.
    """

    id: ClassVar[str] = "openai-compatible"
    name: ClassVar[str] = "OpenAI Compatible"
    models: ClassVar[List[str]] = ["*"]
    help: ClassVar[str] = "Please enter the name of the model as according to your OpenAI compatible API"
    
    model_id_key: ClassVar[str] = "model_name"
    
    pypi_package_deps: ClassVar[List[str]] = ["langchain_openai"]
    api_key: ClassVar[str] = None
    auth_strategy = EnvAuthStrategy(name="OPENAI_API_KEY", keyword_param="api_key")
    registry: ClassVar[bool] = True
    fields: ClassVar[List[Field]] = [
        #TextField(key="model_name", label="Model Name", format="text"),
        TextField(key="base_url", label="Base API URL (optional)", format="text")
    ]


class ChatOpenAICompatibleProvider(BaseProvider, ChatOpenAI):
    """
    A JupyterAI model registry provider for OpenAI compatible APIs.
    """
    id: ClassVar[str] = "openai-chat-compatible"
    name: ClassVar[str] = "OpenAI Chat Compatible"
    models: ClassVar[List[str]] = ["*"]
    help: ClassVar[str] = "Please enter the name of the model as according to your OpenAI compatible API"
    model_id_key: ClassVar[str] = "model_name"
    pypi_package_deps: ClassVar[List[str]] = ["langchain_openai"]
    api_key: ClassVar[str] = None
    auth_strategy = EnvAuthStrategy(name="OPENAI_API_KEY", keyword_param="api_key")

    fields: ClassVar[List[Field]] = [
        TextField(key="model_name", label="Model Name", format="text"),
        TextField(key="base_url", label="Base API URL (optional)", format="text")
    ]


# Hold off on this one until jupyter-ai supports embedding configuration
# class OpenAIEmbeddingsProvider(BaseEmbeddingsProvider, OpenAIEmbeddings):
#    id = "openai-compatible"
#    name = "OpenAI Compatible"
#    models = json.loads(os.getenv("OPENAI_EMBEDDING_MODELS", '["*"]'))
#    model_id_key = "model"
#    pypi_package_deps = ["langchain_openai"]
#    api_key: ClassVar[str] = None
#    auth_strategy = EnvAuthStrategy(name="OPENAI_EMBEDDING_KEY", keyword_param="api_key")
#    base_url = os.getenv("OPENAI_EMBEDDING_URL")
