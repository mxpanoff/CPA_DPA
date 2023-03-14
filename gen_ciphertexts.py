import csv
import argparse
import os
import warnings
from tqdm import tqdm
from logging import log
def extract_ciphertexts_from_csv(dir_path):
    file_list = os.listdir(dir_path)
    ciphertexts = []
    for csv_filepath in tqdm(file_list):
        # ciphertexts = []
        if csv_filepath[-4:] != '.csv':
            log('skipping {}, not a csv'.format(csv_filepath))
            continue
        csv_file = open(dir_path + os.path.sep + csv_filepath)
        csv_file.readline()
        csv_file.readline()
        for line in csv_file.readlines():
            values = line.split(',')
            out_valid = values[6]
            CT = values[-1]
            # print("start")
            # print(CT)
            if out_valid == '1':
                ciphertexts.append(CT)
                break
            # ciphertexts.append(PT)
            # print(ciphertexts)
        csv_file.close()
        # print(ciphertexts)
    return ciphertexts



def main(args):
    dir_path = args.path_to_dir
    mode = args.mode
    ciphertext_path = args.ciphertext_path

    assert os.path.isdir(dir_path), "{} is not a directory".format(dir_path)

    known_modes = ['csv']
    assert mode in known_modes, "{} is not a supported mode".format(mode)

    if os.path.isfile(ciphertext_path):
        log('Overwriting {}'.format(ciphertext_path))
    else:
        assert not os.path.isdir(ciphertext_path), "{} is a directory".format(ciphertext_path)

    if mode == 'csv':
        ciphertexts = extract_ciphertexts_from_csv(dir_path)

    ciphertext_file = open(ciphertext_path, 'w+')
    # print(plaintexts)
    ciphertext_file.writelines(ciphertexts)
    ciphertext_file.close()





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_dir', type=str, default='traces', help='Path to data directory')
    parser.add_argument('--mode', type=str, default='csv', help='Format of data in directory')
    parser.add_argument('--ciphertext_path', type=str, default='cipher.txt', help='File to save ciphertexts in')

    args = parser.parse_args()
    main(args)

