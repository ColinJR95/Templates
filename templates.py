import os 
import webapp2
import jinja2

 

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
                        
form_html = """ 
<form>
<h2>Add a food</h2>
<input type="text" name="food">
%s
<button>Add</button>
</form>
"""


class Handler(webapp2.RequestHandler): 
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **parms):
        t = jinja_env.get_template(template)
        return t.render(parms)

    def render(self, template, **kw):
        self.write(self.render_str(template,**kw))
        
class MainPage(Handler):
    def get(self):
       
        items = self.request.get_all("food")
        self.render('shopping_list.html', items = items)
       
#         
        #self.write(output)
        
        
class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n', 0)
        n = n and int(n)
        self.render('fizzbuzz.html', n = n)
        
app = webapp2.WSGIApplication([('/',MainPage),
                               ('/fizzbuzz', FizzBuzzHandler),
                               ],
                               debug=True)