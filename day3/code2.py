import os
#绝对、文件（夹）存在、文件（1）、文件夹（1）
print(os.path.abspath('code1.py'))
print(os.path.exists('test'))
print(os.path.isfile('test'))
print(os.path.isdir('code1.py'))
#访问、修改、大小
print(os.path.getatime('code1.py'))
print(os.path.getmtime('code2.py'))
print(os.path.getsize('code1.py'))
#命令、当前脚本路径、环境变量
print(os.system('whoami'))
print(os.getcwd())
print(os.environ)
#创建文件夹、删除文件夹、列出文件、改名
# os.mkdir('test2')
# os.rmdir('test1')
print(os.listdir('.'))
# os.rename('test2','test1')

# os.remove('test.py')

#拼接成路径
print(os.path.join('149','q','qeq'))