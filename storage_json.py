import json


def blog_list():
    """shows posts in json file """
    with open('static/data.json', "r") as data:
        datablogs = json.load(data)
        bloglist = []
        for article in datablogs:
            article = {
                'id': article['id'],
                'author': article['author'],
                'title': article['title'],
                'content': article['content']
            }
            bloglist.append(article)
        return bloglist


def add_post(new_post):
    """add to json file """
    file = 'static/data.json'
    with open(file, "r") as data:
        blogs = json.load(data)
        blogs.append(new_post)
        # write te to jason file
    with open(file, 'w') as json_file:
        return json.dump(blogs, json_file, indent=4, separators=(',', ': '))


def delete_post(id):
    """delete from json file """
    file = 'static/data.json'
    with open(file, "r") as data:
        blogs = json.load(data)
        for article in blogs:
            if id == article['id']:
                blogs.remove(article)
    with open(file, 'w') as json_file:
        return json.dump(blogs, json_file, indent=4, separators=(',', ': '))


def update_post(id, author, title, content):
    """update json file """
    file = 'static/data.json'
    with open(file, "r") as data:
        blogs = json.load(data)
        for article in blogs:
            if id == article['id']:
                article['author'] = author
                article['title'] = title
                article['content'] = content
    with open(file, 'w') as json_file:
        return json.dump(blogs, json_file, indent=4, separators=(',', ': '))




