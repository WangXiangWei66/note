# 如果没安装 mysql.connector 需要自行使用 pip 安装
# pip install mysql-connector
# pip install MySQL-connector-python | 8.0 还需要安装这个
import mysql.connector
import time

# 连接 mysql
# 如果 自己的mysql配置不同 请自行修改

# 后缀
suffix = str(time.time()).replace('.', '_')

# 删除数据库语句
drop_database_sql = 'DROP DATABASE IF EXISTS `test_%s`;' % suffix
# 创建数据库语句
create_database_sql = "CREATE DATABASE IF NOT EXISTS `test_%s` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_0900_ai_ci';" % suffix
# 选择数据库语句
use_database_sql = 'USE `test_%s`;' % suffix

# 创建数据表语句
# 以下字符集与排序规则是通过网上整理得出常用的编码
# 0900 >= MySQL8.0
# utf8mb4 (3字节1字符) | utf8mb3 (3字节1字符)
# as 区分重音 | ai 不区分重音
# cs 区分大小写 | ci 不区分大小写
# bin 二进制存储方式 区分大小写
create_table_sql = """
CREATE TABLE IF NOT EXISTS `test_%s` (
    `test_id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '编号',  
    `utf8mb4_0900_as_cs` VARCHAR(4) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_0900_as_cs' COMMENT 'utf8mb4_0900_as_cs',
    `utf8mb4_0900_ai_ci` VARCHAR(4) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_0900_ai_ci' COMMENT 'utf8mb4_0900_ai_ci',
    `utf8mb4_0900_bin` VARCHAR(4) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_0900_bin' COMMENT 'utf8mb4_0900_bin',
    `utf8mb4_general_ci` VARCHAR(4) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' COMMENT 'utf8mb4_general_ci',
    `utf8mb4_unicode_ci` VARCHAR(4) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' COMMENT 'utf8mb4_general_ci',
    `utf8mb4_bin` VARCHAR(4) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_bin' COMMENT 'utf8mb4_bin',
    `utf8_general_ci` VARCHAR(4) CHARACTER SET 'utf8mb3' COLLATE 'utf8_general_ci' COMMENT 'utf8_general_ci',
    `utf8_unicode_ci` VARCHAR(4) CHARACTER SET 'utf8mb3' COLLATE 'utf8_unicode_ci' COMMENT 'utf8_unicode_ci',
    `utf8_bin` VARCHAR(4) CHARACTER SET 'utf8mb3' COLLATE 'utf8_bin' COMMENT 'utf8_bin'
) COMMENT '测试表';
""" % suffix

# 插入语句
# 9个字段
size = 9
value_items = ('（）', '()', ',', '，', ';', '；')  # 中文(全角) 后者英文(半角) | 假设还有很多 全角和半角的
insert_table_sql = "INSERT INTO `test_%s` VALUES (null, '{0}');" % suffix

insert_table_sql_items = []

for item in value_items:
    insert_table_sql_items.append(insert_table_sql.format("','".join([item] * size)))

# 查询表结构
desc_sql = 'DESC `test_%s`;' % suffix;
# 查询表
select_sql = 'SELECT COUNT(*) `count` FROM `test_%s` WHERE `{0}` LIKE "%%{1}%%";' % suffix;

with mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
) as conn:
    with conn.cursor() as cursor:
        # 执行 删除数据库语句
        cursor.execute(drop_database_sql)

        # 执行 创建数据库语句
        cursor.execute(create_database_sql)

        # 执行 创建数据库语句
        cursor.execute(use_database_sql)

        # 执行 创建数据表语句
        cursor.execute(create_table_sql)

        # 执行 添加数据语句
        for item in insert_table_sql_items:
            cursor.execute(item)

        conn.commit()  # 提交

        # 执行 查询结构
        cursor.execute(desc_sql)
        where_field = tuple(map(lambda _: _[0], cursor.fetchall()))  # 直接 map 不会执行内部函数
        where_field = [item for item in where_field if item != 'test_id']

        # print(where_field)

        # 执行 查询数据语句
        for field in where_field:
            new_select_sql = select_sql.format(field, '{0}')

            for item in value_items:
                sql = new_select_sql.format(item)
                print('-' * 80)
                print(sql)
                cursor.execute(sql)
                print(cursor.fetchone())

        # utf8mb4_0900_ai_ci 和 utf8_unicode_ci 通过这个例子 能否说明 只有这两个排序规则能够做到 查询具有圆角或半角的字符串时 是不区分是否圆角或半角??

        # 删除数据库 | 自行将 0 改为 1
        if 1 == 1:
            # 执行 删除数据库语句
            cursor.execute(drop_database_sql)
            conn.commit()  # 提交
