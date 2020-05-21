import requests

# host = "https://api.apiopen.top"
host="http://api.douban.com"
# path = "/getJoke?page=1&count=2&type=video"
path = "/v2/movie/in_theaters"
url=host+path

res=requests.post(url,

                  data={
                        "Content-Type": "application/json; charset=utf-8",
                        "apikey":"0df993c66c0c636e29ecbb5344252a4a",
                        'start':0,
                        'count':10
                  }
                  )

# res=requests.get(
#     url
# )
print(res)
