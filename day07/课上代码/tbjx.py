# print('from the tbjx.py')

__all__ = ['read1', 'read2']
name = '太白金星'


def read1():
    print('tbjx模块：', name)


def read2():
    print('tbjx模块')
    read1()


def change():
    global name
    name = 'barry'
    

def read3():
    with open('xx', encoding='utf-8', mode='w') as f1:
        pass
    print('read3 调试成功')
    
# print(__name__)  # 当成执行文件：__main__

if __name__ == '__main__':
    read3()




