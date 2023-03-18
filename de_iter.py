import argparse
import os

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-f', "--folder_path", type=str, default='')

opt = parser.parse_args()

folder_path = opt.folder_path

for filename in os.listdir(folder_path):
    # 获取文件的绝对路径
    filepath = os.path.join(folder_path, filename)

    # 修改文件名
    # start = filename.find('_')
    # end = filename.find('.')
    # new_filename = filename[:start] + filename[end:]
    new_filename = filename[:4] + '.png'
    new_filepath = os.path.join(folder_path, new_filename)
    os.rename(filepath, new_filepath)
