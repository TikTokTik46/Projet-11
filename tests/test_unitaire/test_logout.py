class TestLogout:
    def test_logout(self, client):
            response = client.post('/showSummary', data={'email': 'admin@irontemple.com'})
            assert response.status_code == 200
            response = client.get('/logout', follow_redirects=True)
            data = response.data.decode()
            assert "Welcome to the GUDLFT Registration Portal!" in data


