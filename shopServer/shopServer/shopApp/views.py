from django.shortcuts import render


from django.http import HttpResponse

import os


import datetime 
import random


from django.db import connection

import json

# Create your views here.

def home(request):

    # cursor = connection.cursor()

 

    # name = "liu";

    # cursor.execute('CREATE TABLE ad(adid varchar(255),imgs varchar(255),adtime timestamp not null default current_timestamp)')

    # cursor.execute('CREATE TABLE manager(username varchar(255),pwd varchar(255))')

    # cursor.execute('CREATE TABLE Persons2(Id_P int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255))')


    



    # cursor.execute('create table xxx');
    return render(request , "base.html");


def error(request):
    return HttpResponse("我是404");



def goodsManage(request):
    return render(request , "goodsManage.html");

def adPage(request):
    return render(request , "adPage.html");


def userManage(request):
    return render(request , "userManage.html");

def orderManage(request):
    print("*****************");
    return render(request , "orderManage.html");

def adManage(request):
    return render(request , "adManage.html");

def activeManage(request):

    return render(request , "activeManage.html");

def addGoods(request):
    return render(request, "goodsAdd.html")

def changePic(request):
	return render(request, "changePic.html")

#改变轮播图界面
def changePic(request):
	return render(request,"changePic.html")


# 根据用户名创建属于他的表格
def personal(request):
    # name=request.get["name"];
    name=request.POST["name"]
    try:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE %s_lookhistory(lookId varchar(255),userId varchar(255),looktime timestamp not null default current_timestamp)'%name)
        cursor.execute('CREATE TABLE %s_carts(cartsId varchar(255),number varchar(255),goodsId varchar(255),userId varchar(255))'%name)
        cursor.execute('CREATE TABLE %s_favorite(favoriteId varchar(255),goodsId varchar(255),userId varchar(255),favtime timestamp not null default current_timestamp)'%name)
        cursor.execute('CREATE TABLE %s_recharge(rechargeId varchar(255),money varchar(255),status varchar(255),rechargetime timestamp not null default current_timestamp)'%name)
        cursor.execute('CREATE TABLE %s_orderlist(orderlistId varchar(255),userId varchar(255),orderId varchar(255))'%name)
        cursor.execute('CREATE TABLE %s_ordertable(orderId varchar(255),userId varchar(255),ordertime timestamp not null default current_timestamp,isaudit tinyint(1),ispass tinyint(1),iscancel tinyint(1),ispay tinyint(1),issend tinyint(1),ispaydone tinyint(1),isclose tinyint(1))'%name)
        cursor.execute('CREATE TABLE %s_score(scoreId varchar(255),scoretime timestamp not null default current_timestamp,getpath nvarchar(255),scorecount varchar(255))'%name)
        cursor.execute('CREATE TABLE %s_rewardtable(rewardId varchar(255),userId varchar(255))'%name)
    except Exception as e:    
            return HttpResponse(json.dumps({'data':"创建该用户的其他表失败", 'status':'error'}), content_type="application/json");

    statusDic = {"status" : "ok" , "message" : "创建用户其他表成功"};
    return HttpResponse(json.dumps(statusDic) , content_type = "application/json");



# 登录界面
def login(request):
    
    return render(request , "login.html");


# 登录接口 (ok)
def loginApi(request):
 
    userName = request.POST["name"]
    password = request.POST["password"]
    # userName = "admin"
    # password = "123456"

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM manager WHERE username=\"%s\" AND pwd=\"%s\"'%(userName , password))
    a = cursor.fetchall()
    cursor.close()
   
    if a:
        successMSG = {"status":"ok","message":"登陆成功"}
        return HttpResponse(json.dumps(successMSG) , content_type="application/json")
    else:
        errorMSG = {"status":"error","message":"登录失败"}
        return HttpResponse(json.dumps(errorMSG) , content_type="application/json")


