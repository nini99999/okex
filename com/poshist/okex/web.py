#!/usr/bin/python

from websocket import create_connection
import gzip
from io import BytesIO
import zlib

ws = create_connection("wss://real.okex.com:10441/websocket")
ws.send("{event:'login',parameters:{userId:'ae4e42eb-33d2-40a2-85bc-28eba22936b19d502ae6fd8f4654',binary:1}}")
result =  ws.recv()
print("Received '%s'" % result)
res=zlib.decompress(result, -zlib.MAX_WBITS)
print("Received '%s'" % res)

print(type(result))
ws.send("{event:'addChannel',parameters:{base:'ugc',binary:'1',product:'spot','quote':'eth',type:'order'}}")
result =  ws.recv()
res=zlib.decompress(result, -zlib.MAX_WBITS)
print("Received '%s'" % result)
print("Received '%s'" % res)

ws.send("{'event':'ping'}")
result =  ws.recv()
print("Received '%s'" % result)

ws.close()