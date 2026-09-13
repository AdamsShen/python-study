# python-study

Python 学习笔记与实践代码仓库，按知识点分章节整理，包含**课堂代码**、**课后作业**与**学习笔记**，适合从零开始系统学习 Python。

## 项目简介

本仓库记录了 Python 从入门到面向对象进阶的完整学习过程，共 15 个章节。每个章节采用统一的目录结构，便于查阅与复习。

## 目录结构

```
python-study/
├── 01_Python入门/                    # 概述、注释、输出输入、变量
├── 02_Python运算符/                  # 数据类型、算术/赋值/比较/逻辑/成员运算符
├── 03_Python分支结构/                # if 分支、match-case 匹配
├── 04_Python循环结构/                # while / for 循环、range、break/continue
├── 05_Python列表和数值&随机数操作/   # 列表操作、math、random
├── 06_Python元组和字典/              # 元组、字典、集合、深浅拷贝
├── 07_Python字符串/                  # 字符串基本操作与常用方法
├── 08_函数基础/                      # 函数入门、嵌套、匿名函数、回调
├── 09_函数作用域和装饰器/            # 作用域、闭包、装饰器
├── 10_列表推导式和生成器和包与模块管理/  # 递归、迭代器、生成器、模块与包
├── 11_Python常用模块/                # os、json、time/datetime、文件操作
├── 12_面向对象入门/                  # 类与对象、self、构造/析构、属性
├── 13_面向对象进阶/                  # property、类/静态方法、继承、重写
├── 14_异常处理/                      # try/except 异常捕获
├── 15_虚拟环境/                      # 虚拟环境的使用
├── hello.py                          # 示例脚本
├── requirement.txt                   # 项目依赖清单
└── README.md                         # 项目说明
```

各章节内部统一组织为：

| 目录 | 说明 |
| --- | --- |
| `代码/` | 课堂示例代码，按知识点顺序编号 |
| `作业/` | 课后练习题 |
| `笔记/` | 学习笔记（Markdown + PDF） |

## 环境要求

- Python 3.11+
- pip

## 安装依赖

```bash
# 建议先创建并激活虚拟环境（见「15_虚拟环境」）
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

pip install -r requirement.txt
```

当前项目依赖：

| 包名 | 版本 |
| --- | --- |
| requests | 2.32.5 |
| urllib3 | 2.6.3 |
| certifi | 2026.7.22 |
| charset-normalizer | 3.5.1 |
| idna | 3.19 |

## 使用方法

按章节顺序运行对应的示例代码即可：

```bash
cd 01_Python入门/代码
python 01_hello.py
```

## 学习进度

- [x] 01 Python 入门
- [x] 02 Python 运算符
- [x] 03 Python 分支结构
- [x] 04 Python 循环结构
- [x] 05 Python 列表和数值 & 随机数操作
- [x] 06 Python 元组和字典
- [x] 07 Python 字符串
- [x] 08 函数基础
- [x] 09 函数作用域和装饰器
- [x] 10 列表推导式和生成器和包与模块管理
- [x] 11 Python 常用模块
- [x] 12 面向对象入门
- [x] 13 面向对象进阶
- [x] 14 异常处理
- [x] 15 虚拟环境

## 说明

- 笔记内容版权归 **智泊AI**（作者：Jeff）所有，仅用于个人学习记录。
- 代码部分为个人练习实践，欢迎交流指正。
