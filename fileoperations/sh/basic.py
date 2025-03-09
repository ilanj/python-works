import errno
import os

import sh

sh.pwd()
try:
    sh.mkdir("new_folder")
except Exception as e:
    pass
sh.touch("new_file.txt")
sh.whoami()
sh.echo("This is great!")


def create_dir_if_not_exists(dir_name):
    if not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
