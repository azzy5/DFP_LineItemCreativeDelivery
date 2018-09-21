
import sys
import os
import time
from PIL import Image
from selenium import webdriver

def fullpage_screenshot(driver, file):
    print("Starting chrome full page screenshot workaround ...")

    total_width =600+ driver.execute_script("return document.body.offsetWidth")
    total_height = 150+driver.execute_script("return document.body.parentNode.scrollHeight")
    viewport_width =600+ driver.execute_script("return document.body.clientWidth")
    viewport_height = 150+driver.execute_script("return window.innerHeight")
    print("Total: ({0}, {1}), Viewport: ({2},{3})".format(total_width, total_height,viewport_width,viewport_height))
    rectangles = []

    i = 0
    while i < total_height:
        ii = 0
        top_height = i + viewport_height

        if top_height > total_height:
            top_height = total_height

        while ii < total_width:
            top_width = ii + viewport_width

            if top_width > total_width:
                top_width = total_width

            print("Appending rectangle ({0},{1},{2},{3})".format(ii, i, top_width, top_height))
            rectangles.append((ii, i, top_width,top_height))

            ii = ii + viewport_width

        i = i + viewport_height

    stitched_image = Image.new('RGB', (total_width, total_height))
    previous = None
    part = 0

    for rectangle in rectangles:
        if not previous is None:
            driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
            print("Scrolled To ({0},{1})".format(rectangle[0], rectangle[1]))
            time.sleep(0.5)


        file_name = "part_{0}.png".format(part)
        print("Capturing {0} ...".format(file_name))

        driver.get_screenshot_as_file(file_name)
        screenshot = Image.open(file_name)

        if rectangle[1] + viewport_height > total_height:
            offset = (rectangle[0],  total_height - viewport_height)
        else:
            offset = (rectangle[0], rectangle[1])

        print("Adding to stitched image with offset ({0}, {1})".format(offset[0],offset[1]))
        stitched_image.paste(screenshot, offset)

        del screenshot
        os.remove(file_name)
        part = part + 1
        previous = rectangle

    stitched_image.save(file)
    print("Finishing chrome full page screenshot workaround...")
    return True

if __name__ == '__main__':
  # Initialize client object.
  options = webdriver.ChromeOptions()
  options.add_argument("--start-maximized")
  driver = webdriver.Chrome(executable_path='/Users/sahmed/Desktop/chromedriver',chrome_options=options)
  #driver.set_window_size(200+driver.execute_script("return document.body.offsetWidth"),150+driver.execute_script("return document.body.parentNode.scrollHeight"))
  driver.get('https://bbc.com/')
  fullpage_screenshot(driver, "test1236.png")
  driver.quit()
#
# version = 'v201802'
#
# def getLICAresponse(client,lineitemID, creativeID):
#     # ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
#     #lica_service = client.GetService('LineItemCreativeAssociationService', version = version)
#     #lica_response = lica_service.getPreviewUrl(lineitemID,creativeID,"http://output.jsbin.com/kavobal/")
#     #print lica_response
#     options = webdriver.ChromeOptions()
#     url='http://bbc.com'
#     browser = webdriver.Chrome(executable_path='/Users/sahmed/Desktop/chromedriver',chrome_options=options)
#     browser.set_window_size(1500, 1000)
#     browser.get(url)
#     height = browser.execute_script("return document.body.parentNode.scrollHeight")
#
#     # 2. get screenshot
#     browser.set_window_size(1500, height)
#     browser.save_screenshot("test2.png")
#
#     browser.quit()
#     #=============
#     # options = webdriver.ChromeOptions()
#     # browser = webdriver.Chrome(executable_path='/Users/sahmed/Desktop/chromedriver',chrome_options=options)
#     # browser.set_window_size('700', '600')
#     # browser.get(url)
#     # time.sleep(10)
#     # total_height = browser.execute_script("return document.body.parentNode.scrollHeight")
#     # browser.quit()
#     # # 2. get screenshot
#     # browser = webdriver.Chrome(executable_path='/Users/sahmed/Desktop/chromedriver',chrome_options=options)
#     # browser.set_window_size('700', total_height)
#     # browser.get(url)
#     # browser.save_screenshot('test2.png')
#     #---------------
#     # chrome_options.add_argument("--incognito")
#     #
#     # driver = webdriver.Chrome(executable_path='/Users/sahmed/Desktop/chromedriver',chrome_options=options)
#     # driver.get(url)
#     # driver.implicitly_wait(10)
#     # # options = webdriver.ChromeOptions()
#     # # options.add_argument('--ignore-certificate-errors')
#     # # options.add_argument("--test-type")
#     # # options.executable_path ="/Users/sahmed/Desktop/chromedriver"
#     # # driver = webdriver.Chrome(options)
#     # #
#     # # driver.get(lica_response)
#     # # driver.implicitly_wait(10)
#     # driver.save_screenshot("test.png")
#     # driver.close()
#     return None
