
from random import randint
from googleads import ad_manager

version = 'v201802'
def getLineItemResponse(lineitemID):
    ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
    lineItem_service = ad_manager_client.GetService('LineItemService', version = version)
    lineitem_statement = (ad_manager.StatementBuilder()
            .Where('lineItemId = :lineItemId')
            .WithBindVariable('lineItemId', lineitemID))
    lineItem_response = lineItem_service.getLineItemsByStatement(lineitem_statement.ToStatement())
    if 'results' in lineItem_response and len(lineItem_response['results']):
        print "Line Item Details : " + str(lineItem_response)
        return lineItem_response
    else :
        print "something went wrong"
        return False


def getCreativeResponse(client, creativeID):
    creative_service = client.GetService('CreativeService', version = version)
    creative_statement = (ad_manager.StatementBuilder()
               .Where('creativeType = :id')
               .WithBindVariable('id', creativeID))
    creative_response = creative_service.getLineItemsByStatement(creative_statement.ToStatement())
    if 'results' in creative_response and len(creative_response['results']):
        print "Creative details : " + str(creative_response)
        return creative_response
    else :
        print "something went wrong"
        return False

def getLICAresponse(lineitemID):
    lica_service = client.GetService('LineItemCreativeAssociationService', version = version)
    lica_statement = (ad_manager.StatementBuilder()
               .Where('lineItemId = :lineItemId')
               .WithBindVariable('lineItemId', lineitemID))
    lica_response = lica_service.getLineItemsByStatement(lica_statement.ToStatement())
    if 'results' in lica_response and len(lica_response['results']):
        print "  LICA details Details : " + str(lica_response)
        return lica_response
    else :
        print "something went wrong"
        return False

''' returns a random number between 10000 to 9999 '''
def get_random_key():
    return (randint(1000,9999))
