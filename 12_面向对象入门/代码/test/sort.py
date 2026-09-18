
def sort1(l) -> list:
    lis = list(l)          # 先拷贝，避免修改原列表
    return sorted(lis, reverse=True)

def sort2(l) -> list:
    return sorted(l)

def find_index(l, n) -> list:
    return [i for i in range(len(l)) if l[i] == n ]

# 模块名称
# 1.如果在当前文件执行，则__name__的值是"__main__"
# 2.在其他地方导入当前模块后，在其他地方执行，则__name__是当前模块名 test.sort
print('__name__', __name__)  # __main__

# 1. 作为文件入口： 代码开始执行的地方
# 2. 在当前模块的测试代码
if __name__ == '__main__':
    print(sort1([1,2,3,4,5]))



print(find_index.__name__)  # 函数名称 find_index