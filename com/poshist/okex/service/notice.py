import time
import requests

def notice(type,var,info):
    if('sellOrder'==var):
        print(type+'-----大额卖单挂单预警：金额-'+info[0]+'  份数-'+info[1])
        reqpost(type+'-----大额卖单预警：金额-'+info[0]+'  份数-'+info[1])
    elif('sellOrderLost'==var):
        print(type + '-----大额卖单撤单预警：金额-' + info[0] + '  撤单份数-' + info[1])
        reqpost(type + '-----大额卖单撤单预警：金额-' + info[0] + '  撤单份数-' + info[1])
    elif('buyOrder'==var):
        print(type + '-----' + '大额买单挂单预警：金额-' + info[0] + '  份数-' + info[1])
        reqpost(type + '-----' + '大额买单挂单预警：金额-' + info[0] + '  份数-' + info[1])
    elif('buyOrderLost'==var):
        print(type + '-----大额买单撤单预警：金额-' + info[0] + '  撤单份数-' + info[1])
        reqpost(type + '-----大额买单撤单预警：金额-' + info[0] + '  撤单份数-' + info[1])
    elif('deal'==var):
        timearr = time.localtime(info[2]/ 1000.0)
        print(type+ '-----' +'大额成交预警:金额-'+info[1]+ '  份数-'+info[0]+'   时间-'+time.strftime("%Y-%m-%d %H:%M:%S", timearr) )
        reqpost(type+ '-----' +'大额成交预警:金额-'+info[1]+ '  份数-'+info[0]+'   时间-'+time.strftime("%Y-%m-%d %H:%M:%S", timearr))
    elif('dealChange'==var):
        timearr = time.localtime(info[2] / 1000.0)
        print(type+ '-----' +'价格波动预警:金额-'+info[1]+ '  份数-'+info[0]+'   时间-'+time.strftime("%Y-%m-%d %H:%M:%S", timearr)+'比上一交易单波动'+str(info[3])+'%')
        reqpost(type+ '-----' +'价格波动预警:金额-'+info[1]+ '  份数-'+info[0]+'   时间-'+time.strftime("%Y-%m-%d %H:%M:%S", timearr)+'比上一交易单波动'+str(info[3])+'%')


def reqpost(message):
    #r = requests.post("https://api.telegram.org/bot523899634:AAFKSpJ8Akg_oBdrWrIqPrkAmwZv3uh6j_I/sendMessage?parse_mode=Markdown&chat_id=-319771183&text=测试---"+message)
    # print("https://api.telegram.org/bot523899634:AAFKSpJ8Akg_oBdrWrIqPrkAmwZv3uh6j_I/sendMessage?parse_mode=Markdown&chat_id=-31977183&text="+message)
    # print(r.text)
    pass