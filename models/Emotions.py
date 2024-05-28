from enum import Enum


class Emotions(Enum):
    HAPPY = (1, '행복')
    SAD = (2, '슬픔')
    ANGRY = (3, '화남')
    NEUTRAL = (4, '중립')

    def __init__(self, num: int, description: str):
        self.num = num
        self.description = description

    @staticmethod
    def from_description(description: str):
        for emotion in Emotions:
            if emotion.description == description:
                return emotion
        return None
