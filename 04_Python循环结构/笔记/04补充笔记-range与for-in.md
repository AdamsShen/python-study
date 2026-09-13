# 补充笔记：深入理解 range 与 for...in

> 对应 04笔记.md 中《for循环》一节的补充说明
>
> 解决的问题：
> 1. `range(len(nums))` 返回的类型到底是什么？
> 2. `for ... in` 后面为什么可以直接跟 range，而不是数组？

---

## 一、`range(len(nums))` 的类型是 range

```python
nums = [10, 20, 30]
r = range(len(nums))   # r = range(0, 3)

print(type(r))         # <class 'range'>
print(r)               # range(0, 3)
print(list(r))         # [0, 1, 2]
```

`range` 的特点：

- **惰性序列**：不会真的生成一整个列表，只是"记住"起始值、结束值、步长，按需现场计算产生整数。所以即使 `len(nums)` 有一亿，`range` 也几乎不占内存。
- **不可变**：不能修改里面的元素，没有 `append` 方法。
- **可迭代、可下标**：能用 `for` 遍历，也能 `r[i]` 按下标访问、`len(r)` 取长度、`r[1:3]` 切片（Python 3.3+ 支持切片）。
- 它 **不是** list。如果确实需要列表，要显式转换：`list(range(3))`。

```python
# 在 for i in range(len(nums)) 中，遍历到的 i 是索引（整数），配合 nums[i] 取值
nums = ["a", "b", "c"]
for i in range(len(nums)):
    print(i, nums[i])   # 0 a / 1 b / 2 c
```

---

## 二、`for ... in` 后面跟的是"可迭代对象"，不一定是数组

常见误解：以为 `in` 后面必须跟数组（list）。

实际规则：**`for ... in` 只要求后面是可迭代对象（iterable），也就是实现了 `__iter__` 方法的对象。**

```python
nums = [10, 20, 30]

# list 能迭代，是因为它有 __iter__ 方法
hasattr(nums, '__iter__')      # True

# range 也有 __iter__ 方法，所以也能直接跟在 in 后面
r = range(len(nums))           # range(0, 3)
hasattr(r, '__iter__')         # True
```

---

## 三、for 循环的真实执行机制

```python
for x in 对象:
    ...
```

Python 实际是这样执行的：

1. 调用 `iter(对象)`，看对象有没有 `__iter__` 方法
2. 得到一个**迭代器**，每次调用 `next()` 取出下一个值
3. 直到抛出 `StopIteration` 异常，循环结束

手动模拟一遍，就理解为什么 range 可以用了：

```python
it = iter(range(3))
next(it)   # 0
next(it)   # 1
next(it)   # 2
next(it)   # 抛 StopIteration → for 循环在这里结束
```

---

## 四、可迭代对象的常见例子

```python
for i in range(3):          # range 可迭代
for i in [0, 1, 2]:         # list 可迭代
for c in "abc":             # 字符串可迭代（每次取一个字符）
for k in {"a": 1}:          # 字典可迭代（默认遍历键）
for line in open("f.txt"):  # 文件对象可迭代（每次取一行）
```

数组（list）只是可迭代对象中的一种，range 也是，所以 `for i in range(len(nums))` 完全可以。

---

## 五、小结与建议

| 写法 | 遍历到的是什么 | 说明 |
|------|--------------|------|
| `for n in nums` | 元素 | 最简单，推荐 |
| `for i in range(len(nums))` | 索引 | 需要下标时用 |
| `for i, n in enumerate(nums)` | 索引 + 元素 | 同时要下标和元素时推荐 |

- 只需要元素 → 直接 `for n in nums`
- 只需要下标 → `for i in range(len(nums))`
- 下标和元素都要 → `for i, n in enumerate(nums)`

