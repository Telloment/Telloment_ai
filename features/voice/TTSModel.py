from transformers import AutoTokenizer
import torch
import scipy
from transformers import pipeline
from datasets import load_dataset
import soundfile as sf

# model = VitsModel.from_pretrained("facebook/mms-tts-kor")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-kor")
synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)


def TTS(text: str, save_path: str):
    pass


def TTS_speecht5(text: str, save_path: str):
    speech = synthesiser(text, forward_params={"speaker_embeddings": speaker_embedding})
    sf.write(save_path, speech["audio"], samplerate=speech["sampling_rate"])
