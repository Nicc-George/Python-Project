from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_pages(url):
    driver = webdriver.Chrome()
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.pt-5"))).text
    name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2[data-testid='hero-product-card-name']"))).text
    driver.quit()
    return name, price
    
urls = [
    "https://www.warhammer.com/en-US/shop/chaos-space-marines-legionaries-2025",
    "https://www.warhammer.com/en-US/shop/Chaos-Space-Marine-Terminators-2019",
    "https://www.warhammer.com/en-US/shop/chaos-space-marines-chaos-lord-2024"
    ]
total = 0
for url in urls:
    name, price = scrape_pages(url)
    print(name + "| " + price)
    price_value = float(price.replace("$", ""))
    total += price_value

print(f"Total: ${total:.2f}")


