import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

# payload = "q=English%20is%20hard%2C%20but%20detectably%20so"
payload = "q=jhvdusevfcjvsdhsyeyfcidsvfcivdsfcdh"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "30ff3cf097msh1b6bbd6f631e885p1fb448jsn43188caa6b07",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)