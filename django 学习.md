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