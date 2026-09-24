from typing import Protocol
class LLMProvider(Protocol):
    def answer(self,question:str)->str: ...
class DevelopmentProvider:
    def answer(self,question:str)->str:
        return 'Development provider: '+question
