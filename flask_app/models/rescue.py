from flask_app.config.mysqlconnetcion import connectToMySQL
from flask_app.models.user import User

class Rescue:
    db = "paws_rescue_schema"
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.breed = data['breed']
        self.location = data['location']
        self.age = data['age']
        self.gender = data['gender']
        self.size = data['size']
        self.fixed = data['fixed']
        self.type = data['type']
        self.image_path = data['image_path']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        # class association
        self.owner = None

    @classmethod 
    def create_rescue(cls, data):
        query = """ 
            INSERT INTO rescues
            (name, description, breed, location, age, gender, size, fixed, type, image_path, user_id)
            VALUES (%(name)s,%(description)s,%(breed)s,%(location)s,%(age)s,
            %(gender)s,%(size)s,%(fixed)s,%(type)s,%(image_path)s,%(user_id)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)



    @classmethod
    def get_all_rescues(cls):
        query = """ SELECT * FROM rescues
            LEFT JOIN users ON rescues.user_id = users.id;
        """
        results = connectToMySQL(cls.db).query_db(query)

        all_rescues = []

        for row in results:
            one_rescue = cls(row)

            user_data = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at'],
            }
            one_rescue.owner = User(user_data)
            all_rescues.append(one_rescue)
        return all_rescues

    @classmethod
    def get_one_rescue(cls, data):
        query = """ SELECT * FROM rescues
            LEFT JOIN users ON rescues.user_id = users.id
            WHERE rescues.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)

        one_rescue = cls(results[0])

        user_data = {
                'id' : results[0]['users.id'],
                'first_name' : results[0]['first_name'],
                'last_name' : results[0]['last_name'],
                'email': results[0]['email'],
                'password': results[0]['password'],
                'created_at': results[0]['users.created_at'],
                'updated_at': results[0]['users.updated_at'],
            }
        one_rescue.owner = User(user_data)
        return one_rescue

    @classmethod
    def update_rescue(cls, data):
        query = """ UPDATE rescues
            SET name = %(name)s, description = %(description)s, breed = %(breed)s,
            location = %(location)s, age = %(age)s, gender = %(gender)s,
            size = %(size)s, fixed = %(fixed)s, type = %(type)s, image_path = %(image_path)s
            
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete_rescue(cls, data):
        query = """ DELETE FROM rescues
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)


