# importing all the modules
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
  print 'json : library not found'

try:
    import requests
except ImportError:
  print 'requests : library not found'

try:
    import urllib
except ImportError:
  print'urllib : library not found'

try:
    import io
except ImportError:
  print'io : library not found'

sys.path.append('./helpers')

from utils import *
from Validation import *
from FormsCheck import *

app = Flask(__name__)
client = ad_manager.AdManagerClient.LoadFromStorage()
app.secret_key = 'Let it be a secrete'

''' The index page should only have the Search bar and the search button '''
@app.route("/",methods=['GET', 'POST'])
def index():
    form = EmbedSearch(request.form)
    return render_template('index.html',form = form)

''' /string page should do the following '''
@app.route("/search",methods=['GET', 'POST'])
def searchOrder():
    form = EmbedSearch(request.form)
    inputFromPage = str(request.form['lineItemId']).replace(" ","")
    orderDetials = getOrderDetails(client, inputFromPage)
    print orderDetials
    lineitem_list = getLineItemListWithOrder(client, inputFromPage)
    return render_template('order_template.html',form = form, data= [orderDetials,lineitem_list])

''' /lineitem page should do the following '''
@app.route("/lica_",methods=['GET', 'POST'])
def doLiCa():
    form = EmbedSearch(request.form)
    inputFromPage = request.form['li_id']
    lineItemdata = getLineItemResponse(client, inputFromPage)
    licadata = getLICAresponse(client, inputFromPage)
    # lineItemdata = lineItemdata_dummy
    # licadata = licadata_dummy
    #print lineItemdata
    if lineItemdata:
        return render_template('lineitem_template.html',form = form, data=[lineItemdata, licadata])
    else:
        return render_template('somthing_wrong.html')

@app.route("/generatePreviewURL",methods=['GET', 'POST'])
def createPreview():
    form = EmbedSearch(request.form)
    index = request.form['r_id']
    previewURL = request.form['previewURL']
    lineitem_ = request.form['li_'+index]
    creative_ = request.form['cr_'+index]
    print lineitem_ + " , " + creative_ + " , " +index + " , " +previewURL
    return render_template('preview.html')


if __name__ == '__main__':
    app.run(debug=True)
