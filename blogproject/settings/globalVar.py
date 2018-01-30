
MY_NAME = "BlueFeng丨羽枫"
MY_NAME_E = "BlueFeng"
MY_NAME_C = "羽枫"
MY_TITLE = "BlueFeng丨羽枫的博客"
MY_DES = "游戏开发工程师（码农一个）, 不断学习中, 人生ing"

MY_EMAIL = "zhhyf521@163.com"


def seo_processor(requests):
    value = {
        'MY_NAME': MY_NAME,
        'MY_TITLE': MY_TITLE,
        'MY_DES': MY_DES,
        'MY_EMAIL': MY_EMAIL,
        'MY_NAME_E':MY_NAME_E,
    }
    return value