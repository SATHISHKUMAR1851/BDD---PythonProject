import time

from selenium import webdriver
from behave import given, then, when
from selenium.webdriver.common.by import By


@given(u'I open the application URL in th browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.magicbricks.com/")
    time.sleep(3)


@when(u'I entered the preferred locations in search tab')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/header/section[2]/div/ul/li[1]/a").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "/html/body/header/section[1]/div/div[1]/div[2]/a").click()
    time.sleep(3)


@when(u'I Navigate and click on the search tab')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                "/html/body/header/section[1]/div/div[1]/div[2]/div/div[1]/div[3]/ul/li[3]/a").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "/html/body/section/section/div/div[1]/div[3]/div[4]").click()
    time.sleep(3)


@then(u'I Get the properties based on locations')
def step_impl(context):
    context.driver.quit()


@when(u'I want to find an agent')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/header/section[1]/div/div[1]/div[2]/a").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "/html/body/header/section[1]/div/div[1]/div[2]/div/div[1]/div[3]/ul/li[3]/a").click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, "/html/body/section/section/div/div[1]/div[3]/div[4]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH,
                                "/html/body/div/div[1]/div/div[2]/div[4]/div/div/div[1]/div[2]/ul/li[3]/a").click()
    time.sleep(3)


@then(u'I can get a contact of a agent for a given location')
def step_impl(context):
    context.driver.quit()


@when(u'I want to give an Minimum and Maximum budgets levels')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/header/section[1]/div/div[1]/div[2]/a").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH,
                                "/html/body/header/section[1]/div/div[1]/div[2]/div/div[1]/div[3]/ul/li[3]/a").click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, "/html/body/section/section/div/div[1]/div[3]/div[3]/div[1]").click()
    time.sleep(3)

    context.driver.find_element(By.XPATH,
                                "/html/body/section/section/div/div[1]/div[3]/div[3]/div[2]/div/div[2]/div[2]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH,
                                "/html/body/section/section/div/div[1]/div[3]/div[3]/div[2]/div/div[1]/input[2]").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH,
                                "/html/body/section/section/div/div[1]/div[3]/div[3]/div[2]/div/div[3]/div[8]").click()
    time.sleep(3)


@when(u'I want to click on the search tab')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/section/section/div/div[1]/div[3]/div[4]").click()
    time.sleep(3)


@then(u'Properties for the given location are shown')
def step_impl(context):
    context.driver.quit()


@given(u'I navigate to the Tips and guides Tab')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/header/section[2]/div/ul/li[1]/a").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "/html/body/header/section[2]/div/ul/li[1]/div/div/div/div/div[5]/ul/li[4]/a").click()
    time.sleep(3)
    child_window_handle = context.driver.window_handles[-1]
    context.driver.switch_to.window(child_window_handle)
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0,500,document.body.scrollHeight);")
    time.sleep(5)


@when(u'I want to select Two locations based on my interest')
def step_impl(context):
    context.driver.find_element(By.ID, "locOne").send_keys("Chennai")
    time.sleep(5)
    context.driver.find_element(By.XPATH,
                        "/html/body/div/div/div[1]/div[5]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[3]/a").click()
    time.sleep(8)
    context.driver.find_element(By.ID, "locTwo").send_keys("Chennai")
    time.sleep(5)
    context.driver.find_element(By.XPATH,
                        "/html/body/div/div/div[1]/div[5]/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[5]/a").click()
    time.sleep(8)

@when(u'I navigate to the compare tab')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[5]/div[2]/div/div[2]/div[2]/div/div[4]/input").click()
    time.sleep(10)

@then(u'I can able to Compare the two properties based on locations')
def step_impl(context):
    context.driver.quit()



@when(u'I want to click the Prop worth button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/header/section[2]/div/ul/li[1]/a").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "/html/body/header/section[2]/div/ul/li[1]/div/div/div/div/div[5]/ul/li[1]/a").click()
    time.sleep(5)


@then(u'I can able to see Prop worth page is shown for selected locations')
def step_impl(context):
    context.driver.quit()


@when(u'I want to click on the rates and trends')
def step_impl(context):
    context.driver.get("https://www.magicbricks.com/property-for-sale-rent-in-Chennai/residential-real-estate-Chennai")
    context.driver.maximize_window()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "/html/body/header/section[2]/div/ul/li[1]/a").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH,
                                "/html/body/header/section[2]/div/ul/li[1]/div/div/div/div/div[5]/ul/li[2]/a").click()
    time.sleep(3)


@then(u'I can able to see the rates and trends option')
def step_impl(context):
    context.driver.quit()
