from enum import Enum


class Emotions(Enum):
    HAPPY = (1, '행복', 2)
    SAD = (2, '슬픔', 1)
    ANGRY = (3, '화남', 3)
    NEUTRAL = (4, '중립', 0)

    def __init__(self, num: int, description: str, clova_code):
        self.num = num
        self.description = description
        self.clova_code = clova_code

    @staticmethod
    def from_description(description: str):
        for emotion in Emotions:
            if emotion.description == description:
                return emotion
        return None
