## 西班牙签证位置监听 (base英国)
### 一、简介
项目是基于 [one-focus/visa-spain](https://github.com/one-focus/visa-spain) 改的，抽出了关键代码，针对英国的BLS的网站改了一下。请不要拿来用作盈利用途，否则会追究责任。

在python3.6 + macOS Catalina上运行成功，没在别的环境上做过测试。

#### 功能
如果放了签证预约空位，会收到机器人的短信。目前只通知日期，不会精确到小时，但个人用途足矣。


### 二、文件介绍
```text
.
├── monitor.py         # starter
├── visa.py            # modify xpath for UK BLS
├── utils
│   ├── basic.py       
│   ├── config.py      # configuration, you have to change this file!
│   ├── decorators.py
│   └── log.py
├── requirements.txt   # pip install -r requirements.txt
└── readme.md
```

### 三、运行
1. 安装依赖
    ```shell
    pip install -r requirements.txt
    ```
2. 修改config.py

    ```
    根据自己账号与登录页面地址修改config.py里的内容：
    OPENED_PAGE
    EMAIL
    PASSWORD
    ```
3. 修改接受短信手机号 

  ```
  monitor.py
  在这一行里修改成相应接收短信的手机号https://github.com/qingshan-zhang/spain-visa/blob/main/monitor.py#L42 
  (optional)另，在test_notify里也有手机号待修改，如在运行前需要测试短信接收可修改这个function里的内容.
  ```

3. 运行
    ```shell
    python3 monitor.py
    ```
    机器人会先测试通知可达，之后有slot的话才会发通知给你。
