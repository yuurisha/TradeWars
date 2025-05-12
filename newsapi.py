import http.client

conn = http.client.HTTPSConnection("real-time-news-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': '',
    'x-rapidapi-host': "real-time-news-data.p.rapidapi.com"
}

conn.request("GET", "/search?query=Trump%20US%20Tariff&time_published=1y&country=MY&lang=en", headers=headers)

res = conn.getresponse()
data = res.read()

with open("news6_MY.json", "w", encoding="utf-8") as f:
    f.write(data.decode("utf-8"))