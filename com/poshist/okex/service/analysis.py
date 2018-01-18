from com.poshist.okex.service.util import jsonLoad
from com.poshist.okex.service.rule import rule
from com.poshist.okex.service.notice import notice


def analysisWsMessage(type,message,ws):

    if'['==message[0:1]:
        jm=jsonLoad(message[1:len(message)-1])
        # print(jm)
        if(None==jm.get('channel')):

            if ('depth'==jm.get('type')):
                analysisOrder(type, jm,ws)
            elif('deal'==jm.get('type')):
                analysisDeal(type,jm,ws)
            elif('kline'==jm.get('type')):
                pass
                #print(jm)

def analysisOrder(type,jm,ws):
    sellOrders=jm.get('data').get('asks')
    buyOrders=jm.get('data').get('bids')
    for sellorder in sellOrders:
        #大额卖单挂单判断
        if float(sellorder['totalSize'])>=rule.sellOrder:
            notice(type,'sellOrder',[sellorder['price'],sellorder['totalSize']])
        #大额卖单撤单判断
        if(None!=ws.sellOrders.get(sellorder['price'])):
            if ws.sellOrders.get(sellorder['price'])-float(sellorder['totalSize'])>=rule.sellOrder:
                notice(type, 'sellOrderLost', [sellorder['price'], str(ws.sellOrders.get(sellorder['price'])-float(sellorder['totalSize']))])
        ws.sellOrders[sellorder['price']]=float(sellorder['totalSize'])

    for buyOrder in buyOrders:
        #大额买单挂单预警
        if float(buyOrder['totalSize'])>=rule.buyOrder:
            notice(type,'buyOrder',[buyOrder['price'],buyOrder['totalSize']])
        #大额买单撤单预警
        if(None!=ws.buyOrders.get(buyOrder['price'])):
            if ws.buyOrders.get(buyOrder['price'])-float(buyOrder['totalSize'])>=rule.buyOrder:
                notice(type, 'buyOrderLost', [buyOrder['price'], str(ws.buyOrders.get(buyOrder['price'])-float(buyOrder['totalSize']))])
        ws.buyOrders[buyOrder['price']]=float(buyOrder['totalSize'])

def analysisDeal(type,jm,ws):
    deals=jm.get('data')
    for deal in deals:
        #大额交易判断
        if float(deal.get('amount'))>=rule.deal:
            notice(type,'deal',[deal.get('amount'),deal.get('price'),deal.get('createdDate')])
        #交易差值判断
        if ws.dealInit:
            ws.dealInit=False
        else:
            change=float(deal.get('price'))/ws.info[0]-1
            if change<0:
                change=0-change
            if change>rule.dealChange:
               notice(type,'dealChange',[deal.get('amount'),deal.get('price'),deal.get('createdDate'),change*100])
        ws.info[0] = float(deal.get('price'))