# 用户添加接口
def userManageJsonAdd(request):
    # userid = request.POST["userid"]
    # username = request.POST["username"]
    # headimg = request.POST["headimg"]
    # phone = request.POST["phone"]
    # pwd = request.POST["pwd"]
    # wxid = request.POST["wxid"]
    # acountmoney = request.POST["acountmoney"]
    # rewardmoney = request.POST["rewardmoney"]
    # activecode = request.POST["activecode"]
    # redpack = request.POST["redpack"]
    # upperson = request.POST["upperson"]
    # downperson = request.POST["downperson"]
    # rebate = request.POST["rebate"]
    # integral = request.POST["integral"]
    # bankcard = request.POST["bankcard"]
    # power = request.POST["power"]
    # address = request.POST["address"]

    userid = None;
    username = "";
    headimg = "";
    phone = "";
    pwd = "";
    wxid = "";
    acountmoney = "";
    rewardmoney = "";
    activecode = "";
    redpack = "";
    upperson = "";
    downperson = "";
    rebate = "";
    integral = "";
    bankcard = "";
    power = "";
    address = "";
    if request.POST["username"]:
        username = request.POST["username"]
    # if request.POST["pwd"]:
    #     username = request.POST["pwd"]
    # if request.POST["headimg"]:
    #     headimg = request.POST["headimg"]
    # if request.POST["phone"]:
    #     phone = request.POST["phone"]
    if request.POST["pwd"]:
        pwd = request.POST["pwd"]
    # if request.POST["wxid"]:
    #     wxid = request.POST["wxid"]
    # if request.POST["acountmoney"]:
    #     acountmoney = request.POST["acountmoney"]
    # if request.POST["rewardmoney"]:
    #     rewardmoney = request.POST["rewardmoney"]
    # if request.POST["activecode"]:
    #     activecode = request.POST["activecode"]
    # if request.POST["redpack"]:
    #     redpack = request.POST["redpack"]
    # if request.POST["upperson"]:
    #     upperson = request.POST["upperson"]
    # if request.POST["downperson"]:
    #     downperson = request.POST["downperson"]
    # if request.POST["rebate"]:
    #     rebate = request.POST["rebate"]
    # if request.POST["integral"]:
    #     integral = request.POST["integral"]
    # if request.POST["bankcard"]:
    #     bankcard = request.POST["bankcard"]
    # if request.POST["power"]:
    #     power = request.POST["power"]
    # if request.POST["address"]:
    #     address = request.POST["address"]


    cursor = connection.cursor();
    # cursor.execute("ALTER TABLE yyy.user MODIFY COLUMN username VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;");
    result = cursor.execute("INSERT INTO user(username , pwd)VALUES('%s' , '%s')"%(username , pwd))
    # result = cursor.execute("INSERT INTO user(userId , username , headimg , phone , pwd , wxid , acountmoney , rewardmoney , activecode , redpack , upperson , downperson , rebate , integral , bankcard , power , address) VALUES('%s' , '%s' , '%s' , '%s' ,'%s' , '%s' , '%s' , '%s' ,'%s' , '%s' , '%s' , '%s' ,'%s' , '%s' , '%s' , '%s' , '%s')"%(userid , username , headimg , phone , pwd , wxid , acountmoney , rewardmoney , activecode , redpack , upperson , downperson , rebate , integral , bankcard , power , address));
    cursor.close()
   
    print("9999999");
    statusDic = "";
    if result == 1:
        statusDic = {"status" : "ok" , "message" : "添加用户成功"};
    else :
        statusDic = {"status" : "error" , "message" : "添加用户失败"};
    return HttpResponse(json.dumps(statusDic) , content_type = "application/json");

# 用户查询接口  有待测试 尚德勋
def userManageJsonSelect(request):

    cursor=connection.cursor()

    sql = 'SELECT * FROM user'
    allUsertables = []

    try:
        cursor.execute(sql)
        for row in cursor.fetchall():
            usertable = {
                'userid':row[0],
                'username':row[1],
                'headimg':row[2],
                'phone':row[3],
                'pwd':row[4],
                'wxid':row[5],
                'acountmoney':row[6],
                'rewardmoney':row[7],
                'activecode':row[8],
                'redpack':row[9],
                'upperson':row[10],
                'downperson':row[11],
                'rebate':row[12],
                'integral':row[13],
                'bankcard':row[14],
                'power':row[15],
                'address':row[16],
                'registetime':str(row[17]),
            }
            allUsertables.append(usertable)
            cursor.close();
        return HttpResponse(json.dumps({'data':allUsertables, 'status':'ok'}), content_type="application/json")
   
    except Exception as e:    
            return HttpResponse(json.dumps({'data':allUsertables, 'status':'error'}), content_type="application/json");

