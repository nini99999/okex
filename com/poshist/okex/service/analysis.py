from com.poshist.okex.service.util import jsonLoad
from com.poshist.okex.service.rule import rule
from com.poshist.okex.service.notice import notice


def analysisWsMessage(type,message):
    jm=jsonLoad(message[1:len(message)-1])
    #print(jm)
    if(None==jm.get('channel')):

        if ( isinstance(jm.get('data'),dict) and None != jm.get('data').get('asks') ):
            analysisOrder(type, jm)


def analysisOrder(type,jm):
    sellOrders=jm.get('data').get('asks')
    buyOrders=jm.get('data').get('bids')
    for sellorder in sellOrders:
        if float(sellorder['totalSize'])>=rule.sellOrder:
            notice(type,'sellOrder',[sellorder['price'],sellorder['totalSize']])
    for buyOrder in buyOrders:
        if float(buyOrder['totalSize'])>=rule.buyOrder:
            notice(type,'buyOrder',[buyOrder['price'],buyOrder['totalSize']])



def analysisDeal(jm):
    pass
