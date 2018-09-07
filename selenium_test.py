
from selenium import webdriver
from googleads import ad_manager

version = 'v201802'

def getLICAresponse(client,lineitemID, creativeID):
    # ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
    lica_service = client.GetService('LineItemCreativeAssociationService', version = version)
    lica_response = lica_service.getPreviewUrl(lineitemID,creativeID,"http://output.jsbin.com/kavobal/")
    #print lica_response


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    
    driver = webdriver.Chrome(executable_path='/Users/sahmed/Desktop/chromedriver',chrome_options=chrome_options)
    driver.get(lica_response)
    driver.implicitly_wait(10)
    # options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument("--test-type")
    # options.executable_path ="/Users/sahmed/Desktop/chromedriver"
    # driver = webdriver.Chrome(options)
    #
    # driver.get(lica_response)
    # driver.implicitly_wait(10)
    # driver.save_screenshot(lineitemID+"_"+creativeID+".png")
    driver.close()
    return None


if __name__ == '__main__':
  # Initialize client object.
  ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
  getLICAresponse(ad_manager_client, '4789971322', '138243382365')
