## 数据表建议 -- wanglei版本
我们可以创建两个表，一个用于存储灾害事件的基本信息（用于列表页），另一个用于存储灾害事件的详细信息（用于详情页）。
1. disasters_summary（灾害概要）

| 字段名         | 数据类型 | 描述                                       |
|------------|-------|------------------------------------------|
| dis_id     | INTEGER | 灾害事件的唯一标识符，设为主键                        |
| year       | INTEGER | 灾害事件发生的年份                              |
| disaster_group | TEXT    | 灾害事件的大类别                            |
| disaster_type  | TEXT    | 灾害事件的类型                              |
| country    | TEXT    | 灾害事件发生的国家或地区                        |
| iso        | TEXT    | 该国家或地区的ISO 3166-1 alpha-3代码       |
| total_affected | INTEGER | 该灾害事件总共影响到的人数                   |
| total_damages_usd | REAL    | 该灾害事件总共造成的损失，单位为千美元         |

2. disasters_details（灾害详情）

| 字段名               | 数据类型 | 描述                                 |
|------------------|-------|------------------------------------|
| dis_id           | INTEGER | 灾害事件的唯一标识符，与disasters_summary表的dis_id关联 |
| seq              | INTEGER | 该年中该灾害事件的序号                     |
| disaster_subgroup   | TEXT    | 灾害事件的子类别                       |
| disaster_subtype    | TEXT    | 灾害事件的子类型                       |
| disaster_subsubtype | TEXT    | 灾害事件的子子类型                     |
| event_name       | TEXT    | 灾害事件的名称或描述                     |
| region           | TEXT    | 该国家或地区所属的联合国统计分区              |
| continent        | TEXT    | 该国家或地区所属的洲                      |
| location         | TEXT    | 灾害事件发生的具体位置                     |
| origin           | TEXT    | 灾害事件的起因或来源                       |
| associated_dis   | TEXT    | 与该灾害事件相关的其他灾害事件的Glide编号  |
| associated_dis2  | TEXT    | 与该灾害事件相关的另一个灾害事件的Glide编号 |
| ofda_response    | INTEGER | 是否有美国联邦紧急管理署（OFDA）参与应对该灾害事件（0：否，1：是） |
| appeal           | INTEGER | 联合国是否发布了为该灾害事件发起的人道主义援助呼吁（0：否，1：是） |
| declaration      | INTEGER | 联合国是否发布了为该灾害事件的官方声明（0：否，1：是）  |
| aid_contribution | REAL    | 提供给该灾害事件的援助总金额                 |
| dis_mag_value    | REAL    | 该灾害事件的规模或严重程度                   |
| dis_mag_scale    | TEXT    | 灾害事件规模或严重程度的计量标准             |
| latitude         | REAL    | 灾害事件发生地的纬度                         |
| longitude        | REAL    | 灾害事件发生地的经度                         |
| local_time       | TEXT    | 灾害事件发生的当地时间                       |
| river_basin      | TEXT    | 该灾害事件所在的河流流域                     |
| start_year       | INTEGER | 灾害事件开始的年份                           |
| start_month      | INTEGER | 灾害事件开始的月份                           |
| start_day        | INTEGER | 灾害事件开始的日期                           |
| end_year         | INTEGER | 灾害事件结束的年份                           |
| end_month        | INTEGER | 灾害事件结束的月份                           |
| end_day          | INTEGER | 灾害事件结束的日期                           |
| total_deaths     | INTEGER | 该灾害事件导致的总死亡人数                   |
| no_injured       | INTEGER | 该灾害事件导致的受伤人数                     |
| no_affected      | INTEGER | 该灾害事件导致的受影响人数                   |
| no_homeless      | INTEGER | 该灾害事件导致的无家可归的人数               |
| reconstruction_costs_usd | REAL | 灾后重建的总成本，单位为千美元         |
| insured_damages_usd      | REAL | 该灾害事件造成的已投保损失，单位为千美元 |
| total_damages_usd        | REAL | 该灾害事件总共造成的损失，单位为千美元   |
| cpi               | REAL    | 该灾害事件发生时的消费者物价指数             |
| adm_level         | INTEGER | 地理行政区划级别，例如国家、省、市、县等      |
| admin1_code       | TEXT    | 一级行政区划的代码                           |
| admin2_code       | TEXT    | 二级行政区划的代码                           |
| geo_locations     | TEXT    | 该灾害事件的地理位置信息                     |

