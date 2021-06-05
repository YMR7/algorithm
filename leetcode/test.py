def get_name(s):
    if not s:
        return ''
    res = ''
    stack = []
    left_set = {'(', '[', '【', '〔'}
    right_set = {')', ']', '】', '〕'}
    for c in s:
        if c in left_set:
            stack.append(c)
        elif c in right_set:
            stack.pop()
        elif c not in [',', '，']:
            if not stack:
                res += c
    return res


anms = get_name('惠特曼[美]，[英]')
print(anms)

# create table recommended(
#     id int unsigned auto_increment,
#     recommended_id int comment '推荐内容id',
#     user_id int comment '用户id',
#     status int comment '0:未推荐，1：取消推荐'
#     create_time date not null,
#     update_time date not null,
#     delete_time date not null,
#     primary key(id),
#     index(recommended_id),
#     index(user_id),
# )engine=innodb default charset=utf8;


def match(pattern, s):
    