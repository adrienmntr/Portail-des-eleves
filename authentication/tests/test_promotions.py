import json

from associations.models import User
from backend.tests_utils import BaseTestCase


class PromotionsTestCase(BaseTestCase):
    fixtures = ("birthdays_test.json",)

    def test_if_not_logged_in_then_401(self):
        res = self.get("/promotions/")
        self.assertStatusCode(res, 401)

    def test_promotions(self):
        self.user = self.create_and_login_user("17simple")

        res = self.get("/promotions/")
        self.assertStatusCode(res, 200)

        promotions = json.loads(res.content)["promotions"]

        self.assertEqual(
            sorted(promotions, reverse=True),
            promotions,
            msg="Promotions are not sorted from the newest to the oldest.",
        )

        self.assertSetEqual(
            set(promotions), set(user.promotion for user in User.objects.all())
        )