# coding=utf-8
from pymysql import *


def main():
    conn = connect(host='localhost', port=3306, database='python', user='root', password='mysql', charset='utf8')
    # 创建游标对象
    cs1 = conn.cursor()
    # 执行insert语句
    # 增加
    # count = cs1.execute('insert into employee values(0,"李四","65000", 1)')
    # 查询行
    count = cs1.execute('select * from employee where id>=4')
    # 打印受影响函数
    # print(count)
    # 查询单行
    # for i in range(count):
    #     reslut = cs1.fetchone()
    #     print(reslut)
    # 查询多行,返回一个元组
    result = cs1.fetchall()
    print(result)
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()