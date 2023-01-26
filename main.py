import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/gp/product/B07JKQLHF1/ref=ox_sc_saved_title_1?smid=A3652ZBQ53FUEE&th=1&psc=1"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get("https://www.amazon.com/gp/product/B07JKQLHF1/ref=ox_sc_saved_title_1?smid=A3652ZBQ53FUEE&th=1&psc=1", headers=HEADERS)
amazon_page = response.text
# print(amazon_page)

soup = BeautifulSoup(amazon_page, 'html.parser')

title = soup.find(id="productTitle").get_text().strip()
amazon_price = soup.select_one(selector="span .a-offscreen")
amazon_price_f = float(amazon_price.getText().strip("$"))
print(amazon_price_f)
print(title)

MY_EMAIL = "srt499123@gmail.com"
MY_PASSWORD = "################"

if amazon_price_f < 59.99:
    message = f"{title} is now ${amazon_price_f}"

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
