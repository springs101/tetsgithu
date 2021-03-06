import pymysql
import copy
import re
import time
import logging
logger = logging.getLogger("users")


class OperateDB():
    host = '192.168.86.71'
    pasword = ''
    user = 'root'
    # host = '114.55.187.143'
    # pasword = 'CrEoKHe5n-qVjQ9vFa#n0Y'
    # user = 'tidb_write'
    port = 4000
    db = 'asterdata'
    charset = 'utf8'
    opretateData = []
    objectArray = []
    outputobjecArray = []
    delarray = ''
    conn = ''
    strsqlorder = ''
    strsqlitem = ''
    delItem = ''

    def __init__(self, date):
        self.opretateData = copy.deepcopy(date)
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.pasword, db=self.db, charset=self.charset,
                                    cursorclass=pymysql.cursors.DictCursor)

    def sqlecude(self, flag):
        try:
            with self.conn.cursor() as cursor:
                if flag == 1:
                    self.handSqlStr()
                    self.groupData(self.opretateData)
                    # print(self.outputobjecArray)
                    cow = cursor.executemany(
                        self.strsqlorder, self.outputobjecArray)
                else:
                    self.handitemorder()
                    self.groupItemData(self.opretateData)
                    # print(self.outputobjecArray[0])
                    delcow = cursor.execute(self.delItem, self.delarray)
                    addcow = cursor.executemany(
                        self.strsqlitem, self.outputobjecArray)
                self.conn.commit()
        except Exception as err:
            self.conn.rollback()
            logger.error(err)
        finally:
            self.conn.close()
            logger.info('finisth commit')
        return

    def groupData(self, groupDic):
        for val in groupDic:
            val['createTime'] = time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            val['updateTime'] = time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            node = []
            for i in self.objectArray:
                node.append(val[i])
            self.outputobjecArray.append(node)
        # print(self.outputobjecArray)
        return

    def groupItemData(self, groupDic):
        # print(groupDic)
        for val in groupDic:
            val['createTime'] = time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            val['updateTime'] = time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            node = []
            for i in self.objectArray:
                node.append(val[i])
                if i == 'tid':
                    self.delarray = val[i]
            self.outputobjecArray.append(node)
        # print(self.outputobjecArray)
        return

    def handitemorder(self):
        self.delItem = 'delete from s_order_item where tid = %s'

        self.strsqlitem = "insert into s_order_item(tid,\
pro_detail_code,\
pro_name,\
specification,\
barcode,\
combine_barcode,\
iscancel,\
isscheduled,\
stock_situation,\
isbook_pro,\
iscombination,\
isgifts,\
gift_num,\
book_storage,\
pro_num,\
send_num,\
refund_num,\
refund_renum,\
inspection_num,\
timeinventory,\
cost_price,\
sell_price,\
average_price,\
original_price,\
sys_price,\
ferght,\
item_discountfee,\
inspection_time,\
weight,\
shopid,\
out_tid,\
out_proid,\
out_prosku,\
proexplain,\
buyer_memo,\
seller_remark,\
distributer,\
distribut_time,\
second_barcode,\
product_no,\
brand_number,\
brand_name,\
book_inventory,\
product_specification,\
discount_amount,\
MD5_encryption,\
sncode,\
store_location,\
pro_type,\
storage_id,\
credit_amount,\
createTime,\
updateTime) values (%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s,%s,%s)"
        temp = re.findall(r'[(](.*?)[)]', self.strsqlitem)
        object = temp[0].split(',')
        self.objectArray = copy.deepcopy(object)
        return

    def handSqlStr(self):
        self.strsqlorder = "insert into s_order(resultNum,\
storage_id,\
transaction_id,\
customer_id,\
distributor_id,\
shop_name,\
out_tid,\
out_pay_tid,\
voucher_id,\
shopid,\
serial_num,\
order_channel,\
order_from,\
buyer_id,\
buyer_name,\
type,\
status,\
abnormal_status,\
merge_status,\
receiver_name,\
receiver_mobile,\
phone,\
province,\
city,\
district,\
address,\
post,\
email,\
is_bill,\
invoice_name,\
invoice_situation,\
invoice_title,\
invoice_type,\
invoice_content,\
pro_totalfee,\
order_totalfee,\
reference_price_paid,\
invoice_fee,\
cod_fee,\
other_fee,\
refund_totalfee,\
discount_fee,\
discount,\
channel_disfee,\
merchant_disfee,\
order_disfee,\
commission_fee,\
is_cod,\
point_pay,\
cost_point,\
point,\
superior_point,\
royalty_fee,\
external_point,\
express_no,\
express,\
express_coding,\
online_express,\
sending_type,\
real_income_freight,\
real_pay_freight,\
gross_weight,\
gross_weight_freight,\
net_weight_freight,\
freight_explain,\
total_weight,\
tid_net_weight,\
tid_time,\
pay_time,\
get_time,\
order_creater,\
business_man,\
payment_received_operator,\
payment_received_time,\
review_orders_operator,\
review_orders_time,\
finance_review_operator,\
finance_review_time,\
advance_printer,\
printer,\
print_time,\
is_print,\
adv_distributer,\
adv_distribut_time,\
distributer,\
distribut_time,\
is_inspection,\
inspecter,\
inspect_time,\
cancel_operator,\
cancel_time,\
revoke_cancel_er,\
revoke_cancel_time,\
packager,\
pack_time,\
weigh_operator,\
weigh_time,\
book_delivery_time,\
delivery_operator,\
delivery_time,\
locker,\
lock_time,\
book_file_time,\
file_operator,\
file_time,\
finish_time,\
modity_time,\
is_promotion,\
promotion_plan,\
out_promotion_detail,\
good_receive_time,\
receive_time,\
verificaty_time,\
enable_inte_sto_time,\
enable_inte_delivery_time,\
alipay_id,\
alipay_status,\
pay_mothed,\
pay_status,\
platform_status,\
rate,\
currency,\
delivery_status,\
buyer_message,\
service_remarks,\
inner_lable,\
distributor_mark,\
system_remarks,\
other_remarks,\
message,\
message_time,\
is_stock,\
related_orders,\
related_orders_type,\
import_mark,\
delivery_name,\
is_new_customer,\
distributor_level,\
cod_service_fee,\
express_col_fee,\
product_num,\
sku,\
item_num,\
single_num,\
flag_color,\
is_flag,\
taobao_delivery_order_status,\
taobao_delivery_status,\
taobao_delivery_method,\
order_process_time,\
is_break,\
breaker,\
break_time,\
break_explain,\
plat_send_status,\
plat_type,\
is_adv_sale,\
provinc_code,\
city_code,\
area_code,\
express_code,\
last_returned_time,\
last_refund_time,\
deliver_centre,\
deliver_station,\
is_pre_delivery_notice,\
jd_delivery_time,\
Sorting_code,\
cod_settlement_vouchernumber,\
three_codes,\
send_site_name,\
distributing_centre_name,\
originCode,\
destCode,\
big_marker,\
platform_preferential,\
tid,createTime,updateTime) values(%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s\
,%s,%s,%s\
) on duplicate key update resultNum=values(resultNum),storage_id=values(storage_id),\
    transaction_id=values(transaction_id),\
    customer_id=values(customer_id),\
    distributor_id=values(distributor_id),\
    shop_name=values(shop_name),\
    out_tid=values(out_tid),\
    out_pay_tid=values(out_pay_tid),\
    voucher_id=values(voucher_id),\
    shopid=values(shopid),\
    serial_num=values(serial_num),\
    order_channel=values(order_channel),\
    order_from=values(order_from),\
    buyer_id=values(buyer_id),\
    buyer_name=values(buyer_name),\
    type=values(type),\
    status=values(status),\
    abnormal_status=values(abnormal_status),\
    merge_status=values(merge_status),\
    receiver_name=values(receiver_name),\
    receiver_mobile=values(receiver_mobile),\
    phone=values(phone),\
    province=values(province),\
    city=values(city),\
    district=values(district),\
    address=values(address),\
    post=values(post),\
    email=values(email),\
    is_bill=values(is_bill),\
    invoice_name=values(invoice_name),\
    invoice_situation=values(invoice_situation),\
    invoice_title=values(invoice_title),\
    invoice_type=values(invoice_type),\
    invoice_content=values(invoice_content),\
    pro_totalfee=values(pro_totalfee),\
    order_totalfee=values(order_totalfee),\
    reference_price_paid=values(reference_price_paid),\
    invoice_fee=values(invoice_fee),\
    cod_fee=values(cod_fee),\
    other_fee=values(other_fee),\
    refund_totalfee=values(refund_totalfee),\
    discount_fee=values(discount_fee),\
    discount=values(discount),\
    channel_disfee=values(channel_disfee),\
    merchant_disfee=values(merchant_disfee),\
    order_disfee=values(order_disfee),\
    commission_fee=values(commission_fee),\
    is_cod=values(is_cod),\
    point_pay=values(point_pay),\
    cost_point=values(cost_point),\
    point=values(point),\
    superior_point=values(superior_point),\
    royalty_fee=values(royalty_fee),\
    external_point=values(external_point),\
    express_no=values(express_no),\
    express=values(express),\
    express_coding=values(express_coding),\
    online_express=values(online_express),\
    sending_type=values(sending_type),\
    real_income_freight=values(real_income_freight),\
    real_pay_freight=values(real_pay_freight),\
    gross_weight=values(gross_weight),\
    gross_weight_freight=values(gross_weight_freight),\
    net_weight_freight=values(net_weight_freight),\
    freight_explain=values(freight_explain),\
    total_weight=values(total_weight),\
    tid_net_weight=values(tid_net_weight),\
    tid_time=values(tid_time),\
    pay_time=values(pay_time),\
    get_time=values(get_time),\
    order_creater=values(order_creater),\
    business_man=values(business_man),\
    payment_received_operator=values(payment_received_operator),\
    payment_received_time=values(payment_received_time),\
    review_orders_operator=values(review_orders_operator),\
    review_orders_time=values(review_orders_time),\
    finance_review_operator=values(finance_review_operator),\
    finance_review_time=values(finance_review_time),\
    advance_printer=values(advance_printer),\
    printer=values(printer),\
    print_time=values(print_time),\
    is_print=values(is_print),\
    adv_distributer=values(adv_distributer),\
    adv_distribut_time=values(adv_distribut_time),\
    distributer=values(distributer),\
    distribut_time=values(distribut_time),\
    is_inspection=values(is_inspection),\
    inspecter=values(inspecter),\
    inspect_time=values(inspect_time),\
    cancel_operator=values(cancel_operator),\
    cancel_time=values(cancel_time),\
    revoke_cancel_er=values(revoke_cancel_er),\
    revoke_cancel_time=values(revoke_cancel_time),\
    packager=values(packager),\
    pack_time=values(pack_time),\
    weigh_operator=values(weigh_operator),\
    weigh_time=values(weigh_time),\
    book_delivery_time=values(book_delivery_time),\
    delivery_operator=values(delivery_operator),\
    delivery_time=values(delivery_time),\
    locker=values(locker),\
    lock_time=values(lock_time),\
    book_file_time=values(book_file_time),\
    file_operator=values(file_operator),\
    file_time=values(file_time),\
    finish_time=values(finish_time),\
    modity_time=values(modity_time),\
    is_promotion=values(is_promotion),\
    promotion_plan=values(promotion_plan),\
    out_promotion_detail=values(out_promotion_detail),\
    good_receive_time=values(good_receive_time),\
    receive_time=values(receive_time),\
    verificaty_time=values(verificaty_time),\
    enable_inte_sto_time=values(enable_inte_sto_time),\
    enable_inte_delivery_time=values(enable_inte_delivery_time),\
    alipay_id=values(alipay_id),\
    alipay_status=values(alipay_status),\
    pay_mothed=values(pay_mothed),\
    pay_status=values(pay_status),\
    platform_status=values(platform_status),\
    rate=values(rate),\
    currency=values(currency),\
    delivery_status=values(delivery_status),\
    buyer_message=values(buyer_message),\
    service_remarks=values(service_remarks),\
    inner_lable=values(inner_lable),\
    distributor_mark=values(distributor_mark),\
    system_remarks=values(system_remarks),\
    other_remarks=values(other_remarks),\
    message=values(message),\
    message_time=values(message_time),\
    is_stock=values(is_stock),\
    related_orders=values(related_orders),\
    related_orders_type=values(related_orders_type),\
    import_mark=values(import_mark),\
    delivery_name=values(delivery_name),\
    is_new_customer=values(is_new_customer),\
    distributor_level=values(distributor_level),\
    cod_service_fee=values(cod_service_fee),\
    express_col_fee=values(express_col_fee),\
    product_num=values(product_num),\
    sku=values(sku),\
    item_num=values(item_num),\
    single_num=values(single_num),\
    flag_color=values(flag_color),\
    is_flag=values(is_flag),\
    taobao_delivery_order_status=values(taobao_delivery_order_status),\
    taobao_delivery_status=values(taobao_delivery_status),\
    taobao_delivery_method=values(taobao_delivery_method),\
    order_process_time=values(order_process_time),\
    is_break=values(is_break),\
    breaker=values(breaker),\
    break_time=values(break_time),\
    break_explain=values(break_explain),\
    plat_send_status=values(plat_send_status),\
    plat_type=values(plat_type),\
    is_adv_sale=values(is_adv_sale),\
    provinc_code=values(provinc_code),\
    city_code=values(city_code),\
    area_code=values(area_code),\
    express_code=values(express_code),\
    last_returned_time=values(last_returned_time),\
    last_refund_time=values(last_refund_time),\
    deliver_centre=values(deliver_centre),\
    deliver_station=values(deliver_station),\
    is_pre_delivery_notice=values(is_pre_delivery_notice),\
    jd_delivery_time=values(jd_delivery_time),\
    Sorting_code=values(Sorting_code),\
    cod_settlement_vouchernumber=values(cod_settlement_vouchernumber),\
    three_codes=values(three_codes),\
    send_site_name=values(send_site_name),\
    distributing_centre_name=values(distributing_centre_name),\
    originCode=values(originCode),\
    destCode=values(destCode),\
    big_marker=values(big_marker),\
    updateTime=values(updateTime),\
    platform_preferential=values(platform_preferential)"
        temp = re.findall(r'[(](.*?)[)]', self.strsqlorder)
        object = temp[0].split(',')
        self.objectArray = copy.deepcopy(object)
