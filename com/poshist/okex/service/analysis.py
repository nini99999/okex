from com.poshist.okex.service.util import jsonLoad
from com.poshist.okex.service.rule import rule
from com.poshist.okex.service.notice import notice


def analysisWsMessage(type,message,ws):

    jm=jsonLoad(message[1:len(message)-1])
    # print(jm)
    if(None==jm.get('channel')):

        if ('depth'==jm.get('type')):
            analysisOrder(type, jm)
        elif('deal'==jm.get('type')):
            analysisDeal(type,jm,ws)
        elif('kline'==jm.get('type')):
            pass
            #print(jm)

def analysisOrder(type,jm):
    sellOrders=jm.get('data').get('asks')
    buyOrders=jm.get('data').get('bids')
    for sellorder in sellOrders:
        if float(sellorder['totalSize'])>=rule.sellOrder:
            notice(type,'sellOrder',[sellorder['price'],sellorder['totalSize']])
    for buyOrder in buyOrders:
        if float(buyOrder['totalSize'])>=rule.buyOrder:
            notice(type,'buyOrder',[buyOrder['price'],buyOrder['totalSize']])



def analysisDeal(type,jm,ws):
    deals=jm.get('data')
    for deal in deals:
        if float(deal.get('amount'))>=rule.deal:
            notice(type,'deal',[deal.get('amount'),deal.get('price'),deal.get('createdDate')])
            if ws.dealInit:
                ws.dealInit=False
            else:
               change=float(deal.get('price'))/ws.info[0]-1
               if change<0:
                   change=0-change
               if change>rule.dealChange:
                   notice(type,'dealChange',[deal.get('amount'),deal.get('price'),deal.get('createdDate'),change*100])

            ws.info[0] = float(deal.get('price'))




