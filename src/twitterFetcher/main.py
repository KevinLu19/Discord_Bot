from selenium.common import exceptions
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os

def fire_fox_browser():
    options = webdriver.FirefoxOptions()
    # options.headless = True
    driver = webdriver.Firefox(options = options, executable_path = r"C:\Users\Kevin\OneDrive\Desktop\Yuna2.0\geckodriver.exe")

    return driver

def twitter_login(driver):
    twitter_login_url = "https://www.twitter.com/login"
    twitter_username = os.environ.get("TWITTER_USERNAME")
    twitter_pass = os.environ.get("TWITTER_PASS")
    try:
        driver.get(twitter_login_url)
        username_xpath = '//input[@name="session[username_or_email]"]'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, username_xpath)))
        username_input = driver.find_element_by_xpath(username_xpath)
        username_input.send_keys(twitter_username)
    except:
        print("Something happened when bot tries to login to Twitter")
        return False

    password_input = driver.find_element_by_xpath('//input[@name="session[password]"]')
    password_input.send_keys(twitter_pass)

    try:
        password_input.send_keys(Keys.RETURN)
        expected_url = "https://www.twitter.com/home"
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
    except:
        print("Something happened during transistion to twitter home page.")

    return True

def find_searched_input(searching_user, driver):
    driver.implicitly_wait(10) # Let the driver load the page before trying to find element.

    search_box_xpath = '//input[@aria-label="Search query"]'
    search_input = driver.find_element_by_xpath(search_box_xpath)
    search_input.send_keys(searching_user)
    search_input.send_keys(Keys.RETURN)

    driver.implicitly_wait(10) # Wait for 10 seconds for the program to load before doing find_element

    people_text_link =  driver.find_element_by_link_text("People")
    people_text_link.click()

    twitter_user_profile = '//div[@data-testid="UserCell"]'
    navigate_to_user_profile = driver.find_element_by_xpath(twitter_user_profile)
    navigate_to_user_profile.click()

    return True

def generate_tweet_id(tweet):
    return "".join(tweet) # Formulates a unique id to each tweet by combining the tweet itself.

def collect_all_tweet_from_view(driver, lookback_limit = 10):
    page_cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')

    if len(page_cards) <= lookback_limit:
        return page_cards
    else:
        return page_cards[-lookback_limit:]

def extact_tweet_data(card):
    try:
        user = card.find_element_by_xpath('.//span').text
    except exceptions.NoSuchElementException:
        user = ""
    except exceptions.StaleElementReferenceException:
        return
    try:
        handle = card.find_element_by_xpath('.//span[contains(text(), "@")]').text
    except exceptions.NoSuchElementException:
        handle = ""
    try:
        postdate = card.find_element_by_xpath('.//time').get_attribute('datetime')
    except exceptions.NoSuchElementException:
        return

    tweet = (user, handle, postdate)
    return tweet

def twitter_main(twitter_search):
    driver = fire_fox_browser()
    unique_tweet = set()

    login = twitter_login(driver)
    if not login:
        return

    search = find_searched_input(twitter_search, driver)
    if not search:
        return

    tweets = collect_all_tweet_from_view(driver)

    for tweet in tweets:
        try:
            each_tweet = extact_tweet_data(tweet)

        except exceptions.StaleElementReferenceException:
            continue

        if not each_tweet:
            continue

        tweet_id = generate_tweet_id(each_tweet)

        if tweet_id not in unique_tweet:
            unique_tweet.add(tweet_id)

if __name__ == "__main__":
    twitter_main("Noahgraphicz")