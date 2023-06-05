class TestBookingPage:
    def test_with_good_club_and_good_competition(self, client):
            response = client.get('/book/Fall Classic/Iron Temple')
            assert response.status_code == 200

    def test_with_wrong_club_and_good_competition(self, client):
        response = client.get('/book/Fall Classic/Wrong Club', follow_redirects=True)
        data = response.data.decode()
        assert "Welcome to the GUDLFT Registration Portal!" in data

    def test_with_wrong_club_and_good_competition(self, client):
        response = client.get('/book/Wrong Competition/Iron Temple', follow_redirects=True)
        data = response.data.decode()
        assert "Welcome to the GUDLFT Registration Portal!" in data

