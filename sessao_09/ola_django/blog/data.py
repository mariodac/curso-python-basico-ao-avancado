import requests

def get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    data_json = response.json()
    return data_json

if __name__ == '__main__':
    print(get_posts())