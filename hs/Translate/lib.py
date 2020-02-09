# 作りたいもん@Py
import requests

url = "https://script.google.com/macros/s/AKfycbwcQayK15gTHEPrmAwwSEgEyV7W8rHeQzJ7O8UsLG4Cr4No-ZY/exec?text=%E3%81%93%E3%82%93%E3%81%AB%E3%81%A1%E3%81%AF&source=ja&target=en"

r = requests.get(url)

print(r)

