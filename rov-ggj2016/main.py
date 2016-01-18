
import os 
import logging

import jinja2
import webapp2

logging.debug('######## Start up application!')

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)

class MainPage(BaseHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write('Hello, World!')
        #template = JINJA_ENVIRONMENT.get_template('test.html')
        template = JINJA_ENVIRONMENT.get_template('public/index.html')
        self.response.write(template.render())

class TestPage(BaseHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('test.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/test', TestPage)
], debug=True)

