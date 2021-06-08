面了3轮，最后是和HR mm唠嗑。
没有考算法。
和第一位面试官主要在聊做过的项目，详细问了项目中某个算法的实现；
第二个面试官比较飘逸，感觉主要考能力，比如逻辑严谨性，问了个假如豆瓣启动页要根据用户生日显示祝贺，应该怎么写代码的问题，这感觉真正写起来加上调试也就10分钟的事儿吧，有点懵，反而不知道该怎么写了，反问了一下能不能用系统提供的时间方法之类，最后也不知道答得怎么样……后来又问了对之前公司产品的看法，你准备如何改进，详细追问了改进的思路，然后还闲聊了些比如平时都看什么blog之类的；
第三位面试官考了一些基本概念，比如AutoLayout中Hugging和Compression的区别，手动写约束条件加到哪里，包括NSRunloop的概念和用处等。
总体感觉不错，一直很喜欢豆瓣，最终没有成功去豆厂是因为自己能力问题。祝豆瓣越来越好

面试内容主要是优化笔试题，还有数据库python啥的。面试官人很好每次我有做错或者不会的都耐心解释了答案。之后当天就发了offer。


一面2个人，问了一下之前网上的做的题目，说了一下思路，在提示之下发现不完善的地方。然后问了一些Python相关的问题。然后是交叉面，也是两个人，问了一个算法，然后根据简历问了一些数据库、git相应的知识点。最后是总监面试，主要就是看性格是否适合team了。



笔试题
第一题
```Python
def get_name(s):
    if not s:
        return ''
    res = ''
    flag = 0
    left_set = {'(', '[', '【', '〔'}
    right_set = {')', ']', '】', '〕'}
    for c in s:
        if c in left_set:
            flag = 1
        elif c in right_set:
            flag = 0
        elif c not in [',', '，']:
            if not flag:
                res += c
    return res
anms = get_name('惠特曼[美]，[英]')
print(anms)
```
第二题
```sql
create table user_recommended(
    id int unsigned auto_increment,
    content_id int comment '推荐内容id',
    user_id int comment '用户id',
    recommended_status int comment '1：推荐，0：取消推荐'
    create_time datetime not null,
    update_time datetime not null,
    primary key(id),
    index(content_id),
    index(user_id),
)engine=innodb default charset=utf8;


create table content(
    id int unsigned auto_increment,
    user_id int comment '用户id',
    detail varchar(200) not null,
    create_time datetime not null,
    update_time datetime not null,
    delete_time datetime null,
    primary key(id),
)engine=innodb default charset=utf8;


create table user(
    id int unsigned auto_increment,
    user_name varchar(20) not null,
    user_status int comment '1：使用中，0：已注销',
    create_time datetime not null,
    update_time datetime not null,
    primary key(id),
)engine=innodb default charset=utf8;

select user_id from user_recommended where content_id=xxx and recommended_status=1

select user_name from user_recommended join user on user_recommended.user_id= user.id where content_id=xxx and recommended_status=1

select content_id from user_recommended where user_id=xxx and recommended_status=1 order by update_time desc

update content set delete_time=now() where content_id=xxx
update user_recommended set recommended_status=0,update_time=now() where content_id=xxx
```