def userManageJsonDelete(request):
    print(request)
    for key in request.POST:
        userid = request.POST.getlist(key)[0]

    cursor=connection.cursor();
    # print(cursor)
    try:
        cursor.execute("DELETE  FROM user WHERE userid = %s"%(userid))
        # connection.commit();
        cursor.close();
        return HttpResponse(json.dumps({'message': '删除成功','status':'ok'}), content_type="application/json");
            
    except Exception as e:   
         # connection.rollback();
         return HttpResponse(json.dumps({"message":'删除失败' , "status":"error"}) , content_type="application/json");
    
# 按时间获取随机字符串
def randomString():
    for i in range (0,10):  
        nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S");  
        randomNum=random.randint(0,100);
        if randomNum<=10:  
            randomNum=str(0)+str(randomNum);  
        randomId=str(nowTime)+str(randomNum);
        return randomId


def adManageJsonAdd(request):
    
    imgs = request.FILES["imgsFile"];
    # print(imgs);
    # print(type(imgs));
    # print(imgs.__dict__);    
    imgsName = randomString() + ".jpg";

    imagePath = imgsName;

    filepath = "./shopApp/static/myfile";
    filename = os.path.join(filepath,imgsName)
    filename = open(filename , "wb");
    filename.write(imgs.__dict__["file"].read());
    sqlfilename = filepath+imgsName

    # imgs = str(imgs)
    adId = randomString();

    print("************   " , sqlfilename);
    # 

    cursor = connection.cursor();
    result = cursor.execute("INSERT INTO ad(adid , imgs) VALUES ('%s' , '%s' )" % (adId , sqlfilename));

    statusDic = "";
    if result == 1:
        statusDic = {"status" : "ok" , "message" : "添加成功" , "imagePath":imagePath};
    else :
        statusDic = {"status" : "error" , "message" : "添加失败"};
    return HttpResponse(json.dumps(statusDic) , content_type = "application/json");

# 广告添加接口
# def adManageJsonAdd(request):
#     imgs = request.FILES["imgsFile"];
#     imgsName = str(imgs)
#     adId = randomString();

#     cursor = connection.cursor();
#     result = cursor.execute("INSERT INTO ad(adid , imgs) VALUES ('%s' , '%s' )" % (adId , imgsName));

#     statusDic = "";
#     if result == 1:
#         statusDic = {"status" : "ok" , "message" : "添加成功"};
#     else :
#         statusDic = {"status" : "error" , "message" : "添加失败"};
#     return HttpResponse(json.dumps(statusDic) , content_type = "application/json");

# 广告列表接口
def adManageJsonSelect(request):
    myData = []
    cursor = connection.cursor()
    cursor.execute('SELECT imgs,adid,adtime FROM ad')
    datas = cursor.fetchall()
    for data in datas:
        imgs = data[0];#图片
        adid = data[1];#广告id
        adtime = data[2];#时间
        
        tempDic = {"imgs":imgs , "adid":adid , "adtime":str(adtime) }
        myData.append(tempDic)

    return HttpResponse(json.dumps(myData) , content_type="application/json");

# 广告删除接口 韩乐天
def adManageJsonDelete(request):
    # adid = '1'
    adid = request.POST["adid"]
    cursor=connection.cursor();

    try:
        cursor.execute("DELETE FROM ad where adid = '%s'"%(adid))
        # connection.commit();
        cursor.close();
        return HttpResponse(json.dumps({'message': '删除成功','status':'ok'}), content_type="application/json");
        
    except Exception as e:   
        # connection.rollback();
        return HttpResponse(json.dumps({"message":'删除失败' , "status":"error"}) , content_type="application/json");

