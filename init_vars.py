import torch
from kobert_tokenizer import KoBERTTokenizer
from transformers import BertModel
import gluonnlp as nlp

torch_device = torch.device("mps" if torch.cuda.is_available() else "cpu") #todo mps to amd gpu
tokenizer = KoBERTTokenizer.from_pretrained('skt/kobert-base-v1')
model = BertModel.from_pretrained('skt/kobert-base-v1')
vocab = nlp.vocab.BERTVocab.from_sentencepiece(tokenizer.vocab_file, padding_token='[PAD]')
