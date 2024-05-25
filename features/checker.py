# check file is wav format

def _is_wav_header(file_path: str) -> bool:
    with open(file_path, 'rb') as file:
        header = file.read(4)
    return header == b'RIFF'


def is_wav(file: File) -> bool:
    if not _is_wav_header(file.filename):
        return false
    return file.filename.endswith('.wav')
