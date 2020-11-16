import hashlib
from common_lib.result import Result
from common_lib.defs import LoginParams
from common_lib import validators


def convert_login_params(username: str,
                         password: str) -> (LoginParams, Result):
    password = hashlib.md5(
        ('_m' + password).encode(encoding='utf-8')).hexdigest()
    return LoginParams(username=username, password=password), Result()


def convert_embedded_categorys(l) -> (list, Result):
    try:
        # 增加key、value字段，树形需要
        for i in l:
            i['key'] = i['id']
            i['value'] = i['id']
        li = []

        # 递归嵌套
        def embed(li):
            if not li:
                pid = 0
                for i in l:
                    if i['pid'] == 0:
                        li.append(i)
                        # l.pop(l.index(i))
                if not li:  # 防止无数据时无限循环
                    return li
                embed(li)
            for i in li:
                pid = i['id']
                i['children'] = []
                for k in l:
                    if k['pid'] == pid:
                        i['children'].append(k)
                        # l.pop(l.index(k))
                if i['children']:
                    embed(i['children'])

            return li, Result()

        return embed(li)
    except Exception as e:
        return None, Result(err=True, msg="Convert Embedded_categories Error")
