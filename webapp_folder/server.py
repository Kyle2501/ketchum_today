#!/usr/bin/env python
# -*- coding: latin-1 -*-


Site = 'Ketchum.today'

Stripe_key = ''


# - System
import os
import cgi
import urllib2, urllib, json
import wsgiref.handlers
import datetime
import time

# - Appengine
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import images
from urlparse import urlparse
# -
from google.appengine.ext import db
from google.appengine.ext import ndb
import webapp2
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp.util import run_wsgi_app

from pytz.gae import pytz # . timezones

import html_page_code as html
import account_code as html_account
import publish_code as html_publish

import stripe


class User_db(db.Model):
    addTime = db.DateTimeProperty(auto_now_add=True)
    user = db.UserProperty()
    flag = db.StringProperty()
    visibility = db.StringProperty()
    data_type = db.StringProperty()
    data_id = db.StringProperty()
  # -
    user_id = db.StringProperty()
    user_name = db.StringProperty()

  # -
    payment_status = ndb.StringProperty()
    payment_rate = ndb.StringProperty()


class addUser(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        date_time = datetime.datetime.now(pytz.timezone('US/Mountain')).strftime("%Y%m%d_%H%M%S")
        data_id = date_time
        item = User_db(key_name=data_id)
        if users.get_current_user():
            user_id = user.user_id()
            user_name = user.nickname()
            data_id = date_time + '_' + user_id
            item.user = users.get_current_user()
            item.user_name = user_name
            item.user_id = user_id
        else:
            user_name = 'No User'
            item.user_name = user_name
      #
        item.data_id = data_id
        item.data_type = 'user_data'
        item.visibility = 'show'
        item.flag = '-'
        item.put()
        self.redirect('/account')

class editUser(webapp2.RequestHandler):
    def post(self):
        user_id = base.split('?')[1]
        item = db.Query(User_db).filter('user_id =', user_id).get()
        user = users.get_current_user()

        item.user_name = self.request.get('user_name')
        item.put()
        self.redirect('/account')


regular_page_layout = 'hi test'


#----------------------------------------------#
#            Page Data Stucture                #
#----------------------------------------------#
class Page_db(ndb.Model):
    addTime = ndb.DateTimeProperty(auto_now_add=True)
    flag = ndb.StringProperty()
    visibility = ndb.StringProperty()
#
    data_type = ndb.StringProperty()
    data_id = ndb.StringProperty()
# -
    user_id = ndb.StringProperty()
    user_name = ndb.StringProperty()
# -
    page_id = ndb.StringProperty()
    page_class = ndb.StringProperty()
    page_type = ndb.StringProperty()
    page_kind = ndb.StringProperty()
    
# -
    page_name = ndb.StringProperty()
    page_phone = ndb.StringProperty()
    page_email = ndb.StringProperty()
#
    page_url_link = ndb.StringProperty()
    page_facebook = ndb.StringProperty()
    page_youtube = ndb.StringProperty()
    page_instagram = ndb.StringProperty()
    page_twitter = ndb.StringProperty()
# -
    page_html = ndb.TextProperty()
    page_logo = ndb.BlobProperty()
    has_logo = ndb.StringProperty()
    
    
    @classmethod
    def _get_page_list(self):
      q = Page_db.query()
      db_data = []
      for item in q.iter():
        db_data.append(item.to_dict(exclude=['addTime']))
      return json.dumps(db_data)


    @classmethod
    def _get_own_page(self,data_id):
      if data_id == users.get_current_user().user_id():
        item = Page_db.query(Page_db.user_id == data_id).get()
      if item:
        db_data = item.to_dict(exclude=['addTime'])
      else: 
        db_data = None
      return json.dumps(db_data)
  
    @classmethod
    def _get_one_data(self,data_id):
      item = Page_db.get_by_id(data_id)
      if item:
        db_data = item.to_dict(exclude=['addTime'])
      else: 
        db_data = None
      return json.dumps(db_data)


class registerNew_Page_db(webapp2.RequestHandler):
    def post(self):
# -
        date_time = datetime.datetime.now(pytz.timezone('US/Mountain')).strftime("%Y%m%d%H%M%S")
        data_id = date_time
        
        item = Page_db(id=data_id)
# -
        user = users.get_current_user()
        if users.get_current_user():
            user_id = user.user_id()
            user_name = user.nickname()
            item.user_name = user_name
            item.user_id = user_id
        else:
            user_name = 'No User'
            user_id = 'none'
            item.user_name = user_name

    # -
        item.visibility = 'hide'
        item.flag = '-'
        item.data_type = 'page_data'
        item.data_id = data_id

    # -
        item.page_id = data_id
        item.page_class = 'regular_page'
        item.page_type = 'regular_page'
        item.page_kind = 'regular_page'
        item.page_html = '-'
# -
        page_name = self.request.get('page_name')
        if page_name:
            item.page_name = page_name
        else:
            item.page_name = user_name

    # -

    # -
        item.put()
        self.redirect('/pages/welcome')



class editPageHTML_db(webapp2.RequestHandler):
  def post(self):

    user = users.get_current_user()
    if user:
      user_id = user.user_id()
      account_id = user_id
      data_id = self.request.get('data_id')
      if data_id and data_id != '':
        item = Page_db.get_by_id(data_id)
        self.redirect('/error_page')
      else:
        self.redirect('/error_page')
        return
      
      item.page_html = self.request.get('page_html')

      item.put()
      time.sleep(1)

    self.redirect('/pages/welcome')



class registerNew_Page_db_old(webapp2.RequestHandler):
    def post(self):
# -
        date_time = datetime.datetime.now(
            pytz.timezone('US/Mountain')).strftime("%Y%m%d_%H%M%S")
        data_id = date_time
        
# -
        user = users.get_current_user()
        if users.get_current_user():
            user_id = user.user_id()
            user_name = user.nickname()
            data_id = date_time + '_' + user_id
            item = Page_db(id=user_id)
            item.user_name = user_name
            item.user_id = user_id
        else:
            user_name = 'No User'
            user_id = 'none'
            item = Page_db(id=user_id)
            item.user_name = user_name
        
    # -
        item.visibility = 'hide'
        item.flag = '-'
# -
        page_name = self.request.get('page_name')
        if page_name:
            item.page_name = page_name
        else:
            item.page_name = data_id + ' ' + user_name
        item.page_link = self.request.get('page_link')
        item.page_phone = self.request.get('page_phone')
        item.page_email = self.request.get('page_email')

    # -
        item.page_id = data_id + '_' + user_name
        item.page_class = 'regular_page'
    # - 
        item.page_phone = self.request.get('page_phone')
        item.page_email = self.request.get('page_email')
    #
        item.page_url_link = self.request.get('page_url_link')
        item.page_facebook = self.request.get('page_facebook')
        item.page_youtube = self.request.get('page_youtube')
        item.page_instagram = self.request.get('page_instagram')
        item.page_twitter = self.request.get('page_twitter')
    # -

    #
        item.page_html = regular_page_layout

    # -
        page_logo = self.request.get('page_logo')
        if page_logo:
          item.page_logo = images.resize(page_logo, 800, 600)
          item.has_logo = 'yes'
        else:
          if not item.page_logo:
            item.has_logo = 'no'
    # -
        item.put()
        self.redirect('/pages/welcome')


class editPage(webapp2.RequestHandler):
    def post(self):
        page_id = base.split('?')[1]
        item = db.Query(Page_db).filter('page_id =', page_id).get()
        user = users.get_current_user()
        
        item.page_name = self.request.get('page_name')
        item.page_html = self.request.get('page_html')
        item.put()
        self.redirect('/pages')







class News_db(db.Model):
    addTime = db.DateTimeProperty(auto_now_add=True)
    user = db.UserProperty()
    flag = db.StringProperty()
    visibility = db.StringProperty()
    data_type = db.StringProperty()
    data_id = db.StringProperty()
  # -
    user_id = db.StringProperty()
    user_name = db.StringProperty()
    article_id = db.StringProperty()
    article_class = db.StringProperty()
    article_headline = db.StringProperty()
    article_bodytext = db.TextProperty()
    
class addNews(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        date_time = datetime.datetime.now(pytz.timezone('US/Mountain')).strftime("%Y%m%d_%H%M%S")
        data_id = date_time
        item = News_db(key_name=data_id)
        if users.get_current_user():
            user_id = user.user_id()
            user_name = user.nickname()
            data_id = date_time + '_' + user_id
            item.user = users.get_current_user()
            item.user_name = user_name
            item.user_id = user_id
        else:
            user_name = 'No User'
            item.user_name = user_name
        article_headline = self.request.get('article_headline')
        if article_headline:
            item.article_headline = article_headline
        else:
            item.article_headline = data_id + ' ' + user_name
        item.article_bodytext = self.request.get('article_bodytext')
        item.article_id = data_id
      #
        item.data_id = data_id
        item.data_type = 'news_data'
        item.visibility = 'show'
        item.flag = '-'
        item.put()
        self.redirect('/news')

class editNews(webapp2.RequestHandler):
    def post(self):
        article_id = base.split('?')[1]
        item = db.Query(News_db).filter('article_id =', article_id).get()
        user = users.get_current_user()

        item.article_headline = self.request.get('article_headline')
        item.article_bodytext = self.request.get('article_bodytext')
        item.put()
        self.redirect('/news')


class Event_db(db.Model):
    addTime = db.DateTimeProperty(auto_now_add=True)
    user = db.UserProperty()
    flag = db.StringProperty()
    visibility = db.StringProperty()
    data_type = db.StringProperty()
    data_id = db.StringProperty()
  # -
    user_id = db.StringProperty()
    user_name = db.StringProperty()
    event_id = db.StringProperty()
    event_class = db.StringProperty()
    event_name = db.StringProperty()
    event_start_date = db.StringProperty()
    event_start_time = db.StringProperty()
    event_info = db.TextProperty()
    
class addEvent(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        date_time = datetime.datetime.now(pytz.timezone('US/Mountain')).strftime("%Y%m%d_%H%M%S")
        data_id = date_time
        item = Event_db(key_name=data_id)
        if users.get_current_user():
            user_id = user.user_id()
            data_id = date_time + '_' + user_id
            user_data = db.Query(User_db).filter('user_id =', user_id).get()
            if user_data:
                user_name = user_data.user_name
            else:
                user_name = user.nickname()
            item.user = users.get_current_user()
            item.user_name = user_name
            item.user_id = user_id
        else:
            user_name = 'No User'
            item.user_name = user_name
        event_name = self.request.get('event_name')
        if event_name:
            item.event_name = event_name
        else:
            item.event_name = data_id + ' ' + user_name
        item.event_start_date = self.request.get('event_start_date')
        item.event_start_time = self.request.get('event_start_time')
        item.event_info = self.request.get('event_info')
        item.event_id = data_id
      #
        item.data_id = data_id
        item.data_type = 'event_data'
        item.visibility = 'show'
        item.flag = '-'
        item.put()
        self.redirect('/events')

class editEvent(webapp2.RequestHandler):
    def post(self):
        event_id = base.split('?')[1]
        item = db.Query(Event_db).filter('event_id =', event_id).get()
        user = users.get_current_user()

        item.event_name = self.request.get('event_name')
        item.event_start_date = self.request.get('event_start_date')
        item.event_start_time = self.request.get('event_start_time')
        item.event_info = self.request.get('event_info')
        item.put()
        self.redirect('/events')


class listData_1(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        page_address = self.request.uri
        uri = urlparse(page_address)
        subdomain = uri.hostname.split('.')[0]
        date_today = datetime.datetime.now(pytz.timezone('US/Mountain')).strftime("%Y-%m-%dT%H:%M:%S")
        base = os.path.basename(page_address)
        if base == 'news':
            q = db.Query(News_db, projection=('data_type', 'data_id', 'article_id', 'article_headline'))
            db_data = q.filter('visibility =', 'show').fetch(50)
        if base == 'events':
            q = db.Query(Event_db, projection=('data_type', 'data_id', 'event_id', 'event_name', 'event_start_time'))
            db_data = q.filter('visibility =', 'show').fetch(50)
        if base == 'pages':
            q = db.Query(Page_db, projection=('data_type', 'data_id', 'page_id', 'page_name', 'event_start_time', 'event_info'))
            db_data = q.filter('visibility =', 'show').fetch(50)
        data = []
        for f in db_data:
            data.append(db.to_dict(f))
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(data))


class weatherData(webapp2.RequestHandler):
    def get(self):
        
        
        weather_data = ''
        weather_today_text = ''
        weather_today_temp = ''
        weather_today_humidity = ''
        weather_today_visibility = ''
        weather_today_sunset = ''
        
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select * from weather.forecast where woeid=2431969"
        yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"

#      result = urllib2.urlopen(yql_url).read()
#      data = json.loads(result)
#      weather_data = data['query']['results']
#      weather_today_text = data['query']['results']['channel']['item']['condition']['text']
#      weather_today_temp = data['query']['results']['channel']['item']['condition']['temp']
#      weather_today_humidity = data['query']['results']['channel']['atmosphere']['humidity']
#      weather_today_visibility = data['query']['results']['channel']['atmosphere']['visibility']
#      weather_today_sunset = data['query']['results']['channel']['astronomy']['sunset']






#----------------------------------------------#
#             Payment Records                  #
#----------------------------------------------#
class chargeCard(webapp2.RequestHandler):
  def post(self):

    # - stripe key and plan
    stripe.api_key = Stripe_key

    # stripe.Plan.create(
    #   amount=55000,
    #   interval='month',
    #   name='Platinum',
    #   currency='usd',
    #   id='Platinum')

    # stripe.Plan.create(
    #   amount=33000,
    #   interval='month',
    #   name='Gold',
    #   currency='usd',
    #   id='Gold')

    # stripe.Plan.create(
    #   amount=20000,
    #   interval='month',
    #   name='Silver',
    #   currency='usd',
    #   id='Silver')

    # stripe.Plan.create(
    #   amount=10000,
    #   interval='day',
    #   name='Bronze',
    #   currency='usd',
    #   id='Bronze')

    # Get the credit card details submitted by the form
    token = self.request.POST['stripeToken']
    client_email = users.get_current_user().email()
    # data_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if not Client_db._in_this_db(client_email):
      item = Client_db(id=client_email)
    else:
      item = Client_db.get_by_id(client_email)
 
    item.client_name = self.request.get('client_name')
    item.client_email = self.request.get('client_email')
    item.client_program = self.request.get('client_program')
    item.client_phone = self.request.get('client_phone')
    item.client_address = self.request.get('client_address')
    if not item.client_photo:
      item.has_photo = False
    item.add_time = datetime.datetime.now(pytz.timezone(Timezone)).strftime("%Y/%m/%d %H:%M:%S")
    
    # - create stripe customer
    try:
      customer = stripe.Customer.create(
      source=token,
      plan=item.client_program,
      email=item.client_email
      )
    except stripe.error.CardError, e:
        self.response.out.write(str(e)) 
    except stripe.error.RateLimitError, e:
        self.response.out.write(str(e)) 
    except stripe.error.InvalidRequestError, e:
        self.response.out.write(str(e)) 
    except stripe.error.AuthenticationError, e:
        self.response.out.write(str(e)) 
    except stripe.error.APIConnectionError, e:
        self.response.out.write(str(e)) 
    except stripe.error.StripeError, e:
        self.response.out.write(str(e)) 
    else:
      item.program_status = 'Active'
      item.stripe_cus_id = customer["id"]
      item.stripe_subscription_id = customer["subscriptions"]["data"][0]["id"]
      item.put()

      self.redirect('/payment_success')

class cancelProgram(webapp2.RequestHandler):
  def get(self):

# - stripe key 
    stripe.api_key = Stripe_key

    if users.get_current_user():
      client_email = users.get_current_user().email()
      item = Client_db.get_by_id(client_email)
      
      try:
        customer = stripe.Customer.retrieve(item.stripe_cus_id)
        customer.subscriptions.retrieve(item.stripe_subscription_id).delete()
      except stripe.error.CardError, e:
        self.response.out.write(str(e)) 
      except stripe.error.RateLimitError, e:
        self.response.out.write(str(e)) 
      except stripe.error.InvalidRequestError, e:
        self.response.out.write(str(e)) 
      except stripe.error.AuthenticationError, e:
        self.response.out.write(str(e)) 
      except stripe.error.APIConnectionError, e:
        self.response.out.write(str(e)) 
      except stripe.error.StripeError, e:
        self.response.out.write(str(e)) 
      else:
        item.program_status = 'Canceled'
        item.put()
        self.redirect('/cancel_program_success')

def cancelProgram_admin(client_email):
    #- stripe key 
    stripe.api_key = Stripe_key

    item = Client_db.get_by_id(client_email)
    if item.program_status == 'Active' and item.stripe_cus_id and item.stripe_subscription_id:
      try:
        customer = stripe.Customer.retrieve(item.stripe_cus_id)
        customer.subscriptions.retrieve(item.stripe_subscription_id).delete()
      except stripe.error.CardError, e:
        return str(e) 
      except stripe.error.RateLimitError, e:
        return str(e) 
      except stripe.error.InvalidRequestError, e:
        return str(e) 
      except stripe.error.AuthenticationError, e:
        return str(e) 
      except stripe.error.APIConnectionError, e:
        return str(e) 
      except stripe.error.StripeError, e:
        return str(e) 
      else:
        item.program_status = 'Canceled'
        item.put()
        return 'success'

class redirect2Payment(webapp2.RequestHandler):
  def get(self):
    program_chosen = self.request.get('program_chosen')
    url = "http://payment.shannycohen.fitness/?program_chosen=" + program_chosen
    self.redirect(str(url), True)






class publicSite(webapp2.RequestHandler):
    def get(self):
   
# - Time Data
        timestamp = ''
        date_time = datetime.datetime.now(pytz.timezone('US/Mountain')).strftime("%A &nbsp; %b, %m %Y &nbsp; %I:%M %p")
        day = datetime.datetime.now(pytz.timezone('US/Mountain')).strftime("%A")
        date = datetime.datetime.now(pytz.timezone('US/Mountain')).strftime("%b, %m %Y")
        time = datetime.datetime.now(pytz.timezone('US/Mountain')).strftime("%I:%M %p")

# - Weather Data
        weather_data = ''
        weather_today_text = ''
        weather_today_temp = ''
        weather_today_humidity = ''
        weather_today_visibility = ''
        weather_today_sunset = ''
        
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select * from weather.forecast where woeid=2431969"
        yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
        
        result = urllib2.urlopen(yql_url).read()
        data = json.loads(result)
        weather_data = data['query']['results']
        
        weather_today_text = data['query']['results']['channel']['item']['condition']['text']
        weather_today_temp = data['query']['results']['channel']['item']['condition']['temp']
        weather_today_humidity = data['query']['results']['channel']['atmosphere']['humidity']
        weather_today_visibility = data['query']['results']['channel']['atmosphere']['visibility']
        weather_today_sunset = data['query']['results']['channel']['astronomy']['sunset']
        
# - Page URL Address
        page_address = self.request.uri
        url_path = urlparse(page_address)[2]
        path_layer = urlparse(page_address)[2].split('/')[1]
        base = os.path.basename(page_address)
        
# - User Data
        user = users.get_current_user()
        if users.get_current_user(): # - logged in
            login_key = users.create_logout_url(self.request.uri)
            gate = 'Sign out'
            user_name = user.nickname()
        else: # - logged out
            login_key = users.create_login_url(self.request.uri)
            gate = 'Sign in'
            user_name = 'No User'

        
# - Page Data
        app = Site
        page_ads = html.google_ad + html.register_ad
        
        item_id = ''
        item_list = ''
        item_data = ''
        item_owner = ''
        
        account_id = ''
        
 
 # - Main Site Pages
        Page = 'Front'
        page_id = 'front_page'
        page_html = html.front_page
        page_ads = page_ads
        page_class = 'main'
        ad_class = 'yes'
        nav_select = 'tempeture'

        html_file = 'mainPage'


# - Pages Page

        if path_layer == 'page_layout':
            page_id = 'pages'
            nav_select = 'pages'
            page_html = html.page_layout_template_html + page_ads
            timestamp = 'true'
        
        
        if path_layer == 'page':
            page_id = 'page'
            page_html = html.page_item + page_ads
            nav_select = 'pages'
            item_id = base.split('?')[1]
            account_id = item_id


        if path_layer == 'pages':
            page_id = 'pages'
            page_html = html.pages_page + page_ads
            nav_select = 'pages'
            timestamp = 'true'
            if base == 'register':
                page_id = 'register'
                nav_select = 'register'
                page_html = html_account.register_page_login
                if user:
                    page_html = html_account.register_page_name
            if base == 'welcome':
                page_id = 'welcome'
                nav_select = 'welcome'
                page_html = html_account.register_page_login
                if user:
                    page_html = html_account.new_page_welcome
                    nav_select = 'account'
                    user_id = user.user_id()
                    account_id = user_id
            if base == 'payment':
                page_id = 'payment'
                nav_select = 'payment'
                page_html = html.register_page_login_html
                if user:
                    page_html = html.page_payment_html



# - Maps Page
        if path_layer == 'maps':
            page_id = 'maps'
            page_class = 'no_ads'
            page_html = html.maps_page
            page_ads = ''
            ad_class = 'off'
            nav_select = 'maps'


# - News Page
        if path_layer == 'news':
            page_id = 'news'
            page_html = html.news_page + page_ads
            q = db.Query(News_db).order('-addTime')
            item_list = q.fetch(75)
            timestamp = 'true'
        
        if path_layer == 'article':
            page_class = 'sub'
            page_html = ''
            article_id = base.split('?')[1]
            item_data = db.Query(News_db).filter('article_id =', article_id).get()
            if user_name != 'No User':
                if user_name == item_data.user_name:
                    item_owner = 'true'


# - Events Page
        if path_layer == 'events':
            page_id = 'events'
            page_html = html.events_page + page_ads
            q = db.Query(Event_db).order('-addTime')
            item_list = q.fetch(75)
            timestamp = 'true'
            ad_class = 'off'

        if path_layer == 'create':
            page_id = 'create_intro'
            page_class = 'create'
            page_html = html.create_intro_html
            ad_class = 'off'
            if base == 'ads':
                page_id = 'create_ads'
                page_html = html.create_ads_html


# - Account Page
        if path_layer == 'account':
            page_id = 'account'
            page_html = html_account.account_page
            nav_select = 'account'
            if base == 'settings':
                page_id = 'account_settings'
                page_html = html_account.account_settings
            if base == 'price':
                page_id = 'account_price'
                page_html = html_account.account_price



# - Publish . Manage . Edit
        if path_layer == 'publish':
            page_id = 'publish_intro'
            ad_class = 'off'
            page_class = 'no_ads'
            page_html = html.publish_intro + page_ads
            if base == 'news':
                page_id = 'publish_news'
                page_html = ''
            if base == 'event':
                page_id = 'publish_event'
                page_html = html.publish_event
        
        if path_layer == 'edit':
            page_class = 'no_ads'
            ad_class = 'off'
            page_id = 'edit_page'
            page_html = html_publish.publish_page
            item_id = base.split('?')[1]
            user_id = user.user_id()
            account_id = user_id


        if path_layer == 'create':
            page_id = 'create_intro'
            page_class = 'create'
            page_html = html.create_intro_html
            ad_class = 'off'
            if base == 'ads':
                page_id = 'create_ads'
                page_html = html.create_ads_html


# - {{ Template }}
        page_objects = {
            'Site': app,

            'login_key': login_key,
            'gate': gate,
            'user_name': user_name,
        # -
            'date_time': date_time,
            'day': day,
            'date': date,
            'time': time,
        # -

            'timestamp': timestamp,
            'weather_today_sunset': weather_today_sunset,
            'weather_today_temp': weather_today_temp,
            'weather_today_text': weather_today_text,

          # - data
            'path_layer': path_layer,
            'Page': Page,
            'page_id': page_id,
            'page_class': page_class,            
            
            'page_html': page_html,
            'page_ads': page_ads,
            'ad_class': ad_class,
            'nav_select': nav_select,
            
            
            'account_id': account_id,
            
            'item_id': item_id,
            'item_list': item_list,
            'item_data': item_data,
            'item_owner': item_owner,
            
        }
      # - render and send to browser
        html_template = os.path.join(os.path.dirname(__file__),
             'html_template_files/%s.html') %html_file
        self.response.out.write(template.render(html_template, page_objects))



class listData_2(webapp2.RequestHandler):
    def get(self):

        user = users.get_current_user()
        date_today = datetime.datetime.now(pytz.timezone('US/Mountain')).strftime("%Y-%m-%dT%H:%M:%S")

        page_address = self.request.uri
        uri = urlparse(page_address)
        subdomain = uri.hostname.split('.')[0]
        base = os.path.basename(page_address)

        if base == 'news':
            q = db.Query(News_db, projection=('data_type', 'data_id', 'article_id', 'article_headline'))
            db_data = q.filter('visibility =', 'show').fetch(50)
        if base == 'events':
            q = db.Query(Event_db, projection=('data_type', 'data_id', 'event_id', 'event_name', 'event_start_time'))
            db_data = q.filter('visibility =', 'show').fetch(50)
            
        if base == 'pages':
            q = db.Query(Page_db, projection=('data_id', 'page_name'))
            db_data = q.fetch(50)

        data = []
        for f in db_data:
            data.append(db.to_dict(f))
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(data))

class listData(webapp2.RequestHandler):
    def get(self):
        page_address = self.request.uri
        base = os.path.basename(page_address)
        split_address = base.split('?')
        data_set = split_address[1]
        data_id = None
        if len(split_address) == 3:
          data_id = split_address[2]
    
        
        if data_set == 'page_code' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Page_db._get_own_page(data_id))
        
        if data_set == 'page_item' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Page_db._get_one_data(data_id))
        
        if data_set == 'account_page' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Page_db._get_own_page(data_id))

        if data_set == 'page_list' and not data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Page_db._get_page_list())
        
        if data_set == 'pages' and data_id:
          self.response.headers['Content-Type'] = 'application/json'
          self.response.out.write(Page_db._get_one_data(data_id))


