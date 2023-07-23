import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 4. Test case: Verify that the user can play a video on youtube.com
# Steps:
# Launch the browser and navigate to https://www.youtube.com
def launch_browser_go_to_website(url):
    driver.get(url)

# Locate the search box and enter a video title or keyword "music"
# Click on the search button or press enter
def search():
    search_box = driver.find_element(By.XPATH, "//input[@id='search']")
    search_box.send_keys("music")
    time.sleep(2)
    search_box.submit()
    time.sleep(2)

# Select a video from the results page by clicking on its title or image
def select_video_and_click():
    driver.find_element(By.XPATH, "//div[@id='title-wrapper']").click()

# On the video page, click on the play button or wait for the video to start automatically
# Verify that the video is playing and the progress bar is moving along with the sound
def click_and_verify_that_video_is_playing():
    player_state = driver.execute_script("return document.getElementById('movie_player').getPlayerState();")

    assert player_state == 1, "The video is playing, TEST PASSED"
    driver.quit()


if __name__ == '__main__':
    url = "https://www.youtube.com"

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()


    launch_browser_go_to_website(url)
    search()
    select_video_and_click()
    click_and_verify_that_video_is_playing()