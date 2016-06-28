# encoding=utf-8

SOCRightConfig = {

    # 系统版本号，可以通过该参数reload，js，css资源文件
    # 'version':'0.9.1',
    # 站点名称
    # 'siteName': '云海统一权限管理平台',
    # js域名前缀，不需要修改
    # 'jsDomain': '/static/',
    # css域名前缀，不需要修改
    # 'cssDomain': '/static/',

    # 后台站点的域名，需要根据实际情况修改
    # 'siteDomain': 'http://127.0.0.1:8000/',
    # 服务站点的域名，需要根据实际情况修改
    # 'serviceSiteDomain': 'http://127.0.0.1:8000/',

    # 页面分页每页显示数
    'size': 15,
    # 搜索选择列表分页每页显示数
    'modelSize': 5,
    # 该系统的应用编号，不需要修改
    # 'appCode': 'SOCRight',
    # 权限服务保存cookie的key
    # 'rightCookieName': 'soc_right_user',
    # 权限后台保存cookie的key
    # 'adminCookieName': 'soc_right_admin_user',

    'SOCCookieName': 'soc_right_user',

    # 系统部署目录，需要根据实际情况修改
    # 'realPath' : '/opt/web/sso.socsoft.net/',
    # 导出用户信息目录，不需要修改
    # 'exportUserPath' : 'app/static/export/user/',
    # 导出操作日志信息目录，不需要修改
    # 'exportOperLogPath' : 'app/static/export/operlog/',
}

# 系统数据库配置，根据实际情况修改
db = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'db': 'assets',
    'charset': 'utf8'
}




# 域登陆服务器
ldap_config = {'ldap_host': 'ldap://ad.huimai365.com'}

# 登录密码解密KEY
private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIICXwIBAAKBgQDOuFOvoK6xnjiFl9dxkGbTvU4fNAjavPTNYTf4RDA6zPkvfE2c
ThNYXwGZv/CHSMSnKFK7l16G29ebQBmgfTFR+cRw3aNGhxF/evaQNX2BfYPUeBSw
9RYQfCy9aW7Rsk0ZViRROvWg+vobkWj/2t4ZcLd2WxZvR/1A9T19u2KgoQIDAQAB
AoGBAIEWcAPjZlO6Rvd9q2baUqv0sf0gREs75e7+v7HD+w4tA4qYp+psgv4TTe+S
AYSpd0wfDRLh4oB6djgXnikvJIU5b13yYHdtx2QgZSOH0/hxp5XSR1FkKMP0UFWH
Zid/3FfYvHJFY/SAkmdie7hA3Cy4zgFWYbibiCqddN9JkuO1AkEA10h18zkt7EW6
YpxsWyz0/P6YivkMr6e8/+dQcsNaN9kbKCttCSxrJLTA1x0KN15hSEN+/x2xdVT4
+c9SO8TIfwJBAPXRQ1xFioTsErZ5Gr7Ghd+rmfUYXa7Th9eY8RWZI6GwBvr4d0o5
ZPLu+YBousDj3SIsoSB9PGxYqYfFsKc7Bt8CQQDVisOsuegKeHPUAtMccXClTyki
mL1zs0+vCtRqscnYodrlMoYaVlwE8eJiviR3HYAjvQfIqLxw5RN+P56TOLOjAkEA
lwbX9PQA1APax2OGjBmanL5om845mLT76/lafaOV4bwtvbo0SFUU8bDjeAJgYyxc
a6ex4y0ul36twe4yx7wbTwJBANNM01YghBvSbq0qkGwsVpfKFcOuThCw2F3NcHNZ
oo5b8aLQLx/wHasFsr8Sa9zrg+87hnbyZWhWStn3uiIt6OU=
-----END RSA PRIVATE KEY-----'''
