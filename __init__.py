from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from functions.driver import go_next, wait_for_it, send_keys_delay
from functions.miscellaneous import load_yaml, get_config

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get('https://missions.ingress.com')

# Load the config files
try:
    missions_config = load_yaml("missions.yaml")
except FileNotFoundError:
    missions_config = None
try:
    credentials = load_yaml("login.yaml")
except FileNotFoundError:
    credentials = None
# Press the button to login
driver.find_element(By.CLASS_NAME, 'sign-in-button').click()
driver.find_element(By.CLASS_NAME, 'signin-provider-facebook').click()

# This can be done much better since it waits one second but it could be a longer wait..
time.sleep(1)

# Change tab and go to the login one
driver.switch_to.window(driver.window_handles[1])

# Accept the cookies
driver.find_element(By.XPATH, "//*[@data-cookiebanner='accept_button']").click()

# Enter the email and password (only if the credentials are set hence the file exist)
if credentials is not None:
    email = get_config(credentials,"email")
    password = get_config(credentials,"password")
    driver.find_element(By.ID, 'email').send_keys(email)
    driver.find_element(By.ID, 'pass').send_keys(password)
    # Login
    driver.find_element(By.XPATH, "//input[@name='login']").click()
else:
    # It has to wait until the user manually login
    while len(driver.window_handles) > 1:  # It loops until the login window is open
        continue

# Go back to the main tab
driver.switch_to.window(driver.window_handles[0])

number_of_missions = missions_config["number_of_missions"]
for i in range(0, number_of_missions):  # Loop over all missions
    i = str(i + 1)
    # Wait until the new page has loaded
    wait_for_it(driver, "create-mission-button")

    # Create new mission
    button = driver.find_element(By.CLASS_NAME, 'create-mission-button').click()

    # Wait until the page loads
    wait_for_it(driver, "bullet")

    # We select the mission type (Sequential or Any Order)
    mission_type = get_config(missions_config, "mission_type")
    driver.find_element(By.XPATH, f"//*[contains(text(), '{mission_type}')]").click()

    # Go to the next page
    go_next(driver)
    wait_for_it(driver, "//*[contains(text(),'Logo')]", By.XPATH)

    # From the config load the mission data
    titolo = get_config(missions_config, "title").replace("%d", i).replace("%n",str(number_of_missions))
    descrizione = get_config(missions_config, "description").replace("%d",i)
    logo = get_config(missions_config, "path_logo").replace("%d", i.zfill(2))
    luogo = get_config(missions_config, "location", error=False)
    passphrase = get_config(missions_config, "passphrase_first_mission", error=False)

    # Find the elements and send the data
    driver.find_element(By.XPATH, "//*[contains(@placeholder,'Add mission name')]").send_keys(titolo)
    driver.find_element(By.XPATH, "//*[contains(@placeholder,'Add mission description')]").send_keys(descrizione)
    driver.find_element(By.ID, "logo-upload-input").send_keys(logo)

    # Go to the next page
    go_next(driver)
    wait_for_it(driver, "autocomplete", By.ID)

    # Search the location (key by key) if set
    if luogo is not None:
        luogo_elemento = driver.find_element(By.ID, "autocomplete")
        send_keys_delay(luogo_elemento, luogo)  # Inviamo le lettere uno ad uno così da poterlo ricercare
        luogo_elemento.send_keys(Keys.ENTER)

    # We set the first mission to have a passphrase to check if the user is doing the right mission
    # (if the passphrase is set in the config)
    if passphrase is not None:
        wait_for_it(driver, "//div[contains(@class,'number') and text() = 1]", By.XPATH, timeout=3600)
        driver.find_element(By.XPATH, "//select[contains(@class,'fill-width')]/option[6]").click()
        driver.find_element(By.XPATH,"//textarea[contains(@class,'fill-width')]").send_keys(passphrase)
        driver.find_element(By.XPATH,"//input[contains(@placeholder,'Answer to the question')]").send_keys(i)

    # We log in the browser console the last mission inserted just in case we need to remember it
    wait_for_it(driver, "//div[contains(@class,'number') and text() = 6]", By.XPATH, timeout=3600)
    ultima_missione = driver.find_elements(By.CLASS_NAME, 'title')[-1]
    ultima_missione = ultima_missione.text.replace("\"", "\\\"").replace("'", "\\'")
    driver.execute_script(f'console.log("{ultima_missione}")')

    wait_for_it(driver, "mission-description", timeout=3600)
    go_next(driver)