# 商品添加接口
def goodsManageJsonAdd(request):

    goodsid = request.POST["goodsid"]
    rebate = request.POST["rebate"]
    lookhistoryid = request.POST["lookhistoryid"]
    standard = request.POST["standard"]
    images = request.POST["images"]
    details = request.POST["details"]
    shopname = request.POST["shopname"]
    status = request.POST["status"]
    price = request.POST["price"]
    goodsname = request.POST["goodsname"]
    stock = request.POST["stock"]
    
    cursor = connection.cursor()
    try:
        result = cursor.execute("INSERT INTO goods (goodsid , rebate , lookhistoryid , standard , images , details ,shopname , status , price , goodsname , stock) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (goodsid , rebate , lookhistoryid , standard , images , details ,shopname , status , price , goodsname , stock))

        if result == 1 :
            statusDic = {"status" : "ok" , "message" : "添加成功"};
            return HttpResponse(json.dumps(statusDic) , content_type = "application/json");
        else:
            statusDic = {"status" : "error" , "message" : "添加失败"};
            return HttpResponse(json.dumps(statusDic) , content_type = "application/json");
    except Exception as e:    
        return HttpResponse(json.dumps({'message':"添加失败", 'status':'error'}), content_type="application/json");

# 商品列表接口
def goodsManageJsonSelect(request):
    myData=[];
    mypage = 0
    mypage = (int(request.GET["page"]) - 1) * 10
    cursor = connection.cursor();
    cursor.execute("SELECT * FROM goods LIMIT %d , 10"%mypage);
    datas=cursor.fetchall();
    try:
        for row in datas:
            goods = {
                'goodsid':row[0],
                'rebate':row[1],
                'lookhistoryid':row[2],
                'standard':row[3],
                'images':row[4],
                'details':row[5],
                'shopname':row[6],
                'status':row[7],
                'uptime':row[8].strftime('%Y-%m-%d %H:%M:%S'),
                'downtime':row[9].strftime('%Y-%m-%d %H:%M:%S'),
                'price':row[10],
                'goodsname':row[11],
                'stock':row[12],
            }
            myData.append(goods);
        cursor.close();
        cursor = connection.cursor();
        cursor.execute("SELECT COUNT(*) FROM goods")
        goodscount  = cursor.fetchall();
        goodscount = goodscount[0][0]
        return HttpResponse(json.dumps({'data':myData, 'status':'ok' , 'goodscount':str(goodscount) }), content_type="application/json")
    
    except Exception as e: 
        raise e   
        return HttpResponse(json.dumps({'data':myData, 'status':'error', 'goodscount':'0'}), content_type="application/json");


# 商品列表接口
# def goodsManageJsonSelect(request):
#     myData=[];
#     cursor = connection.cursor();
#     cursor.execute("SELECT * FROM goods");
#     datas=cursor.fetchall();
#     try:
#         for row in datas:
#             goods = {
#                 'goodsid':row[0],
#                 'rebate':row[1],
#                 'lookhistoryid':row[2],
#                 'standard':row[3],
#                 'images':row[4],
#                 'details':row[5],
#                 'shopname':row[6],
#                 'status':row[7],
#                 'uptime':row[8].strftime('%Y-%m-%d %H:%M:%S'),
#                 'downtime':row[9].strftime('%Y-%m-%d %H:%M:%S'),
#                 'price':row[10],
#                 'goodsname':row[11],
#                 'stock':row[12],
#             }
#             myData.append(goods);
#         cursor.close();
#         return HttpResponse(json.dumps({'data':myData, 'status':'ok'}), content_type="application/json")
    
#     except Exception as e: 
#         raise e   
#         return HttpResponse(json.dumps({'data':myData, 'status':'error'}), content_type="application/json");

# 商品列表删除接口
def goodsManageJsonDelete(request):
  # goodsid = '1'
    goodsidsDict =  request.POST
    goodsids = goodsidsDict.getlist("goodsids")

    # goodsids = goodsidsStr[2:-2].split("\",\"")
    # print(goodsids)
    # print(type(goodsids['goodsids']), goodsids['goodsids'])

    cursor=connection.cursor();
    result = 0
    result = 0
    try:
        for goodsid in goodsids:
            cursor.execute("DELETE FROM goods where goodsid = '%s'"%(goodsid))
            result += 1
        # result = cursor.execute("DELETE FROM goods where goodsid = '%s'"%(goodsid))
        # connection.commit();
        cursor.close();
        if result != 0:
            return HttpResponse(json.dumps({'message': '删除成功','status':'ok', 'deleteCount':result}), content_type="application/json");
        else: 
            return HttpResponse(json.dumps({"message":'删除失败' , "status":"error"}) , content_type="application/json");

    except Exception as e:   
        return HttpResponse(json.dumps({"message":'删除失败' , "status":"error"}) , content_type="application/json");

#商品详情列表展示 有待测试 吕健威
def goodsSelectByid(request):
    cursor = connection.cursor()
    # goodsid = "123456789"
    goodsid = request.POST["goodsid"]
    sql = "SELECT * FROM goods WHERE goodsid = '%s'" % goodsid
    allGoodMes = []
    try:
        cursor.execute(sql)
        for row in cursor.fetchall():
            goods = {
                'goodsid':row[0],
                'rebate':row[1],
                'lookhistoryid':row[2],
                'standard':row[3],
                'images':row[4],
                'details':row[5],
                'shopname':row[6],
                'status':row[7],
                'uptime':row[8].strftime('%Y-%m-%d %H:%M:%S'),
                'downtime':row[9].strftime('%Y-%m-%d %H:%M:%S'),
                'price':row[10],
                'goodsname':row[11],
                'stock':row[12],
            }
            allGoodMes.append(goods)
            
        # 关闭连接
        cursor.close()
        return HttpResponse(json.dumps({'data':allGoodMes, 'status':'ok'}), content_type="application/json")
    except Exception as e:
        return HttpResponse(json.dumps({'data':allGoodMes, 'status':'error'}), content_type="application/json")

# 商品模糊查询接口有待测试 黄景召
def commodityQuery(request):
    myData = []
    cursor = connection.cursor()
    # commName = "xiaomi"
    commName = request.POST["commName"]
    cursor.execute("select goodsname from goods where goodsname like '%%%%%s%%%%'"% (commName))
    datas = cursor.fetchall()
    for goodsname in datas:
        temDat = {"goodsname":goodsname[0]};
        myData.append(temDat);
    return HttpResponse(json.dumps(myData) , content_type="application/json");


# 商品修改列表修改接口 有待测试 黄景召
def goodsManageJsonUpdata(request):
    
    datas = request.POST
    print(datas)
    for key in list(datas):
        cursor = connection.cursor()
        cursor.execute("update goods set %s='%s' where goodsid='%s'"%(key , datas[key] , datas["goodsid"]))
    data = {'data':'success', 'status':'ok'}
    return HttpResponse(json.dumps(data) , content_type="application/json");


# 订单添加接口 有待测试 胡亚洲
def ordertableManageJsonAdd(request):
    ordertableid = request.POST["ordertableid"]
    userid = request.POST["userid"]
    goodsid = request.POST["goodsid"]
    isaudit = request.POST["isaudit"]
    ispass = request.POST["ispass"]
    iscancel = request.POST["iscancel"]
    ispay = request.POST["ispay"]
    issend = request.POST["issend"]
    ispaydone = request.POST["ispaydone"]
    isclose = request.POST["isclose"]
    # 获取游标
    cursor = connection.cursor()
    sql = "INSERT  INTO xxx (ordertableid,userid,goodsid,isaudit,ispass,iscancel,ispay,issend,ispaydone,isclose) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    param=(ordertableid,userid,goodsid,isaudit,ispass,iscancel,ispay,issend,ispaydone,isclose)
    cursor.execute(sql, param)
    # 关闭连接
    cursor.close()
    try:
        status = json.dumps({
        'status':'ok',
        })
        return HttpResponse(status, content_type="application/json")
    except Exception as e:
        status = json.dumps({
        'status':'error',
        })
        return HttpResponse(status, content_type="application/json")

# 订单列表接口  有待测试 胡亚洲
def ordertableManageJsonSelete(request):
    userid = request.POST["userid"]
    # 获取游标
    if request.GET["userid"]:      
        userid = request.GET["userid"]
        if request.GET["status"] == "1":
            isaudit = request.POST["status"]
            cursor = connection.cursor()
            sql = "SELECT orderid,userid,ordertime,isaudit,ispass,iscancel,ispay,issend,ispaydone,isclose FROM ordertable WHERE userid = '%s'AND isaudit = '%s'" % (userid,isaudit);
            allOrdertables = [];
            try:
                cursor.execute(sql)
                for row in cursor.fetchall():
                    ordertable = {
                            'orderid':row[0],
                            'userid':row[1],
                            'ordertime':row[2].strftime('%Y-%m-%d %H:%M:%S'),
                            'isaudit':row[3],
                            'ispass':row[4],
                            'iscancel':row[5],
                            'ispay':row[6],
                            'issend':row[7],
                            'ispaydone':row[8],
                            'isclose':row[9],
                    }
                    allOrdertables.append(ordertable)
                cursor.close()
                return HttpResponse(json.dumps({'data':allOrdertables, 'status':'ok'}), content_type="application/json")
            except Exception as e:
                return HttpResponse(json.dumps({'data':allOrdertables, 'status':'error'}), content_type="application/json")
        if request.GET["status"] == "2":
            ispass = request.POST["status"]
            cursor = connection.cursor()
            sql = "SELECT orderid,userid,ordertime,isaudit,ispass,iscancel,ispay,issend,ispaydone,isclose FROM ordertable WHERE userid = '%s'AND ispass = '%s'" % (userid,ispass);
            allOrdertables = [];
            try:
                cursor.execute(sql)
                for row in cursor.fetchall():
                    ordertable = {
                            'orderid':row[0],
                            'userid':row[1],
                            'ordertime':row[2].strftime('%Y-%m-%d %H:%M:%S'),
                            'isaudit':row[3],
                            'ispass':row[4],
                            'iscancel':row[5],
                            'ispay':row[6],
                            'issend':row[7],
                            'ispaydone':row[8],
                            'isclose':row[9],
                    }
                    allOrdertables.append(ordertable)
                cursor.close()
                return HttpResponse(json.dumps({'data':allOrdertables, 'status':'ok'}), content_type="application/json")
            except Exception as e:
                return HttpResponse(json.dumps({'data':allOrdertables, 'status':'error'}), content_type="application/json")
        if request.GET["status"] == "7":
                iscancel = request.GET["status"];
                cursor = connection.cursor()
                sql = "SELECT orderid,userid,ordertime,isaudit,ispass,iscancel,ispay,issend,ispaydone,isclose FROM ordertable WHERE userid = '%s'AND iscancel = '%s'" % (userid,iscancel);
                allOrdertables = [];
                try:
                    cursor.execute(sql)
                    for row in cursor.fetchall():
                        ordertable = {
                                'orderid':row[0],
                                'userid':row[1],
                                'ordertime':row[2].strftime('%Y-%m-%d %H:%M:%S'),
                                'isaudit':row[3],
                                'ispass':row[4],
                                'iscancel':row[5],
                                'ispay':row[6],
                                'issend':row[7],
                                'ispaydone':row[8],
                                'isclose':row[9],
                        }
                        allOrdertables.append(ordertable)
                    cursor.close()
                    return HttpResponse(json.dumps({'data':allOrdertables, 'status':'ok'}), content_type="application/json")
                except Exception as e:
                    return HttpResponse(json.dumps({'data':allOrdertables, 'status':'error'}), content_type="application/json")
        if request.GET["status"] == "3":
            ispay = request.GET["status"];
            cursor = connection.cursor()
            sql = "SELECT orderid,userid,ordertime,isaudit,ispass,iscancel,ispay,issend,ispaydone,isclose FROM ordertable WHERE userid = '%s'AND ispay = '%s'" % (userid,ispay);
            allOrdertables = [];
            try:
                cursor.execute(sql)
                for row in cursor.fetchall():
                    ordertable = {
                            'orderid':row[0],
                            'userid':row[1],
                            'ordertime':row[2].strftime('%Y-%m-%d %H:%M:%S'),
                            'isaudit':row[3],
                            'ispass':row[4],
                            'iscancel':row[5],
                            'ispay':row[6],
                            'issend':row[7],
                            'ispaydone':row[8],
                            'isclose':row[9],
                    }
                    allOrdertables.append(ordertable)
                cursor.close()
                return HttpResponse(json.dumps({'data':allOrdertables, 'status':'ok'}), content_type="application/json")
            except Exception as e:
                return HttpResponse(json.dumps({'data':allOrdertables, 'status':'error'}), content_type="application/json")
        if request.GET["status"] =="6":
            issend = request.GET["status"];
            cursor = connection.cursor()
            sql = "SELECT orderid,userid,ordertime,isaudit,ispass,iscancel,ispay,issend,ispaydone,isclose FROM ordertable WHERE userid = '%s'AND issend = '%s'" % (userid,issend);
            allOrdertables = [];
            try:
                cursor.execute(sql)
                for row in cursor.fetchall():
                    ordertable = {
                            'orderid':row[0],
                            'userid':row[1],
                            'ordertime':row[2].strftime('%Y-%m-%d %H:%M:%S'),
                            'isaudit':row[3],
                            'ispass':row[4],
                            'iscancel':row[5],
                            'ispay':row[6],
                            'issend':row[7],
                            'ispaydone':row[8],
                            'isclose':row[9],
                    }
                    allOrdertables.append(ordertable)
                cursor.close()
                return HttpResponse(json.dumps({'data':allOrdertables, 'status':'ok'}), content_type="application/json")
            except Exception as e:
                return HttpResponse(json.dumps({'data':allOrdertables, 'status':'error'}), content_type="application/json")
        if request.GET["status"] == "4":
            ispaydone = request.GET["status"];
            cursor = connection.cursor()
            sql = "SELECT orderid,userid,ordertime,isaudit,ispass,iscancel,ispay,issend,ispaydone,isclose FROM ordertable WHERE userid = '%s'AND ispaydone = '%s'" % (userid,ispaydone);
            allOrdertables = [];
            try:
                cursor.execute(sql)
                for row in cursor.fetchall():
                    ordertable = {
                            'orderid':row[0],
                            'userid':row[1],
                            'ordertime':row[2].strftime('%Y-%m-%d %H:%M:%S'),
                            'isaudit':row[3],
                            'ispass':row[4],
                            'iscancel':row[5],
                            'ispay':row[6],
                            'issend':row[7],
                            'ispaydone':row[8],
                            'isclose':row[9],
                    }
                    allOrdertables.append(ordertable)
                cursor.close()
                return HttpResponse(json.dumps({'data':allOrdertables, 'status':'ok'}), content_type="application/json")
            except Exception as e:
                return HttpResponse(json.dumps({'data':allOrdertables, 'status':'error'}), content_type="application/json")
        if request.GET["status"]=="8":
            isclose = request.GET["status"];
            cursor = connection.cursor()
            sql = "SELECT orderid,userid,ordertime,isaudit,ispass,iscancel,ispay,issend,ispaydone,isclose FROM ordertable WHERE userid = '%s'AND isclose = '%s'" % (userid,isclose);
            allOrdertables = [];
            try:
                cursor.execute(sql)
                for row in cursor.fetchall():
                    ordertable = {
                            'orderid':row[0],
                            'userid':row[1],
                            'ordertime':row[2].strftime('%Y-%m-%d %H:%M:%S'),
                            'isaudit':row[3],
                            'ispass':row[4],
                            'iscancel':row[5],
                            'ispay':row[6],
                            'issend':row[7],
                            'ispaydone':row[8],
                            'isclose':row[9],
                    }
                    allOrdertables.append(ordertable)
                cursor.close()
                return HttpResponse(json.dumps({'data':allOrdertables, 'status':'ok'}), content_type="application/json")
            except Exception as e:
                return HttpResponse(json.dumps({'data':allOrdertables, 'status':'error'}), content_type="application/json")
    else:
        orderid = request.GET["orderid"];
        cursor = connection.cursor()
        sql = "SELECT orderid,userid,ordertime,isaudit,ispass,iscancel,ispay,issend,ispaydone,isclose FROM ordertable WHERE orderid = '%s'" % orderid;
        allOrdertables = [];
        try:
            cursor.execute(sql)
            for row in cursor.fetchall():
                ordertable = {
                    'orderid':row[0],
                    'userid':row[1],
                    'ordertime':row[2].strftime('%Y-%m-%d %H:%M:%S'),
                    'isaudit':row[3],
                    'ispass':row[4],
                    'iscancel':row[5],
                    'ispay':row[6],
                    'issend':row[7],
                    'ispaydone':row[8],
                    'isclose':row[9],
                }
                allOrdertables.append(ordertable)
            cursor.close()
            print(allOrdertables)
            return HttpResponse(json.dumps({'data':allOrdertables, 'status':'ok'}), content_type="application/json")
        except Exception as e:
            return HttpResponse(json.dumps({'data':allOrdertables, 'status':'error'}), content_type="application/json")
# 订单删除接口 吕建威
def ordertableDelete(request):
    cursor = connection.cursor()
    # ordertableid = "123456789"
    ordertableid = request.POST["ordertableid"]
    try:
        result = cursor.execute("DELETE FROM xxx WHERE ordertableid=%s" % ordertableid)
        if result == 1 :
            statusDic = {"status" : "ok" , "message" : "删除订单成功"};
            return HttpResponse(json.dumps(statusDic) , content_type = "application/json");
        else:
            statusDic = {"status" : "error" , "message" : "删除订单失败"};
            return HttpResponse(json.dumps(statusDic) , content_type = "application/json");
    except Exception as e: 
        # raise e   
        return HttpResponse(json.dumps({'message':"删除订单失败", 'status':'error'}), content_type="application/json");

# 活动查询接口  有待测试
def activeManageJsonSelect(request):
    myData=[]
    cursor=connection.cursor()

    cursor.execute("SELECT activeid,activedetail,activetime FROM activetable")
    try:
        for data in cursor.fetchall():
            activeid=data[0]
            activedetail=data[1]
            activetime=data[2].strftime('%Y-%m-%d %H:%M:%S')
        
            tempDic={"activeid":activeid,"activedetail":activedetail,"activetime":activetime}
            myData.append(tempDic);
        cursor.close()
        return HttpResponse(json.dumps({'data':myData, 'status':'ok'}), content_type="application/json")
    except Exception as e:   
        # raise e
        return HttpResponse(json.dumps({"data":myData , "status":"error"}) , content_type="application/json");

# 活动添加接口 刘斌
def activetableManageJsonAdd(request):
        # activeid="123";
        # activetime="465";
        # activedetail="798";
        activeid = request.POST["activeid"]
        activedetail = request.POST["activedetail"]
        cursor=connection.cursor()
        try:
            cursor.execute("INSERT INTO order (activeid,activetime,activedetail) VALUES (%d,%s,%s)"% (activeid,str(activetime),activedetail))
            statusDis={"status":"ok","message":"添加成功"};
            return HttpResponse(json.dumps(statusDis),content_type="application/json");
        except Exception as e :
            statusDis={"status":"error","message":"添加失败"};
            return HttpResponse(json.dumps(statusDis),content_type="application/json");


# 活动删除接口 有待测试 刘斌
def activetableManageJsonDelete(request):
    cursor=connection.cursor()
    active_id = request.POST["activeid"];
    try:
        cursor.execute("DELETE FROM activetable WHERE activeid='%s'"% (active_id))
        cursor.close()
        return HttpResponse(json.dumps({"message":"删除成功","status":"ok"}),content_type="application/json")
    except expression as identifier:
        return HttpResponse(json.dumps({"message":"删除失败","status":"error"}),content_type="application/json")



# 问题接口:  商品修改列表修改接口(黄景召)    存在参数给的不对的问题,自己代码思路问题
#           活动添加接口(刘斌)      不清楚时间是什么时间, 结束时间？开始时间？ 存在不明确的问,
#                                 修改了数据库中活动表的时间字段,数据类型由DataTime修改为timestamp,加入默认值为记录创建时间


