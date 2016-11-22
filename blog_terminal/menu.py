from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user = input("Enter author name: ")
        self.user_blog = None #added and dont know why
        if self._user_has_account():
            print("Welcome back {}.".format(self.user) )
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs',{'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog's titlte: ")
        description = input("Enter blog's description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog=blog

    def run_menu(self):
        read_or_write = input("Do you want to read (R) or write (W): ")
        if read_or_write in "rR":
            self._list_blogs()
            self._view_blogs()

        elif read_or_write in "wW":
            self.user_blog.new_post()
        else:
            print("Thank you for reading!")
            #try with return

    def _list_blogs(self):
        #y tuong cua tui la list all blogs: blogs = Blog.from_mongo()
        blogs = Database.find(collection='blogs',
                              query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['author'], blog['title']))

    def _view_blogs(self):
        #double kill lan 2
        blog_to_see = input("Enter blog id you wanna see: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_post()
        for post in posts:
           # y tuong nua cua toi: print(post)
            print("Date: {}, title: {} \n\n{}".format(post['created_date'], post['title'], post['content']))
