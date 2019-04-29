# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

class AHandJob(models.Model):
    jobname = models.CharField(db_column='jobName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    startTime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endTime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    subjobnum = models.IntegerField(db_column='subJobNum', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    finishtime = models.DateTimeField(db_column='finishTime', blank=True, null=True)  # Field name made lowercase.
    effectnum = models.IntegerField(db_column='effectNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'a_hand_job'

class AJobLog(models.Model):
    jobname = models.CharField(db_column='jobName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    jobtype = models.CharField(db_column='jobType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    handjobid = models.IntegerField(db_column='handJobId', blank=True, null=True)  # Field name made lowercase.
    handsubjobno = models.IntegerField(db_column='handSubJobNo', blank=True, null=True)  # Field name made lowercase.
    pageNo = models.IntegerField(db_column='pageNo', blank=True, null=True)  # Field name made lowercase.
    startTime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endTime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    createTime = models.DateTimeField(db_column='createTime', blank=True,auto_now_add=True)  # Field name made lowercase.
    finishTime = models.DateTimeField(db_column='finishTime', blank=True,auto_now_add=True)  # Field name made lowercase.
    effectnum = models.IntegerField(db_column='effectNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aster_job_log'

class AJobLogBak(models.Model):
    jobname = models.CharField(db_column='jobName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    jobtype = models.CharField(db_column='jobType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    handjobid = models.IntegerField(db_column='handJobId', blank=True, null=True)  # Field name made lowercase.
    handsubjobno = models.IntegerField(db_column='handSubJobNo', blank=True, null=True)  # Field name made lowercase.
    pageNo = models.IntegerField(db_column='pageNo', blank=True, null=True)  # Field name made lowercase.
    startTime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endTime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    createTime = models.DateTimeField(db_column='createTime', blank=True)  # Field name made lowercase.
    finishTime = models.DateTimeField(db_column='finishTime', blank=True)  # Field name made lowercase.
    effectnum = models.IntegerField(db_column='effectNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aster_getDatajob_log_bak'

class APropertie(models.Model):
    name = models.CharField(unique=True, max_length=100)
    value = models.TextField(blank=True, null=True)
    propdesc = models.CharField(db_column='propDesc', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'a_propertie'


class ASearchConditionGroup(models.Model):
    loginid = models.CharField(db_column='loginId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    searchname = models.CharField(db_column='searchName', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'a_search_condition_group'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SEdbShop(models.Model):
    shopid = models.CharField(db_column='shopId', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    shopname = models.CharField(db_column='shopName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    platformtype = models.CharField(db_column='platformType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platformname = models.CharField(db_column='platformName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platformcode = models.CharField(db_column='platformCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    isbigshop = models.IntegerField(db_column='isBigShop', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_edb_shop'


class SOrder(models.Model):
    resultNum = models.CharField(db_column='resultNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    storage_id = models.CharField(max_length=100, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    customer_id = models.CharField(max_length=100, blank=True, null=True)
    distributor_id = models.CharField(max_length=100, blank=True, null=True)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    out_tid = models.CharField(max_length=100, blank=True, null=True)
    out_pay_tid = models.CharField(max_length=100, blank=True, null=True)
    voucher_id = models.CharField(max_length=100, blank=True, null=True)
    shopid = models.CharField(max_length=100, blank=True, null=True)
    serial_num = models.CharField(max_length=100, blank=True, null=True)
    order_channel = models.CharField(max_length=100, blank=True, null=True)
    order_from = models.CharField(max_length=100, blank=True, null=True)
    buyer_id = models.CharField(max_length=100, blank=True, null=True)
    buyer_name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    abnormal_status = models.CharField(max_length=100, blank=True, null=True)
    merge_status = models.CharField(max_length=100, blank=True, null=True)
    receiver_name = models.CharField(max_length=100, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    post = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    is_bill = models.CharField(max_length=100, blank=True, null=True)
    invoice_name = models.CharField(max_length=100, blank=True, null=True)
    invoice_situation = models.CharField(max_length=100, blank=True, null=True)
    invoice_title = models.CharField(max_length=100, blank=True, null=True)
    invoice_type = models.CharField(max_length=100, blank=True, null=True)
    invoice_content = models.CharField(max_length=100, blank=True, null=True)
    pro_totalfee = models.CharField(max_length=100, blank=True, null=True)
    order_totalfee = models.CharField(max_length=100, blank=True, null=True)
    reference_price_paid = models.CharField(max_length=100, blank=True, null=True)
    invoice_fee = models.CharField(max_length=100, blank=True, null=True)
    cod_fee = models.CharField(max_length=100, blank=True, null=True)
    other_fee = models.CharField(max_length=100, blank=True, null=True)
    refund_totalfee = models.CharField(max_length=100, blank=True, null=True)
    discount_fee = models.CharField(max_length=100, blank=True, null=True)
    discount = models.CharField(max_length=100, blank=True, null=True)
    channel_disfee = models.CharField(max_length=100, blank=True, null=True)
    merchant_disfee = models.CharField(max_length=100, blank=True, null=True)
    order_disfee = models.CharField(max_length=100, blank=True, null=True)
    commission_fee = models.CharField(max_length=100, blank=True, null=True)
    is_cod = models.CharField(max_length=100, blank=True, null=True)
    point_pay = models.CharField(max_length=100, blank=True, null=True)
    cost_point = models.CharField(max_length=100, blank=True, null=True)
    point = models.CharField(max_length=100, blank=True, null=True)
    superior_point = models.CharField(max_length=100, blank=True, null=True)
    royalty_fee = models.CharField(max_length=100, blank=True, null=True)
    external_point = models.CharField(max_length=100, blank=True, null=True)
    express_no = models.CharField(max_length=100, blank=True, null=True)
    express = models.CharField(max_length=100, blank=True, null=True)
    express_coding = models.CharField(max_length=100, blank=True, null=True)
    online_express = models.CharField(max_length=100, blank=True, null=True)
    sending_type = models.CharField(max_length=100, blank=True, null=True)
    real_income_freight = models.CharField(max_length=100, blank=True, null=True)
    real_pay_freight = models.CharField(max_length=100, blank=True, null=True)
    gross_weight = models.CharField(max_length=100, blank=True, null=True)
    gross_weight_freight = models.CharField(max_length=100, blank=True, null=True)
    net_weight_freight = models.CharField(max_length=100, blank=True, null=True)
    freight_explain = models.CharField(max_length=100, blank=True, null=True)
    total_weight = models.CharField(max_length=100, blank=True, null=True)
    tid_net_weight = models.CharField(max_length=100, blank=True, null=True)
    tid_time = models.CharField(max_length=100, blank=True, null=True)
    pay_time = models.CharField(max_length=100, blank=True, null=True)
    get_time = models.CharField(max_length=100, blank=True, null=True)
    order_creater = models.CharField(max_length=100, blank=True, null=True)
    business_man = models.CharField(max_length=100, blank=True, null=True)
    payment_received_operator = models.CharField(max_length=100, blank=True, null=True)
    payment_received_time = models.CharField(max_length=100, blank=True, null=True)
    review_orders_operator = models.CharField(max_length=100, blank=True, null=True)
    review_orders_time = models.CharField(max_length=100, blank=True, null=True)
    finance_review_operator = models.CharField(max_length=100, blank=True, null=True)
    finance_review_time = models.CharField(max_length=100, blank=True, null=True)
    advance_printer = models.CharField(max_length=100, blank=True, null=True)
    printer = models.CharField(max_length=100, blank=True, null=True)
    print_time = models.CharField(max_length=100, blank=True, null=True)
    is_print = models.CharField(max_length=100, blank=True, null=True)
    adv_distributer = models.CharField(max_length=100, blank=True, null=True)
    adv_distribut_time = models.CharField(max_length=100, blank=True, null=True)
    distributer = models.CharField(max_length=100, blank=True, null=True)
    distribut_time = models.CharField(max_length=100, blank=True, null=True)
    is_inspection = models.CharField(max_length=100, blank=True, null=True)
    inspecter = models.CharField(max_length=100, blank=True, null=True)
    inspect_time = models.CharField(max_length=100, blank=True, null=True)
    cancel_operator = models.CharField(max_length=100, blank=True, null=True)
    cancel_time = models.CharField(max_length=100, blank=True, null=True)
    revoke_cancel_er = models.CharField(max_length=100, blank=True, null=True)
    revoke_cancel_time = models.CharField(max_length=100, blank=True, null=True)
    packager = models.CharField(max_length=100, blank=True, null=True)
    pack_time = models.CharField(max_length=100, blank=True, null=True)
    weigh_operator = models.CharField(max_length=100, blank=True, null=True)
    weigh_time = models.CharField(max_length=100, blank=True, null=True)
    book_delivery_time = models.CharField(max_length=100, blank=True, null=True)
    delivery_operator = models.CharField(max_length=100, blank=True, null=True)
    delivery_time = models.CharField(max_length=100, blank=True, null=True)
    locker = models.CharField(max_length=100, blank=True, null=True)
    lock_time = models.CharField(max_length=100, blank=True, null=True)
    book_file_time = models.CharField(max_length=100, blank=True, null=True)
    file_operator = models.CharField(max_length=100, blank=True, null=True)
    file_time = models.CharField(max_length=100, blank=True, null=True)
    finish_time = models.CharField(max_length=100, blank=True, null=True)
    modity_time = models.CharField(max_length=100, blank=True, null=True)
    is_promotion = models.CharField(max_length=100, blank=True, null=True)
    promotion_plan = models.TextField()
    out_promotion_detail = models.CharField(max_length=100, blank=True, null=True)
    good_receive_time = models.CharField(max_length=100, blank=True, null=True)
    receive_time = models.CharField(max_length=100, blank=True, null=True)
    verificaty_time = models.CharField(max_length=100, blank=True, null=True)
    enable_inte_sto_time = models.CharField(max_length=100, blank=True, null=True)
    enable_inte_delivery_time = models.CharField(max_length=100, blank=True, null=True)
    alipay_id = models.CharField(max_length=100, blank=True, null=True)
    alipay_status = models.CharField(max_length=100, blank=True, null=True)
    pay_mothed = models.CharField(max_length=100, blank=True, null=True)
    pay_status = models.CharField(max_length=100, blank=True, null=True)
    platform_status = models.CharField(max_length=100, blank=True, null=True)
    rate = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=100, blank=True, null=True)
    delivery_status = models.CharField(max_length=100, blank=True, null=True)
    buyer_message = models.CharField(max_length=300, blank=True, null=True)
    service_remarks = models.TextField()
    inner_lable = models.CharField(max_length=300, blank=True, null=True)
    distributor_mark = models.TextField()
    system_remarks = models.TextField()
    other_remarks = models.TextField()
    message = models.CharField(max_length=100, blank=True, null=True)
    message_time = models.CharField(max_length=100, blank=True, null=True)
    is_stock = models.CharField(max_length=100, blank=True, null=True)
    related_orders = models.CharField(max_length=100, blank=True, null=True)
    related_orders_type = models.CharField(max_length=100, blank=True, null=True)
    import_mark = models.CharField(max_length=100, blank=True, null=True)
    delivery_name = models.CharField(max_length=100, blank=True, null=True)
    is_new_customer = models.CharField(max_length=100, blank=True, null=True)
    distributor_level = models.CharField(max_length=100, blank=True, null=True)
    cod_service_fee = models.CharField(max_length=100, blank=True, null=True)
    express_col_fee = models.CharField(max_length=100, blank=True, null=True)
    product_num = models.CharField(max_length=100, blank=True, null=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    item_num = models.CharField(max_length=100, blank=True, null=True)
    single_num = models.CharField(max_length=100, blank=True, null=True)
    flag_color = models.CharField(max_length=100, blank=True, null=True)
    is_flag = models.CharField(max_length=100, blank=True, null=True)
    taobao_delivery_order_status = models.CharField(max_length=100, blank=True, null=True)
    taobao_delivery_status = models.CharField(max_length=100, blank=True, null=True)
    taobao_delivery_method = models.CharField(max_length=100, blank=True, null=True)
    order_process_time = models.CharField(max_length=100, blank=True, null=True)
    is_break = models.CharField(max_length=100, blank=True, null=True)
    breaker = models.CharField(max_length=100, blank=True, null=True)
    break_time = models.CharField(max_length=100, blank=True, null=True)
    break_explain = models.CharField(max_length=200, blank=True, null=True)
    plat_send_status = models.CharField(max_length=100, blank=True, null=True)
    plat_type = models.CharField(max_length=100, blank=True, null=True)
    is_adv_sale = models.CharField(max_length=100, blank=True, null=True)
    provinc_code = models.CharField(max_length=100, blank=True, null=True)
    city_code = models.CharField(max_length=100, blank=True, null=True)
    area_code = models.CharField(max_length=100, blank=True, null=True)
    express_code = models.CharField(max_length=100, blank=True, null=True)
    last_returned_time = models.CharField(max_length=100, blank=True, null=True)
    last_refund_time = models.CharField(max_length=100, blank=True, null=True)
    deliver_centre = models.CharField(max_length=100, blank=True, null=True)
    deliver_station = models.CharField(max_length=100, blank=True, null=True)
    is_pre_delivery_notice = models.CharField(max_length=100, blank=True, null=True)
    jd_delivery_time = models.CharField(max_length=100, blank=True, null=True)
    Sorting_code = models.CharField(db_column='Sorting_code', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cod_settlement_vouchernumber = models.CharField(max_length=100, blank=True, null=True)
    three_codes = models.CharField(max_length=100, blank=True, null=True)
    send_site_name = models.CharField(max_length=100, blank=True, null=True)
    distributing_centre_name = models.CharField(max_length=100, blank=True, null=True)
    originCode = models.CharField(db_column='originCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    destCode = models.CharField(db_column='destCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    big_marker = models.CharField(max_length=100, blank=True, null=True)
    platform_preferential = models.CharField(max_length=100, blank=True, null=True)
    createTime = models.DateTimeField(db_column='createTime', blank=True,auto_now_add=True)  # Field name made lowercase.
    updateTime = models.DateTimeField(db_column='updateTime', blank=True,auto_now=True)  # Field name made lowercase.
    masterId = models.CharField(db_column='masterId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    IDSource = models.CharField(db_column='IDSource', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tid = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_order'


class SOrderItem(models.Model):
    tid = models.CharField(max_length=20, blank=True, null=True)
    pro_detail_code = models.CharField(max_length=20, blank=True, null=True)
    pro_name = models.CharField(max_length=100, blank=True, null=True)
    specification = models.CharField(max_length=100, blank=True, null=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    combine_barcode = models.CharField(max_length=100, blank=True, null=True)
    iscancel = models.CharField(max_length=100, blank=True, null=True)
    isscheduled = models.CharField(max_length=100, blank=True, null=True)
    stock_situation = models.CharField(max_length=100, blank=True, null=True)
    isbook_pro = models.CharField(max_length=100, blank=True, null=True)
    iscombination = models.CharField(max_length=100, blank=True, null=True)
    isgifts = models.CharField(max_length=100, blank=True, null=True)
    gift_num = models.IntegerField(blank=True, null=True)
    book_storage = models.CharField(max_length=100, blank=True, null=True)
    pro_num = models.IntegerField(blank=True, null=True)
    send_num = models.IntegerField(blank=True, null=True)
    refund_num = models.IntegerField(blank=True, null=True)
    refund_renum = models.IntegerField(blank=True, null=True)
    inspection_num = models.IntegerField(blank=True, null=True)
    timeinventory = models.CharField(max_length=100, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    sell_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    average_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    original_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    sys_price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    ferght = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    item_discountfee = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    inspection_time = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    shopid = models.CharField(max_length=100, blank=True, null=True)
    out_tid = models.CharField(max_length=100, blank=True, null=True)
    out_proid = models.CharField(max_length=100, blank=True, null=True)
    out_prosku = models.CharField(max_length=100, blank=True, null=True)
    proexplain = models.CharField(max_length=100, blank=True, null=True)
    buyer_memo = models.CharField(max_length=1000, blank=True, null=True)
    seller_remark = models.CharField(max_length=1000, blank=True, null=True)
    distributer = models.CharField(max_length=100, blank=True, null=True)
    distribut_time = models.CharField(max_length=100, blank=True, null=True)
    second_barcode = models.CharField(max_length=100, blank=True, null=True)
    product_no = models.CharField(max_length=100, blank=True, null=True)
    brand_number = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    brand_name = models.CharField(max_length=100, blank=True, null=True)
    book_inventory = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    product_specification = models.CharField(max_length=100, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    MD5_encryption = models.CharField(db_column='MD5_encryption', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sncode = models.CharField(max_length=100, blank=True, null=True)
    store_location = models.CharField(max_length=100, blank=True, null=True)
    pro_type = models.CharField(max_length=100, blank=True, null=True)
    createTime = models.DateTimeField(db_column='createTime', blank=True,auto_now_add=True)  # Field name made lowercase.
    updateTime = models.DateTimeField(db_column='updateTime', blank=True,auto_now=True)  # Field name made lowercase.
    storage_id = models.CharField(max_length=100, blank=True, null=True)
    credit_amount = models.CharField(max_length=100, blank=True, null=True)
    masterId = models.CharField(db_column='masterID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    IDSource = models.CharField(db_column='IDSource', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 's_order_item'


class UTimeline(models.Model):
    userid = models.CharField(db_column='userId', max_length=32, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    recordtime = models.DateTimeField(db_column='recordTime', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_timeline'


class UUser(models.Model):
    userid = models.BigIntegerField(db_column='userId', unique=True, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(unique=True, max_length=50, blank=True, null=True)
    aliwangwang = models.CharField(unique=True, max_length=100, blank=True, null=True)
    wechatid = models.CharField(db_column='wechatId', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    zimeihuiuserid = models.CharField(db_column='zimeihuiUserId', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    headimgurl = models.TextField(db_column='headImgurl', blank=True, null=True)  # Field name made lowercase.
    shendenguid = models.CharField(db_column='shendengUid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    birthday = models.CharField(max_length=50, blank=True, null=True)
    birthyear = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    province = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    county = models.CharField(max_length=20, blank=True, null=True)
    chatcount = models.IntegerField(db_column='chatCount', blank=True, null=True)  # Field name made lowercase.
    firstchattime = models.DateTimeField(db_column='firstChatTime', blank=True, null=True)  # Field name made lowercase.
    firstchatplatform = models.CharField(db_column='firstChatPlatform', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstchatwith = models.CharField(db_column='firstChatWith', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchattime = models.DateTimeField(db_column='lastChatTime', blank=True, null=True)  # Field name made lowercase.
    lastchatplatform = models.CharField(db_column='lastChatPlatform', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastchatwith = models.CharField(db_column='lastChatWith', max_length=50, blank=True, null=True)  # Field name made lowercase.
    payamount = models.FloatField(db_column='payAmount', blank=True, null=True)  # Field name made lowercase.
    paycount = models.IntegerField(db_column='payCount', blank=True, null=True)  # Field name made lowercase.
    refundamount = models.FloatField(db_column='refundAmount', blank=True, null=True)  # Field name made lowercase.
    refundcount = models.IntegerField(db_column='refundCount', blank=True, null=True)  # Field name made lowercase.
    lastpayamount = models.FloatField(db_column='lastPayAmount', blank=True, null=True)  # Field name made lowercase.
    lastpaytime = models.DateTimeField(db_column='lastPayTime', blank=True, null=True)  # Field name made lowercase.
    firstpayamount = models.FloatField(db_column='firstPayAmount', blank=True, null=True)  # Field name made lowercase.
    firstpaytime = models.DateTimeField(db_column='firstPayTime', blank=True, null=True)  # Field name made lowercase.
    firstlogintime = models.DateTimeField(db_column='firstLoginTime', blank=True, null=True)  # Field name made lowercase.
    firstloginplatform = models.CharField(db_column='firstLoginPlatform', max_length=100, blank=True, null=True)  # Field name made lowercase.
    istaobaouser = models.IntegerField(db_column='isTaobaoUser', blank=True, null=True)  # Field name made lowercase.
    iswechatuser = models.IntegerField(db_column='isWechatUser', blank=True, null=True)  # Field name made lowercase.
    iszimeihuiuser = models.IntegerField(db_column='isZimeihuiUser', blank=True, null=True)  # Field name made lowercase.
    istaobaochated = models.IntegerField(db_column='isTaobaoChated', blank=True, null=True)  # Field name made lowercase.
    iswechatchated = models.IntegerField(db_column='isWechatChated', blank=True, null=True)  # Field name made lowercase.
    iszimeihuichated = models.IntegerField(db_column='isZimeihuiChated', blank=True, null=True)  # Field name made lowercase.
    istaobaopayed = models.IntegerField(db_column='isTaobaoPayed', blank=True, null=True)  # Field name made lowercase.
    iswechatpayed = models.IntegerField(db_column='isWechatPayed', blank=True, null=True)  # Field name made lowercase.
    iszimeihuipayed = models.IntegerField(db_column='isZimeihuiPayed', blank=True, null=True)  # Field name made lowercase.
    taobaopayamount = models.FloatField(db_column='taobaoPayAmount', blank=True, null=True)  # Field name made lowercase.
    taobaopaycount = models.IntegerField(db_column='taobaoPayCount', blank=True, null=True)  # Field name made lowercase.
    taobaofirstpayamount = models.FloatField(db_column='taobaoFirstPayAmount', blank=True, null=True)  # Field name made lowercase.
    taobaofirstpaytime = models.IntegerField(db_column='taobaoFirstPayTime', blank=True, null=True)  # Field name made lowercase.
    taobaolastpayamount = models.FloatField(db_column='taobaoLastPayAmount', blank=True, null=True)  # Field name made lowercase.
    taobaolastpaytime = models.DateTimeField(db_column='taobaoLastPayTime', blank=True, null=True)  # Field name made lowercase.
    wechatchatcout = models.IntegerField(db_column='wechatChatCout', blank=True, null=True)  # Field name made lowercase.
    wechatchatinfototal = models.IntegerField(db_column='wechatChatInfoTotal', blank=True, null=True)  # Field name made lowercase.
    wechatno = models.CharField(db_column='wechatNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wechatnickname = models.CharField(db_column='wechatNickname', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wechatbelongto = models.TextField(db_column='wechatBelongTo', blank=True, null=True)  # Field name made lowercase.
    wechatfirstadd = models.CharField(db_column='wechatFirstAdd', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wechatfirstaddtime = models.DateTimeField(db_column='wechatFirstAddTime', blank=True, null=True)  # Field name made lowercase.
    wechatfirstchatwith = models.CharField(db_column='wechatFirstChatWith', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wechatfirstchattime = models.DateTimeField(db_column='wechatFirstChatTime', blank=True, null=True)  # Field name made lowercase.
    wechatlastchatwith = models.CharField(db_column='wechatLastChatWith', max_length=200, blank=True, null=True)  # Field name made lowercase.
    wechatlastchattime = models.DateTimeField(db_column='wechatLastChatTime', blank=True, null=True)  # Field name made lowercase.
    wechatpayamount = models.FloatField(db_column='wechatPayAmount', blank=True, null=True)  # Field name made lowercase.
    wechatpaycount = models.IntegerField(db_column='wechatPayCount', blank=True, null=True)  # Field name made lowercase.
    wechatfirstpaytime = models.DateTimeField(db_column='wechatFirstPayTime', blank=True, null=True)  # Field name made lowercase.
    wecahtfirstpayamount = models.FloatField(db_column='wecahtFirstPayAmount', blank=True, null=True)  # Field name made lowercase.
    wecahtlastpaytime = models.DateTimeField(db_column='wecahtLastPayTime', blank=True, null=True)  # Field name made lowercase.
    wechatlastpayamount = models.FloatField(db_column='wechatLastPayAmount', blank=True, null=True)  # Field name made lowercase.
    wechatlifestatus = models.CharField(db_column='wechatLifeStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    wechatisvipcarduser = models.IntegerField(db_column='wechatIsVIPCardUser', blank=True, null=True)  # Field name made lowercase.
    wechatvipcardbalance = models.FloatField(db_column='wechatVIPCardBalance', blank=True, null=True)  # Field name made lowercase.
    wechatvipcardamount = models.FloatField(db_column='wechatVIPCardAmount', blank=True, null=True)  # Field name made lowercase.
    zimeihuiphone = models.CharField(db_column='zimeihuiPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zimeihuinickname = models.CharField(db_column='zimeihuiNickname', max_length=200, blank=True, null=True)  # Field name made lowercase.
    zimeihuifxrole = models.CharField(db_column='zimeihuiFXRole', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zimeihuiregistertime = models.DateTimeField(db_column='zimeihuiRegisterTime', blank=True, null=True)  # Field name made lowercase.
    zimeihuifirstpaytime = models.DateTimeField(db_column='zimeihuiFirstPayTime', blank=True, null=True)  # Field name made lowercase.
    zimeihuifirstpayamount = models.FloatField(db_column='zimeihuiFirstPayAmount', blank=True, null=True)  # Field name made lowercase.
    zimeihuilastpaytime = models.DateTimeField(db_column='zimeihuiLastPayTime', blank=True, null=True)  # Field name made lowercase.
    zimeihuipayamount = models.FloatField(db_column='zimeihuiPayAmount', blank=True, null=True)  # Field name made lowercase.
    zimeihuipaycount = models.IntegerField(db_column='zimeihuiPayCount', blank=True, null=True)  # Field name made lowercase.
    iswoaregister = models.IntegerField(db_column='isWOARegister', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createsource = models.CharField(db_column='createSource', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'u_user'


class UUserBasicInfoRecord(models.Model):
    userid = models.CharField(db_column='userId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=50, blank=True, null=True)
    sourceid = models.CharField(db_column='sourceId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    headimgurl = models.CharField(db_column='headImgurl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(blank=True, null=True)
    birthday = models.CharField(max_length=20, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=10, blank=True, null=True)
    province = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    county = models.CharField(max_length=10, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'u_user_basic_info_record'


class UUserTag(models.Model):
    userid = models.BigIntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    tagname = models.CharField(db_column='tagName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tagtype = models.CharField(db_column='tagType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryId', blank=True, null=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    firstcategoryid = models.IntegerField(db_column='firstCategoryId', blank=True, null=True)  # Field name made lowercase.
    uidvalue = models.CharField(db_column='uidValue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uidtype = models.CharField(db_column='uidType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tagsrc = models.CharField(db_column='tagSrc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tagdetaillink = models.CharField(db_column='tagDetailLink', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'u_user_tag'
