import os
import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv

load_dotenv()
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
SMTP = os.getenv("SMTP")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

para = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
}
response = requests.get(url=URL, headers=para)
res = response.text
soup = BeautifulSoup(res, 'html.parser')
print(soup.prettify())
tag= soup.find("span",class_="a-offscreen")
price = f"{tag.text.split("$")[1]}"
print(price)
# if float(price)<100:
#     with smtplib.SMTP(SMTP) as connect:
#         connect.starttls()
#         connect.login(user=EMAIL, password=PASSWORD)
#         connect.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg=f"Subject : AMAZON!! \n\n HEY THE PRICES ARE DROP. \n GO FAST AND CHECK PRICE NOW IS {price}!!!!!!")

