#ERROR: Entering a unknown email crashes the app #01
class TestLogin:
    def test_login_with_email_in_data(self, client):
            response = client.post('/showSummary', data={'email': 'admin@irontemple.com'})
            assert response.status_code == 200

    def test_login_with_email_not_in_data(self, client):
            response = client.post('/showSummary', data={'email': 'wrong_adress@gmail.com'})
            assert response.status_code == 302
            assert response.location == 'http://localhost/'

