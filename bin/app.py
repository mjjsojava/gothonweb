#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-14 20:16:04
# @Author  : 马俊杰 (mjjsojava@163.com)
# @Link    :

import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/',base = "layout")

class Index:
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet = "Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)

if __name__ == '__main__':
    app.run()
