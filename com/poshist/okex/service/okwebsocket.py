import websocket
import _thread
import time


wsSendJsons=("{event:'addChannel',parameters:{\"base\":\"ugc\",\"binary\":\"0\",\"product\":\"spot\",\"quote\":\"usdt\",\"type\":\"depth\"}}","{event:'addChannel',parameters:{\"base\":\"ugc\",\"binary\":\"0\",\"product\":\"spot\",\"quote\":\"usdt\",\"type\":\"deal\"}}")
wsUrl="wss://okexcomreal.bafang.com:10441/websocket"

def on_message(ws, message):
        print("Received '%s'" % message)



def on_error(ws, error):
    print (error)

def on_close(ws):
    print ("### closed ###")

def on_open(ws):
    def run(*args):
        # 初始化频道
        for wsj in wsSendJsons:
            ws.send(wsj)

        for i in range(30000):
            time.sleep(3)

        time.sleep(1)
        ws.close()
        print ("thread terminating...")
    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(wsUrl,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)

    ws.on_open = on_open

    ws.run_forever()