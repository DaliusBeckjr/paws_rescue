from flask_app.config.mysqlconnetcion import connectToMySQL

from flask_app.models.rescue import Rescue

class Like:
    db = 'paws_rescue_schema'

    def __init__(self, data):
        self.user_id = data['user_id']
        self.rescue_id = data['rescue_id']

# think about it like we are creating a like in the db
    @classmethod
    def user_like_rescue(cls, data):
        query = """
        INSERT INTO likes(user_id, rescue_id)
        VALUES (%(user_id)s, %(rescue_id)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)

# think of it as user is deleting a like from the db
    @classmethod
    def user_unlike_rescue(cls, data):
        query = """
        DELETE FROM likes
        WHERE user_id = %(user_id)s
        AND rescue_id = %(rescue_id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)

# was thinking what if the user only wanted to see all of their liked animals
    @classmethod
    def get_liked_rescues_by_user(cls, data):
        query = """
        SELECT * from rescues
        JOIN likes ON rescues.id = likes.rescue_id
        WHERE likes.user_id = %(user_id)s
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        rescues = []
        for row in results:
            rescues.append(Rescue(row))
        return rescues



# wouldn't we want to check if it is liked 
    @classmethod
    def check_if_liked(cls, data):
        query = """
        SELECT * FROM likes
        WHERE user_id = %(user_id)s
        AND rescue_id = %(rescue_id)s;
        """
        result = connectToMySQL(cls.db).query_db(query, data)
        return len(result) > 0