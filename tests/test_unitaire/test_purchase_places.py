import html

class TestPurchase:

    def test_purchase_more_than_points_available(self, client,
                                                 load_clubs_fixture,
                                                 load_competitions_fixture):
        response = client.post(
            "/showSummary",
            data={"email": "admin@irontemple.com"}, follow_redirects=True
        )
        assert response.status_code == 200
        response = client.post(
            "/purchasePlaces",
            data={
                "competition": load_competitions_fixture["competitions"][1]["name"],
                "club": load_clubs_fixture["clubs"][1]["name"],
                "places": 5,
            },
        )
        data = response.data.decode()
        # La fonction ci-dessous permet de permetre la lecture des caractéres encodés sur les pages HTML
        decoded_data = html.unescape(data)
        assert "You don't have enough points" in decoded_data

    def test_purchase_less_or_equal_than_points_available(self, client,
                                                 load_clubs_fixture,
                                                 load_competitions_fixture):
        response = client.post(
            "/showSummary",
            data={"email": "admin@irontemple.com"}, follow_redirects=True
        )
        assert response.status_code == 200
        response = client.post(
            "/purchasePlaces",
            data={
                "competition": load_competitions_fixture["competitions"][1]["name"],
                "club": load_clubs_fixture["clubs"][1]["name"],
                "places": 3,
            },
        )
        data = response.data.decode()
        assert "Great-booking complete!" in data
        assert "Points available: 1" in data

    def test_purchase_more_than_twelve_places(self, client,
                                                 load_clubs_fixture,
                                                 load_competitions_fixture):
        response = client.post(
            "/showSummary",
            data={"email": "john@simplylift.co"}, follow_redirects=True
        )
        assert response.status_code == 200
        response = client.post(
            "/purchasePlaces",
            data={
                "competition": load_competitions_fixture["competitions"][1]["name"],
                "club": load_clubs_fixture["clubs"][0]["name"],
                "places": 13,
            },
        )
        data = response.data.decode()
        decoded_data = html.unescape(data)
        assert "You can't book more than 12 places in one competition" in decoded_data

