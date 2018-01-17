def notice(type,var,info):
    if('sellOrder'==var):
        print(type+'-----'+'卖单预警：金额-'+info[0]+'  份数-'+info[1])
    elif('buyOrder'==var):
        print(type + '-----' + '买单预警：金额-' + info[0] + '  份数-' + info[1])
