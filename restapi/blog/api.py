from tastypie.resources import ModelResource
from blog.models import Post, Comment
from tastypie.authorization import Authorization
from tastypie import fields

class PostResource(ModelResource):
  author = fields.CharField(attribute="author")
  title = fields.CharField(attribute="title")
  text = fields.CharField(attribute="text")
  is_public = fields.BooleanField(attribute="is_public", use_in="detail")
  comments_list = fields.ToManyField('blog.api.CommentResource', "comment_set", related_name="post", null=True, use_in="detail", full=True)
  class Meta:
    queryset = Post.objects.all()
    resource_name = 'post'
    authorization = Authorization()
    always_return_data = True

class CommentResource(ModelResource):
  author = fields.CharField(attribute="author", null=False)
  text = fields.CharField(attribute="text")
  post = fields.ToOneField('blog.api.PostResource', 'post')
  class Meta:
    queryset = Comment.objects.all()
    resource_name = 'comment'
    authorization = Authorization()
    always_return_data = True