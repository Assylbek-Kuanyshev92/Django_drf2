import requests
#
url = 'http://localhost:8000/posts/'
# response = requests.get(url, params={'post_id': 3})
# response = requests.post(url, json={'title': 'DRF intro'})
response = requests.post(url, json={'title': 'DRF intro',
                                    'content': 'Serializer,api_view decorator',
                                    'author': 1
                                    })

# url = 'http://localhost:8000/comments/'
# # response = requests.get(url, params={'post_id': 3})
# # response = requests.post(url, json={'title': 'DRF intro'})
# response = requests.post(url, json={'title': 'DRF comment'})


# print(response)
print(response.headers)
print("====================================")
print(response.text)
