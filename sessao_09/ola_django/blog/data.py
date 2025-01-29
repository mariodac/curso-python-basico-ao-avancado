import requests

def get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    data_json = response.json()
    return data_json

def search_by_id(list_dict:list, id:int):
    for dic in list_dict:
        if dic['id'] == id:
            return list_dict.index(dic)
    return None

if __name__ == '__main__':
    # print(get_posts())
    posts = get_posts()
    for post in posts:
        post['photo'] = f'https://picsum.photos/300?r={post["id"]}'
        print(post['title'])
    print(posts)