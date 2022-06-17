import mysql.connector

def get_connection():
    connection = mysql.connector. connect(
        host = 'yh-db.ctttsro2er9u.ap-northeast-2.rds.amazonaws.com',
        database = 'recipe_db',
        user = 'recipe_user',
        password = 'leem0929'
    )
    return connection