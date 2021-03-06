from flask import render_template, request, redirect, url_for, abort 
from flask_login import login_required,current_user 
from . import main  
from .forms import BookingForm
from ..models import Event, Role,User,Booking
from .. import db

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Zuru Ke'

    events = Event.query.all()
    
    return render_template('index.html', title = title,events=events)

@main.route('/event/<int:id>', methods=['GET','POST'])
@login_required
def events(id):

    form = BookingForm()

    if form.validate_on_submit():
        name = form.event_name.data
        email = form.email.data
        phone_number = form.phone_number.data
        new_booking = Booking(email=email,name=name,phone_number=phone_number,event_id=id,user=current_user._get_current_object() )

        new_booking.save_booking()
        return redirect(url_for('main.index'))

    event = Event.query.filter_by(id=id).first()
    
    title = f'{event.event_name}'
    
    return render_template('event.html', title=title, event=event, booking_form=form)