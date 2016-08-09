from dogbreed.models import *
from dogbreed.exceptions import *


class Actions(object):

    @classmethod
    def get_all_dogs(cls, order_by=None):
        """
        Retrieves all dogs optionally ordered/grouped by breed name, or vote count

        :param order_by: optional param to determine order by either breed, votes, or None (default)
        :type order_by: string
        :return: list of dogs with nested breed and votes if any
        :rtype: list of dicts
        """
        if order_by == 'breed':
            # order by breed (ascending)
            dogs = db.session.query(Dog).join(Breed).outerjoin(Vote).options(contains_eager(Dog.breed), contains_eager(Dog.votes)).order_by(Breed.breed_name.asc()).all()
        elif order_by == 'votes':
            # order by votes (descending)
            dogs = db.session.query(Dog).join(Breed).outerjoin(Vote).options(contains_eager(Dog.breed), contains_eager(Dog.votes)).order_by(Vote.counter.desc()).all()
        else:
            # in no particular order
            dogs = Dog.query.all()
        return [dog.as_dict(fields_to_expand=['breed','votes']) for dog in dogs]

    @classmethod
    def get_dog(cls, dog_id):
        """
        Retrieves a single dog by dog id

        :param dog_id: required dog id of dog to retrieve
        :type dog_id: integer
        :return: dog with nested breed and votes if any
        :rtype: dict
        """
        dog = Dog.query.filter_by(id=dog_id).first()
        return dog.as_dict(fields_to_expand=['breed','votes'])

    @classmethod
    def get_all_breeds(cls):
        """
        Retrieves all breeds

        :return: list of breeds
        :rtype: list of dicts
        """
        breeds = Breed.query.all()
        return [breed.as_dict() for breed in breeds]

    @classmethod
    def get_all_dogs_by_breed(cls, breed_id):
        """
        Retrieves all dogs by breed id

        :param breed_id: required breed id of dogs to retrieve
        :type breed_id: integer
        :return: list of dogs with nested breed and votes if any
        :rtype: list of dicts
        """
        dogs = Dog.query.filter_by(breed_id=breed_id).all()
        return [dog.as_dict(fields_to_expand=['breed','votes']) for dog in dogs]

    @classmethod
    def submit_dog_vote(cls, dog_id, user_agent):
        """
        Submits a dog vote.  Only allows one vote per user.

        :param dog_id: required dog id of dog to vote for
        :type dog_id: integer
        :param user_agent: unique identifier (user agent) of voter to prevent multiple vote casting
        :type user_agent: string
        :return: new vote count of dog that was voted for
        :rtype: dict
        """
        client = Client.query.filter_by(client_name=user_agent).first()
        if client:
            # user already voted
            # raise a NotAllowed custom exception which will be translated into a HTTP 403
            raise NotAllowed("User already voted")
        client = Client(client_name=user_agent)
        db.session.add(client)
        db.session.commit()
        vote = Vote.query.filter_by(dog_id=dog_id).first()
        if not vote:
            vote = Vote(dog_id=dog_id, counter=1)
            db.session.add(vote)
        else:
            vote.counter = Vote.counter + 1  # this prevents a race condition rather than letting python increment using +=
        db.session.commit()
        return {'vote': vote.counter}
