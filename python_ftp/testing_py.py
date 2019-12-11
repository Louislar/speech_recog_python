from os import environ, path
from pocketsphinx import Decoder
from sphinxbase import *



# model_dir = '/home/wmlab/CMU_try/zh_broadcastnews_ptm256_8000/'
# lm_dir = '/home/wmlab/CMU_try/try_python/6687.lm'
# dict_dir = '/home/wmlab/CMU_try/try_python/6687.dic'
# # lm_dir = '/home/wmlab/CMU_try/try_python/usable_version/0506.lm'
# # dict_dir = '/home/wmlab/CMU_try/try_python/usable_version/0506.dic'
# # wav_file = '/home/wmlab/CMU_try/testing_audio/testing003.wav'
# # wav_file = '/home/wmlab/CMU_try/testing_audio/testing_du_coffee_bag.wav'
# wav_file = '/home/wmlab/CMU_try/testing_audio/testing_karshi.wav'

# speech_rec = Decoder(hmm = model_dir, lm=lm_dir, dict=dict_dir)
# wavFile = file(wav_file, 'rb')
# wavFile.seek(44)
# speech_rec.decode_raw(wavFile)
# result = speech_rec.get_hyp()
# print(result[0])

class CMU_Sphinx_recognizer():
    def __init__(self):
        self.model_dir = '/home/wmlab/CMU_try/zh_broadcastnews_ptm256_8000/'
        self.lm_dir = '/home/wmlab/CMU_try/try_python/6687.lm'
        self.dict_dir = '/home/wmlab/CMU_try/try_python/6687.dic'
        # self.lm_dir = '/home/wmlab/CMU_try/try_python/usable_version/0506.lm'
        # self.dict_dir = '/home/wmlab/CMU_try/try_python/usable_version/0506.dic'
        # self.wav_file = '/home/wmlab/CMU_try/testing_audio/testing003.wav'
        # self.wav_file = '/home/wmlab/CMU_try/testing_audio/testing_du_coffee_bag.wav'
        self.wav_file = '/home/wmlab/CMU_try/testing_audio/testing_karshi.wav'
    
    def recognize(self):
        speech_rec = Decoder(hmm = self.model_dir, lm=self.lm_dir, dict=self.dict_dir)
        wavFile = file(self.wav_file, 'rb')
        wavFile.seek(44)
        speech_rec.decode_raw(wavFile)
        result = speech_rec.get_hyp()
        print(result[0])
        return result[0]

if __name__ == "__main__":
    sp_recogzier = CMU_Sphinx_recognizer()
    sp_recogzier.recognize()