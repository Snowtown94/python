import pymongo

from database import Database
from models.blog import Blog


Database.initialize()

blog = Blog(author="Jose",
            title="Sample title",
            description="Sample description")
blog.new_post()
blog.save_to_mongo()
from_database = Blog.from_mongo(blog.id)
Blog.from_mongo(blog.id)
print(blog.get_post())
