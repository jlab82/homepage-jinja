#!/usr/bin/env python
import os
import jinja2
import webapp2
import time


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")

class AboutHandler(BaseHandler):
    def get(self):
        fecha = time.strftime("%X")
        params = {"fecha": fecha}
        return self.render_template("about_me.html", params=params)

class MyProjectsHandler(BaseHandler):
    def get(self):
        return self.render_template("my_projects.html")

class BlogHandler(BlogHandler):
    def get(self):
        return self.render_template("blog.html")

class ContactHandler(ContactHandler):
    def get(self):
        return self.render_template("contact.html")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/about', AboutHandler),
    webapp2.Route('/my-projects', MyProjectsHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/contact', ContactHandler),

], debug=True)
