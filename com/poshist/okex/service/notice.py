import time
import requests

def notice(type,var,info):
    if('sellOrder'==var):
        reqpost(type+'-----大额卖单预警：金额-  '+info[0]+'  份数-  '+info[1])
    elif('sellOrderLost'==var):
        reqpost(type + '-----大额卖单撤单预警：金额-  ' + info[0] + '  撤单份数-  ' + info[1])
    elif('buyOrder'==var):
        reqpost(type + '-----' + '大额买单挂单预警：金额-  ' + info[0] + '  份数-  ' + info[1])
    elif('buyOrderLost'==var):
        reqpost(type + '-----大额买单撤单预警：金额-  ' + info[0] + '  撤单份数-  ' + info[1])
    elif('deal'==var):
        timearr = time.localtime(info[2]/ 1000.0)
        reqpost(type+ '-----' +'大额成交预警:金额-  '+info[1]+ '  份数-  '+info[0]+'   时间-  '+time.strftime("%Y-%m-%d %H:%M:%S", timearr))
    elif('dealChange'==var):
        timearr = time.localtime(info[2] / 1000.0)
        reqpost(type+ '-----' +'价格波动预警:金额-  '+info[1]+ '  份数-  '+info[0]+'   时间-  '+time.strftime("%Y-%m-%d %H:%M:%S", timearr)+'  比上一交易单波动-  '+str(info[3])+'%')
    elif('klineVule'==var):
        timearr = time.localtime(info[1] / 1000.0)
        reqpost(type+ '-----' +'交易放量预警:时间-  '+time.strftime("%Y-%m-%d %H:%M:%S", timearr)+'   交易量-  '+info[0]+'   比上一周期增量-  '+info[2])

def reqpost(message):
    print(message)
    #r = requests.post("https://api.telegram.org/bot523899634:AAFKSpJ8Akg_oBdrWrIqPrkAmwZv3uh6j_I/sendMessage?parse_mode=Markdown&chat_id=-319771183&text=测试---"+message)
    # print("https://api.telegram.org/bot523899634:AAFKSpJ8Akg_oBdrWrIqPrkAmwZv3uh6j_I/sendMessage?parse_mode=Markdown&chat_id=-31977183&text="+message)
    # print(r.text)
    pass