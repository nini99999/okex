import _thread
import time

from com.poshist.okex.service.okwebsocket import wsclint
from com.poshist.okex.service.rule import rule

for inout in rule.inout:
    ws=wsclint(inout[0],inout[1],[0,0,0],True,{},{})
    _thread.start_new_thread(ws.wsStart, ())
while True:
    time.sleep(1)