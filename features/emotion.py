from init_vars import tokenizer, model, vocab, torch_device
from transformers import BertModel
from models.BERTDataset import BERTDataset
from torch.utils.data import DataLoader
import numpy as np
import torch

tok = tokenizer.tokenize
max_len = 64
batch_size = 64


def _get_classifier() -> BertModel:
    model = torch.load('resources/model/telloment_senti_10.pth')
    model.to(torch_device)
    return model


classifier: BertModel = _get_classifier()


def _predict(predict_sentence):
    data = [predict_sentence, '0']
    dataset_another = [data]

    another_test = BERTDataset(dataset_another, 0, 1, tok, vocab, max_len, True, False)
    test_dataloader = DataLoader(another_test, batch_size=batch_size, num_workers=5)

    classifier.eval()

    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):

        token_ids = token_ids.long().to(torch_device)
        segment_ids = segment_ids.long().to(torch_device)
        valid_length = valid_length
        out = classifier(token_ids, valid_length, segment_ids)
        test_eval = []
        print(out)
        for i in out:
            logits = i
            logits = logits.detach().cpu().numpy()
            print(logits)
            if np.argmax(logits) == 0:  # 분
                test_eval.append("분노")
            elif np.argmax(logits) == 1:
                test_eval.append("슬픔")  # 슬
            elif np.argmax(logits) == 2:
                test_eval.append("행복")  # 행
            elif np.argmax(logits) == 3:
                test_eval.append("중립")  # 중립이

        return test_eval


def get_emotion(text: str) -> (str, int):
    pred = _predict(text)
    return pred[0], 0

