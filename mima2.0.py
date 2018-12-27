"""
功能：判断密码强度
版本：2.0
日期：2018/12/26
"""
def check_nubmer_exist(password_str):
    has_number = False
    for c in password_str:
        if c.isnumeric():
            has_number = True
            break
    return has_number
def check_letter_exist(password_str):
    has_alpha = False
    for c in password_str:
        if c.isalpha():
            has_alpha = True
            break
    return has_alpha
def main():
    try_times = 5
    while try_times >= 1:
        password = input('请输入密码：')
        strength_level = 0
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度小于8')
        if check_nubmer_exist(password):
            strength_level += 1
        else:
            print('密码不包含数字')
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码不包含字母')
        if strength_level == 3:
            print('密码强度符合规范')
            break
        else:
            print('密码强度不符合规范')
            try_times -= 1
    if try_times <= 0:
        print('密码尝试次数过多')

if __name__ == '__main__':
    main()