try:
    import sys
except ImportError:
     print ('sys : Module not found.  ')
try:
    import os
except ImportError:
     print ('os : Module not found')
try:
    from flask import *
except ImportError:
    print ('flask : Module not found')

try:
    import json
except ImportError:
  print'  json : library not found.  '
  print ('flask : Module not found')

try:
    import requests
except ImportError:
  print'  requests : library not found.  '

try:
    import urllib
except ImportError:
  print'  urllib : library not found.  '

sys.path.append('./helpers')

from utils import *
from Validation import *
from FormsCheck import *

app = Flask(__name__)
app.secret_key = 'Let it be a secrete'

''' The index page should only have the Search bar and the search button '''
@app.route("/",methods=['GET', 'POST'])
def index():
    form = EmbedSearch(request.form)
    return render_template('index.html',form = form)

''' /string page should do the following

'''
@app.route("/<string:search>",methods=['GET', 'POST'])
def searchEmbed(search):
    form = EmbedSearch(request.form)
    return render_template('index.html',form = form)

if __name__ == '__main__':
    app.run(debug=True)
