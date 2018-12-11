DB_PATH = r'D:\24期周末班\day07\register'
LOG_PATH = r'D:\24期周末班\day07\access.log'


def logger(f):
    def inner(*args, **kwargs):
        with open(LOG_PATH, encoding='utf-8', mode='a+') as f1:
            f1.write('您访问了%s' %(f.__name__))
        ret = f(*args, **kwargs)
        return ret
    return inner

def register():
    with open(DB_PATH, encoding='utf-8', mode='a+') as f1:
        f1.write('太白金星|123\n')


def login():
    pass

@logger
def comment():
    print('欢迎访问评论页面')

@logger
def article():
    print('欢迎访问文章页面')

@logger
def diary():
    print('欢迎访问日记页面')
    

dic = {
    1: register,
    2: login,
    3: comment,
    4: article,
    5: diary
}

def run():
    while 1:
        choice = input('请输入')
        if choice.isdigit():
            choice = int(choice)
            dic[choice]()
        else:
            print('请重新输入')

run()