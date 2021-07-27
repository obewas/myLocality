from django.test import TestCase, RequestFactory
from users import views as user_views
# Create your tests here.
class HomePageTest(TestCase):
 	def test_environment_set_in_context(self):
 		request = RequestFactory().get('/')
 		view = user_views.profile_page()
 		view.setup(request)

 		context = view.get_context_data()
 		self.assertIn('environment', context)
