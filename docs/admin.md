智能药箱——管理员接口设计
==========

快速参考
--------
所有API调用均在/api/admin命名空间下，访问域名，正式环境：http://admin.smart_medical_kit.com，测试环境：http://admin-dev.smart_medical_kit.com

URL|HTTP|功能
---|----|----
[/login](#登录)|POST|登录
[/logout](#退出登录)|GET|退出登录
[/reset_password](#重置密码)|POST|重置密码

#### 登录
向/login发送POST请求，请求参数如下：

字段|类型|意义
----|----|----
username|string|用户名
password|string|密码

登录成功，result返回用户信息：

字段|类型|意义
----|----|----
id|number|管理员ID
username|string|管理员用户名
token|string|令牌token

#### 退出登录
向/logout发送GET请求，请求参数如下：

字段|类型|意义
----|----|----
token|string|令牌token

退出登录成功，返回errcode=0错误码

字段|类型|意义
----|----|----
updated_at|date|更新时间

#### 重置密码
向/reset_password发送POST请求，请求参数如下：

字段|类型|意义
----|----|----
old_password|string|旧密码
new_password|string|新密码
token|string|令牌token

设置成功，返回errcode=0错误码