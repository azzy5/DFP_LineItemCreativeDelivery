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
        print order_response['results'][0]
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




def getCreativesdetails(client, creativeID):

    creative_service = client.GetService('CreativeService', version = version)
    creative_statement = (ad_manager.StatementBuilder()
               .Where('id = :creativeid')
               .Limit(1)
               .WithBindVariable('creativeid', creativeID))
    creative_response = creative_service.getCreativesByStatement(creative_statement.ToStatement())
    #print "Creative details : " + str(creative_response)
    if 'results' in creative_response and len(creative_response['results']):
        return creative_response['results'][0]
    else :
        return False

def getLICAresponse(client,lineitemID):
    # ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
    lica_service = client.GetService('LineItemCreativeAssociationService', version = version)
    lica_statement = (ad_manager.StatementBuilder()
               .Where('lineItemId = :lineItemId')
               .WithBindVariable('lineItemId', lineitemID))
    lica_response = lica_service.getLineItemCreativeAssociationsByStatement(lica_statement.ToStatement())
    if 'results' in lica_response and len(lica_response['results']):
        return lica_response
    else :
        print "something went wrong"
        return False

def getAllCreativeResponse(client):
    creative_service = client.GetService('CreativeService', version = version)
    creative_statement = (ad_manager.StatementBuilder()
               .Where('id = :creativeid')
               .WithBindVariable('creativeid', ['138236007035','138235934673','138206449211']))
    creative_response = creative_service.getCreativesByStatement(creative_statement.ToStatement())
    #print "Creative details : " + str(creative_response)
    if 'results' in creative_response and len(creative_response['results']):
        return creative_response['results']
    else :
        return False
