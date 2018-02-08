# 하위 디렉토리 검색하기

# C:/Python/sub_dir_search.py

# 방법1

import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

search("C:/")

# 방법2 : os.walk 이

import os

for (path, dir, files) in os.walk("C:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py'
            print("%s%s" % (path, filename))
