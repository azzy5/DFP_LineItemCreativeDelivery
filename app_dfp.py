#!/usr/bin/env python
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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
        return order_response['results']
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

def getLineItemListWithOrder(client, orderID):
    lineItem_service = client.GetService('LineItemService', version = version)
    lineitem_statement = (ad_manager.StatementBuilder()
            .Where('orderId = :order_ID')
            .WithBindVariable('order_ID', orderID))
    lineItem_response = lineItem_service.getLineItemsByStatement(lineitem_statement.ToStatement())
    if 'results' in lineItem_response and len(lineItem_response['results']):
        for idx,item in enumerate( lineItem_response['results']):
            print item['name']
        return lineItem_response['results']
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
        return [lica_response['results'],creativeDetialsList]
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

def getCreativesdetails(client, creativeID):

    creative_service = client.GetService('CreativeService', version = version)
    creative_statement = (ad_manager.StatementBuilder()
               .Where('id = :creativeid')
               .WithBindVariable('creativeid', creativeID))
    creative_response = creative_service.getCreativesByStatement(creative_statement.ToStatement())
    #print "Creative details : " + str(creative_response)
    if 'results' in creative_response and len(creative_response['results']):
        return creative_response['results'][0]
    else :
        return False





if __name__ == '__main__':
  # Initialize client object.
  client = ad_manager.AdManagerClient.LoadFromStorage()
  #print getAllCreativeResponse(client,[47762031781, 47762033101])
  #print getLineItemDetails(client, '397756981')
  print getLICAresponse(client, '378634861')
#Steps
