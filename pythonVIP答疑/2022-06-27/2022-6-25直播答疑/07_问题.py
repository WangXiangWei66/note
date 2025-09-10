import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
)

cursor = db.cursor()

def query(sql):
    cursor.execute(sql)
    row = cursor.fetchone()
    return row


a = 'https://www.mashibing.com/subject/5?courseNo=66'
s = "SELECT HEX('%s');" % a
ret = query(s)
ret = ret[0]
# 68747470733A2F2F7777772E6D6173686962696E672E636F6D2F7375626A6563742F353F636F757273654E6F3D3636
print(ret, len(ret))

step = 2
item = map(lambda _: chr(int(ret[_:_ + step], 16)), range(0, len(ret), step))
print(''.join(item))  # 数字和英文结合的字符串可解 | https://www.mashibing.com/subject/5?courseNo=66

print('=' * 80)
a = '马士兵教育'
s = "SELECT HEX('%s');" % a
ret = query(s)
ret = ret[0]
# E9A9ACE5A3ABE585B5E69599E882B2
print(ret)

# print(ret, len(ret))
# item = map(lambda _: chr(int(ret[_:_ + step], 16)), range(0, len(ret), step))
# print(''.join(item))  # 直接乱码了 | é©¬å£«åµæè²
#
# print('=' * 80)
# item = map(lambda _: ret[_:_ + step].lower(), range(0, len(ret), step))
# print(ret.lower(), a.encode('utf-8'))  # 通过对比分析 一个是字符串 一个是byte
# print(tuple(item))
#
# # 问题: 如何使用 python 将 ret 或 item 转为 byte 最后转为字符串?  (该字符串等于 mysql的 unhex, 下面的是通过unhex转换)
# print('=' * 80)
#
# s = "SELECT UNHEX('%s');" % ret
# ret = query(s)
# ret = ret[0]
# print(ret, len(ret))
# ret = ret.decode('utf-8')
# print(ret, len(ret))