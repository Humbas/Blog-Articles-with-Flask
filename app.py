from flask import Flask, render_template, request, redirect
import storage_json

app = Flask(__name__)

blog_posts = storage_json.blog_list()


def fetch_post_by_id(post_id):
    """compares posts id with id in url """
    for post in blog_posts:
        if post_id == post['id']:
            return post


@app.route('/add', methods=['GET', 'POST'])
def add():
    """adds blog posts by POST method"""
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')
        id_blog = len(blog_posts) * 2 + 1
        article = {
            'id': id_blog,
            'title': title,
            'author': author,
            'content': content
        }
        blog_posts.append(article)
        storage_json.add_post(article)
        return redirect("/", code=302)
    else:
        return render_template('add.html')


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """updates post dict by  POST method"""
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')
        post['tite'] = title
        post['author'] = author
        post['content'] = content
        storage_json.update_post(post_id, author, title, content)
        return redirect("/", code=302)
    return render_template('update.html', post=post)


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """deletes posts by obtain post id url """
    for article in blog_posts:
        if article['id'] == post_id:
            blog_posts.remove(article)
            storage_json.delete_post(post_id)
    return redirect("/", code=302)


@app.route('/', methods=['GET', 'POST'])
def home():
    """returns page with blog lists"""
    blog_length = len(blog_posts)
    return render_template('index.html', blog_posts=blog_posts, blog_length=blog_length)


if __name__ == '__main__':
    app.run(debug=True)
