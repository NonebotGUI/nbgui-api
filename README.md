# nbgui-api
供 NoneBot GUI 公告栏系统使用的 api 仓库，基于 Python Http Server


# Usage

#### Base URL
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
/api/nbgui/proxy/adapters.json

#驱动器
/api/nbgui/proxy/drivers.json

#插件
/api/nbgui/proxy/plugins.json
```

#### 获取快速部署列表
```
/api/nbgui/deploy/list
```


##### 获取对应的部署详细内容
```
/api/nbgui/deploy/detail?id=<id>
```