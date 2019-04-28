#-*- coding: utf-8 -*-

from syn_edb import models
from multiprocessing import Process,Pool
import datetime
import os
import time
import json
import hashlib
import requests
from django.http import HttpResponse
import importlib,sys
from django.apps import apps
from syn_edb.OperateDB import OperateDB
from syn_edb.OperateDB_Pool import OperateDB_Pool
from django.views.decorators.csrf import csrf_exempt
import logging
from django.db.models import Max
logger = logging.getLogger("users")
logger_remedy = logging.getLogger("remedy")

# Create your views here.

g_current = datetime.datetime(2015,1,1,0,0)
g_start = datetime.date(g_current.year,1,1)
last_day = datetime.date(g_current.year,12,31)
g_isfirst = g_start.weekday()
g_last_week = last_day.strftime('%W')

g_weeks={}
if g_isfirst !=0:
    end = datetime.timedelta(7-g_start.weekday()-1)
    g_weeks[0]=[g_start,g_start+end]
g_start += datetime.timedelta(7 - g_start.weekday())


def print_date(i):
    days = datetime.timedelta(weeks=i)
    end = g_start + days  # 每周的开始时间

    if i + 1 == int(g_last_week):
        g_weeks[i + 1] = [end, last_day]
    else:
        g_weeks[i + 1] = [end, end + datetime.timedelta(6)]

def allweeks():
    for i in range(0, int(g_last_week)):
        print_date(i)
    return g_weeks

