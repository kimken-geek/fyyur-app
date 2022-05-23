from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Artist(db.Model):
      __tablename__ = 'artists'

      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String)
      city = db.Column(db.String(120))
      state = db.Column(db.String(120))
      phone = db.Column(db.String(120))
      genres = db.Column(db.ARRAY(db.String))
      facebook_link = db.Column(db.String(120))
      image_link = db.Column(db.String(500))
      website = db.Column(db.String(120))
      seeking_venue = db.Column(db.Boolean)
      seeking_description = db.Column(db.String(500))
      shows = db.relationship('Show', backref="artist", lazy=True)

      def __repr__(self):
            return f'<Artist {self.id} {self.name}>'
          
class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def __repr__(self):
        return f'<Show {self.id} {self.artist_id} {self.venue_id} {self.start_time}>'
