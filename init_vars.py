import torch
from kobert_tokenizer import KoBERTTokenizer
from transformers import BertModel
import gluonnlp as nlp
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    clova_secret: str
    clova_id: str
    model_config = SettingsConfigDict(env_file=".env")

configs = Settings()

torch_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = KoBERTTokenizer.from_pretrained('skt/kobert-base-v1')
model = BertModel.from_pretrained('skt/kobert-base-v1')
vocab = nlp.vocab.BERTVocab.from_sentencepiece(tokenizer.vocab_file, padding_token='[PAD]')
