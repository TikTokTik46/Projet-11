#FEATURE: When the user is connected, clubs name and points should be visible #05

class TestClubsInWelcomePage:

    def test_clubs_in_welcome_page(self, client, load_clubs_fixture,
                                load_competitions_fixture):
        response = client.post(
            "/showSummary",
            data={"email": "admin@irontemple.com"}, follow_redirects=True
        )
        data = response.data.decode()
        for club in load_clubs_fixture["clubs"]:
            assert club["points"] in data and club["name"] in data

