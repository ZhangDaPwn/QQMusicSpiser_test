import requests


url = "http://v9-dy-z.ixigua.com/57b4a83433275e222085a430311f6fb6/5bc047a5/video/m/22071461854f5324a31a1d4cd9c357438cf1154439200006962abd2a371/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

response = requests.get(url, headers=headers)

with open('video.video', 'wb') as f:

    f.write(response.content)
