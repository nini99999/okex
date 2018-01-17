from com.poshist.okex.service.okwebsocket import wsclint

import _thread
import time
ws1=wsclint('ugc','usdt')
ws2=wsclint('ugc','eth')
_thread.start_new_thread(ws1.wsStart, ())
_thread.start_new_thread(ws2.wsStart, ())
while True:
    time.sleep(1)