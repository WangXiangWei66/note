import call_black

def run(url):
    before_list = call_black.parse(url)
    print(before_list)

if __name__ == '__main__':
    run('https://aj.newhouse.fang.com/house/s/')