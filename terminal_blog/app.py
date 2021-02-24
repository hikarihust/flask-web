from database import Database
from models.post import Post


Database.initialize()

post = Post(blog_id="123",
            title="Another great post",
            content="This is some sample content",
            author="jose"
            )

post.from_mongo('965ae76cb1364f60a62904ca48ea106f')
print(post.json())
