## Django 学习

Django和PyMySQL是两个不同的工具，但可以一起使用来构建和管理数据库驱动的Web应用程序。

Django是一个高级Python Web框架，可以让开发者快速创建复杂的、数据库驱动的网站。它强调代码重用性、可插拔性、快速开发和DRY原则（Don't Repeat Yourself）。Django内置了一个对象关系映射器（ORM），可以使用Python代码对数据库进行操作，无需编写SQL语句。

PyMySQL，顾名思义，是一个Python MySQL客户端库，它允许Python程序直接连接MySQL数据库，并执行SQL语句进行操作。PyMySQL可以被看作是连接Python和MySQL的桥梁。

### 数据库迁移与同步

**假设我和朋友共同开发基于django连接mysql的项目，显然我们在调试过程中会向数据库加入数据。我们是不是可以利用django的数据库迁移同步我们的数据库的内容，包括所有数据**

不完全正确。Django的数据库迁移功能主要用于同步数据库的结构，即你的模型的改变，比如增加字段，删除字段，更改字段类型等。这些改变会被Django记录并生成迁移文件，然后通过迁移命令应用到数据库上，使数据库的结构与你的模型保持一致。

然而，Django的数据库迁移并不包括数据的同步。也就是说，你在一个环境中（比如开发环境）向数据库中添加的数据，并不会因为数据库迁移而自动出现在另一个环境中（比如生产环境）。你需要自己手动导入或者通过其它方式同步数据。

如果你想要同步数据，可以考虑使用Django的数据导出（dumpdata）和导入（loaddata）命令，或者直接使用数据库的备份和恢复功能。

> 是的，你可以利用Django的数据库迁移功能来同步你们的数据库内容，包括所有数据。数据库迁移是Django的一个强大特性，它允许你通过定义数据库模型的变化来自动更新数据库结构。
>
> 当你的数据库模型发生变化时，你可以运行以下命令来生成迁移文件：
>
> python manage.py makemigrations
>
> 然后，你可以运行以下命令来应用这些迁移文件，将数据库结构同步到最新的模型定义：
>
> python manage.py migrate
>
> 这样，你们的数据库结构就会被更新，同时保留现有的数据。
>
> 注意，当你修改了数据库模型后，你需要重新运行makemigrations命令来生成新的迁移文件，并且再次运行migrate命令来应用这些迁移文件。这样可以确保你的数据库和模型定义保持同步。
>
> 另外，如果你们需要在调试过程中向数据库添加数据，你可以使用Django的数据迁移文件来进行初始化数据的添加。你可以在迁移文件中使用RunPython命令来编写自定义的Python代码来插入初始数据。
>
> 希望这个回答对你有帮助，如果你还有其他问题，请随时提问。

**`Forbidden (Origin checking failed - [http://localhost:5173](http://localhost:5173/) does not match any trusted origins.): /polls/login`**

