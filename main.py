# 这个文件用于编写代码
# 从键盘输入一行字符
string = input()
# 初始化各类型字符的计数为 0
letter_count = 0
digit_count = 0
space_count = 0
other_count = 0
# 遍历输入的每一个字符
for char in string:
    # 判断是否为英文字符（字母）
    if char.isalpha():
        letter_count += 1
    # 判断是否为数字
    elif char.isdigit():
        digit_count += 1
    # 判断是否为空格
    elif char.isspace():
        space_count += 1
    # 其他情况则为其他字符
    else:
        other_count += 1
# 按照要求的格式输出结果
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
