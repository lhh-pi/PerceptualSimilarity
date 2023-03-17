import os
import shutil

folder_path = './imgs/500'

for filename in os.listdir(folder_path):
    # 获取文件的绝对路径
    filepath = os.path.join(folder_path, filename)

    # 修改文件名
    start = filename.find('_')
    end = filename.find('.')
    new_filename = filename[:start] + filename[end:]
    new_filepath = os.path.join(folder_path, new_filename)
    os.rename(filepath, new_filepath)