> This error message means that the origin of the request, in this case [http://localhost:5173](http://localhost:5173/), is not listed as a trusted origin in the server's configuration.
>
> In the context of CORS (Cross-Origin Resource Sharing), the origin is the domain that is making the request. The server checks this against a list of domains that it trusts. If the origin is not in the list, it blocks the request for security reasons.
>
> To fix this issue, you need to add [http://localhost:5173](http://localhost:5173/) to the list of trusted origins in the server's configuration. The process to do this will depend on the server you are using.
>
> For example, if you are using Django, you can add the origin to the CORS_ORIGIN_WHITELIST setting in your settings.py file:
>
> CORS_ORIGIN_WHITELIST = ( '[http://localhost:5173](http://localhost:5173/)', )
>
> After adding the origin to the whitelist, you should restart your server for the changes to take effect.
>
> Remember that you should only add origins that you trust, as they will be able to make requests to your server. If you add an untrusted origin, it could potentially make malicious requests to your server.

**前端的POST方法给用django写的后端一个 json 对象，但是后端似乎没有读到这个 JSON，请问，哪里出问题了？**

> 问题可能在于Django处理POST JSON数据的方式。在Django中，如果前端发送的是JSON格式的数据，那么不能直接通过`request.POST`获取数据，而需要通过`request.body`获取到数据后转换成JSON。
>
> 可以尝试以下代码：
>
> ```typescript
> import json
> def login(request):
>     data = json.loads(request.body)
>     username = data.get('username', 'jj')
>     password = data.get('password', 'kk')
>     print(username)
>     print(password)
>     return JsonResponse({
>         'success': True,
>         'messsage': '恭喜！登陆成功~',
>         'username': username,
>         'password': password
>     })
> ```
>
> 这样你就可以从前端发送的JSON数据中获取到username和password。注意此处`request.body`获取到的是一个byte类型的数据，需要使用`json.loads()`将其转换为字典后才能使用。

**简述通过django作为后端并连接的数据库的可行性与优势**

Django是一个高级Python Web框架，它可以快速开发高质量的Web应用程序。使用Django作为后端并连接数据库的可行性和优势表现在以下几个方面：

1. 易用性：Django框架的设计目标是使得开发复杂的数据库驱动的网站变得简单。它提供了大量的实用工具和功能，让开发者可以专注于编写应用程序，而不是重复造轮子。
2. 强大的ORM：Django有一个强大的对象关系映射（ORM），它可以支持大多数主流的数据库系统，如MySQL、PostgreSQL、SQLite等。通过ORM，开发者可以用Python代码操作数据库，而无需编写SQL语句。
3. 安全性：Django提供了一系列的安全功能，包括防止跨站脚本（XSS）、跨站请求伪造（CSRF）和SQL注入攻击等。这使得使用Django开发的网站具有较高的安全性。
4. 易于扩展：Django有一个模块化的设计，可以很容易地添加和扩展功能。它还有一个活跃的社区，提供了大量的第三方应用和插件。
5. DRY原则：Django遵循“DRY”（Don't Repeat Yourself）原则，这意味着每一段代码在整个项目中只应该被定义一次。这使得代码更易于维护，更少出错。
6. 优秀的文档：Django有非常全面和详细的文档，这对于开发者学习和使用Django非常有帮助。

总的来说，通过Django作为后端并连接数据库的方式，可以大大简化和加速Web开发过程，提高开发效率，同时也能保证应用的安全性和健壮性。





Let’s look at what [`startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject) created:

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

These files are:

- The outer `mysite/` root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
- `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about `manage.py` in [django-admin and manage.py](https://docs.djangoproject.com/en/5.0/ref/django-admin/).
- The inner `mysite/` directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. `mysite.urls`).
- `mysite/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) in the official Python docs.
- `mysite/settings.py`: Settings/configuration for this Django project. [Django settings](https://docs.djangoproject.com/en/5.0/topics/settings/) will tell you all about how settings work.
- `mysite/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in [URL dispatcher](https://docs.djangoproject.com/en/5.0/topics/http/urls/).
- `mysite/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See [How to deploy with ASGI](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/) for more details.
- `mysite/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/) for more details.

The [`path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path) function is passed four arguments, two required: `route` and `view`, and two optional: `kwargs`, and `name`. At this point, it’s worth reviewing what these arguments are for.



 [`path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path) argument: `route`[¶](https://docs.djangoproject.com/en/5.0/intro/tutorial01/#path-argument-route)

`route` is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in `urlpatterns` and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches.

Patterns don’t search GET and POST parameters, or the domain name. For example, in a request to `https://www.example.com/myapp/`, the URLconf will look for `myapp/`. In a request to `https://www.example.com/myapp/?page=3`, the URLconf will also look for `myapp/`.



 [`path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path) argument: `view`[¶](https://docs.djangoproject.com/en/5.0/intro/tutorial01/#path-argument-view)

When Django finds a matching pattern, it calls the specified view function with an [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest) object as the first argument and any “captured” values from the route as keyword arguments. We’ll give an example of this in a bit.



 [`path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path) argument: `kwargs`[¶](https://docs.djangoproject.com/en/5.0/intro/tutorial01/#path-argument-kwargs)

Arbitrary keyword arguments can be passed in a dictionary to the target view. We aren’t going to use this feature of Django in the tutorial.



 [`path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path) argument: `name`[¶](https://docs.djangoproject.com/en/5.0/intro/tutorial01/#path-argument-name)

Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.

When you’re comfortable with the basic request and response flow, read [part 2 of this tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial02/) to start working with the database.



---

 数据库

**SQLite和Python的关系**

SQLite是一种轻型的数据库，是一种轻型的事务处理数据库，被广泛应用在各种环境中。Python是一种解释型、面向对象、动态数据类型的高级程序设计语言。

SQLite和Python的关系在于：Python提供了对SQLite的支持，使得在Python程序中能够很方便地使用SQLite数据库。

Python标准库中的sqlite3模块就是对SQLite的封装，使得在Python程序中可以直接使用SQLite数据库，而无需安装任何其他的库或驱动。这使得Python程序可以很方便地进行本地的数据存储和处理。

通过Python操作SQLite，可以进行数据库的创建、表的增删改查、数据的增删改查等操作。同时，也可以利用Python的强大功能，对SQLite数据库进行各种高级的操作，例如数据分析、数据挖掘等。