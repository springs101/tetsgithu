# tetsgithu
获取订单内容

请自己建立数据库，并且建立两个表单

CREATE TABLE `s_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tid` varchar(100) DEFAULT NULL COMMENT 'E店宝订单号',
  `masterId` varchar(100) DEFAULT NULL COMMENT '所属人员id',
  `IDSource` varchar(100) DEFAULT NULL COMMENT '所属用户id判定依据',
  `resultNum` varchar(20) DEFAULT NULL COMMENT '结果号',
  `storage_id` varchar(100) DEFAULT NULL COMMENT '仓库编号',
  `transaction_id` varchar(100) DEFAULT NULL COMMENT '交易编号',
  `customer_id` varchar(100) DEFAULT NULL COMMENT '客户编号',
  `distributor_id` varchar(100) DEFAULT NULL COMMENT '分销商编号',
  `shop_name` varchar(100) DEFAULT NULL COMMENT '店铺名称',
  `out_tid` varchar(100) DEFAULT NULL COMMENT '外部平台单号',
  `out_pay_tid` varchar(100) DEFAULT NULL COMMENT '外部平台付款单号',
  `voucher_id` varchar(100) DEFAULT NULL COMMENT '凭证单号',
  `shopid` varchar(100) DEFAULT NULL COMMENT '店铺代码',
  `serial_num` varchar(100) DEFAULT NULL COMMENT '流水号',
  `order_channel` varchar(100) DEFAULT NULL COMMENT '订单渠道',
  `order_from` varchar(100) DEFAULT NULL COMMENT '订单来源',
  `buyer_id` varchar(100) DEFAULT NULL COMMENT '买家ID',
  `buyer_name` varchar(100) DEFAULT NULL COMMENT '买家姓名',
  `type` varchar(100) DEFAULT NULL COMMENT '订单类型',
  `status` varchar(100) DEFAULT NULL COMMENT '处理状态',
  `abnormal_status` varchar(100) DEFAULT NULL COMMENT '异常状态',
  `merge_status` varchar(100) DEFAULT NULL COMMENT '合并状态',
  `receiver_name` varchar(100) DEFAULT NULL COMMENT '收货人',
  `receiver_mobile` varchar(100) DEFAULT NULL COMMENT '收货手机',
  `phone` varchar(100) DEFAULT NULL COMMENT '电话',
  `province` varchar(100) DEFAULT NULL COMMENT '省',
  `city` varchar(100) DEFAULT NULL COMMENT '市',
  `district` varchar(100) DEFAULT NULL COMMENT '区',
  `address` varchar(200) DEFAULT NULL COMMENT '地址',
  `post` varchar(100) DEFAULT NULL COMMENT '邮编',
  `email` varchar(100) DEFAULT NULL COMMENT '电子邮件',
  `is_bill` varchar(100) DEFAULT NULL COMMENT '是否开发票',
  `invoice_name` varchar(100) DEFAULT NULL COMMENT '发票名称',
  `invoice_situation` varchar(100) DEFAULT NULL COMMENT '开票情况',
  `invoice_title` varchar(100) DEFAULT NULL COMMENT '发票抬头',
  `invoice_type` varchar(100) DEFAULT NULL COMMENT '发票类型',
  `invoice_content` varchar(100) DEFAULT NULL COMMENT '开票内容',
  `pro_totalfee` varchar(100) DEFAULT NULL COMMENT '产品总金额',
  `order_totalfee` varchar(100) DEFAULT NULL COMMENT '订单总金额',
  `reference_price_paid` varchar(100) DEFAULT NULL COMMENT '实收参考价格',
  `invoice_fee` varchar(100) DEFAULT NULL COMMENT '发票价格',
  `cod_fee` varchar(100) DEFAULT NULL COMMENT '货到付款金额',
  `other_fee` varchar(100) DEFAULT NULL COMMENT '其它费用',
  `refund_totalfee` varchar(100) DEFAULT NULL COMMENT '退款总金额',
  `discount_fee` varchar(100) DEFAULT NULL COMMENT '优惠金额',
  `discount` varchar(100) DEFAULT NULL COMMENT '折扣',
  `channel_disfee` varchar(100) DEFAULT NULL COMMENT '渠道优惠金额',
  `merchant_disfee` varchar(100) DEFAULT NULL COMMENT '商家优惠金额',
  `order_disfee` varchar(100) DEFAULT NULL COMMENT '整单优惠',
  `commission_fee` varchar(100) DEFAULT NULL COMMENT '佣金',
  `is_cod` varchar(100) DEFAULT NULL COMMENT '是否货到付款',
  `point_pay` varchar(100) DEFAULT NULL COMMENT '是否积分换购',
  `cost_point` varchar(100) DEFAULT NULL COMMENT '消耗积分',
  `point` varchar(100) DEFAULT NULL COMMENT '获得积分',
  `superior_point` varchar(100) DEFAULT NULL COMMENT '上级积分',
  `royalty_fee` varchar(100) DEFAULT NULL COMMENT '提成金额',
  `external_point` varchar(100) DEFAULT NULL COMMENT '外部积分',
  `express_no` varchar(100) DEFAULT NULL COMMENT '快递单号',
  `express` varchar(100) DEFAULT NULL COMMENT '快递公司',
  `express_coding` varchar(100) DEFAULT NULL COMMENT '快递代码',
  `online_express` varchar(100) DEFAULT NULL COMMENT '线上快递公司',
  `sending_type` varchar(100) DEFAULT NULL COMMENT '配送方式',
  `real_income_freight` varchar(100) DEFAULT NULL COMMENT '实收运费',
  `real_pay_freight` varchar(100) DEFAULT NULL COMMENT '实付运费',
  `gross_weight` varchar(100) DEFAULT NULL COMMENT '运费（猜测）',
  `gross_weight_freight` varchar(100) DEFAULT NULL COMMENT '毛重运费',
  `net_weight_freight` varchar(100) DEFAULT NULL COMMENT '净重运费',
  `freight_explain` varchar(100) DEFAULT NULL COMMENT '运费说明',
  `total_weight` varchar(100) DEFAULT NULL COMMENT '总重量',
  `tid_net_weight` varchar(100) DEFAULT NULL COMMENT '订单净重',
  `tid_time` varchar(100) DEFAULT NULL COMMENT '订货时间',
  `pay_time` varchar(100) DEFAULT NULL COMMENT '付款时间',
  `get_time` varchar(100) DEFAULT NULL COMMENT '获取时间',
  `order_creater` varchar(100) DEFAULT NULL COMMENT '下单员',
  `business_man` varchar(100) DEFAULT NULL COMMENT '业务员',
  `payment_received_operator` varchar(100) DEFAULT NULL COMMENT '到款员',
  `payment_received_time` varchar(100) DEFAULT NULL COMMENT '到款时间',
  `review_orders_operator` varchar(100) DEFAULT NULL COMMENT '审单员',
  `review_orders_time` varchar(100) DEFAULT NULL COMMENT '审单时间',
  `finance_review_operator` varchar(100) DEFAULT NULL COMMENT '财务审核人',
  `finance_review_time` varchar(100) DEFAULT NULL COMMENT '财务审核时间',
  `advance_printer` varchar(100) DEFAULT NULL COMMENT '预打印员',
  `printer` varchar(100) DEFAULT NULL COMMENT '打印员',
  `print_time` varchar(100) DEFAULT NULL COMMENT '打印时间',
  `is_print` varchar(100) DEFAULT NULL COMMENT '是否打印',
  `adv_distributer` varchar(100) DEFAULT NULL COMMENT '预配货员',
  `adv_distribut_time` varchar(100) DEFAULT NULL COMMENT '预配货时间',
  `distributer` varchar(100) DEFAULT NULL COMMENT '配货员',
  `distribut_time` varchar(100) DEFAULT NULL COMMENT '配货时间',
  `is_inspection` varchar(100) DEFAULT NULL COMMENT '是否验货',
  `inspecter` varchar(100) DEFAULT NULL COMMENT '验货员',
  `inspect_time` varchar(100) DEFAULT NULL COMMENT '验货时间',
  `cancel_operator` varchar(100) DEFAULT NULL COMMENT '取消员',
  `cancel_time` varchar(100) DEFAULT NULL COMMENT '取消时间',
  `revoke_cancel_er` varchar(100) DEFAULT NULL COMMENT '反取消员',
  `revoke_cancel_time` varchar(100) DEFAULT NULL COMMENT '反取消时间',
  `packager` varchar(100) DEFAULT NULL COMMENT '打包员',
  `pack_time` varchar(100) DEFAULT NULL COMMENT '打包时间',
  `weigh_operator` varchar(100) DEFAULT NULL COMMENT '称重员',
  `weigh_time` varchar(100) DEFAULT NULL COMMENT '是称重时间',
  `book_delivery_time` varchar(100) DEFAULT NULL COMMENT '预计发货时间',
  `delivery_operator` varchar(100) DEFAULT NULL COMMENT '发货员',
  `delivery_time` varchar(100) DEFAULT NULL COMMENT '发货时间',
  `locker` varchar(100) DEFAULT NULL COMMENT '锁定员',
  `lock_time` varchar(100) DEFAULT NULL COMMENT '锁定时间',
  `book_file_time` varchar(100) DEFAULT NULL COMMENT '预计归档时间',
  `file_operator` varchar(100) DEFAULT NULL COMMENT '归档员',
  `file_time` varchar(100) DEFAULT NULL COMMENT '归档时间',
  `finish_time` varchar(100) DEFAULT NULL COMMENT '完成时间',
  `modity_time` varchar(100) DEFAULT NULL COMMENT '订单修改时间',
  `is_promotion` varchar(100) DEFAULT NULL COMMENT '促销标记',
  `promotion_plan` text DEFAULT NULL COMMENT '满足的促销方案',
  `out_promotion_detail` varchar(100) DEFAULT NULL COMMENT '外部平台促销详情',
  `good_receive_time` varchar(100) DEFAULT NULL COMMENT '到货日期',
  `receive_time` varchar(100) DEFAULT NULL COMMENT '生成应收时间',
  `verificaty_time` varchar(100) DEFAULT NULL COMMENT '核销日期',
  `enable_inte_sto_time` varchar(100) DEFAULT NULL COMMENT '启用智能仓库时间',
  `enable_inte_delivery_time` varchar(100) DEFAULT NULL COMMENT '启用智能快递时间',
  `alipay_id` varchar(100) DEFAULT NULL COMMENT '支付宝账户',
  `alipay_status` varchar(100) DEFAULT NULL COMMENT '支付宝状态',
  `pay_mothed` varchar(100) DEFAULT NULL COMMENT '支付方式',
  `pay_status` varchar(100) DEFAULT NULL COMMENT '付款状态',
  `platform_status` varchar(100) DEFAULT NULL COMMENT '外部平台状态',
  `rate` varchar(100) DEFAULT NULL COMMENT '汇率',
  `currency` varchar(100) DEFAULT NULL COMMENT '币种',
  `delivery_status` varchar(100) DEFAULT NULL COMMENT '发货状态',
  `buyer_message` varchar(300) DEFAULT NULL COMMENT '买家留言',
  `service_remarks` varchar(1500) DEFAULT NULL COMMENT '客服备注',
  `inner_lable` varchar(300) DEFAULT NULL COMMENT '内部便签',
  `distributor_mark` text DEFAULT NULL COMMENT '分销商便签',
  `system_remarks` text DEFAULT NULL COMMENT '系统备注',
  `other_remarks` text DEFAULT NULL COMMENT '其他备注',
  `message` varchar(100) DEFAULT NULL COMMENT '短信通知',
  `message_time` varchar(100) DEFAULT NULL COMMENT '短信发送时间',
  `is_stock` varchar(100) DEFAULT NULL COMMENT '是否缺货',
  `related_orders` varchar(100) DEFAULT NULL COMMENT '相关订单',
  `related_orders_type` varchar(100) DEFAULT NULL COMMENT '相关订单类型',
  `import_mark` varchar(100) DEFAULT NULL COMMENT '导入标记:不导入,未导入,已处理,已导入,已取消',
  `delivery_name` varchar(100) DEFAULT NULL COMMENT '第三方快递名称',
  `is_new_customer` varchar(100) DEFAULT NULL COMMENT '是否新客户',
  `distributor_level` varchar(100) DEFAULT NULL COMMENT '分销商等级',
  `cod_service_fee` varchar(100) DEFAULT NULL COMMENT '货到付款服务费',
  `express_col_fee` varchar(100) DEFAULT NULL COMMENT '产品数量',
  `product_num` varchar(100) DEFAULT NULL COMMENT '产品数量',
  `sku` varchar(100) DEFAULT NULL COMMENT '产品条形码',
  `item_num` varchar(100) DEFAULT NULL COMMENT '单品条数',
  `single_num` varchar(100) DEFAULT NULL COMMENT '单品数量',
  `flag_color` varchar(100) DEFAULT NULL COMMENT '旗帜颜色',
  `is_flag` varchar(100) DEFAULT NULL COMMENT '是否插旗',
  `taobao_delivery_order_status` varchar(100) DEFAULT NULL COMMENT '淘宝快递订单状态',
  `taobao_delivery_status` varchar(100) DEFAULT NULL COMMENT '淘宝快递状态',
  `taobao_delivery_method` varchar(100) DEFAULT NULL COMMENT '淘宝快递方式',
  `order_process_time` varchar(100) DEFAULT NULL COMMENT '处理订单需要的时间戳',
  `is_break` varchar(100) DEFAULT NULL COMMENT '是否中断',
  `breaker` varchar(100) DEFAULT NULL COMMENT '中断员',
  `break_time` varchar(100) DEFAULT NULL COMMENT '中断时间',
  `break_explain` varchar(200) DEFAULT NULL COMMENT '中断说明',
  `plat_send_status` varchar(100) DEFAULT NULL COMMENT '平台发货状态',
  `plat_type` varchar(100) DEFAULT NULL COMMENT '平台类型',
  `is_adv_sale` varchar(100) DEFAULT NULL COMMENT '是否预售',
  `provinc_code` varchar(100) DEFAULT NULL COMMENT '省编码',
  `city_code` varchar(100) DEFAULT NULL COMMENT '市编码',
  `area_code` varchar(100) DEFAULT NULL COMMENT '区编码',
  `express_code` varchar(100) DEFAULT NULL COMMENT '快递编码',
  `last_returned_time` varchar(100) DEFAULT NULL COMMENT '最后一次退货时间',
  `last_refund_time` varchar(100) DEFAULT NULL COMMENT '最后一次退款时间',
  `deliver_centre` varchar(100) DEFAULT NULL COMMENT '配送中心名称',
  `deliver_station` varchar(100) DEFAULT NULL COMMENT '配送站点名称',
  `is_pre_delivery_notice` varchar(100) DEFAULT NULL COMMENT '是否送货前通知',
  `jd_delivery_time` varchar(100) DEFAULT NULL COMMENT '送货时间',
  `Sorting_code` varchar(100) DEFAULT NULL COMMENT '分拣代码',
  `cod_settlement_vouchernumber` varchar(100) DEFAULT NULL COMMENT '结算担保号',
  `three_codes` varchar(100) DEFAULT NULL COMMENT '三个号（猜测）',
  `send_site_name` varchar(100) DEFAULT NULL COMMENT '配送站名称',
  `distributing_centre_name` varchar(100) DEFAULT NULL COMMENT '配送中心名称',
  `originCode` varchar(100) DEFAULT NULL COMMENT '原始号',
  `destCode` varchar(100) DEFAULT NULL COMMENT '目标号（猜测）',
  `big_marker` varchar(100) DEFAULT NULL COMMENT '上级市场人员（猜测）',
  `platform_preferential` varchar(100) DEFAULT NULL COMMENT '平台标识（猜测）',
  `createTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '数据创建时间',
  `updateTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '数据更新时间',
  PRIMARY KEY (`id`),
  KEY `index_masterId` (`masterId`),
  KEY `index_createTime` (`createTime`),
  KEY `index_updateTime` (`updateTime`),
  KEY `index_shopid` (`shopid`),
  KEY `index_receiver_mobile` (`receiver_mobile`),
  KEY `index_out_tid` (`out_tid`),
  UNIQUE KEY `unique_tid` (`tid`),
  KEY `index_masterId_type_payStatus` (`masterId`,`type`,`pay_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=7620001 COMMENT='E店宝订单表';



CREATE TABLE `s_order_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tid` varchar(100) DEFAULT NULL COMMENT '订单编号',
  `pro_detail_code` varchar(20) DEFAULT NULL COMMENT '产品明细编号',
  `pro_name` varchar(100) DEFAULT NULL COMMENT '网店产品名称',
  `specification` varchar(100) DEFAULT NULL COMMENT '规格',
  `barcode` varchar(100) DEFAULT NULL COMMENT '条形码',
  `combine_barcode` varchar(100) DEFAULT NULL COMMENT '套装条形码',
  `iscancel` varchar(100) DEFAULT NULL COMMENT '是否取消',
  `isscheduled` varchar(100) DEFAULT NULL COMMENT '是否预定',
  `stock_situation` varchar(100) DEFAULT NULL COMMENT '产品缺货情况',
  `isbook_pro` varchar(100) DEFAULT NULL COMMENT '是否预售产品',
  `iscombination` varchar(100) DEFAULT NULL COMMENT '是否组合',
  `isgifts` varchar(100) DEFAULT NULL COMMENT '是否赠品',
  `gift_num` int(11) DEFAULT NULL COMMENT '赠品数量',
  `book_storage` varchar(100) DEFAULT NULL COMMENT '预分配库存',
  `pro_num` int(11) DEFAULT NULL COMMENT '订货数量',
  `send_num` int(11) DEFAULT NULL COMMENT '发货数量',
  `refund_num` int(11) DEFAULT NULL COMMENT '退货数量',
  `refund_renum` int(11) DEFAULT NULL COMMENT '退货到货数量',
  `inspection_num` int(11) DEFAULT NULL COMMENT '验货数量',
  `timeinventory` varchar(100) DEFAULT NULL COMMENT '当期库存',
  `cost_price` decimal(20,0) DEFAULT NULL COMMENT '成本价',
  `sell_price` decimal(20,0) DEFAULT NULL COMMENT '销售单价',
  `average_price` decimal(20,0) DEFAULT NULL COMMENT '加权平均单价',
  `original_price` decimal(20,0) DEFAULT NULL COMMENT '原始价格',
  `sys_price` decimal(20,0) DEFAULT NULL COMMENT '软件销售单价',
  `ferght` decimal(20,0) DEFAULT NULL COMMENT '运费',
  `item_discountfee` decimal(20,0) DEFAULT NULL COMMENT '单品优惠金额',
  `inspection_time` varchar(100) DEFAULT NULL COMMENT '验货日期',
  `weight` decimal(20,0) DEFAULT NULL COMMENT '重量',
  `shopid` varchar(100) DEFAULT NULL COMMENT '店铺编号',
  `out_tid` varchar(100) DEFAULT NULL COMMENT '外部平台单号',
  `out_proid` varchar(100) DEFAULT NULL COMMENT '外部平台产品id',
  `out_prosku` varchar(100) DEFAULT NULL COMMENT '外部平台产品sku_id',
  `proexplain` varchar(100) DEFAULT NULL COMMENT '产品简介',
  `buyer_memo` varchar(1000) DEFAULT NULL COMMENT '买家留言',
  `seller_remark` varchar(1000) DEFAULT NULL COMMENT '卖家备注',
  `distributer` varchar(100) DEFAULT NULL COMMENT '配货员',
  `distribut_time` varchar(100) DEFAULT NULL COMMENT '备用条码',
  `second_barcode` varchar(100) DEFAULT NULL COMMENT '发票价格',
  `product_no` varchar(100) DEFAULT NULL COMMENT '产品编号',
  `brand_number` decimal(20,0) DEFAULT NULL COMMENT '品牌编号',
  `brand_name` varchar(100) DEFAULT NULL COMMENT '品牌名称',
  `book_inventory` decimal(20,0) DEFAULT NULL COMMENT '自己猜测',
  `discount_amount` decimal(20,0) DEFAULT NULL COMMENT '打折金额',
  `MD5_encryption` varchar(100) DEFAULT NULL COMMENT 'MD5加密值',
  `sncode` varchar(100) DEFAULT NULL COMMENT '自己猜测',
  `store_location` varchar(100) DEFAULT NULL COMMENT '自己猜测',
  `pro_type` varchar(100) DEFAULT NULL COMMENT '自己猜测',
  `storage_id` varchar(100) DEFAULT NULL,
  `credit_amount` varchar(100) DEFAULT NULL,
  `masterID` varchar(100) DEFAULT NULL,
  `IDSource` varchar(100) DEFAULT NULL,
  `product_specification` varchar(100) DEFAULT NULL,
  `createTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '数据创建时间',
  `updateTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '数据更新时间',
  PRIMARY KEY (`id`),
  KEY `index_shopid` (`shopid`),
  KEY `index_createTime` (`createTime`),
  KEY `index_updateTime` (`updateTime`),
  KEY `index_tid` (`tid`),
  KEY `index_pro_name` (`pro_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=100650001 COMMENT='E店宝订单详情表';

