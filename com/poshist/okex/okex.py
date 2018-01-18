from com.poshist.okex.service.okwebsocket import wsclint

import _thread
import time
ws1=wsclint('ugc','usdt')
_thread.start_new_thread(ws1.wsStart, ())
while True:
    time.sleep(1)