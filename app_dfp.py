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
lineitemID = '114239941'
creativeID = ''

def main(client):
    lineItem_service = client.GetService('LineItemService', version = version)
    # Create a statement to select creatives.
    lineitem_statement = (ad_manager.StatementBuilder()
             .Where('lineItemId = :lineItemId')
             .WithBindVariable('lineItemId', lineitemID))
     # lica_response = lica_service.getLineItemCreativeAssociationsByStatement(lica_statement.ToStatement())
    lineItem_response = lineItem_service.getLineItemsByStatement(lineitem_statement.ToStatement())
    if 'results' in lineItem_response and len(lineItem_response['results']):
        print "Line Item Details : " + str(lineItem_response)
        return lineItem_response
    else :
        print "something went wrong"
        return False

        # Create a statement to select creatives.

if __name__ == '__main__':
  # Initialize client object.
  ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
  main(ad_manager_client)
