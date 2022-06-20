# from http import HTTPStatus
# from flask import request
# from flask_jwt_extended import get_jwt_header, get_jwt_identity, jwt_required
# from flask_restful import Resource
# from mysql.connector.errors import Error
# import mysql.connector
# from mysql_connection import get_connection

# ### API를 만들기 위한 클래스 작성
# ### class(클래스)란? 변수와 함수로 구성된 묶음
# ### 클래스는 상속이 가능하다.
# ### API를 만들기 위한 클래스는, flask_restful 라이브러리의
# ### Resource 클래스를 상속해서 만들어야 한다.

# class RecipeListResource(Resource):
#     # 위 괄호의 리소스는 flask_restful 라이브러리의 Resource 클래스여야 한다.
#     # restful API의 method 에 해당하는 함수 작성 
   
#     # @jwt_required() : 헤더 부분에 토큰이 없으면 처리를 안 해줌
#     @jwt_required()
#     def post(self):
#         # API 실행 코드를 여기에 작성.

#         # 클라이언트에서, body에 작성한 json을 받아오는 코드
#         data = request.get_json()

#         # 암호화한 id를 다시 복호화해서 가져오는 함수
#         user_id = get_jwt_identity()

#         # 받아온 데이터를 다시 저장하자.
#         try :
#             # 데이터 insert
#             # 1. DB 연결
#             connection = get_connection()

#             # 2. 쿼리문 만들기 (%s는 변수 처리해준다는 뜻) 
#             query = '''insert into recipe
#                     (name, description, cook_time, directions, user_id)
#                     values
#                     ( %s, %s, %s, %s, %s);'''

#             record = (data['name'], data['description'], data['cook_time'], data['directions'], user_id)
            

#             # 3. 커서를 가져온다.
#             cursor = connection.cursor()

#             # 4. 커서를 이용해서 쿼리문을 실행한다.
#             cursor.execute(query, record)

#             # 5. 커넥션을 커밋해줘야 한다. == DB에 영구적으로 반영하라는 것임.
#             connection.commit()

#             # 6. 자원 해제
#             cursor.close()
#             connection.close()

#         except mysql.connector.Error as e:
#             print(e)
#             cursor.close()
#             connection.close()
#             # HTTPStatus.SERVICE_UNAVAILABLE  == 503
#             return {'error' : str(e)}, 503


#         # 뒤에 숫자는 프로토콜 코드이다.
#         return {'result' : 'success'}, 200



#     def get(self):
#         # 쿼리 스트링(URL에서 ?뒤에 있는 부분)으로 나오는 데이터는 아래처럼 처리해준다.
#         offset = request.args.get('offset')
#         limit = request.args.get('limit')

#         # DB로부터 데이터를 받아서, 클라이언트에 받아준다.

#         try :
#             connection = get_connection()

#             query = '''select * 
#                     from recipe
#                     limit '''+offset+''', '''+limit+''';'''
            

#             # select 문은 dictionary = True 해준다.

#             cursor = connection.cursor(dictionary = True)

#             cursor.execute(query)

#             # select 문은, 아래 함수를 이용해서, 데이터를 가져온다.
#             result_list = cursor.fetchall()

#             print(result_list)

#             # 중요! 디비에서 가져온 timestamp 는 
#             # 파이썬의 datetime 으로 자동 변경된다.
#             # 문제는! 이데이터를 json 으로 바로 보낼수 없으므로,
#             # 문자열로 바꿔서 다시 저장해서 보낸다.
#             i = 0
#             for record in result_list :
#                 result_list[i]['created_at'] = record['created_at'].isoformat()
#                 result_list[i]['updated_at'] = record['updated_at'].isoformat()
#                 i = i + 1      


#             cursor.close()
#             connection.close()

#         except mysql.connector.Error as e:
#             print(e)
#             cursor.close()
#             connection.close()
        
#         return {"result" : "success", "count" : len(result_list), "reult_list" : result_list[0]} , 200

from http import HTTPStatus
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from mysql.connector.errors import Error
from mysql_connection import get_connection
import mysql.connector

### API 를 만들기 위한 클래스 작성
### class(클래스) 란??  변수와 함수로 구성된 묶음!
### 클래스는 상속이 가능하다!
### API를 만들기 위한 클래스는, flask_restful 라이브러리의
### Resource 클래스를 상속해서 만들어야 한다.

class RecipeListResource(Resource):
    # restful api 의 method 에 해당하는 함수 작성

    # @jwt_required() : 헤더 부분에 토큰이 없으면 처리를 안 해줌
    @jwt_required()
    def post(self) :
        # api 실행 코드를 여기에 작성

        # 클라이언트에서, body 부분에 작성한 json 을
        # 받아오는 코드
        data = request.get_json()

        user_id = get_jwt_identity()

        # 받아온 데이터를 디비 저장하면 된다.
        try :
            # 데이터 insert 
            # 1. DB에 연결
            connection = get_connection()

            # 2. 쿼리문 만들기
            query = '''insert into recipe
                    (name, description, cook_time, directions, user_id)
                    values
                    ( %s , %s , %s ,%s, %s);'''
            
            record = (data['name'], data['description'], data['cook_time'], data['directions'],  user_id  )

            # 3. 커서를 가져온다.
            cursor = connection.cursor()

            # 4. 쿼리문을 커서를 이용해서 실행한다.
            cursor.execute(query, record)

            # 5. 커넥션을 커밋해줘야 한다 => 디비에 영구적으로 반영하라는 뜻
            connection.commit()

            # 6. 자원 해제
            cursor.close()
            connection.close()

        except mysql.connector.Error as e :
            print(e)
            cursor.close()
            connection.close()
            return {"error" : str(e)}, 503

        return {"result" : "success"}, 200

    def get(self) :
        # 쿼리 스트링으로 오는 데이터는 아래처럼 처리해준다.
        offset = request.args.get('offset')
        limit = request.args.get('limit')

        # 디비로부터 데이터를 받아서, 클라이언트에 보내준다.
        try :
            connection = get_connection()

            query = '''select *
                    from recipe
                    where is_publish = 1
                    limit '''+offset+''' , '''+limit+''';'''
            
            # select 문은, dictionary = True 를 해준다.
            cursor = connection.cursor(dictionary = True)

            cursor.execute(query)

            # select 문은, 아래 함수를 이용해서, 데이터를 가져온다.
            result_list = cursor.fetchall()

            print(result_list)

            # 중요! 디비에서 가져온 timestamp 는 
            # 파이썬의 datetime 으로 자동 변경된다.
            # 문제는! 이데이터를 json 으로 바로 보낼수 없으므로,
            # 문자열로 바꿔서 다시 저장해서 보낸다.
            i = 0
            for record in result_list :
                result_list[i]['created_at'] = record['created_at'].isoformat()
                result_list[i]['updated_at'] = record['updated_at'].isoformat()
                i = i + 1                

            cursor.close()
            connection.close()

        except mysql.connector.Error as e :
            print(e)
            cursor.close()
            connection.close()

            return {"error" : str(e)}, 503


        return { "result" : "success" , 
                "count" : len(result_list) ,
                "result_list" : result_list }, 200
    








    
