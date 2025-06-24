from abc import ABC
from typing import Type

class AIModel(ABC):
    input_model: Type
    output_model: Type
    prompt_template: str

    def run(self, input_data):
        print(f"[MockAI] Running {self.__class__.__name__} with input:")
        print(input_data.dict())
        return self.output_model(**{
            key: self.mock_value(key) for key in self.output_model.__fields__
        })


    def mock_value(self, name):
        if "score" in name:
            return 0.8
        if "level" in name:
            return "Medium"
        if "time" in name:
            return "4 hours"
        if "route" in name:
            return "Tier 2 Support"
        if "escalate" in name:
            return True
        return "unknown"
