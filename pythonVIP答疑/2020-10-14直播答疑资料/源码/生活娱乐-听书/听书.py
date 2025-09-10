import pyttsx3     # 第三方库，用于发出声音

# 听书模块
def listen_books(text):
    book = pyttsx3.init()    # 初始化一个可以说话的对象

    rate = book.getProperty('rate')       # 获取说话速度的属性
    book.setProperty('rate', rate+50)    # 设置说话速度

    volume = book.getProperty('volume')      # 取说话y音量的属性
    book.setProperty('volume', volume-0.5)  # 设置说话音量

    book.say(text)            # 设置说话的文本内容
    book.runAndWait()         # 开始执行说话的功能

def read_text():
    with open('book.txt', 'r', encoding='utf-8') as file:  # 文件的名字和格式，路径 文件打开方式为r w a
        text = file.read()
        print(text)
    return text

if __name__ == '__main__':
    book_text = read_text()
    listen_books(book_text)
