#! /usr/bin/python3
'A short utility for re-containering video files into mkv format.'
import subprocess as sbp
from multiprocessing import Pool

def get_file_names():
    'runs find and returns dict of lists containing video filepaths.'
    find_return = sbp.check_output('find').decode('UTF-8')
    find_return = find_return.split('\n')
    mp4 = []
    avi = []
    for path in find_return:
        extension = path[-4:]
        if extension == '.mp4':
            mp4.append(path)
        elif extension == '.avi':
            avi.append(path)
    print(mp4)
    print(avi)
    return mp4

def to_mkv(filepath=None):
    'Runs ffmpeg to re-container given file.'
    if filepath is not None:
        in_file = filepath
        out_file = filepath.replace(filepath[-3:], 'mkv')
    ret_val = sbp.call(['ffmpeg', '-i', in_file, '-vcodec',
             'copy', '-acodec', 'copy', out_file,
             '-loglevel', 'error', '-y'])
        #'ffmpeg -i {} -vcodec copy -acodec copy {}'.format(in_file, out_file))
    if ret_val is 0:
        sbp.call(['rm', '-f', in_file])
    print(out_file)

def convert_files(filelist=None):
    'Takes a list of filespaths and assings a pool worker to convert it.'
    pool = Pool(16)
    results = pool.map(to_mkv, filelist)
    pool.close()
    pool.join()
    return results

def main():
    'main loop, gets the list of non .mkv files and converts them.'
    to_conv = get_file_names()
    convert_files(to_conv)

if __name__ == '__main__':
    main()
