# freesay _ 0524周五

## 距离 “移动互联网” 课程项目汇报还有 *10* 天

## 基本战略

1. ==持续推进、积少成多==
2. ==以尽早完成[要实现的功能](#功能与创新性)为导向==，先组织前端组件、设计逻辑、实现功能，最后进行美化
3. 先搞***标签、提问推荐、公有墙***等等，**完全不搞回复 *thread* 和私聊**（也*暂时不搞*用户头像设置等细节）
4. 最后尽量搞回复 *thread* 和私聊

## 下一步计划

- [x] ~~0505周日晚 21:35 （已删除）~~；~~0514周二晚（已完成）~~；~~0520 周中（已完成）~~

- [ ] 0524 周末

  > 完成了可以前面打✔
  >
  > ~~一些内容具体见：（*Ctrl+单击* 去往） [数据库设计与前后端交互接口说明.md](./数据库设计与前后端交互接口说明.md)（或：Typora 左边导航栏中点击打开）~~~

  【后端】

  - [ ] **实现请求：**名为 `username` 的人设置（或 “修改”）个性签名：`\setsignature`，POST 方法，数据 `{username: string, signature: string}`

  - [ ] `post` 表格增加==提问者 “是否匿名” 的 boolean 属性 `is_anonymous`==

    - [ ] 所有涉及问答帖的数据交互全都要考虑 `is_anonymous` 这个属性，比如 `/post` 和 `/getpost` 、`/gethostpost` 请求

      > 此处，有需要则进行讨论

  - [ ] 关于标签，**实现请求：**提问者*提问的同时，给帖子打标签*。

    `/post` 请求会附带一个数组 `tags[string] = [tag1, tag2, ... tagk]`，需要以此更新 `tag` 表和 `with_tag` 表

  - [ ] （基于这些东西，完成 ER 图、关系模式设计，兼数据库 PJ 首次提交作业）

  - [ ] 收集并筛选出 10个左右的 ”提问时的常见问题推荐“ 给前端（纯静态内容，和后端、数据库无关）

  【前端】

  - [ ] 实施与后端对应的新增内容
  - [ ] 调研所需组件、并用好的方法组织组件
  - [ ] ………………

---

Freesay is where you can chat and share freely. 

> lhc：https://github.com/lkdhy
>
> wsh：https://github.com/formula12

此图略，<img src="A.PNG" alt="此图略" style="zoom: 50%;">

## 本项目目录结构

* 前端（基于 Vue）：`frontend` 目录
* 后端（基于 Django）：`backend` 目录
* 一些学习实践的记录：
  * `Vue 学习.md`
  * `django 学习.md`
* 助教 Vue 讲座文件：`env_H班Vue讲解.md`
* 本文件：`README.md`
* 其它：测试、草稿等文件

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