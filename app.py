from LineNotify import LineNotify

if __name__ == '__main__':
    line = LineNotify("your_token")
    line.setMessages("Test Message")
    line.disableDatetime()
    res = line.sendMessage()
    print(res)