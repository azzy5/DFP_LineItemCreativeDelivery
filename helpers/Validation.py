# importing all the modules



from random import randint

search_URL ='http://ts-tools.next-staging.ooyala.com/triage_api/v1/search?value='
asset_URL ='http://ts-tools.next-staging.ooyala.com/triage_api/v1/'

'''Returns the accunt information for the given seacrh values
ProviderID, Email, APIKey, Pcode ---> Json obkject with account detials
'''
def getAccountInfo(input):
        account_url = search_URL+input
        response = urllib.urlopen(account_url)
        account_data = json.loads(response.read())
        return account_data


''' Returns the asset detials for the given Embed Pcode
Provider ID AND embedcode --> Json object with Asset get_asset_detials
'''
def getAssetData(input, id):
        asset_url=asset_URL+id+'/assets/'+input+'/'
        response_asset = urllib.urlopen(asset_url)
        asset_data = json.loads(response_asset.read())
        return asset_data


''' input EmbedCode ==>  [is the ifnromation searchable?, accountInfo, AssetInfo]'''

def getData(embedcode):
    accountInfo = getAccountInfo(embedcode)
    if(accountInfo['Status']!=404):
        assetInfo = getAssetData(embedcode,accountInfo['ProviderId'])
        return [True, accountInfo, assetInfo]
    else:
        return [False, None, None]

''' Checks if the search input is a valid or not
If the input is related to the account or an embed code'''
def validateData(input):
        url = search_URL+input
        response = urllib.urlopen(url)
        response = json.loads(response.read())
        if(response['Status']!=404 and response['Status']!=422 ):
            return [True, response]
        else:
            return [False, response]

'''Idenfies if the given input is not a valid embedcode
then this will identify the input type '''
def notAccountInfo(response, input):
    checkList = ['ProviderId', 'Pcode','Name', 'Email', 'APIKey', 'APISecret']
    for item in checkList:
        if response[item] == input:
            return item
    return False


''' returns a random number between 10000 to 9999 '''
def get_random_key():
    return (randint(11111111,99911212))


def check_status(data):
    q =  pyqrcode.create(data)
    q.svg('static/test.svg',module_color='black',scale=20,quiet_zone=4)
    return True


def encrypt_data(data):
    result=''
    #print data
    get_random_key = randint(1,9)
    for i in range(0, len(data) ):
        result = result + chr(ord(data[i]) - get_random_key)
    #result2 = ''
    #for i in range(0, len(result)):
    #    result2 = result2 + chr(ord(result[i]) + 2)
    print result
    return result + str(get_random_key)
