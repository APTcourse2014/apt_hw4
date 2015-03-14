from nose2.tools import such
from sure import expect
from tastypie.test import TestApiClient
import json


client = TestApiClient()


def test_post_model():
    from blog.models import Post
    post = Post(author="abc", title="xyz", text="asdasd")
    post_repr = str(post)
    post_repr.should.be.equal("abc: xyz")


def test_comment_model():
    from blog.models import Comment
    comment = Comment(author="abc", text="asdasd")
    comment_repr = str(comment)
    comment_repr.should.be.equal("abc: asdasd")


with such.A("blog API") as it:

    @it.should("allow to get list of posts")
    def test_get_posts():
        resp = client.get("/api/v1/post/")
        expect(resp.status_code).must.be.equal(200)
        data = json.loads(resp.content)
        data["meta"]["total_count"].should.be.equal(0)

    @it.should("allow to create a post")
    def test_create_a_post():
        resp = client.post("/api/v1/post/", data={
            "author": "abc",
            "title": "xyz",
            "text": "asdasd"
        })
        expect(resp.status_code).must.be.equal(201)
        data = json.loads(resp.content)
        data["title"].should.be.equal("xyz")
        it.post_uri = data["resource_uri"]

    @it.should("allow to get post detail")
    def test_get_post_detail():
        resp = client.get(it.post_uri)
        expect(resp.status_code).must.be.equal(200)

    it.createTests(globals())

# TODO:
# create post
# get post detail
# edit post
# get post list, there is no comments field
# create comment
# get post detail, there is comments field, with one comment
# delete post
