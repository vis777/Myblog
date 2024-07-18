from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Test Post', content='Test Content')

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'New Post',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args=[self.post.pk]), {
            'title': 'Updated Post',
            'content': 'Updated Content'
        })

def test_post_update_view(self):
    response = self.client.post(reverse('post_edit', args=[self.post.pk]), {
        'title': 'Updated Post',
        'content': 'Updated Content'
    })
    self.assertEqual(response.status_code, 302)
    self.post.refresh_from_db()
    self.assertEqual(self.post.title, 'Updated Post')

def test_post_delete_view(self):
    response = self.client.post(reverse('post_delete', args=[self.post.pk]))
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Post.objects.count(), 0)
