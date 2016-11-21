import pymongo

from models.post import Post

#post = Post()
post = Post(title="post title", author="post author", content="post content")
post2 = Post("post 2 title", "post 2 content", "post 2 author")

post2.title = "post 2 title"
post2.author = "chau"
post2.date = 12
post2.content = "this is post 2 content"

print(post2.date)
print(post.author)
