from conf import settings
# from bin import start
#
# start.run()

def logger(f):
    def inner(*args, **kwargs):
        with open(settings.LOG_PATH, encoding='utf-8', mode='a+') as f1:
            f1.write('您访问了%s' %(f.__name__))
        ret = f(*args, **kwargs)
        return ret
    return inner




