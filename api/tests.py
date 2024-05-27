from django.test import TestCase

# Create your tests here.


# Note: The tests below rely upon static assets (for the rendered templates), so require that either:
# 1. The static assets have been processed - ie: `./manage.py collectstatic` has been run.
# 2. Or, the tests are run in debug mode (which means WhiteNoise will use auto-refresh mode),
#    using: `./manage.py test --debug-mode`
class HoustonAPITest(TestCase):
    def test_index_view_status_code(self):
        response = self.client.get("/api")
        self.assertEqual(response.status_code, 200)
