import os

# os  用于获取系统的功能，主要用于操作文件或者文件夹

print(os.name)   # nt 表示window操作系统
print(os.getcwd())   # 当前目录


# 创建目录: mkdir()  如果文件存在会报错
# 创建多层目录: makedirs('a/b/c')
if not os.path.exists('test'):
    os.mkdir('test')
# os.makedirs('test/test1/test2')

# 删除空目录: rmdir

# 删除文件: remove


# 重命名: rename
# os.rename('hello','hello2')

# listdir() : 返回指定目录下的所有文件或文件夹名组成的列表
dir_list = os.listdir('test')
print(dir_list)

# dir_list = os.listdir(r'C:\Users\EDY\Desktop\Python\pythonProject\11_Python常用模块\代码')
print(dir_list)

# os.path
#  os.path.exists : 文件或文件夹是否存在
#  os.path.isfile() : 是否为文件
# os.path.isdir() : 是否为目录

print(os.path.exists(r'C:\Users\EDY\Desktop\Python')) # True
print(os.path.isfile(r'C:\Users\EDY\Desktob\Python')) # False

# 合并路径

print(os.path.join(r'C:\Users\EDY\Desktop\Python', 'a.py'))


# 需求: 将指定目录下的子目录的绝对路径打印
path = r'E:\github-workspace\python-study\11_Python常用模块\代码'
list_dir = os.listdir(path)
print(list_dir)  # ['01_os模块(了解).py', '02_json模块.py', '03_时间模块time和datetime.py', '04_文件操作.py', '10作业答案', 'hello.json', 'hello.xml', 'test']

for i in list_dir:
    tmp_dir = os.path.join(path, i)  # 拼接路径
    if os.path.isdir(tmp_dir):
        print(tmp_dir)

    if os.path.isfile(tmp_dir):
        print("文件:", tmp_dir)
    else:
        print('目录:', tmp_dir)

# 绝对路径: 从盘符开始的路径
# 相对路径: 从当前文件所在目录开始的路径
# 项目路径: 从项目根目录往下找

# os.path.split : 拆分

print(os.path.split(r'E:\github-workspace\python-study\11_Python常用模块\代码'))  # ('E:\\github-workspace\\python-study\\11_Python常用模块', '代码')

# os.path.splitext() : 拆分文件的扩展名
print(os.path.splitext(r'E:\github-workspace\python-study\11_Python常用模块\代码\hello.json')) # ('E:\\github-workspace\\python-study\\11_Python常用模块\\代码\\hello', '.json')

# 文件大小:字节 (了解)
print()
print(os.path.getsize('hello.json')) # 204

# 绝对路径  (了解)
print()
print(os.path.abspath('hello.json'))  # E:\github-workspace\python-study\11_Python常用模块\代码\hello.json





