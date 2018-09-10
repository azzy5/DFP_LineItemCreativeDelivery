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


# 1. Read Order ID from Search Bar
# 2. Get order details and line item Details with the Lineitem and Order services (object --> data['order',['lineitems']])
# 3. Render the page with page with order details & list of line item and details

''' /string page should do the following '''
@app.route("/search",methods=['GET', 'POST'])
def searchOrder():
    form = EmbedSearch(request.form)
    inputFromPage = str(request.form['lineItemId']).replace(" ","")
    orderDetials = getOrderDetails(client, inputFromPage)
    if  not orderDetials:
        return render_template('somthing_wrong.html',form = form)
    #orderDetials =order_dummy
    lineitem_list = getLineItemListWithOrder(client, inputFromPage)
    #lineitem_list =lineitems_dummy

    return render_template('order_template.html',form = form, data= [orderDetials,lineitem_list])


#1. read line item ID from Form
#2. Get line item Details and creatives details associated with the line lineItemId
#3. infalte the page with line item creative details also inflate the form to read
''' /lineitem page should do the following '''
@app.route("/lica_",methods=['GET', 'POST'])
def doLiCa():
    form = EmbedSearch(request.form)
    inputFromPage = request.form['li_id']
    lineItemdata = getLineItemDetails(client, inputFromPage)
    creative_listdata = getLICAresponse(client, inputFromPage)
    #lineItemdata = lineItemdata_dummy
    #licadata = creative_list_dummy[0]
    #creative_listdata = creative_list_dummy
    #print creative_listdata
    if lineItemdata:
        return render_template('lineitem_template.html',form = form, data=[lineItemdata, creative_listdata])
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
    if request.form['preview'] == 'screenshot':
        print "btn - screenshot"
    elif request.form['preview'] =='preview':
        return redirect(getLiCaURL(client, lineitem_,creative_),code=302)
    return render_template('preview.html',form = form, data=[None, None])

if __name__ == '__main__':
    app.run(debug=True)
