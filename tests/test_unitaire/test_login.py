import html
#ERROR: Entering a unknown email crashes the app #01
class TestLogin:
    def test_login_with_email_in_data(self, client):
            response = client.post('/showSummary', data={'email': 'admin@irontemple.com'})
            assert response.status_code == 200


    def test_login_with_email_not_in_data(self, client):
            response = client.post('/showSummary', data={'email': 'wrong_adress@gmail.com'}, follow_redirects=True)
            data = response.data.decode()
            decoded_data = html.unescape(data)
            assert "Cette adresse e-mail n'est pas présente dans la base de données" in decoded_data
            assert response.status_code == 200

