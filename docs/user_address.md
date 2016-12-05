智能药箱——用户地址接口设计
==========

快速参考
--------
所有API调用均在/api/user_address命名空间下，访问域名，正式环境：http://admin.smart_medical_kit.com，测试环境：http://admin-dev.smart_medical_kit.com

URL|HTTP|功能
---|----|----
[/create](#创建)|POST|创建
[/update](#更新)|POST|更新
[/list](#列表)|GET|列表
[/delete](#删除)|GET|删除
[/set_default](#设置默认)|POST|设置默认

#### 创建
向/create发送POST请求，请求参数如下：

字段|类型|意义
----|----|----
user_id|number|用户ID
region_code|string|地区编码
street|string|街道地址
consignee|string|收货人
contact|string|联系电话
token|string|令牌token

创建成功，返回创建时间：

字段|类型|意义
----|----|----
id|number|用户地址ID
created_at|date|创建时间

#### 更新
向/update发送POST请求，请求参数如下：

字段|类型|意义
----|----|----
user_address_id|number|用户地址ID
region_code|string|地区编码
street|string|街道地址
consignee|string|收货人
contact|string|联系电话
token|string|令牌token

更新成功，返回更新时间：

字段|类型|意义
----|----|----
updated_at|date|更新时间

#### 列表
向/list发送GET请求，请求参数如下：

字段|类型|意义
----|----|----
user_id|number|用户ID
token|string|令牌token

获取成功，result返回用户地址信息：

字段|类型|意义
----|----|----
errcode|number|错误码
total_count|number|结果总数
result|array|返回结果
result[0].id|number|用户地址ID
result[0].user_id|number|用户ID
result[0].region_code|string|地区编码
result[0].street|string|街道地址
result[0].is_default|boolean|是否默认地址
result[0].consignee|string|收货人
result[0].contact|string|联系电话
result[0].created_at|date|注册时间

#### 删除
向/delete发送GET请求，请求参数如下：

字段|类型|意义
----|----|----
user_address_id|number|用户地址ID
token|string|令牌token

删除成功，返回删除时间：

字段|类型|意义
----|----|----
deleted_at|date|删除时间

#### 设置默认
向/set_default发送POST请求，请求参数如下：

字段|类型|意义
----|----|----
user_address_id|number|用户地址ID
token|string|令牌token

设置成功，返回errcode=0错误码
