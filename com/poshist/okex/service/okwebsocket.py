import _thread
import time

import websocket

from com.poshist.okex.service.analysis import analysisWsMessage
from com.poshist.okex.service.rule import rule


class wsclint(object):
    wsSendJsons=('{event:"addChannel",parameters:{"base":"xxin","binary":"0","product":"spot","quote":"xxout","type":"depth"}}','{event:"addChannel",parameters:{"base":"xxin","binary":"0","product":"spot","quote":"xxout","type":"deal"}}','{event:"addChannel",parameters:{"base":"xxin","binary":"0","period":"kPeriod","product":"spot","quote":"xxout","type":"kline"}}')
    wsUrl="wss://okexcomreal.bafang.com:10441/websocket"

    def __init__(self,instr,outsrt,info,dealInit,buyOrders,sellOrders):
        self.instr = instr
        self.outstr = outsrt
        self.info=info
        self.dealInit=dealInit
        self.buyOrders=buyOrders
        self.sellOrders=sellOrders

    def on_message(self,ws,message):
            analysisWsMessage(str(self.instr)+'-'+str(self.outstr),message,self)



    def on_error(self,ws,error):
        print (error)

    def on_close(self,ws):
        print ("### closed ###")
        print("### restart ###")
        self.wsStart()

    def on_open(self,ws):
        def run(*args):
            # 初始化频道
            for wsj in self.wsSendJsons:
                wsj=wsj.replace('xxin',self.instr)
                wsj=wsj.replace('xxout',self.outstr)
                wsj = wsj.replace('kPeriod', rule.kPeriod)
                ws.send(wsj)

            while True:
                time.sleep(5)
                ws.send('{"event":"ping"}')

                #ws.close()
            print ("thread terminating...")
        _thread.start_new_thread(run, ())

    def wsStart(self):

        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(self.wsUrl,
                                    on_message = self.on_message,
                                    on_error = self.on_error,
                                    on_close = self.on_close)
        ws.on_open = self.on_open
        ws.run_forever()
