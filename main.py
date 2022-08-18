# -*- coding : utf-8 -*-

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient
import sys
import re
import template

msg = """
#####################################
# VRChat Open Sound Control         #
# Chatbox Canned text input support #
#                                   #
# Version Alpha 0.0.0               #
#                                   #
#####################################
"""
    
ip = "127.0.0.1"
client_port = 9000
server_port = 9001

def template_read():
    # 外部の辞書型を読み取って使えるものだけ抜き出して投げる
    temp = template.template
    return num_of_char(template_isascii(temp))


def template_isascii(template):
    # OSC inputは今のところASCII文字のみしか対応していないためそれ以外は置き換える
    # 後でUTF-8に対応するらしい
    for i in template:
        if template[i].isascii():
            pass
        else:
            template[i] = "Use is not available"

    return template


def num_of_char(template):
    # 144文字までしか入力できないのでそれ以上の長さの物は消す
    for i in template:
        if 144 <= len(template[i]):
            template[i] = "Use is not available"

    return template


def print_template(template):
    # テンプレをprintする
    for i in template:
        print(i, ":", template[i])


if __name__ == "__main__":

    client = SimpleUDPClient(ip, client_port)
    temp = template_read()
    print(msg)
    print_template(temp)

    try:

        def print_handler(address, *args):
            #print(f"{address}: {args}")

            if address == "/avatar/parameters/chattext":
                client.send_message("/chatbox/input", [temp[int(re.sub(r"\D", "", str(args)))], True])

                # /chatbox/input string bool で渡す
                # boolがFalseだとキーボードが展開しstrが入力され
                # boolがTrueだとそのままstrが送信される

                # /chatbox/typing bool
                # 入力中の...を表示させるかさせないかを任意で表示できる

        def default_handler(address, *args):
            print(f"DEFAULT {address}: {args}")

        dispatcher = Dispatcher()
        dispatcher.map("/avatar/*", print_handler)
        dispatcher.set_default_handler(default_handler)

        server = BlockingOSCUDPServer((ip, server_port), dispatcher)
        server.serve_forever()

    except KeyboardInterrupt:
        sys.exit()