3.user（用户表）
| 字段名         | 数据类型 | 描述                                       |
|---------------|----------|--------------------------------------------|
| user_id       | INTEGER  | 用户ID，唯一标识一个用户                   |
| user_name     | TEXT     | 用户名称                                   |
| user_level    | INTEGER  | 用户级别，用于表示用户权限等级             |
| login_status  | TEXT     | 登陆状态，例如：1表示已登录、0表示未登录             |
| is_banned     | INTEGER  | 是否封禁，用0表示未封禁，1表示封禁           |

## 安装步骤

1.先在codio上面设置虚拟环境
   ```shell
    python3 -m venv .venv 
    source .venv/bin/activate 
```
2.把库拉下来或者更新
   ```shell
 git clone git@github.com:LucasZhengrui/Enterprise_Software_Dev_Note.git
```
或者

```shell
git pull origin main
```

4.在 mysite setting里面的ALLOWED_HOSTS把自己codio的域名加进去
```shell
ALLOWED_HOSTS = ['127.0.0.1','albumhexagon-canvasgenesis-8000.codio-box.uk']
```
5.执行

```shell
python3 manage.py runserver 0.0.0.0:8000
```
如果报错 看看是什么 有可能是自己没安装django 参考布鲁斯的教程搞一下就行。
**
注意我在项目根目录也就是Enterprise_Software_Dev_Note里创建了 .gitignore 
目的是为了不会把codio上面的虚拟环境目录.venv与python cache传到git上去**

## .gitignore 说明

根目录下的 .gitignore 文件是可以让目录忽略提交到github,所以我添加了

```shell
.venv/
*/__pycache__/
*/*/__pycache__/
__pycache__/
```
为了不让每个人的虚拟环境和python django编译时候产生的缓存跑到github上去


## 开发步骤

1.修改自己功能代码

2.git pull origin main 拉一下别人推的代码，有冲突处理冲突

3.git add --all

4.git commit -m '说一下自己改什么了'

5.git push origin main

# **模块分为:**

## 所有的前端页面-- zhengrui cinwei bangqi wanglei
不要用JS-作业要求
根据自己负责的模块修改

## 公共前端页面 + 导航栏的权限控制-- wanglei
header头，导航栏

## 数据录入模块 -- cinwei(主要) + wanglei(配合设计表)
要求数据录入到数据库要完整精确
prase_csv.py : csv精简数据（3000-7000条），设计数据库，设计表结构， 数据录入脚本

## 仪表盘模块 -- wanglei
打算作为首页，要做的好看一些，各种top10,统计图 
disaster_dashboard： 仪表盘大屏显示，柱状图，饼图，地图，报警 等统计数据

## Ucenter模块-- bangqi
disaster_authen ：1.用户认证 2.登录 3.注册 4.用户列表 5.封禁 6.设置权限 等等。

## 接入open ai模块 --wanglei
disaster_chat ：使用openai服务，进行定制化服务（需求待定）。

## 列表页模块 --wanglei
功能较多 需要展示数据，做分页，做搜索，逻辑删除等
disaster_list ：数据管理：列表页+分页+搜索

## 编辑模块 -- zhengrui
disaster_edit ：数据管理：联表查询+详情页显示+编辑

## 恢复删除模块 -- zhengrui
disaster_trash_list： 用于显示已删除的数据+恢复逻辑删除状态。



## CSV解释

## 1900_2021_DISASTERS.xlsx - emdat data.csv

这些字段包含了关于一个灾害事件的多种信息，下面是各个字段的解释：
这些字段中包含了大量有关灾害事件的信息，这些信息可以用来进行统计和分析，以便更好地理解和预测未来可能发生的自然和人为灾害。

