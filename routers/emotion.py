from fastapi import APIRouter
from features import emotion

router = APIRouter()
path = "/emotion"


@router.get(path, tags=["emotion"])
async def get_emotion(text: str):
    (emo, n) = emotion.get_emotion(text)
    return {
        "emotion": emo,
        "score": n,
    }


# functions that set list of float to 0 to 1 that sum of all elements is 1

def normalize_list(lst: list) -> list:
    # add min value to each element of list if lst has negative value
    min_val = min(lst)
    if min_val < 0:
        lst = [x + abs(min_val) for x in lst]

    # normalize lst
    sum_lst = sum(lst)
    return [x / sum_lst for x in lst]

    # log scale normalization
    # return [np.log(x+1) for x in lst]