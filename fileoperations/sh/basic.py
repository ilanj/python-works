import sh

sh.pwd()
try:
    sh.mkdir('new_folder')
except Exception as e:
    pass
sh.touch('new_file.txt')
sh.whoami()
sh.echo('This is great!')