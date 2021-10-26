# **Py自动化框架**

## 框架介绍

- 框架分两大块,业务逻辑处理,以及公共方法
- 业务模块:主要负责业务的处理(测试用例的编写),框架支持并发执行,故用例编写有特定要求
    - 业务模块包括（元素定位，元素操作和测试用例）
- 公共包:主要负责常用方法的封装,减少代码冗余,提高代码维护性（失败截图和日志记录后续封装）

## 公共包主要结构

- allure报告生成相关方法
- selenium相关请求方法
- 数据库驱动相关方法
- 测试数据构造,异常用例生成
- 数据提取,对比验证
- 脚本运行方式

## 框架结构

```
├─base         		 		selenium基础操作方法
│  │ 
│  ├─ base_object    		webdriver操作
│  │ 
│  ├─ base _util            初始化driver
│ 
├─common         	    	公共方法
│  │ 
│  ├─ allure                allure方法
│  │ 
│  ├─ yaml             		yaml处理
│  │ 
│  ├─ .....                 .....
│ 
├─page_object              	元素定位、操作
│ 
├─report			        allure报告
│
├─test_case      			测试用例
│
├─pytest.ini      			pytest执行参数设置
│ 
│─ .....                 .....
└─run.py          			入口

```

# [使用]() 

##  环境准备

 安装相关第三方库

- pip install -r requirements.txt 
- chromedriver设置环境变量