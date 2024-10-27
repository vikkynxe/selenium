from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH

try:
    # Open Google
    driver.get("https://www.google.com")

    # Print the title of the page
    print("Page title is:", driver.title)

    # Find the search box using its name attribute value
    search_box = driver.find_element(By.NAME, "q")

    # Type in a search term and hit Enter
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    # Wait for a few seconds to see the results
    time.sleep(3)

    # Print the title of the results page
    print("Results page title is:", driver.title)

finally:
    # Close the browser
    driver.quit()

#hi it my first chang
