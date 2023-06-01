import json
import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        for Competition in listOfCompetitions:
            Competition['clubsBookedPlaces'] = {}
        return listOfCompetitions


def create_app(config={}):
    app = Flask(__name__)
    app.config.from_object(config)

    app.config.update(config)
    app.secret_key = "something_special"

    competitions = loadCompetitions()
    clubs = loadClubs()

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary', methods=['POST'])
    def showSummary():
        try:
            club = \
                [club for club in clubs if
                 club['email'] == request.form['email']][
                    0]
            return render_template('welcome.html', club=club, clubs=clubs,
                                   competitions=competitions)
        except IndexError:
            flash("Cette adresse e-mail n'est pas présente "
                  "dans la base de données", 'error')
            return redirect(url_for('index'))

    @app.route('/book/<competition>/<club>')
    def book(competition, club):
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = \
        [c for c in competitions if c['name'] == competition][0]
        competitionDate = datetime.datetime.strptime(foundCompetition['date'],
                                                     '%Y-%m-%d %H:%M:%S')
        if foundClub and foundCompetition:
            if competitionDate > datetime.datetime.now():
                flash("Valid competition")
                return render_template('booking.html', club=foundClub,
                                       competition=foundCompetition)
            else:
                flash("This competition is closed.")
                return render_template(
                    "welcome.html", club=foundClub, competitions=competitions,
                    clubs=clubs
                )
        else:
            flash("Something went wrong-please try again")
            return render_template('welcome.html', club=club, clubs=clubs,
                                   competitions=competitions)

    @app.route('/purchasePlaces', methods=['POST'])
    def purchasePlaces():
        competition = \
        [c for c in competitions if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        placesRequired = int(request.form['places'])

        if club['name'] in competition['clubsBookedPlaces']:
            placesAlreadyReserved = competition['clubsBookedPlaces'][club['name']]
        else:
            placesAlreadyReserved = 0
        remainingPlaces = 12 - placesAlreadyReserved

        if placesRequired > int(club['points']):
            flash("You don\'t have enough points")
            return render_template('booking.html', club=club,
                                   competition=competition)
        elif placesRequired > remainingPlaces:
            flash("You can\'t book more than 12 places in one competition")
            return render_template('booking.html', club=club,
                                   competition=competition)
        else:
            competition['numberOfPlaces'] = int(
                competition['numberOfPlaces']) - placesRequired
            competition['clubsBookedPlaces'].update(
                {club['name']: placesAlreadyReserved + placesRequired})
            club['points'] = int(
                club['points']) - placesRequired
            flash('Great-booking complete!')

        return render_template('welcome.html', club=club, clubs=clubs,
                               competitions=competitions)

    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))

    return app
