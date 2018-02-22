from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
      __tablename__ = 'users'

      id = db.Column(db.Integer,primary_key=True)
      username = db.Column(db.String(255))
      role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
      email = db.Column(db.String(255),unique = True,index = True)
      password_hash = db.Column(db.String(255))

      bookings = db.relationship('Booking', backref='user', lazy='dynamic')

      @property
      def password(self):
            raise AttributeError('You cannot read the password attribute')

      @password.setter
      def password(self, password):
            self.password_hash = generate_password_hash(password)

      def verify_password(self, password):
            return check_password_hash(self.password_hash,password)

      def __repr__(self):
            return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'User {self.role_name}'

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone_number = db.Column(db.Integer)
    time_stamp = db.Column(db.Time,default=datetime.utcnow())

    def save_booking(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_booking(cls, user_id):
        bookings = Booking.query.order_by(Booking.id.desc()).filter_by(user_id=user_id).all()

        return bookings

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    cost = db.Column(db.Integer)
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    booking = db.relationship('Booking', backref='events', lazy='dynamic')

    def save_event(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_event(cls, id):
        events = Event.query.filter_by(id=id).all()

        return events
        
    