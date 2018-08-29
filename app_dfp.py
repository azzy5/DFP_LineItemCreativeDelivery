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
"""This example gets all creatives.
"""

# Import appropriate modules from the client library.
from googleads import ad_manager
version = 'v201802'
line_item_id = '113197741'
creativeID = ''

def main(client):
  # Initialize appropriate services.
    lica_service = client.GetService('LineItemCreativeAssociationService', version = version)
    lineItem_service = client.GetService('LineItemService', version = version)
    creative_service = client.GetService('CreativeService', version = version)

  # Create a statement to select creatives.
    lica_statement = (ad_manager.StatementBuilder()
               .Where('lineItemId = :lineItemId')
               .WithBindVariable('lineItemId', line_item_id))

    lineitem_statement = (ad_manager.StatementBuilder()
               .Where('lineItemId = :lineItemId')
               .WithBindVariable('lineItemId', line_item_id))

    creative_statement = (ad_manager.StatementBuilder()
               .Where('creativeType = :id')
               .WithBindVariable('id', creativeID))


    lica_response = lica_service.getLineItemCreativeAssociationsByStatement(lica_statement.ToStatement())
    linetem_response = lineItem_service.getLineItemsByStatement(lineitem_statement.ToStatement())

    if 'results' in lica_response and len(lica_response['results']):
        print str(lica_response) + " \n\n\n\ Line Item Details" + str(linetem_response)
    else :
        print "something went wrong"
if __name__ == '__main__':
  # Initialize client object.
  ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
  main(ad_manager_client)
