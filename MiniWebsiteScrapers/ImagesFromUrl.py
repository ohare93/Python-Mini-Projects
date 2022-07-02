
import requests

image_url = "https://prove.dk/storage/app/book/TheoryBook_FirstAid_ed2_2014_en/files/mobile/[NUM].jpg"
num_from = 1
num_to = 220

for count in range(num_from, num_to+1):
    url_to_download = image_url.replace("[NUM]", str(count))
    img_data = requests.get(url_to_download).content
    with open(f"{count}.jpg", 'wb') as handler:
        handler.write(img_data)

