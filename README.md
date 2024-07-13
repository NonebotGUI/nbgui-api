# nbgui-api
供 NoneBot GUI 公告栏系统使用的 api 仓库，基于 Python Http Server


# Usage

#### Base Url
```
api.zobyic.top
```

### GET
#### 获取公告栏列表
```
/api/nbgui/broadcast/list
```


##### 获取对应的公告内容
```
/api/nbgui/broadcast/detail?id=<公告id>
```

#### NoneBot Registry 列表的美化输出
```
#适配器
/api/nbgui/proxy/adapters

#驱动器
/api/nbgui/proxy/drivers

#插件
/api/nbgui/proxy/plugins
```