#ERROR: Clubs should not be able to book places on a competition that has happened in the past  #05

class TestCompetitionDate:

    def test_purchase_competition_with_valid_date(self, client, load_clubs_fixture,
                                load_competitions_fixture):
        response = client.post(
            "/showSummary",
            data={"email": "admin@irontemple.com"}, follow_redirects=True
        )
        assert response.status_code == 200
        response = client.get(
            "/book/"
            + load_competitions_fixture["competitions"][1]["name"]
            + "/"
            + load_clubs_fixture["clubs"][1]["name"]
        )
        data = response.data.decode()
        assert "Valid competition" in data

    def test_purchase_competition_without_valid_date(self, client, load_clubs_fixture,
                                load_competitions_fixture):
        response = client.post(
            "/showSummary",
            data={"email": "admin@irontemple.com"}, follow_redirects=True
        )
        assert response.status_code == 200
        response = client.get(
            "/book/"
            + load_competitions_fixture["competitions"][0]["name"]
            + "/"
            + load_clubs_fixture["clubs"][1]["name"]
        )
        data = response.data.decode()
        assert "This competition is closed." in data