app = webapp2.WSGIApplication([    # - Pages
    ('/', publicSite),
    ('/news/?', publicSite),
    ('/events/?', publicSite),
    ('/page/?', publicSite),
    ('/pages/?', publicSite),
    ('/page_layout/?', publicSite),
      ('/pages/register/?', publicSite),
      ('/register_new_page/?', registerNew_Page_db),
      ('/pages/welcome/?', publicSite),
      ('/pages/payment/?', publicSite),
    ('/maps/?', publicSite),
    ('/account/?', publicSite),
      ('/account/settings/?', publicSite),
      ('/account/price/?', publicSite),
                               
    ('/publish/?', publicSite),
      ('/publish/news/?', publicSite),
      ('/publish/event/?', publicSite),
    ('/edit/?', publicSite),

    ('/publish_news/?', addNews),
    ('/edit_news/?', editNews),

    ('/list/news/?', listData),
    ('/list/events/?', listData),
    ('/list/pages/?', listData),
    
    ('/list_data/?', listData),
    ('/save_html/?', editPageHTML_db),
    


# -
    ('/confirm_signup/?', publicSite),
    ('/redirect2payment/?', redirect2Payment),
    ('/payment/?', publicSite),
    ('/charge_card/?', chargeCard),
    ('/payment_success', publicSite),
    ('/cancel_program/?', cancelProgram),
    ('/cancel_program_success/?', publicSite),

], debug=True)

