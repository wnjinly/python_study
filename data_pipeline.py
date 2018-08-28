# coding=utf-8
# 创建数据处理管道
import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)

def gen_opener(filenames):
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines) 
for line in pylines:
    print(line)
# 管道方式处理数据可以用来解决各类其他问题。
# 包括解析，读取实时数据，定时轮询等。
# 这种方式一个非常好的特点是，每个生成函数都很小并且独立。
# 这样的话就很容易编写和维护。
# 并且这种方式的内存效率很高，占用内存很小

