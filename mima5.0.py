"""
功能：判断密码强度
版本：5.0
日期：2018/12/28
"""
class PasswdTool:
    def __int__(self, passwd):
        self.passwd = passwd
        self.strength_level = 0

    def process_passwd(self):
        if len(self, passwd) >= 8:
            self.strength_level += 1
        else:
            print('密码长度小于8')
        if self.check_nubmer_exist():
            self.strength_level += 1
        else:
            print('密码不包含数字')
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码不包含字母')

    def check_nubmer_exist(self):
        has_number = False
        for c in self.passwd:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        has_alpha = False
        for c in self.passwd:
            if c.isalpha():
                has_alpha = True
                break
        return has_alpha

def main():
    try_times = 5
    while try_times > 0:
        passwd = input('请输入密码：')
        passwd_tool = PasswdTool(passwd)
        passwd_tool.process_passwd()

        f = open('passwd_5.0.txt', 'a')
        f.write('密码：{}，强度：{}\n' .format(passwd, passwd_tool.strength_level))
        f.close()

        if passwd_tool.strength_level == 3:
            print('密码强度符合规范')
            break
        else:
            print('密码强度不符合规范')
            try_times -= 1
        print()

    if try_times <= 0:
        print('密码尝试次数过多')
if __name__ == '__main__':
    main()