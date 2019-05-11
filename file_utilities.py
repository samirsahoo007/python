import os
import sys
import glob
import mimetypes
from shutil import copyfile
import subprocess


def split_all(source_directory, destination_directory, extension='txt'):
    """
         Traverse Folder and Split files in destination
    """
    os.chdir(source_directory)
    for fn in glob.glob('*.' + extension):
        pattern = fn[:-4] + '_'
        file_path = os.path.join(source_directory, fn)
        dest_path = os.path.join(destination_directory, pattern)
        split_file_by_line(file_path, 5000, 'txt', dest_path)


def split_file_by_line(source_file, no_of_lines, extension, destination_path):
    """
        Split a file in number of files based on line number given
    """
    cmd = 'gsplit -l ' + str(
        no_of_lines) + ' --additional-suffix=.' + extension + ' ' + source_file + ' ' + destination_path
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)


def mv_lines(source_directory, line_limit, pattern, extension, destination_directory):
    """
        Move files to other destination based on number of lines in a text file
    """
    os.chdir(source_directory)
    files = []
    for fn in glob.glob('*.' + extension):
        file_path = os.path.join(source_directory, fn)
        # Is it a text file?
        m_type = mimetypes.guess_type(file_path)

        if m_type[0] == 'text/plain':
            with open(fn) as f:
                file_lines = len(f.readlines())

                if pattern == '>':
                    if file_lines > line_limit:
                        files.append(fn)

                if pattern == '<':
                    if file_lines < line_limit:
                        files.append(fn)

                if pattern == '=':
                    if file_lines == line_limit:
                        files.append(fn)
    if len(files) > 0:
        [copyfile(source_directory + '/' + f, destination_directory + '/' + f) for f in files]

