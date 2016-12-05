智能药箱——用户接口设计
==========

快速参考
--------
所有API调用均在/api/user命名空间下，访问域名，正式环境：http://admin.smart_medical_kit.com，测试环境：http://admin-dev.smart_medical_kit.com

URL|HTTP|功能
---|----|----
[/create](#创建)|POST|创建
[/update](#更新)|POST|更新
[/list](#列表)|GET|列表
[/delete](#删除)|GET|删除

#### 创建
向/create发送POST请求，请求参数如下：

字段|类型|意义
----|----|----
phone_number|number|用户手机号码
nick|string|昵称
register_type|number|注册方式
token|string|令牌token

创建成功返回创建时间：

字段|类型|意义
----|----|----
created_at|date|创建时间

#### 更新
向/update发送POST请求，请求参数如下：

字段|类型|意义
----|----|----
user_id|number|用户ID
sex|number|性别
phone_number|number|用户手机号码
nick|string|昵称
avatar|string|头像URL
token|string|令牌token

修改成功返回更新时间：

字段|类型|意义
----|----|----
updated_at|date|更新时间

#### 列表
向/list发送GET请求，请求参数如下：

字段|类型|意义
----|----|----
page_number|number|第几页，默认第1页
page_size|number|每页返回结果数，默认100
phone_number|number|用户手机号码，可选
token|string|令牌token

登录成功result返回用户信息：

字段|类型|意义
----|----|----
errcode|number|错误码
total_count|number|结果总数
result|array|返回结果
result[0].id|number|用户ID
result[0].username|string|用户名
result[0].sex|number|性别
result[0].phone_number|number|用户手机号码
result[0].nick|string|昵称
result[0].avatar|string|头像URL
result[0].register_type|number|注册方式
result[0].created_at|date|注册时间

#### 删除
向/delete发送GET请求，请求参数如下：

字段|类型|意义
----|----|----
user_id|number|用户ID
token|string|令牌token

删除成功返回删除时间：

字段|类型|意义
----|----|----
deleted_at|date|删除时间
