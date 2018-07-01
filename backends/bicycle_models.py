

from google.appengine.ext import ndb


class Wheel(ndb.Model):
    """
    wheel.to_dict()
    """
    name = ndb.StringProperty()


class Saddle(ndb.Model):
    name = ndb.StringProperty()


class Frame(ndb.Model):
    name = ndb.StringProperty()


class Chain(ndb.Model):
    name = ndb.StringProperty()


class Fork(ndb.Model):
    name = ndb.StringProperty()


class Brake(ndb.Model):
    name = ndb.StringProperty()


class Bicycle(ndb.Model):
    wheels = ndb.StructuredProperty(Wheel, repeated=True)
    saddle = ndb.StructuredProperty(Saddle, repeated=True)
    frame = ndb.StructuredProperty(Frame, repeated=True)
    chain = ndb.StructuredProperty(Chain, repeated=True)
    fork = ndb.StructuredProperty(Fork, repeated=True)
    brakes = ndb.StructuredProperty(Brake, repeated=True)
