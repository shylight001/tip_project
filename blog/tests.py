#blog/test.py
from django.contrib.auth import get_user_model

from django.test import Client, TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    
    def setUp(self):
        reset_sequences = True
        self.user =get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        
        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            payment='debit',
            address='test address',
            total='100.00',
            author=self.user,
        )
        
    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post),post.title)
        
    def test_post_content(self):
        print(f'The id in test2 is {self.post.id}')
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')
    
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_post_detail_view(self):
        print(f'The id in detail_view is {self.post.id}')
        response = self.client.get(f'/post/{self.post.id}/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200 )
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')
        
        