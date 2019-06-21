import os
from aip import AipSpeech
from config.config import role_param
APP_ID = '16574959'
API_KEY = 'q88hUF2oNzvG2wEZQfw8nF9N'
SECRET_KEY = 'NDFmAEIzUoviuG5kPmj7SS92sl3vkuCG'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def text2audio(worlds,out_putfile,lang='zh'):
    result=client.synthesis(worlds,lang,1,role_param)

    if not isinstance(result,dict):
        with open(out_putfile,'wb') as f:
            f.write(result)
        return 'ok'

def audio2text(file_name):
    output_file = anything2pcm(file_name)
    result = client.asr(get_file_content(output_file),'pcm',16000,{
        'dev_pid':1536,
    })
    if result['err_no'] == 0:
        print(result['result'][0])
        return result['result'][0]
    else:
        print('识别失败')

def anything2pcm(input_file):
    """将一切格式的音频转为 pcm 格式，需将ffmpeg 添加到环境变量"""
    # input_file = os.path.join(os.getcwd(), input_file)
    output_file = input_file.rsplit('.', 1)[0] + '.pcm'
    cmd = r'D:\ZhuanYe\ffmpeg-20180619-a990184-win64-shared\bin\ffmpeg -y  -i {}  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {}'.format(input_file, output_file)
    print(os.popen(cmd).read())
    # print('转换完成！')
    return output_file

def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

if __name__ == '__main__':
    file_name='hello.mp3'
    # if text2audio(('你好百度'),role_param,file_name,lang='zh'):
    #     print('合成成功')
    # else:
    #     exit('合成失败')

    #测试语音识别
    # output_file = anything2pcm(file_name)
    # result = client.asr(get_file_content(output_file),'pcm',16000,{
    #     'dev_pid':1536,
    # })
    # print(result['result'][0])
    print(audio2text(file_name))
