from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
youtube_url = "https://www.youtube.com/results"

options = webdriver.FirefoxOptions()
options.headless = True
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Firefox(options = options, executable_path=r"C:\Users\Kevin\OneDrive\Desktop\Yuna2.0\geckodriver.exe")


def convert_user_request(video_name):
    return video_name.replace(" ", "_")

def get_requested_video(video_name):
    # fixed_user_requested_string = convert_user_request(video_name)

    driver.get("https://www.youtube.com")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(video_name)
    driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()

    searching_video_url = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))

    searched_video_container = []

    for video_href in searching_video_url:
        searched_video_container.append(video_href.get_attribute("href"))
        #print (video_href.get_attribute("href"))

    # print([my_href.get_attribute("href") for my_href in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))])

    # driver.quit()

    return searched_video_container[0]

if __name__ == "__main__":
    get_requested_video("maplestory ludi pq ost")
