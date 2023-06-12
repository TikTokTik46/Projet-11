import html

def test_login_book_purchase_logout(client, load_clubs_fixture,
                                    load_competitions_fixture):

    # Connexion
    response = client.post('/showSummary',
                           data={'email': 'admin@irontemple.com'})
    data = response.data.decode()
    decoded_data = html.unescape(data)
    assert response.status_code == 200
    assert 'Welcome, admin@irontemple.com' in decoded_data

    # Réservation
    response = client.get('/book/Fall Classic/Iron Temple')
    assert response.status_code == 200
    assert 'Valid competition' in response.data.decode()

    # Achat
    response = client.post('/purchasePlaces', data={
        'competition': 'Fall Classic',
        'club': 'Iron Temple',
        'places': 3
    }, follow_redirects=True)
    data = response.data.decode()
    decoded_data = html.unescape(data)
    assert response.status_code == 200
    assert 'Great-booking complete!' in decoded_data

    # Déconnexion
    response = client.get('/logout', follow_redirects=True)
    data = response.data.decode()
    assert "Welcome to the GUDLFT Registration Portal!" in data