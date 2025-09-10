# CY3761 | 2022-04-13 013 15:13 | 02.测试
import json

class Common:
    ret_to_menu_msg = '你取消%s操作,返回主菜单'

    # 确认退出系统 正在退出系统 你取消退出系统操作,返回主菜单
    # 确定删除 删除成功 删除失败
    # 确定继续删除?(Y) continue

    @staticmethod
    def confirm(ask, t_msg, f_msg):
        print('-' * 80)

        is_true = input(str(ask) + '?(Y)\n').upper() == 'Y'

        print(str(t_msg if is_true else f_msg))

        print('-' * 80)

        return is_true

    @staticmethod
    def exit_confirm():
        do = '退出系统'
        return Common.confirm('确认' + do, '正在%s..' % do, '你取消%s,返回主菜单' % do)  # break / continue

    @staticmethod
    def menu_confirm(do):
        do = str(do)
        return Common.confirm('确认继续' + do, '正在载入%s..' % do, '你取消继续%s,返回主菜单' % do)  # continue / break


def menu():
    menu_items = [
        ['录入学生信息', opt_0],  # 进行 输入姓名, 判断如果存在则提示重新输入
        ['查找学生信息', opt_1],  # 进行 输入姓名, 判断如果不存在则提示重新输入
        ['删除学生信息', opt_2],  # 进行 输入姓名, 判断如果不存在则提示重新输入
        ['修改学生信息', opt_3],  # 进行 输入姓名, 判断如果不存在则提示重新输入
        ['排序', opt_4],  # 进行 如果学生信息为空 则返回信息为空 否则进行排序项选择
        ['统计学生总人数', opt_5],  # 直接返回学生总人数
        ['显示所有学生信息', opt_6],  # 直接读取显示学生信息
        ['退出系统', opt_7],  # 提示是否确认退出
    ]

    while True:
        # 在这里进行加入一段代码, 使其屏幕清空 | (怎么实现?)

        try:
            # try/except 在 循环内 | 使用 raise Exception | 可直接代替 continue
            # raise 不能直接字符串 | TypeError: exceptions must derive from BaseException

            print('-' * 80)
            [print('%d-%s' % (k, _[0])) for k, _ in enumerate(menu_items)]

            menu_len_int = len(menu_items)
            menu_len_str = str(menu_len_int - 1)

            print('-' * 80)
            menu_id = input('请输入菜单序号: (0~' + menu_len_str + ')\n')

            if not menu_id.isdecimal():
                raise Exception('输入的菜单序号不合法,请重新输入')

            menu_id = int(menu_id)
            if menu_id < 0 or menu_id >= menu_len_int:
                print('输入的菜单序号不在 ' + '(0~' + menu_len_str + ') 范围内,请重新输入')
                continue

            print('-' * 80)
            print('你选择了 [%s]' % menu_items[menu_id][0])
            print('-' * 80)

            is_break = menu_items[menu_id][1]()  # 返回 True/False

            if is_break:
                break

        except (Exception, BaseException) as e:
            print(e)


def main():
    menu()


class Collection:
    path = 'data.db'
    encoding = 'utf-8'

    def __init__(self):
        # 追加模式
        open(self.path, 'a', encoding=self.encoding).close()

        self.items = []

        self.read()

    # 读取所有
    def read(self):
        with open(self.path, 'r', encoding=self.encoding) as r:
            items = r.readlines()

        for (k, item) in enumerate(items):
            try:
                items[k] = json.loads(item)
            except (Exception, BaseException) as e:
                items[k] = []

        self.items = items

    # 写入所有
    def write(self):
        with open(self.path, 'w', encoding=self.encoding) as w:
            for (k, item) in enumerate(self.items):
                try:
                    w.write(json.dumps(item) + '\n')
                except (Exception, BaseException) as e:
                    pass
            w.flush()

    def get(self, name):  # 获取一条
        return [item for item in self.items if item.get('name') == name]

    def count(self):  # 获取长度
        return len(self.items)

    def add(self, data):  # 插入一条
        self.items.append(data)
        self.write()

    def update(self, name, data):  # 修改一条
        if self.get(name):
            for (k, item) in enumerate(self.items):
                if item.name == name:
                    self.items[k] = data
        self.write()

    def delete(self, name):
        self.items = [item for item in self.items if item.get('name') != name]
        self.write()


# 录入学生信息
def opt_0():
    while True:
        name = input('请输入学生姓名:\n')

        if not name:
            print('学生姓名不能为空, 请重新输入')
            continue

        coll = Collection()
        is_exists = coll.get(name)

        count = coll.count()

        if is_exists:
            print('该学生已存在, 请重新输入')
            continue

        coll.add(dict(sn=1000 + count, name=name))
        print('学生 [%s] 录入成功' % name)

        if Common.menu_confirm('录入'):
            continue

        break

    return False


# 删除学生信息
def opt_2():
    while True:
        name = input('请输入学生姓名:\n')
        coll = Collection()

        get = coll.get(name)
        count = coll.count()

        if not get:
            print('该学生不存在, 请重新输入')
            continue

        print(get)
        print('-' * 80)
        is_delete = input('确定删除:(Y)\n').upper() == 'Y'

        if is_delete:
            coll.delete(name)
            print('删除成功')

        if (count - 1 > 0) and Common.menu_confirm('删除'):
            continue

        break

    return False


# 查找学生信息
def opt_1():
    while True:
        name = input('请输入学生姓名:\n')
        coll = Collection()

        get = coll.get(name)

        if not get:
            print('该学生不存在')

        if get:
            print(get)

        print('-' * 80)

        if Common.menu_confirm('查找'):
            continue

        break
    return False


# 修改学生信息
def opt_3():
    while True:
        name = input('请输入学生姓名:\n')
        coll = Collection()

        get = coll.get(name)

        if not get:
            print('该学生不存在, 请重新输入')
            continue

        # 修改输入
        print(get)

        get[0]['name'] = '新名字'
        # 这里需要判断下 新值是否存在 如果存在不给予修改

        coll.update(name, get[0])

        print(get)
        print('-' * 80)

        if Common.menu_confirm('修改'):
            continue

        break
    return False


# 排序
def opt_4():
    # 询问排序方式
    return False


# 统计学生总人数
def opt_5():
    coll = Collection()
    print(coll.count())
    return False


# 显示所有学生信息
def opt_6():
    coll = Collection()
    print(coll.items)  # 表格显示
    return False


# 退出系统
def opt_7():
    return Common.exit_confirm()


if __name__ == '__main__':
    main()
