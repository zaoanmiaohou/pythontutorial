# 20190426

# 计算属相以及星座

chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
print(chinese_zodiac[0])  # 鼠
print(chinese_zodiac[0:4])  # 鼠牛虎兔
print(chinese_zodiac[-1])  # 猪
print(chinese_zodiac[-4])  # 猴


zodiac_temp = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
print(zodiac_temp[2018 % 12])  # 狗


# 序列
# 序列是指他的成员都是有序排列，并且可以通过下标偏移量访问它的一个或者几个成员
# 字符串属于序列
# 字符串类型可以是单引号也可以是双引号，只不过在内容中存在单引号时外部要使用双引号，内容存在双引号时，外部要使用单引号
string01 = "this's python"
string02 = 'this is very "important"'
print(string01)  # this's python
print(string02)  # this is very "important"
# 字符串的成员关系操作符  in  not in
print('狗' in chinese_zodiac)  # True
print('狗' not in chinese_zodiac)  # False
# 字符串的连接操作符  +
print(chinese_zodiac + "abc" + zodiac_temp)  # 鼠牛虎兔龙蛇马羊猴鸡狗猪abc猴鸡狗猪鼠牛虎兔龙蛇马羊
# 字符串的重复操作符  *
print(chinese_zodiac * 3)  # 鼠牛虎兔龙蛇马羊猴鸡狗猪鼠牛虎兔龙蛇马羊猴鸡狗猪鼠牛虎兔龙蛇马羊猴鸡狗猪
# 字符串的切片操作符  [:]
print(chinese_zodiac[0:4])  # 鼠牛虎兔