def getItem():###单独查看某一天的http数据
    importlib.reload(sys)

    begin_time = '2019-04-24 00:00:00'
    end_time = '2019-04-25 00:00:00'
    shopid = 142  ##models.S_ShopId.objects.all()

    ZMT_DB_HOST = 'edb_a78207'
    ZMT_APPKEY = 'b83a90e4'
    ZMT_IP = '114.249.217.19'
    ZMT_APPSCRET = 'a409fdd578764d1e8fc5824889d82a57'
    ZMT_TOKEN = '2f2698eed18c4aa38aa0826e25f2ffea'
    ZMT_EDB_URL = 'http://vip3073.edb09.net/rest/index.aspx'
    timestemp = time.strftime("%Y%m%d%H%M", time.localtime())
    ##print(shopid)

    sign_syspram = {'token': ZMT_TOKEN, 'appscret': ZMT_APPSCRET, 'dbhost': ZMT_DB_HOST, 'appkey': ZMT_APPKEY,
                    'format': 'json', 'method': 'edbTradeGet', 'timestamp': timestemp, 'v': '2.0', 'slencry': '0',
                    'ip': ZMT_IP}
    sign_methodpram = {'date_type': '订货日期', 'begin_time': begin_time, 'end_time': end_time, 'shopid': shopid,
                       'page_no': '1', 'page_size': '10'}
    sign_last = dict(sign_syspram, **sign_methodpram)
    sign_tuple = sorted(sign_last.items(), key=lambda e: e[0], reverse=False)
    signsource = ''
    for var in sign_tuple:
        signsource += str(var[0]) + str(var[1])

    signsource = ZMT_APPKEY + signsource

    signsource = signsource.encode("utf-8")

    md5object = hashlib.md5()
    md5object.update(signsource)
    sign = md5object.hexdigest()
    sign = sign.upper()
    ##print(sign)

    sign_temp = {'sign': sign}
    sign_last = dict(sign_last, **sign_temp)
    sign_tuple1 = sorted(sign_last.items(), key=lambda e: e[0], reverse=False)
    ##print(sign_tuple1)

    data = ''
    for var in sign_tuple1:
        if var[0] != 'appscret' and var[0] != 'token':
            if var[0] != 'v':
                data += str(var[0]) + '=' + str(var[1]) + '&'
            else:
                data += str(var[0]) + '=' + str(var[1])

    data = data.encode("utf-8")
    res = requests.post(ZMT_EDB_URL, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    ##print('返回')
    restimp = handleStringFormat(res.text)
    print(res.text)
    resData = json.loads(restimp, strict=False);
    if resData.__contains__('Success') == False:
        return 0

    return res.text
def getData_crontab():##定时器调用接口
    ##weekss=allweeks()
    begindate='2019-03-30 00:00:00'
    enddate='2019-03-30 23:59:59'
    pagesize = 1000
    shoiparray = models.SEdbShop.objects.all().values_list()
    text = ''
    zongtiaoshu=0
    for id in shoiparray:
        totalnum = getTotalNum(begindate, enddate, str(id[1]))
        if totalnum=='0':
            continue
        zongtiaoshu=int(totalnum)
        break
    print("总结果："+str(zongtiaoshu))
    kk="总结果："+str(zongtiaoshu)
    printEndTask()
    return kk
def getData_multiprocess(processtype,benginday,endday): ##多进程调用接口
    processInt=7
    shoiparray = models.SEdbShop.objects.all().values_list()

    lenshop=shoiparray.__len__()
    pagesize=lenshop//processInt

    listshopId=[]
    node = []
    i=0
    for val in shoiparray:
        if i < pagesize:
           node.append(val[1])
           i+=1
        else:
           listshopId.append(node)
           node = []
           node.append(val[1])
           i=1

    if node.__len__()!=0:
        listshopId.append(node)

    logger.info(listshopId)
    minuteProcesstype=['getData_minute_orderdate','getData_minute_paydate','getData_minute_deliverydate','getData_minute_reviewtime','getData_minute_cancletime','getData_minute_complatetime','getData_minute_inspecttime','getData_minute_weighttime']##['订货日期','付款日期','发货日期','审单时间','取消时间','完成时间','验货日期','称重时间']

    obj = models.AJobLog.objects.filter(status=1, jobname__startswith='getData_minute').aggregate(Max('endTime'))
    timeMax=datetime.datetime.strftime(obj["endTime__max"],'%Y-%m-%d %H:%M:%S')

    poolhandle = Pool(8)
    if processtype == 'getData_minute':
        timespliceend = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        timesplicestart = getbeforfiveminute(timespliceend)

        if timeMax < timesplicestart:
            timesplicestart=timeMax

        for tp in minuteProcesstype:
            for shopIdarray in listshopId:
                ##print("开辟分钟进程")
                poolhandle.apply_async(getData_sub,kwds={'shopid': shopIdarray, 'begindate': str(timesplicestart), 'enddate': str(timespliceend),'processtype': str(tp)})
    else:
        for shopIdarray in listshopId:
             ##p = Process(target=getData_sub,kwargs=param)
              logger.info("开辟进程1133")
              poolhandle.apply_async(getData_sub,kwds={'shopid':shopIdarray,'begindate':str(benginday),'enddate':str(endday),'processtype':str(processtype)})

    poolhandle.close()
    poolhandle.join()

    printEndTask()
    return listshopId

def getData_onemonth():
    now_time = datetime.datetime.now()
    first_day = datetime.datetime(now_time.year, now_time.month, 1, 23, 59, 59)
    up_last = first_day - datetime.timedelta(days=1)
    up_first_day = datetime.datetime(up_last.year, up_last.month, 1)
    logger.info("start month day")
    logger.info(up_first_day.strftime("%Y-%m-%d"))
    logger.info(up_last.strftime("%Y-%m-%d"))
    getData_multiprocess('getData_month',up_first_day.strftime("%Y-%m-%d"), up_last.strftime("%Y-%m-%d"))
    return
def getData_sevenDay():
    curentTime= datetime.datetime.now()
    onedaybeforeDay=curentTime.strftime("%Y-%m-%d")
    sevendaybeforeDay = (curentTime - datetime.timedelta(days=8)).strftime("%Y-%m-%d")

    print("start seven day")
    print(sevendaybeforeDay)
    print(onedaybeforeDay)
    getData_multiprocess('getData_sevenday',sevendaybeforeDay,onedaybeforeDay)
    return
def getData_minute():
    obj=models.AJobLog.objects.filter(status=0,jobname__startswith= 'getData_minute')
    if obj.exists():
        return "***************有minute任务未执行完***************************"

    curentTime = datetime.datetime.now()
    curentDay = curentTime.strftime("%Y-%m-%d")
    getData_multiprocess('getData_minute', curentDay, curentDay)
def bakGetDataLog():

    curentTime = datetime.datetime.now()
    onedaybeforeDay = curentTime.strftime("%Y-%m-%d")
    sevendaybeforeDay = (curentTime - datetime.timedelta(days=30)).strftime("%Y-%m-%d")
    print("wenti")
    obj = models.AJobLog.objects.filter(status=1, jobname__startswith='getData_minute',createTime__lte=sevendaybeforeDay )

    return

@csrf_exempt
def getData_remedy(request):
    logger_remedy.info("开始补救！！")
    begindate_error=request.GET.get('begindate_error')
    enddate_error = request.GET.get('enddate_error')
    shopId_error = request.GET.get('shopId_error')
    error_flag = request.GET.get('error_flag')

    if begindate_error == None or begindate_error=='':
        err_msg={'status':1,'err_info':'begindate_error 不能为空'}
        return getresponse(err_msg)
    else:
        if isVaildDate(begindate_error)==False:
            err_msg = {'status': 1, 'err_info': 'begindate_error 不是日期字符串'}
            return getresponse(err_msg)
    if enddate_error == None or enddate_error=='':
        err_msg = {'status': 1, 'err_info': 'enddate_error 不能为空'}
        return getresponse(err_msg)
    else:
        if isVaildDate(enddate_error)==False:
            err_msg = {'status': 1, 'err_info': 'enddate_error 不是日期字符串'}
            return getresponse(err_msg)

    if shopId_error == None or shopId_error=='':
        err_msg = {'status': 1, 'err_info': 'shopId_error 不能为空'}
        return getresponse(err_msg)
    else:
        if is_Integer(shopId_error)==False:
            err_msg = {'status': 1, 'err_info': 'shopId_error 不是数字'}
            return getresponse(err_msg)

    if error_flag == None or error_flag=='':
        err_msg = {'status': 1, 'err_info': 'error_flag 不能为空'}
        return getresponse(err_msg)

    begindate = begindate_error
    enddate = enddate_error
    pagesize = 1000
    shopId=shopId_error
    handleConnPool = OperateDB_Pool()

    if ":" not in begindate:
        begindate = str(begindate_error) + ' 00:00:00'
        enddate = str(enddate_error) + ' 00:00:00'

    logger_remedy.info(begindate)
    logger_remedy.info(enddate)
    logger_remedy.info("*******************#############################")
    totalnum = getTotalNum(begindate, enddate, shopId)

    try:
        if totalnum == '0':
            ##text += '****************ship id:' + str(id[1]) + 'NOthing order\n'  ##id[1]
            handleConnPool.updateLog(error_flag,begindate, enddate, shopId)
        else:
            mo = int(totalnum) % pagesize
            pageNum = int(totalnum) // pagesize
            getformEDB(begindate, enddate, shopId, pageNum, str(pagesize), mo,1,handleConnPool)
            handleConnPool.updateLog(error_flag,begindate, enddate, shopId)
    except Exception as err:
        logger_remedy.error(err)
        msg={'status':1,'err_info':err}
        return getresponse(msg)

    logger_remedy.info("补救完成")
    printEndTask()
    msg={'status':0}
    return getresponse(msg)
@csrf_exempt
def hartbeat(request):
    msg = {'status': 0}
    return getresponse(msg)
def getresponse(msg):
    response = HttpResponse(json.dumps(msg), content_type="application/json")
    response["Access-Control-Allow-Origin"]="*"
    response["Access-Control-Allow-Methods"]="POST, GET, OPTIONS"
    response["Access-Control-Max-Age"]="1000"
    response["Access-Control-Allow-Headers"]="*"
    return response
def isVaildDate(date):
    try:
        if ":" in date:
            time.strptime(date, "%Y-%m-%d %H:%M:%S")
        else:
            time.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False

def is_Integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

    return False

def getData_sub(**kwds):##具体计算
    logger.info('begin getdata')
    begindate = kwds['begindate']
    enddate = kwds['enddate']
    listarray = kwds['shopid']
    processtype = kwds['processtype']
    minuteProcesstype = {'getData_minute_orderdate': '订货日期', 'getData_minute_paydate': '发货日期','getData_minute_deliverydate': '审单时间', 'getData_minute_reviewtime': '取消时间','getData_minute_cancletime': '取消时间', 'getData_minute_complatetime': '完成时间','getData_minute_inspecttime': '验货日期', 'getData_minute_weighttime': '称重时间'}
    if processtype in minuteProcesstype.keys():
        daylist = getBetweenDay(begindate,enddate,1)
    else:
        daylist = getBetweenDay(begindate,enddate)


    handleConnPool1= OperateDB_Pool()
    ##print(daylist)
    ##print(listarray)
    pagesize = 1000
    ##shoiparray = models.SEdbShop.objects.all().values_list()
    ##text = ''
    ##print("######################################################################################")

    ##########先插入log###############



    paramlist=[]
    for id1 in listarray:
        for var1 in daylist:
            node = []
            print(processtype)
            if processtype in minuteProcesstype.keys():
                begindate = str(kwds['begindate'])
                enddate = str(kwds['enddate'])
            else:
                begindate = (str(var1['beginday']) + ' 00:00:00')
                enddate = (str(var1['endday']) + ' 00:00:00')

            node.append(os.getppid())
            node.append(int(id1))
            node.append(begindate)
            node.append(enddate)
            node.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            node.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            paramlist.append(node)

    ##print(paramlist)
    ###print(daylist)
    handleConnPool1.insertLog(processtype,paramlist)
    totalnum1=0
    for id in listarray:
        for var in daylist:
            if processtype in minuteProcesstype.keys():
                logger.info("yes")
                begindate = str(kwds['begindate'])
                enddate = str(kwds['enddate'])
                totalnum1 = getTotalNum(begindate, enddate, str(id),minuteProcesstype[processtype])
            else:
                logger.info("No")
                begindate = (str(var['beginday']) + ' 00:00:00')
                enddate = (str(var['endday']) + ' 00:00:00')
                logger.info("准备参数：" + begindate + "," + enddate + "," + str(id))
                totalnum1 = getTotalNum(begindate, enddate, str(id))
            logger.info("获得条数："+totalnum1)
            if totalnum1 == '0':
                 ##text += '****************ship id:' + str(id) + 'NOthing order\n'  ##id[1]
                 logger.info("&&&&&&&&&&&&&&&&&&&&&没有数据&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                 logger.info('更新数据:'+processtype+','+begindate+','+enddate+','+str(id))
                 handleConnPool1.updateLog(processtype,begindate,enddate,str(id))
                 continue
            mo = int(totalnum1) % pagesize
            pageNum = int(totalnum1) // pagesize
            logger.info('实际插入')
            if processtype in minuteProcesstype.keys():
                 getformEDB(begindate, enddate, id, pageNum, str(pagesize), mo,1,handleConnPool1,minuteProcesstype[processtype])
            else:
                 getformEDB(begindate, enddate, id, pageNum, str(pagesize), mo, 1,handleConnPool1)
            ##text += time.strftime("%Y%m%d%H%M", time.localtime())
            print("update log:"+processtype+begindate+enddate+id)
            handleConnPool1.updateLog(processtype,begindate, enddate,id)

    return 'finish'
def getbeforfiveminute(current):
    ctime =datetime.datetime.strptime(current, '%Y-%m-%d %H:%M:%S')
    beforeTime=(ctime-datetime.timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
    return beforeTime
@csrf_exempt
def getData(request):##网络调用接口
    ##a=MqMessage()
    txt=getItem()
    ##txt=getData_crontab()
    ##getData_everyDay()
    ##getData_everyDay()
    ##getData_sevenDay()
    ##getData_onemonth()
    ##getData_multiprocess()
    ##getData_minute()
    ##getData_onemonth()
    ##getData_minute()
    return  HttpResponse(txt, content_type="application/json")

def getTotalNum(bgdate,enddate,shopId,data_type='订货日期'):
    importlib.reload(sys)
    logger.info('getdata!!!')
    logger.info(data_type)
    ZMT_DB_HOST = 'edb_a78207'
    ZMT_APPKEY = 'b83a90e4'
    ZMT_IP = '114.249.217.19'
    ZMT_APPSCRET = 'a409fdd578764d1e8fc5824889d82a57'
    ZMT_TOKEN = '2f2698eed18c4aa38aa0826e25f2ffea'
    ZMT_EDB_URL = 'http://vip3073.edb09.net/rest/index.aspx'
    timestemp = time.strftime("%Y%m%d%H%M", time.localtime())
    begin_time =bgdate
    end_time = enddate
    shopid = shopId  ##models.S_ShopId.objects.all()
    ##print(shopid)

    sign_syspram = {'token': ZMT_TOKEN, 'appscret': ZMT_APPSCRET, 'dbhost': ZMT_DB_HOST, 'appkey': ZMT_APPKEY,
                    'format': 'json', 'method': 'edbTradeGet', 'timestamp': timestemp, 'v': '2.0', 'slencry': '0',
                    'ip': ZMT_IP}
    sign_methodpram = {'date_type': data_type, 'begin_time': begin_time, 'end_time': end_time, 'shopid': shopid,
                       'page_no': '1', 'page_size': '1'}
    sign_last = dict(sign_syspram, **sign_methodpram)
    sign_tuple = sorted(sign_last.items(), key=lambda e: e[0], reverse=False)
    signsource = ''
    for var in sign_tuple:
        signsource += str(var[0]) + str(var[1])

    signsource = ZMT_APPKEY + signsource

    signsource = signsource.encode("utf-8")

    md5object = hashlib.md5()
    md5object.update(signsource)
    sign = md5object.hexdigest()
    sign = sign.upper()
    ##print(sign)

    sign_temp = {'sign': sign}
    sign_last = dict(sign_last, **sign_temp)
    sign_tuple1 = sorted(sign_last.items(), key=lambda e: e[0], reverse=False)
    ##print(sign_tuple1)

    data = ''
    for var in sign_tuple1:
        if var[0] != 'appscret' and var[0] != 'token':
            if var[0] != 'v':
                data += str(var[0]) + '=' + str(var[1]) + '&'
            else:
                data += str(var[0]) + '=' + (var[1])

    data = data.encode("utf-8")
    logger.info("begin post")
    logger.info(data)
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    try:
        res = requests.post(ZMT_EDB_URL, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    except Exception as err:
        logger.error(err)
    logger.info("返回")
    logger.info(res.text)
    restimp=handleStringFormat(res.text)

    resData =  json.loads(restimp,strict=False);
    if resData.__contains__('Success') == False:
        logger.error("查询总数失败！11")
        logger.error(restimp)
        return 0
    # tempItem = resData['Success']
    # if tempItem.__contains__('total_results') != False:
    #     print('get num')
    #     print(tempItem)
    #     print(tempItem['total_results'])
    #     return tempItem['total_results']

    productItem = resData['Success']['items']

    if not productItem:
        logger.info("查询总数失败！")
        return
    total_num='0'
    for v in productItem.values():
        for i, val in enumerate(v):
            total_num =val['total_num']
    logger.info("返回总数"+total_num)
    return total_num
def getformEDB(bgdate,enddate,shopId,pageNum,pagesize,mo,isMultiProcess=0,handleConnPool=None,data_type='订货日期'):
    importlib.reload(sys)

    ZMT_DB_HOST = 'edb_a78207'
    ZMT_APPKEY = 'b83a90e4'
    ZMT_IP = '114.249.217.19'
    ZMT_APPSCRET = 'a409fdd578764d1e8fc5824889d82a57'
    ZMT_TOKEN = '2f2698eed18c4aa38aa0826e25f2ffea'
    ZMT_EDB_URL = 'http://vip3073.edb09.net/rest/index.aspx'
    begin_time= bgdate##(datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    end_time=enddate##datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    shopid=shopId##models.S_ShopId.objects.all()
    ##print(shopid)
    pageNO=0
    if mo !=0:
        pageNum+=1
    while 1:
            pageNO+=1
            timestemp = time.strftime("%Y%m%d%H%M", time.localtime())
            sign_syspram={'token':ZMT_TOKEN,'appscret':ZMT_APPSCRET,'dbhost':ZMT_DB_HOST,'appkey':ZMT_APPKEY,'format':'json','method':'edbTradeGet','timestamp':timestemp,'v':'2.0','slencry':'0','ip':ZMT_IP}
            sign_methodpram={'date_type':data_type,'begin_time':begin_time,'end_time':end_time,'shopid':shopid,'page_no':str(pageNO),'page_size':pagesize}
            sign_last = dict(sign_syspram, **sign_methodpram)
            sign_tuple = sorted(sign_last.items(), key=lambda e:e[0], reverse=False)
            signsource=''
            for var in  sign_tuple:
                signsource+=var[0]+var[1]

            signsource=ZMT_APPKEY+signsource

            ##print(signsource)
            signsource = signsource.encode("utf-8")
            print(signsource)
            md5object=hashlib.md5()
            md5object.update(signsource)
            sign=md5object.hexdigest()
            sign=sign.upper()

            sign_temp = {'sign': sign}
            sign_last = dict(sign_last, **sign_temp)
            sign_tuple1 = sorted(sign_last.items(), key=lambda e: e[0], reverse=False)
            ##print(sign_tuple1)

            data=''
            for var in sign_tuple1:
                if var[0]!='appscret' and var[0]!='token':
                    if var[0]!='v':
                       data += var[0]+'='+var[1]+'&'
                    else:
                        data+= var[0]+'='+var[1]

            data=data.encode("utf-8")
           ## models.AJobLog.objects.create(jobname='getData_all',jobtype='auto',handjobid=os.getpid(),handsubjobno=shopid,startTime=begin_time,endTime=end_time,status=0,pageNo=pageNO)
            try:
               res=requests.post(ZMT_EDB_URL,data=data,headers={'Content-Type': 'application/x-www-form-urlencoded','Connection': 'close'})
            except Exception as err:
                logger.error(err)
            logger.info('返回')
            ##print('shopid:'+shopid+',pageNO:'+str(pageNO)+'pagesize:'+pagesize)
            ##print(res.text)
            restimp = handleStringFormat(res.text)
            ##print(restimp)
            resData = json.loads(restimp,strict=False);
            if resData.__contains__('Success')==False:
                return 'error msg:'+resData['error_msg']
            productItem=resData['Success']['items']
            if not productItem:
                return
            listorder=[]
            listItem=[]
            listordertemp=[]
            for v in productItem.values():
                for i,val in enumerate(v):
                    saveItem(val['tid_item'],isMultiProcess,handleConnPool)
                    val.pop('tid_item')
                    val.pop('总数量')
                    val.pop('total_num')
                    lastdic=changeDataFormat(val,0)
                    listorder.append(crate_ordeItem(lastdic))
                    listordertemp.append(lastdic)
            try:
                if isMultiProcess==1:
                    logger.info("开process数据库连接池")
                    handleConnPool.getinputdata(listordertemp)
                    handleConnPool.sqlecude(1)
                else:
                    logger.info("普通数据库连接")
                    op = OperateDB(listordertemp)
                    op.sqlecude(1)
                ##models.SOrderItem.objects.bulk_create(listItem)
                ##models.SOrder.objects.bulk_create(listorder)
            except Exception as err:
                logger.error('******************存储失败************************')
                logger.error(err)
            ##models.AJobLog.objects.filter(jobname='getData_all', jobtype='auto', handjobid=os.getpid(),
            ##                              handsubjobno=shopid, startTime=begin_time, endTime=end_time, status=0,
            ##                              pageNo=pageNO).update(status=1)
            if pageNO >=pageNum:
                break
    return 'shop id'+shopId+'finish\n'

def changeDataFormat(dict,flag):
    modelsstr=''
    if flag==1:
        modelsstr='SOrderItem'
    else:
        modelsstr = 'SOrder'
    modelobj = apps.get_model('syn_edb', modelsstr)
    fielddic={}
    for field in modelobj._meta.fields:
        fielddic[field.name] = field.verbose_name
        if type(field).__name__== 'DecimalField':
            if dict[field.name]=='':
                dict[field.name]=float(0)
        if type(field).__name__== 'IntegerField':
            if dict[field.name]=='':
                dict[field.name]=0
        if type(field).__name__ == 'DateTimeField':
            if field.name!='createTime' and field.name!='updateTime':
                if dict[field.name]=='':
                   dict[field.name]=None
    return dict
def saveItem(productlistItem,is_Process=0,handleConnPool=None):
    print('item insert&&&&&&&&&&&&&&&&&&&&&&&')
    for item in productlistItem:
        ##print(item)
        changeDataFormat(item, 1)
    try:

        if is_Process==1:
            print("开2222222222222数据库连接池")
            handleConnPool.getinputdata(productlistItem)
            handleConnPool.sqlecude(0)
        else:
            op = OperateDB(productlistItem)
            op.sqlecude(0)
        ##models.SOrderItem.objects.bulk_create(listItem)
        ##models.SOrder.objects.bulk_create(listorder)
    except Exception as err:
        print('******************存储失败************************')
        print(err)
    ''' 
    for item in productlistItem:
        print(item)
        changeDataFormat(item,1)
        ##models.SOrderItem.objects.create(**item)
        node=create_buckItem(item)
        liststor.append(node)
    '''
    return
def create_buckItem(dic):

    node=models.SOrderItem(tid=dic['tid'],pro_detail_code=dic['pro_detail_code'],pro_name=dic['pro_name'],specification=dic['specification'],barcode=dic['barcode'],\
                           combine_barcode=dic['combine_barcode'],\
    iscancel=dic['iscancel'],\
    isscheduled=dic['isscheduled'],\
    stock_situation=dic['stock_situation'],\
    isbook_pro=dic['isbook_pro'],\
    iscombination=dic['iscombination'],\
    isgifts=dic['isgifts'],\
    gift_num=dic['gift_num'],\
    book_storage=dic['book_storage'],\
    pro_num=dic['pro_num'],\
    send_num=dic['send_num'],\
    refund_num=dic['refund_num'],\
    refund_renum=dic['refund_renum'],\
    inspection_num=dic['inspection_num'],\
    timeinventory=dic['timeinventory'],\
    cost_price=dic['cost_price'],\
    sell_price=dic['sell_price'],\
    average_price=dic['average_price'],\
    original_price=dic['original_price'],\
    sys_price=dic['sys_price'],\
    ferght=dic['ferght'],\
    item_discountfee=dic['item_discountfee'],\
    inspection_time=dic['inspection_time'],\
    weight=dic['weight'],\
    shopid=dic['shopid'],\
    out_tid=dic['out_tid'],\
    out_proid=dic['out_proid'],\
    out_prosku=dic['out_prosku'],\
    proexplain=dic['proexplain'],\
    buyer_memo=dic['buyer_memo'],\
    seller_remark=dic['seller_remark'],\
    distributer=dic['distributer'],\
    distribut_time=dic['distribut_time'],\
    second_barcode=dic['second_barcode'],\
    product_no=dic['product_no'],\
    brand_number=dic['brand_number'],\
    brand_name=dic['brand_name'],\
    book_inventory=dic['book_inventory'],\
    product_specification=dic['product_specification'],\
    discount_amount=dic['discount_amount'],\
    MD5_encryption=dic['MD5_encryption'],\
    sncode=dic['sncode'],\
    store_location=dic['store_location'],\
    pro_type=dic['pro_type'],\
    storage_id=dic['storage_id'],\
    credit_amount=dic['credit_amount']
    )
    return node
def crate_ordeItem(dic):
    node = models.SOrder(resultNum=dic['resultNum'],storage_id=dic['storage_id'],\
    transaction_id=dic['transaction_id'],\
    customer_id=dic['customer_id'],\
    distributor_id=dic['distributor_id'],\
    shop_name=dic['shop_name'],\
    out_tid=dic['out_tid'],\
    out_pay_tid=dic['out_pay_tid'],\
    voucher_id=dic['voucher_id'],\
    shopid=dic['shopid'],\
    serial_num=dic['serial_num'],\
    order_channel=dic['order_channel'],\
    order_from=dic['order_from'],\
    buyer_id=dic['buyer_id'],\
    buyer_name=dic['buyer_name'],\
    type=dic['type'],\
    status=dic['status'],\
    abnormal_status=dic['abnormal_status'],\
    merge_status=dic['merge_status'],\
    receiver_name=dic['receiver_name'],\
    receiver_mobile=dic['receiver_mobile'],\
    phone=dic['phone'],\
    province=dic['province'],\
    city=dic['city'],\
    district=dic['district'],\
    address=dic['address'],\
    post=dic['post'],\
    email=dic['email'],\
    is_bill=dic['is_bill'],\
    invoice_name=dic['invoice_name'],\
    invoice_situation=dic['invoice_situation'],\
    invoice_title=dic['invoice_title'],\
    invoice_type=dic['invoice_type'],\
    invoice_content=dic['invoice_content'],\
    pro_totalfee=dic['pro_totalfee'],\
    order_totalfee=dic['order_totalfee'],\
    reference_price_paid=dic['reference_price_paid'],\
    invoice_fee=dic['invoice_fee'],\
    cod_fee=dic['cod_fee'],\
    other_fee=dic['other_fee'],\
    refund_totalfee=dic['refund_totalfee'],\
    discount_fee=dic['discount_fee'],\
    discount=dic['discount'],\
    channel_disfee=dic['channel_disfee'],\
    merchant_disfee=dic['merchant_disfee'],\
    order_disfee=dic['order_disfee'],\
    commission_fee=dic['commission_fee'],\
    is_cod=dic['is_cod'],\
    point_pay=dic['point_pay'],\
    cost_point=dic['cost_point'],\
    point=dic['point'],\
    superior_point=dic['superior_point'],\
    royalty_fee=dic['royalty_fee'],\
    external_point=dic['external_point'],\
    express_no=dic['express_no'],\
    express=dic['express'],\
    express_coding=dic['express_coding'],\
    online_express=dic['online_express'],\
    sending_type=dic['sending_type'],\
    real_income_freight=dic['real_income_freight'],\
    real_pay_freight=dic['real_pay_freight'],\
    gross_weight=dic['gross_weight'],\
    gross_weight_freight=dic['gross_weight_freight'],\
    net_weight_freight=dic['net_weight_freight'],\
    freight_explain=dic['freight_explain'],\
    total_weight=dic['total_weight'],\
    tid_net_weight=dic['tid_net_weight'],\
    tid_time=dic['tid_time'],\
    pay_time=dic['pay_time'],\
    get_time=dic['get_time'],\
    order_creater=dic['order_creater'],\
    business_man=dic['business_man'],\
    payment_received_operator=dic['payment_received_operator'],\
    payment_received_time=dic['payment_received_time'],\
    review_orders_operator=dic['review_orders_operator'],\
    review_orders_time=dic['review_orders_time'],\
    finance_review_operator=dic['finance_review_operator'],\
    finance_review_time=dic['finance_review_time'],\
    advance_printer=dic['advance_printer'],\
    printer=dic['printer'],\
    print_time=dic['print_time'],\
    is_print=dic['is_print'],\
    adv_distributer=dic['adv_distributer'],\
    adv_distribut_time=dic['adv_distribut_time'],\
    distributer=dic['distributer'],\
    distribut_time=dic['distribut_time'],\
    is_inspection=dic['is_inspection'],\
    inspecter=dic['inspecter'],\
    inspect_time=dic['inspect_time'],\
    cancel_operator=dic['cancel_operator'],\
    cancel_time=dic['cancel_time'],\
    revoke_cancel_er=dic['revoke_cancel_er'],\
    revoke_cancel_time=dic['revoke_cancel_time'],\
    packager=dic['packager'],\
    pack_time=dic['pack_time'],\
    weigh_operator=dic['weigh_operator'],\
    weigh_time=dic['weigh_time'],\
    book_delivery_time=dic['book_delivery_time'],\
    delivery_operator=dic['delivery_operator'],\
    delivery_time=dic['delivery_time'],\
    locker=dic['locker'],\
    lock_time=dic['lock_time'],\
    book_file_time=dic['book_file_time'],\
    file_operator=dic['file_operator'],\
    file_time=dic['file_time'],\
    finish_time=dic['finish_time'],\
    modity_time=dic['modity_time'],\
    is_promotion=dic['is_promotion'],\
    promotion_plan=dic['promotion_plan'],\
    out_promotion_detail=dic['out_promotion_detail'],\
    good_receive_time=dic['good_receive_time'],\
    receive_time=dic['receive_time'],\
    verificaty_time=dic['verificaty_time'],\
    enable_inte_sto_time=dic['enable_inte_sto_time'],\
    enable_inte_delivery_time=dic['enable_inte_delivery_time'],\
    alipay_id=dic['alipay_id'],\
    alipay_status=dic['alipay_status'],\
    pay_mothed=dic['pay_mothed'],\
    pay_status=dic['pay_status'],\
    platform_status=dic['platform_status'],\
    rate=dic['rate'],\
    currency=dic['currency'],\
    delivery_status=dic['delivery_status'],\
    buyer_message=dic['buyer_message'],\
    service_remarks=dic['service_remarks'],\
    inner_lable=dic['inner_lable'],\
    distributor_mark=dic['distributor_mark'],\
    system_remarks=dic['system_remarks'],\
    other_remarks=dic['other_remarks'],\
    message=dic['message'],\
    message_time=dic['message_time'],\
    is_stock=dic['is_stock'],\
    related_orders=dic['related_orders'],\
    related_orders_type=dic['related_orders_type'],\
    import_mark=dic['import_mark'],\
    delivery_name=dic['delivery_name'],\
    is_new_customer=dic['is_new_customer'],\
    distributor_level=dic['distributor_level'],\
    cod_service_fee=dic['cod_service_fee'],\
    express_col_fee=dic['express_col_fee'],\
    product_num=dic['product_num'],\
    sku=dic['sku'],\
    item_num=dic['item_num'],\
    single_num=dic['single_num'],\
    flag_color=dic['flag_color'],\
    is_flag=dic['is_flag'],\
    taobao_delivery_order_status=dic['taobao_delivery_order_status'],\
    taobao_delivery_status=dic['taobao_delivery_status'],\
    taobao_delivery_method=dic['taobao_delivery_method'],\
    order_process_time=dic['order_process_time'],\
    is_break=dic['is_break'],\
    breaker=dic['breaker'],\
    break_time=dic['break_time'],\
    break_explain=dic['break_explain'],\
    plat_send_status=dic['plat_send_status'],\
    plat_type=dic['plat_type'],\
    is_adv_sale=dic['is_adv_sale'],\
    provinc_code=dic['provinc_code'],\
    city_code=dic['city_code'],\
    area_code=dic['area_code'],\
    express_code=dic['express_code'],\
    last_returned_time=dic['last_returned_time'],\
    last_refund_time=dic['last_refund_time'],\
    deliver_centre=dic['deliver_centre'],\
    deliver_station=dic['deliver_station'],\
    is_pre_delivery_notice=dic['is_pre_delivery_notice'],\
    jd_delivery_time=dic['jd_delivery_time'],\
    Sorting_code=dic['Sorting_code'],\
    cod_settlement_vouchernumber=dic['cod_settlement_vouchernumber'],\
    three_codes=dic['three_codes'],\
    send_site_name=dic['send_site_name'],\
    distributing_centre_name=dic['distributing_centre_name'],\
    originCode=dic['originCode'],\
    destCode=dic['destCode'],\
    big_marker=dic['big_marker'],\
    platform_preferential=dic['platform_preferential'],\
    tid=dic['tid']\
    )
    return node
def handleStringFormat(strinput):
    strinput = strinput.replace("\\n", "").replace("\\r", "")
    return strinput
def getBetweenDay(begin_date1,end_date1,flag=0):
    date_list = []
    if flag==1:
        begin_date = datetime.datetime.strptime(begin_date1, "%Y-%m-%d %H:%M:%S")
        begin_date=begin_date.strftime("%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date1, "%Y-%m-%d %H:%M:%S")
        end_date = end_date.strftime("%Y-%m-%d")
        nodetemp={}
        nodetemp['beginday'] = begin_date1
        nodetemp['end_date'] = end_date1
        date_list.append(nodetemp)
        return date_list

    else:
        strdate1=datetime.datetime.strptime(begin_date1, '%Y-%m-%d')
        enddate_ok=datetime.datetime.strptime(end_date1, '%Y-%m-%d')
        while strdate1 < enddate_ok:
            node={}
            date_str = strdate1.strftime("%Y-%m-%d")
            node['beginday']=date_str
            node['endday'] = (strdate1+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            date_list.append(node)
            strdate1 += datetime.timedelta(days=1)
    return date_list
def printEndTask():
    logger.info('**************************************************************')
    logger.info('commander finish task')
    logger.info('**************************************************************')
    return



