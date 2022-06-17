# 데이터베이스에 접속해서, 데이터 처리하는 테스트 코드
import mysql.connector
from mysql_connection import get_connetion

name = '순두부'
description = '맛있는 순두부찌개 만들기'
cook_time = '25'
direcrions = '육수를 끓이고 양념장을 만든 후 물이 끓을 때 감자를 먼저 넣고 끓이다 양념장과 순두부, 다른 야채를 넣고 끓인다.'


# 예외 처리 코드 : 만약에 접속시도하다 안되면 에러가 나게 만들어준 것. 이는 mysql.connector 을 만든 사람이 그렇게 하도록 정해둔 것.
try :
    # 데이터 insert
    # 1. DB 연결
    connection = get_connetion()

    # 2. 쿼리문 만들기 (%s는 변수 처리해준다는 뜻) 
    query = '''insert into recipe
            (name, description, cook_time, directions)
            values
            ( %s, %s, %s, %s);'''

    record = (name, description, cook_time, direcrions)
    

    # 3. 커서를 가져온다.
    cursor = connection.cursor()

    # 4. 커서를 이용해서 쿼리문을 실행한다.
    cursor.execute(query, record)

    # 5. 커넥션을 커밋해줘야 한다. == DB에 영구적으로 반영하라는 것임.
    connection.commit()

    # 6. 자원 해제
    cursor.close()
    connection.close()

except mysql.connector.Error as e:
    pass

