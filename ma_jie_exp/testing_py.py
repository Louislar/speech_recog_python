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
        self.lm_dir = '/home/wmlab/speech_recog_python/ma_jie_exp/3256.lm'
        self.dict_dir = '/home/wmlab/speech_recog_python/ma_jie_exp/3256.dic'
        # self.lm_dir = '/home/wmlab/CMU_try/try_python/6687.lm'
        # self.dict_dir = '/home/wmlab/CMU_try/try_python/6687.dic
        # self.lm_dir = '/home/wmlab/CMU_try/try_python/usable_version/0506.lm'
        # self.dict_dir = '/home/wmlab/CMU_try/try_python/usable_version/0506.dic'
        # self.wav_file = '/home/wmlab/CMU_try/testing_audio/testing003.wav'
        # self.wav_file = '/home/wmlab/CMU_try/testing_audio/testing_du_coffee_bag.wav'
        self.wav_file = '/home/wmlab/speech_recog_python/ma_jie_exp/hao_ni_ma.wav'
        self.wav_dir = '/home/wmlab/CMU_try/testing_audio/3RD_sheng_kai/'
        self.recog_order_nm = ['FM2', 'K他命', 'K他命k煙', 'K他命拉k', '一粒眠紅豆', '卡西同浴鹽', \
            '卡西同類喵喵', '大麻', '安非他命', '安非他命吸食器', '搖頭丸', '毒咖啡包', \
            '毒梅粉', '海洛因', '海洛因和注射器', '海洛因注射']
    
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
    
    def check_correctness(self, recog_result):
        # print(len(self.recog_order_nm))
        correctness_list = []
        for i in range(len(self.recog_order_nm)): 
            cur_recog_result = recog_result[i]
            cur_recog_result = cur_recog_result.split(' ')
            correctness = \
                [rlt == self.recog_order_nm[i] for rlt in cur_recog_result]
            # print(correctness)
            # print(any(correctness))
            correctness_list.append(any(correctness))
        correctness_list = [str(s) + '\n' for s in correctness_list]
        print(correctness_list)
        with open('./correctness_out.txt', 'w') as open_file: 
            open_file.writelines(correctness_list)
        return correctness_list

if __name__ == "__main__":
    sp_recogzier = CMU_Sphinx_recognizer()
    sp_recogzier.recognize(sp_recogzier.wav_file)
    # recog_result = sp_recogzier.recog_multi_file(sp_recogzier.wav_dir)
    # sp_recogzier.check_correctness(recog_result)