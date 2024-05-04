

# freesay

Freesay is where you can chat and share freely. 

> lhc：https://github.com/lkdhy
>
> wsh：https://github.com/formula12

## 本项目目录结构

* 前端（基于 Vue）：`frontend` 目录
* 后端（基于 Django）：`backend` 目录
* 一些学习实践的记录：
  * `Vue 学习.md`
  * `django 学习.md`
* 助教 Vue 讲座文件：`env_H班Vue讲解.md`
* 本文件：`README.md`
* 其它：测试、草稿等文件

## 环境配置

### 前端

* IDE：建议使用 WebStorm。如果使用 VSCode，可能要安装一些插件。所以，直接用 WebStorm 打开整个 `freesay` 项目文件夹
* （打开 WebStorm 下的终端）建议用 Windows CMD（即 “Command Prompt”），而不是 “Windows PowerShell”

1. 进入前端目录

   `cd frontend`

2. 检查是否安装了包管理器 npm

   ```cmd
   D:\freesay\frontend>npm --version 
   10.5.0
   ```

3. 用 npm 安装项目依赖

   * 可以打开文件 `package.json` 查看。实际上，`npm install` 应该会安装所有 “dependencies”

   * IDE 界面右下角可能也会跳出来安装提示

   * 命令行输入 `npm install` 安装项目依赖

     ```cmd
     D:\freesay\frontend>npm install
     npm WARN deprecated @types/vue@2.0.0: This is a stub types definition for vuejs (https://github.com/vuejs/vue). vuejs provides its own type definitions, so you don't need @types/vu
     e installed!
     
     added 100 packages, and audited 101 packages in 25s
     
     15 packages are looking for funding
       run `npm fund` for details
     
     found 0 vulnerabilities
     
     ```

4. 运行项目

   ```cmd
   D:\freesay\frontend>npm run dev
   
   > vue-project@0.0.0 dev
   > vite
   
   
     VITE v5.2.8  ready in 509 ms
   
     ➜  Local:   http://localhost:5173/
     ➜  Network: use --host to expose
     ➜  press h + enter to show help
   
   ```

   此时，浏览器输入 http://localhost:5173/ 即可。

   * 界面：登录界面
   * “你的用户名” 一栏有默认值 “小明还是小红...”

### 后端

没写数据库，没啥别的。

看一下 `views.py` 和 `urls.py` 的内容，即可。

*注意：`views.py` 用到了 Python 的  `json` 包，因此，需要确保安装了 `json`*

* 启动后端服务器（都懂的）：

  ```cmd
  D:\freesay\backend>python manage.py runserver
  ```

### 登录过程（前后端交互）

在前端的登录界面（打开调试控制台）

有以下两个尝试：

1. 填用户名，但密码不填，点击登录，观察弹出的信息和调试控制台
2. 用户名和密码都随便填，点击登录，观察弹出的信息和调试控制台

OK！

---



## 功能与创新性

freesay 将被设计成一个基于提问箱的社交网站，支持 “公有墙” 与每个人的 “私有墙”。

### 概述

- 注册登录

  用户需要注册账号，登录使用

- 创建提问箱
  - 用户可编辑提问箱主题，生成提问箱链接分享到广场或朋友圈
  - 同时，可以选择一些 *tag*，表示目前希望收到这些类别的问题
  
- 发布提问帖
  - 由分享的链接或在用户主页进入他的提问箱，发布提问帖，可设置帖子为公开还是私密，以及自己匿名还是实名
  - 标记上问题的 *tag*
  
- 回复帖子
  - 箱子主人回复帖子，并可选择将此回复变为公开或私密
  - 支持 *thread*，即提问者和被提问者持续进行互动
  
- 每日 “表白墙”
  - 一个 “公有墙”，每天刷新，内容均公开，但可选择匿名还是实名
  - 支持 *thread*
  
- “个人墙” 的分类搜索

  浏览用户的 “个人墙“ 时，选择某一 *tag* 筛选相关问答贴

- 私信聊天
  
  与好友一对一聊天

### 创新性

#### 提问时的常见问题推荐

在提问界面，提供一些常见问题，可给提问者带来便利和 “灵感”。

> 假期做什么来打发时间？
> 喜欢看什么样的电影？
> 你现在是单身吗？

#### 标签及相关功能

* [*free*]
* [学习]、[恋爱]、[生活]、[二次元] ……

##### 提问箱附带标签

发提问箱的人愿意和他人交流，但其未必乐意看到所有类型的问题，因而最终可能为避免某些尴尬而不发提问箱。

所以考虑给发提问箱的用户提供选择一些 tag 的功能，表示目前希望收到这些类别的问题。

##### “个人墙” 的分类搜索

为用户通过个人墙了解他人的需求提供便利。
