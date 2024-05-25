import torchaudio
import torch


# attach source wav file to dest wav file
def attach_wav(src_path: str, dest_path: str):
    # Load the source wav file
    src_audio, _ = torchaudio.load(src_path)
    # Load the destination wav file
    dest_audio, _ = torchaudio.load(dest_path)
    # Attach the source wav file to the destination wav file
    audio = torch.cat([dest_audio, src_audio], dim=1)
    # Save the attached wav file
    torchaudio.save(dest_path, audio, 16000)
