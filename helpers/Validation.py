
from random import randint
from googleads import ad_manager

version = 'v201802'

def getOrderDetails(client, orderID):
    order_service = client.GetService('OrderService', version = version)
    order_statement = (ad_manager.StatementBuilder()
            .Where('id = :orderID')
            .Limit(1)
            .WithBindVariable('orderID', orderID))
    order_response = order_service.getOrdersByStatement(order_statement.ToStatement())
    if 'results' in order_response and len(order_response['results']):
        return order_response['results'][0]
    else :
        print "something went wrong"
        return False

def getLineItemListWithOrder(client, orderID):
    lineItem_service = client.GetService('LineItemService', version = version)
    lineitem_statement = (ad_manager.StatementBuilder()
            .Where('orderId = :order_ID')
            .WithBindVariable('order_ID', orderID))
    lineItem_response = lineItem_service.getLineItemsByStatement(lineitem_statement.ToStatement())
    if 'results' in lineItem_response and len(lineItem_response['results']):
        # for idx,item in enumerate( lineItem_response['results']):
        #     print item['name']
        return lineItem_response['results']
    else :
        print "something went wrong"
        return False

def getLineItemDetails(client, lineitemID):
    lineItem_service = client.GetService('LineItemService', version = version)
    lineitem_statement = (ad_manager.StatementBuilder()
            .Where('id = :lineItemId')
            .Limit(1)
            .WithBindVariable('lineItemId', lineitemID))
    lineItem_response = lineItem_service.getLineItemsByStatement(lineitem_statement.ToStatement())
    if 'results' in lineItem_response and len(lineItem_response['results']):
        return lineItem_response['results'][0]
    else :
        print "something went wrong"
        return False


def getLICAresponse(client,lineitemID):
    # ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
    lica_service = client.GetService('LineItemCreativeAssociationService', version = version)
    lica_statement = (ad_manager.StatementBuilder()
               .Where('lineItemId = :lineItemId')
               .WithBindVariable('lineItemId', lineitemID))
    lica_response = lica_service.getLineItemCreativeAssociationsByStatement(lica_statement.ToStatement())
    creative_list = []
    for idx,item in enumerate( lica_response['results']):
        creative_list.insert(idx,str(item['creativeId']))
    creativeDetialsList = getAllCreativeResponse(client, creative_list )
    if 'results' in lica_response and len(lica_response['results']):
        return [lica_response['results'],creativeDetialsList,]
    else :
        print "something went wrong"
        return False

def getAllCreativeResponse(client,creativeList):
    creative_service = client.GetService('CreativeService', version = version)
    creative_statement = (ad_manager.StatementBuilder()
               .Where('id = :creativeid')
               .WithBindVariable('creativeid', creativeList))
    creative_response = creative_service.getCreativesByStatement(creative_statement.ToStatement())
    if 'results' in creative_response and len(creative_response['results']):
        return creative_response['results']
    else :
        return False

def getLiCaURL(client,lineitemID, creativeID):
    # ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
    lica_service = client.GetService('LineItemCreativeAssociationService', version = version)
    lica_response = lica_service.getPreviewUrl(lineitemID,creativeID,"http://jsbin.com/zasocig")
    #print lica_response
    return lica_response

def ss_take(lica_response):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--test-type")
    driver = webdriver.Chrome(executable_path='/Users/sahmed/Desktop/chromedriver',chrome_options=chrome_options)
    driver.get(lica_response)
    driver.implicitly_wait(10)
    driver.close()
    return None

''' returns a random number between 10000 to 9999 '''
def get_random_key():
    return (randint(1000,9999))
