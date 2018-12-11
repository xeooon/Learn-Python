from lib import commom
from conf import settings

def register():
    with open(settings.DB_PATH, encoding='utf-8', mode='a+') as f1:
        f1.write('太白金星|123\n')


def login():
    pass


@commom.logger
def comment():
    print('欢迎访问评论页面')


@commom.logger
def article():
    print('欢迎访问文章页面')


@commom.logger
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
