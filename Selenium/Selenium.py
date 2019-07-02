from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#Google chrome browser
browser = webdriver.Chrome()
#Maximize the browser window
browser.maximize_window()

#Open the web page
browser.get("https://www.adidas.com.my/en/men")

#Shop for shoes
shoes=browser.find_element_by_css_selector('.gl-label--l')
shoes.click()

#browser.implicitly_wait(30000)
#Extract product name and price
product_titles = browser.find_elements_by_class_name('title')
price=browser.find_elements_by_class_name('price')
for title in product_titles:
    print(title.text)
for price in price:
    print(price.text)

#Filter it
#Select the sort by dropdown list
filt=browser.find_element_by_xpath('//*[@id="top-sorting-options"]/div/div/a').click()
#Sort by price(low-high)
price=browser.find_element_by_xpath('//*[@id="top-sorting-options"]/div/div/div/div[2]/div/ul/li[6]/span').click()

"""
#Open the web page
browser.get("https://www.adidas.com.my/yeezy")

#Select the select size button
select_size=browser.find_element_by_css_selector('.src-components-___sizes-dropdown__container___1xcFK')
select_size.click()

#add_to_bag=browser.find_element_by_css_selector('.src-components-___add-to-bag-form__addToBagButton___3iEAg')
#add_to_bag.click()

#size=Select(driver.find_element_by_id('src-components-___sizes-dropdown__sizes___ztM1k  src-components-___sizes-dropdown__narrow___3Xl4k'))
#size.select_by_value('1')

#s1=Select(browser.find_element_by_css_selector('.src-components-___sizes-dropdown__sizesDropdown___Dj9Z9 src-components-___sizes-dropdown__mobile___187tx'))
#print(s1.options)

#html_list = self.driver.find_element_by_id("myId")
items = browser.find_elements_by_id("select-size-option")
for item in items:
    text = item.text
    print(text)
"""
"""
#For the yeezy website, we want to click the size chart when we enter the web page
size_chart=browser.find_element_by_css_selector('.src-components-___available__sizeChartLink___3HHCN')
size_chart.click()
"""

"""
# Navigate to the application home page
browser.get("http://www.google.com")

# get the search textbox
search_field = browser.find_element_by_name("q")

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()
"""
