---
id: 2
time: 2024-07-13 22:33
---

感谢您使用 NoneBot Flutter GUI!
本公告栏服务由 nbgui-api 提供，通过 Vercel 部署

你可以选择你喜欢的 http 请求工具来调用这个 api ， 如 ``httpx`` 、 ``requests`` 等


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
/api/nbgui/proxy/adapters.json

#驱动器
/api/nbgui/proxy/drivers.json

#插件
/api/nbgui/proxy/plugins.json
```