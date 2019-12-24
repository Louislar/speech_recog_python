# coding=utf-8
from os import environ, path, listdir
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
        self.wav_dir = '/home/wmlab/CMU_try/testing_audio/3RD_sheng_kai/'
    
    def recognize(self, file_path_in):
        speech_rec = Decoder(hmm = self.model_dir, lm=self.lm_dir, dict=self.dict_dir)
        wavFile = file(file_path_in, 'rb')
        wavFile.seek(44)
        speech_rec.decode_raw(wavFile)
        result = speech_rec.get_hyp()
        print('result: ' + result[0])
        return result[0]

    def recog_multi_file(self, dir_path_in):
        # 讀出資料夾內所有檔案名稱
        files_nm = listdir(dir_path_in)
        # 排序檔案名稱
        sorted_files_nm = sorted(files_nm, key=lambda x: int(x[:-4]))
        # 將所有檔案名稱加入絕對路徑
        abs_files_path = [dir_path_in + f for f in sorted_files_nm]
        # 對所有檔案做辨識
        all_results = [self.recognize(f) for f in abs_files_path]
            
        print(abs_files_path)
        for a in all_results:
            print('result: ' + a) 
        return all_results

if __name__ == "__main__":
    sp_recogzier = CMU_Sphinx_recognizer()
    # sp_recogzier.recognize(sp_recogzier.wav_file)
    sp_recogzier.recog_multi_file(sp_recogzier.wav_dir)