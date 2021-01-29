from django.test import TestCase, Client
from django.urls import reverse
from songs.models import Song
from django.contrib.auth.models import User
from authentication.models import UserFavouriteSong

class SongsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username="admin",
            password="admin",
            email="admin@example.com")
        self.client.force_login(self.user)

        self.test_song_1 = Song.objects.create(
            title = 'Thunder',
            author = 'Volatage',
            genre = 'Rock',
            audio_file = 'audio',
            audio_file_vocal = 'vocal',
            song_image = 'image'
        )
        self.test_song_2 = Song.objects.create(
            title = 'Rain',
            author = 'Silk',
            genre = 'Pop',
            audio_file = 'audio',
            audio_file_vocal = 'vocal',
            song_image = 'image'
        )

        self.test_song_3_list = {
            'title' : 'Mars',
            'author' : 'Musk',
            'genre' : 'Science',
            'audio_file' : 'audio',
            'audio_file_vocal' : 'vocal',
            'song_image' : 'image'
        }

    def test_landing(self):
        response = self.client.get(reverse('landing'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing-page/landing.html')
    
    def test_index(self):
        response = self.client.get(reverse('songs:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'song_index.html')
        self.assertContains(response, 'Thunder')
        self.assertContains(response, 'Rain')
    
    def test_show_details(self):
        response = self.client.get(reverse('songs:show_details',kwargs={'song_id' : 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'details.html')
        self.assertContains(response, 'Thunder')
        self.assertNotContains(response, 'Rain')

    def test_add_song_to_favourite(self):
        response = self.client.get(reverse('songs:add_to_favourite',kwargs={'song_id' : 1}))
        self.assertEquals(response.status_code, 302)
        favourite_songs = UserFavouriteSong.objects.filter(user = self.user, song = self.test_song_1)
        self.assertEquals(self.test_song_1, favourite_songs[0].song)
        self.assertEquals(self.user, favourite_songs[0].user)

    def test_remove_song_to_favourite(self):
        response = self.client.get(reverse('songs:remove_from_favourite',kwargs={'song_id' : 1}))
        self.assertEquals(response.status_code, 302)
        favourite_songs = UserFavouriteSong.objects.filter(user = self.user, song = self.test_song_1)
        self.assertEquals(len(favourite_songs), 0)

    def test_add_new_song_POST_not_valid(self):
        response = self.client.post(reverse('songs:add_new_song'), self.test_song_3_list)
        self.assertEquals(response.status_code, 200)
        songs = Song.objects.filter(title = self.test_song_3_list["title"])
        self.assertEquals(len(songs), 0)
    
    def test_add_new_song_GET(self):
        response = self.client.get(reverse('songs:add_new_song'))
        self.assertEquals(response.status_code, 200)
        songs = Song.objects.filter(title = self.test_song_3_list["title"])
        self.assertEquals(len(songs), 0)
