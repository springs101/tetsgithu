# Generated by Django 2.1.7 on 2019-03-23 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syn_edb', '0003_auto_20190319_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='UOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masterId', models.CharField(blank=True, db_column='masterID', max_length=20, null=True)),
                ('IDSource', models.CharField(blank=True, db_column='IDSource', max_length=20, null=True)),
                ('tid', models.CharField(blank=True, max_length=20, null=True)),
                ('resultNum', models.CharField(blank=True, db_column='resultNum', max_length=20, null=True)),
                ('storage_id', models.CharField(blank=True, max_length=100, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_id', models.CharField(blank=True, max_length=100, null=True)),
                ('distributor_id', models.CharField(blank=True, max_length=100, null=True)),
                ('shop_name', models.CharField(blank=True, max_length=100, null=True)),
                ('out_tid', models.CharField(blank=True, max_length=100, null=True)),
                ('out_pay_tid', models.CharField(blank=True, max_length=100, null=True)),
                ('voucher_id', models.CharField(blank=True, max_length=100, null=True)),
                ('shopid', models.CharField(blank=True, max_length=100, null=True)),
                ('serial_num', models.CharField(blank=True, max_length=100, null=True)),
                ('order_channel', models.CharField(blank=True, max_length=100, null=True)),
                ('order_from', models.CharField(blank=True, max_length=100, null=True)),
                ('buyer_id', models.CharField(blank=True, max_length=100, null=True)),
                ('buyer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('abnormal_status', models.CharField(blank=True, max_length=100, null=True)),
                ('merge_status', models.CharField(blank=True, max_length=100, null=True)),
                ('receiver_name', models.CharField(blank=True, max_length=100, null=True)),
                ('receiver_mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('post', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('is_bill', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_name', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_situation', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_title', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_type', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_content', models.CharField(blank=True, max_length=100, null=True)),
                ('pro_totalfee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('order_totalfee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('reference_price_paid', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_fee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('cod_fee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('other_fee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('refund_totalfee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('discount_fee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('channel_disfee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('merchant_disfee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('order_disfee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('commission_fee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('is_cod', models.CharField(blank=True, max_length=100, null=True)),
                ('point_pay', models.CharField(blank=True, max_length=100, null=True)),
                ('cost_point', models.CharField(blank=True, max_length=100, null=True)),
                ('point', models.CharField(blank=True, max_length=100, null=True)),
                ('superior_point', models.CharField(blank=True, max_length=100, null=True)),
                ('royalty_fee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('external_point', models.CharField(blank=True, max_length=100, null=True)),
                ('express_no', models.CharField(blank=True, max_length=100, null=True)),
                ('express', models.CharField(blank=True, max_length=100, null=True)),
                ('express_coding', models.CharField(blank=True, max_length=100, null=True)),
                ('online_express', models.CharField(blank=True, max_length=100, null=True)),
                ('sending_type', models.CharField(blank=True, max_length=100, null=True)),
                ('real_income_freight', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('real_pay_freight', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('gross_weight', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('gross_weight_freight', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('net_weight_freight', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('freight_explain', models.CharField(blank=True, max_length=100, null=True)),
                ('total_weight', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('tid_net_weight', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('tid_time', models.CharField(blank=True, max_length=100, null=True)),
                ('pay_time', models.CharField(blank=True, max_length=100, null=True)),
                ('get_time', models.CharField(blank=True, max_length=100, null=True)),
                ('order_creater', models.CharField(blank=True, max_length=100, null=True)),
                ('business_man', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_received_operator', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_received_time', models.CharField(blank=True, max_length=100, null=True)),
                ('review_orders_operator', models.CharField(blank=True, max_length=100, null=True)),
                ('review_orders_time', models.CharField(blank=True, max_length=100, null=True)),
                ('finance_review_operator', models.CharField(blank=True, max_length=100, null=True)),
                ('finance_review_time', models.CharField(blank=True, max_length=100, null=True)),
                ('advance_printer', models.CharField(blank=True, max_length=100, null=True)),
                ('printer', models.CharField(blank=True, max_length=100, null=True)),
                ('print_time', models.CharField(blank=True, max_length=100, null=True)),
                ('is_print', models.CharField(blank=True, max_length=100, null=True)),
                ('adv_distributer', models.CharField(blank=True, max_length=100, null=True)),
                ('adv_distribut_time', models.CharField(blank=True, max_length=100, null=True)),
                ('distributer', models.CharField(blank=True, max_length=100, null=True)),
                ('distribut_time', models.CharField(blank=True, max_length=100, null=True)),
                ('is_inspection', models.CharField(blank=True, max_length=100, null=True)),
                ('inspecter', models.CharField(blank=True, max_length=100, null=True)),
                ('inspect_time', models.CharField(blank=True, max_length=100, null=True)),
                ('cancel_operator', models.CharField(blank=True, max_length=100, null=True)),
                ('cancel_time', models.CharField(blank=True, max_length=100, null=True)),
                ('revoke_cancel_er', models.CharField(blank=True, max_length=100, null=True)),
                ('revoke_cancel_time', models.CharField(blank=True, max_length=100, null=True)),
                ('packager', models.CharField(blank=True, max_length=100, null=True)),
                ('pack_time', models.CharField(blank=True, max_length=100, null=True)),
                ('weigh_operator', models.CharField(blank=True, max_length=100, null=True)),
                ('weigh_time', models.CharField(blank=True, max_length=100, null=True)),
                ('book_delivery_time', models.CharField(blank=True, max_length=100, null=True)),
                ('delivery_operator', models.CharField(blank=True, max_length=100, null=True)),
                ('delivery_time', models.CharField(blank=True, max_length=100, null=True)),
                ('locker', models.CharField(blank=True, max_length=100, null=True)),
                ('lock_time', models.CharField(blank=True, max_length=100, null=True)),
                ('book_file_time', models.CharField(blank=True, max_length=100, null=True)),
                ('file_operator', models.CharField(blank=True, max_length=100, null=True)),
                ('file_time', models.CharField(blank=True, max_length=100, null=True)),
                ('finish_time', models.CharField(blank=True, max_length=100, null=True)),
                ('modity_time', models.CharField(blank=True, max_length=100, null=True)),
                ('is_promotion', models.CharField(blank=True, max_length=100, null=True)),
                ('promotion_plan', models.CharField(blank=True, max_length=100, null=True)),
                ('out_promotion_detail', models.CharField(blank=True, max_length=100, null=True)),
                ('good_receive_time', models.CharField(blank=True, max_length=100, null=True)),
                ('receive_time', models.CharField(blank=True, max_length=100, null=True)),
                ('verificaty_time', models.CharField(blank=True, max_length=100, null=True)),
                ('enable_inte_sto_time', models.CharField(blank=True, max_length=100, null=True)),
                ('enable_inte_delivery_time', models.CharField(blank=True, max_length=100, null=True)),
                ('alipay_id', models.CharField(blank=True, max_length=100, null=True)),
                ('alipay_status', models.CharField(blank=True, max_length=100, null=True)),
                ('pay_mothed', models.CharField(blank=True, max_length=100, null=True)),
                ('pay_status', models.CharField(blank=True, max_length=100, null=True)),
                ('platform_status', models.CharField(blank=True, max_length=100, null=True)),
                ('rate', models.CharField(blank=True, max_length=100, null=True)),
                ('currency', models.CharField(blank=True, max_length=100, null=True)),
                ('delivery_status', models.CharField(blank=True, max_length=100, null=True)),
                ('buyer_message', models.CharField(blank=True, max_length=2000, null=True)),
                ('service_remarks', models.CharField(blank=True, max_length=2000, null=True)),
                ('inner_lable', models.CharField(blank=True, max_length=500, null=True)),
                ('distributor_mark', models.CharField(blank=True, max_length=100, null=True)),
                ('system_remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('other_remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.CharField(blank=True, max_length=100, null=True)),
                ('message_time', models.CharField(blank=True, max_length=100, null=True)),
                ('is_stock', models.CharField(blank=True, max_length=100, null=True)),
                ('related_orders', models.CharField(blank=True, max_length=100, null=True)),
                ('related_orders_type', models.CharField(blank=True, max_length=100, null=True)),
                ('import_mark', models.CharField(blank=True, max_length=100, null=True)),
                ('delivery_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_new_customer', models.CharField(blank=True, max_length=100, null=True)),
                ('distributor_level', models.CharField(blank=True, max_length=100, null=True)),
                ('cod_service_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('express_col_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('product_num', models.CharField(blank=True, max_length=100, null=True)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('item_num', models.CharField(blank=True, max_length=100, null=True)),
                ('single_num', models.CharField(blank=True, max_length=100, null=True)),
                ('flag_color', models.CharField(blank=True, max_length=100, null=True)),
                ('is_flag', models.CharField(blank=True, max_length=100, null=True)),
                ('taobao_delivery_order_status', models.CharField(blank=True, max_length=100, null=True)),
                ('taobao_delivery_status', models.CharField(blank=True, max_length=100, null=True)),
                ('taobao_delivery_method', models.CharField(blank=True, max_length=100, null=True)),
                ('order_process_time', models.CharField(blank=True, max_length=100, null=True)),
                ('is_break', models.CharField(blank=True, max_length=100, null=True)),
                ('breaker', models.CharField(blank=True, max_length=100, null=True)),
                ('break_time', models.CharField(blank=True, max_length=100, null=True)),
                ('break_explain', models.CharField(blank=True, max_length=200, null=True)),
                ('plat_send_status', models.CharField(blank=True, max_length=100, null=True)),
                ('plat_type', models.CharField(blank=True, max_length=100, null=True)),
                ('is_adv_sale', models.CharField(blank=True, max_length=100, null=True)),
                ('provinc_code', models.CharField(blank=True, max_length=100, null=True)),
                ('city_code', models.CharField(blank=True, max_length=100, null=True)),
                ('area_code', models.CharField(blank=True, max_length=100, null=True)),
                ('express_code', models.CharField(blank=True, max_length=100, null=True)),
                ('last_returned_time', models.CharField(blank=True, max_length=100, null=True)),
                ('last_refund_time', models.CharField(blank=True, max_length=100, null=True)),
                ('deliver_centre', models.CharField(blank=True, max_length=500, null=True)),
                ('deliver_station', models.CharField(blank=True, max_length=500, null=True)),
                ('is_pre_delivery_notice', models.CharField(blank=True, max_length=100, null=True)),
                ('jd_delivery_time', models.CharField(blank=True, max_length=100, null=True)),
                ('Sorting_code', models.CharField(blank=True, db_column='Sorting_code', max_length=100, null=True)),
                ('cod_settlement_vouchernumber', models.CharField(blank=True, max_length=100, null=True)),
                ('three_codes', models.CharField(blank=True, max_length=100, null=True)),
                ('send_site_name', models.CharField(blank=True, max_length=100, null=True)),
                ('distributing_centre_name', models.CharField(blank=True, max_length=100, null=True)),
                ('originCode', models.CharField(blank=True, db_column='originCode', max_length=100, null=True)),
                ('destCode', models.CharField(blank=True, db_column='destCode', max_length=100, null=True)),
                ('big_marker', models.CharField(blank=True, max_length=100, null=True)),
                ('platform_preferential', models.CharField(blank=True, max_length=100, null=True)),
                ('createTime', models.DateTimeField(blank=True, db_column='createTime', default=datetime.datetime(2019, 3, 23, 13, 55, 1, 480200))),
                ('updateTime', models.DateTimeField(auto_now=True, db_column='updateTime')),
            ],
            options={
                'db_table': 's_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UOrderitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(blank=True, max_length=20, null=True)),
                ('pro_detail_code', models.CharField(blank=True, max_length=20, null=True)),
                ('pro_name', models.CharField(blank=True, max_length=100, null=True)),
                ('storage_id', models.CharField(blank=True, max_length=100, null=True)),
                ('specification', models.CharField(blank=True, max_length=100, null=True)),
                ('barcode', models.CharField(blank=True, max_length=100, null=True)),
                ('combine_barcode', models.CharField(blank=True, max_length=100, null=True)),
                ('iscancel', models.CharField(blank=True, max_length=100, null=True)),
                ('isscheduled', models.CharField(blank=True, max_length=100, null=True)),
                ('stock_situation', models.CharField(blank=True, max_length=100, null=True)),
                ('isbook_pro', models.CharField(blank=True, max_length=100, null=True)),
                ('iscombination', models.CharField(blank=True, max_length=100, null=True)),
                ('isgifts', models.CharField(blank=True, max_length=100, null=True)),
                ('gift_num', models.IntegerField(blank=True, null=True)),
                ('book_storage', models.CharField(blank=True, max_length=100, null=True)),
                ('pro_num', models.IntegerField(blank=True, null=True)),
                ('send_num', models.IntegerField(blank=True, null=True)),
                ('refund_num', models.IntegerField(blank=True, null=True)),
                ('refund_renum', models.IntegerField(blank=True, null=True)),
                ('inspection_num', models.IntegerField(blank=True, null=True)),
                ('timeinventory', models.CharField(blank=True, max_length=100, null=True)),
                ('cost_price', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('sell_price', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('average_price', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('credit_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('original_price', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('sys_price', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('ferght', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('item_discountfee', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('inspection_time', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('shopid', models.CharField(blank=True, max_length=100, null=True)),
                ('out_tid', models.CharField(blank=True, max_length=100, null=True)),
                ('out_proid', models.CharField(blank=True, max_length=100, null=True)),
                ('out_prosku', models.CharField(blank=True, max_length=100, null=True)),
                ('proexplain', models.CharField(blank=True, max_length=100, null=True)),
                ('buyer_memo', models.CharField(blank=True, max_length=1000, null=True)),
                ('seller_remark', models.CharField(blank=True, max_length=1000, null=True)),
                ('distributer', models.CharField(blank=True, max_length=100, null=True)),
                ('distribut_time', models.CharField(blank=True, max_length=100, null=True)),
                ('second_barcode', models.CharField(blank=True, max_length=100, null=True)),
                ('product_no', models.CharField(blank=True, max_length=100, null=True)),
                ('brand_number', models.CharField(blank=True, max_length=100, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=100, null=True)),
                ('book_inventory', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('product_specification', models.CharField(blank=True, max_length=100, null=True)),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('MD5_encryption', models.CharField(blank=True, db_column='MD5_encryption', max_length=100, null=True)),
                ('sncode', models.CharField(blank=True, max_length=100, null=True)),
                ('store_location', models.CharField(blank=True, max_length=100, null=True)),
                ('pro_type', models.CharField(blank=True, max_length=100, null=True)),
                ('createTime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
                ('updateTime', models.DateTimeField(blank=True, db_column='updateTime', null=True)),
            ],
            options={
                'db_table': 's_order_item',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='S_Order',
        ),
    ]
