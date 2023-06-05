class TestIndex:
    def test_index(self, client):
            response = client.get('/')
            data = response.data.decode()
            assert "Welcome to the GUDLFT Registration Portal!" in data

