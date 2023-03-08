import csv
import argparse
import os
import warnings
from tqdm import tqdm
def extract_plaintexts_from_csv(dir_path):
    file_list = os.listdir(dir_path)
    plaintexts = []
    for csv_filepath in tqdm(file_list):
        # plaintexts = []
        if csv_filepath[-4:] != '.csv':
            warnings.warn('skipping {}, not a csv'.format(csv_filepath))
            continue
        csv_file = open(dir_path + os.path.sep + csv_filepath)
        for line in csv_file.readlines():
            values = line.split(',')
            trigger = values[2]
            PT = values[-1]
            # print("start")
            # print(PT)
            if trigger == '1':
                plaintexts.append(PT)
                break
            plaintexts.append(PT)
            # print(plaintexts)
        break
        csv_file.close()
        # print(plaintexts)
    return plaintexts



def main(args):
    dir_path = args.path_to_dir
    mode = args.mode
    plaintext_path = args.plaintext_path

    assert os.path.isdir(dir_path), "{} is not a directory".format(dir_path)

    known_modes = ['csv']
    assert mode in known_modes, "{} is not a supported mode".format(mode)

    if os.path.isfile(plaintext_path):
        warnings.warn('Overwriting {}'.format(plaintext_path))
    else:
        assert not os.path.isdir(plaintext_path), "{} is a directory".format(plaintext_path)

    if mode == 'csv':
        plaintexts = extract_plaintexts_from_csv(dir_path)

    plaintext_file = open(plaintext_path, 'w+')
    # print(plaintexts)
    plaintext_file.writelines(plaintexts)
    plaintext_file.close()





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_dir', type=str, default='traces', help='Path to data directory')
    parser.add_argument('--mode', type=str, default='csv', help='Format of data in directory')
    parser.add_argument('--plaintext_path', type=str, default='plain.txt', help='File to save plaintexts in')

    args = parser.parse_args()
    main(args)

