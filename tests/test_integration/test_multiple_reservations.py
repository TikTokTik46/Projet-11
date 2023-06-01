import html

def test_max_places_per_club(client, load_clubs_fixture, load_competitions_fixture):
    # Effectuer la première réservation de 7 places
    response = client.post(
        "/purchasePlaces",
        data={
            "competition": load_competitions_fixture["competitions"][0]["name"],
            "club": load_clubs_fixture["clubs"][0]["name"],
            "places": 7,
        },
    )
    assert "Great-booking complete!" in response.data.decode()

    # Effectuer la deuxième réservation de 6 places (dépassement du maximum)
    response = client.post(
        "/purchasePlaces",
        data={
            "competition": load_competitions_fixture["competitions"][0]["name"],
            "club": load_clubs_fixture["clubs"][0]["name"],
            "places": 6,
        },
    )
    data = response.data.decode()
    decoded_data = html.unescape(data)
    assert "You can't book more than 12 places in one competition" in decoded_data