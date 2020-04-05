# from django.test import TestCase

# # Create your tests here.
# from django.test import TestCase
# from django.test import SimpleTestCase
# from django.urls import reverse

# # Fix tests to reflect


# class HomePage(SimpleTestCase):

#     def SetUp(self):
#         url = reverse('home')
#         self.response = self.client.get(url)

#     def test_homepage_status_code(self):
#         self.assertEqual(self.response.status_code, 200)

    
#     def test_homepage_template(self):
#         self.assertTemplateUsed(self.response, 'home.html')

#     def test_homepage_contains_correct_html(self):
#         self.assertContains(self.response, 'Homepage')

#     def test_homepage_does_not_contain_incorrect_html(self):
#         self.assertNotContain(
#             self.response, "Random Text"
#         )