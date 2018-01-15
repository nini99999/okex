#!/usr/bin/python
import websocket
import _thread
import time
import zlib

def on_message(ws, message):
    # res=message.encode(encoding="utf-8")
    # print(message)
    # print("{\"event\": \"pong\"}" == res)
    # if "{\"event\": \"pong\"}"==res:
        res = zlib.decompress(message, -zlib.MAX_WBITS)
        print("Received '%s'" % res)
    # else :
    #
    #     print("Received '%s'" % message)


def on_error(ws, error):
    print (error)

def on_close(ws):
    print ("### closed ###")

def on_open(ws):
    def run(*args):
        # ws.send("{event:'login',parameters:{userId:'ae4e42eb-33d2-40a2-85bc-28eba22936b19d502ae6fd8f4654',binary:1}}")
        # ws.send("{event:'addChannel',parameters:{\"base\":\"ugc\",\"binary\":\"1\",\"product\":\"spot\",\"quote\":\"usdt\",\"type\":\"balance\"}}")
        # ws.send("{event:'addChannel',parameters:{base:'ugc',binary:'1',product:'spot',quote:'usdt',type:'ticker'}}")
        # ws.send("{event:'addChannel',parameters:{\"base\":\"ugc\",\"binary\":\"1\",\"product\":\"spot\",\"quote\":\"usdt\",\"type\":\"balance\"}}")
        ws.send("{event:'addChannel',parameters:{\"base\":\"ugc\",\"binary\":\"1\",\"product\":\"spot\",\"quote\":\"usdt\",\"type\":\"depth\"}}")
        # ws.send(    "{event:'addChannel',parameters:{\"base\":\"ugc\",\"binary\":\"1\",\"product\":\"spot\",\"quote\":\"usdt\",\"type\":\"deal\"}}")
        # ws.send("{event:'addChannel',parameters:{\"base\":\"ugc\",\"binary\":\"1\",\"product\":\"spot\",\"quote\":\"usdt\",\"type\":\"order\"}}")
        #ws.send("{event:'addChannel',parameters:{\"base\":\"ugc\",\"binary\":\"1\",\"period\":\"3min\",\"product\":\"spot\",\"quote\":\"usdt\",\"type\":\"kline\"}}")
        ws.send("")
        for i in range(30000):
            time.sleep(3)

        time.sleep(1)
        ws.close()
        print ("thread terminating...")
    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://real.okex.com:10441/websocket",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)

    ws.on_open = on_open

    ws.run_forever()