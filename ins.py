from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'username'))

).send_keys('')
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'password'))
).send_keys('')
driver.find_element(By.XPATH, '//button[@type="submit"]').click()


try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Bilgileri kaydet")]'))
    ).click()
except Exception as e:
    print("İlk 'Bilgileri kaydet' butonu bulunamadı:", e)

try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Şimdi Değil")]'))
    ).click()
except Exception as e:
    print("İkinci 'Şimdi Değil' butonu bulunamadı:", e)
sleep(2)
driver.get("https://www.instagram.com/"anyinstaprofile"/")
sleep(1)
"""try:
    # Arama butonunu bekleyin ve tıklayın
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//svg[@aria-label="Ara"]'))
    )
    search_button.click()
except Exception as e:
    print("Arama butonu bulunamadı, JavaScript ile tıklama denenecek:", e)
    # JavaScript ile tıklama denemesi
    try:
        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//svg[@aria-label="Ara"]'))
        )
        driver.execute_script("arguments[0].click();", search_button)
    except Exception as js_e:
        print("JavaScript ile tıklama başarısız:", js_e)"""




def scrollAllWayDown():
    global driver
    footer = driver.find_element(By.TAG_NAME,'footer')
    last_height =driver.execute_script('return document.body.scrollHeight')
    while True:
        footer.location_once_scrolled_into_view
        sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            print('sayfa bitti')
            break
        else:
            last_height = new_height
scrollAllWayDown()
tumkutular=driver.find_element(By.CLASS_NAME,'x1lliihq ')
tumlinkler=[]
for i in tumkutular:
    tumlinkler.append(i.find_element(By.TAG_NAME,'a'))
tumlinkler[0].click()


while True:
    pass