| 字段名              | 描述                                       |
|-------------------|-------------------------------------------|
| Year              | 灾害事件发生的年份。                            |
| Seq               | 灾害事件在该年中的序号。                          |
| Glide             | 灾害事件的全球灾害和应急响应平台 (GLIDE) 编号。       |
| Disaster Group    | 灾害事件的大类别，包括 Natural、Technological 和 Complex。|
| Disaster Subgroup | 灾害事件的子类别，包括 Climatological、Geophysical、Hydrological、Meteorological 和 Biological。|
| Disaster Type     | 灾害事件的类型，例如 Flood、Drought、Earthquake、Epidemic 等。|
| Disaster Subtype  | 灾害事件的子类型，例如 Flash flood、Landslide、Heat wave、Influenza 等。|
| Disaster Subsubtype | 灾害事件的子子类型，例如 Tropical storm、Mudslide、Wildfire、Malaria 等。 |
| Event Name        | 灾害事件的名称或描述。                           |
| Country           | 灾害事件发生的国家或地区。                         |
| ISO               | 该国家或地区的 ISO 3166-1 alpha-3 代码。           |
| Region            | 该国家或地区所属的联合国统计分区。                     |
| Continent         | 该国家或地区所属的洲。                            |
| Location          | 灾害事件发生的具体位置。                          |
| Origin            | 灾害事件的起因或来源。                           |
| Associated Dis    | 与该灾害事件相关的其他灾害事件的 Glide 编号。          |
| Associated Dis2   | 与该灾害事件相关的另一个灾害事件的 Glide 编号。       |
| OFDA Response     | 是否有美国联邦紧急管理署 (OFDA) 参与应对该灾害事件。        |
| Appeal            | 联合国是否发布了为该灾害事件发起的人道主义援助呼吁。           |
| Declaration       | 联合国是否发布了为该灾害事件的官方声明。                |
| Aid Contribution  | 提供给该灾害事件的援助总金额。                       |
| Dis Mag Value     | 该灾害事件的规模或严重程度。                          |
| Dis Mag Scale     | 灾害事件规模或严重程度的计量标准。                       |
| Latitude          | 灾害事件发生地的纬度。                             |
| Longitude         | 灾害事件发生地的经度。                             |
| Local Time        | 灾害事件发生的当地时间。                           |
| River Basin       | 该灾害事件所在的河流流域。                          |
| Start Year        | 灾害事件开始的年份。                             |
| Start Month       | 灾害事件开始的月份。                             |
| Start Day         | 灾害事件开始的日期。 |
| End Year          | 灾害事件结束的年份。 |
| End Month         | 灾害事件结束的月份。 |
| End Day           | 灾害事件结束的日期。 |
| Total Deaths      | 该灾害事件导致的总死亡人数。 |
| No Injured        | 该灾害事件导致的受伤人数。 |
| No Affected       | 该灾害事件导致的受影响人数。 |
| No Homeless       | 该灾害事件导致的无家可归的人数。 |
| Total Affected    | 该灾害事件总共影响到的人数。 |
| Insured Damages ('000 US$) | 该灾害事件造成的已投保损失，单位为千美元。 |
| Total Damages ('000 US$)   | 该灾害事件总共造成的损失，单位为千美元。 |
| CPI               | 该灾害事件发生时的消费者物价指数 (CPI)。 |
| Adm Level         | 地理行政区划级别，例如国家、省、市、县等。 |
| Admin1 Code       | 一级行政区划的代码。 |
| Admin2 Code       | 二级行政区划的代码。 |
| Geo Locations     | 该灾害事件的地理位置信息。 |

## 1970-2021_DISASTERS.xlsx - emdat data.csv
这些字段是关于一次特定的灾害事件的详细信息，下面是各个字段的解释：
这些字段提供了关于一次灾害事件的非常详细的信息，这些信息可以用于监测和预测灾害事件的趋势，并帮助国家和国际组织及时采取行动来减轻灾害的影响。

| 字段名                          | 描述                                         |
| ------------------------------- | -------------------------------------------- |
| Dis No                          | 该灾害事件的唯一编号，通常由年份、序号和国家/地区的 ISO 3166-1 alpha-3 代码组成。 |
| Year                            | 灾害事件发生的年份。                         |
| Seq                             | 该年中该灾害事件的序号。                     |
| Glide                           | 该灾害事件的全球灾害和应急响应平台 (GLIDE) 编号。 |
| Disaster Group                  | 灾害事件的大类别，包括 Natural (自然灾害)、Technological (技术灾害) 和 Complex (复杂灾害)。 |
| Disaster Subgroup               | 灾害事件的子类别，包括 Climatological (气候灾害)、Geophysical (地质灾害)、Hydrological (水文灾害)、Meteorological (气象灾害) 和 Biological (生物灾害)。 |
| Disaster Type                   | 灾害事件的类型，例如 Flood、Drought、Earthquake、Epidemic 等。 |
| Disaster Subtype                | 灾害事件的子类型，例如 Flash flood、Landslide、Heat wave、Influenza 等。 |
| Disaster Subsubtype             | 灾害事件的子子类型，例如 Tropical storm、Mudslide、Wildfire、Malaria 等。 |
| Event Name                      | 灾害事件的名称或描述。                       |
| Country                         | 灾害事件发生的国家或地区。                   |
| ISO                             | 该国家或地区的 ISO 3166-1 alpha-3 代码。      |
| Region                          | 该国家或地区所属的联合国统计分区。             |
| Continent                       | 该国家或地区所属的洲。                       |
| Location                        | 灾害事件发生的具体位置。                     |
| Origin                          | 灾害事件的起因或来源。                       |
| Associated Dis                  | 与该灾害事件相关的其他灾害事件的 Glide 编号。 |
| Associated Dis2                 | 与该灾害事件相关的另一个灾害事件的 Glide 编号。 |
| OFDA Response                   | 是否有美国联邦紧急管理署 (OFDA) 参与应对该灾害事件。 |
| Appeal                          | 联合国是否发布了为该灾害事件发起的人道主义援助呼吁。 |
| Declaration                     | 联合国是否发布了为该灾害事件的官方声明。     |
| Aid Contribution                | 提供给该灾害事件的援助总金额。               |
| Dis Mag Value                   | 该灾害事件的规模或严重程度。                 |
| Dis Mag Scale                   | 灾害事件规模或严
| Latitude                      | 灾害事件发生地的纬度                 |
| Longitude                     | 灾害事件发生地的经度                 |
| Local Time                    | 灾害事件发生的当地时间               |
| River Basin                   | 该灾害事件所在的河流流域             |
| Start Year                    | 灾害事件开始的年份                   |
| Start Month                   | 灾害事件开始的月份                   |
| Start Day                     | 灾害事件开始的日期                   |
| End Year                      | 灾害事件结束的年份                   |
| End Month                     | 灾害事件结束的月份                   |
| End Day                       | 灾害事件结束的日期                   |
| Total Deaths                  | 该灾害事件导致的总死亡人数           |
| No Injured                    | 该灾害事件导致的受伤人数             |
| No Affected                   | 该灾害事件导致的受影响人数           |
| No Homeless                   | 该灾害事件导致的无家可归的人数       |
| Total Affected                | 该灾害事件总共影响到的人数           |
| Reconstruction Costs ('000 US$)| 灾后重建的总成本，单位为千美元     |
| Insured Damages ('000 US$)    | 该灾害事件造成的已投保损失，单位为千美元 |
| Total Damages ('000 US$)      | 该灾害事件总共造成的损失，单位为千美元 |
| CPI                           | 该灾害事件发生时的消费者物价指数     |
| Adm Level                     | 地理行政区划级别，例如国家、省、市、县等 |
| Admin1 Code                   | 一级行政区划的代码                     |
| Admin2 Code                   | 二级行政区划的代码                     |
| Geo Locations                 | 该灾害事件的地理位置信息             |

## Natural Disaster Management

### 1 - About us

Our website application refers of the open source data from https://www.kaggle.com/datasets/brsdincer/all-natural-disasters-19002021-eosdis. This website application allows users to check disaster data with login or without login, which mean that clients can browse as a user or as a guest. And this website application have mutliple views for the database, which would be avaliable for different kind of users.

### 2 - Main features

* View the summary of disaster data
* View the detail of disaster data
* Edit the summary of disaster data
* Archive the data
* Recover the data
* Differert views for the data
* Message system
* User list
* Login and register
* Specific data downloader

### 3 - Installation

3.1 If you are using Codio:

3.1.1 Create a virtual environment in the terminate of Codio
``` shell
    python3 -m venv .venv 
    source .venv/bin/activate 
```

3.1.2 Clone the repository or pull the code from Github
``` shell
    git clone git@github.com:LucasZhengrui/Enterprise_Software_Dev_Note.git
```
Or

``` shell
    git pull origin main
```

3.1.3 Changed the site details in **ALLOWED_HOSTS** of ```mysite/setting.py```

For example:

``` shell
    ALLOWED_HOSTS = ['127.0.0.1','albumhexagon-canvasgenesis-8000.codio-box.uk']
```

3.1.4 Run the website application

``` shell
    python3 manage.py runserver 0.0.0.0:8000
```

P.S **8000** is decided by what did you input in 3.1.3