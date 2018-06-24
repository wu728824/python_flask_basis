import redis


def add_name():
    # 链接redis　数据库，创建实例
    rs = redis.StrictRedis(host="127.0.0.1",port=6379,decode_responses=True)
    # 给redis数据库添加数据
    result = rs.set("name","james")
    print(result)



def get_name():
    rs = redis.StrictRedis(host="127.0.0.1",port=6379,decode_responses=True)
    # 获取redis　数据库中的数据
    result = rs.get("name")
    print(result)

# redis-trib.rb create --replicas 1 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005

if __name__ == '__main__':
    get_name()