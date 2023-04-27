import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True}

try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    '''sql = """create table go(
    code int primary key,
    name varchar(30) not null,
    su int default 0,
    dan int default 0
    )"""
    cursor.execute(sql)'''

    while True :
        print('\t[레코드 처리 메뉴]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')
        menu = int(input('\t메뉴번호 입력 :'))

        if menu == 1:
            sql = "select * from goods"
            cursor.execute(sql)
            rows = cursor.fetchall()
            for r in rows:
                print('%d %s %d %d'%r)
            print('검색 레코드 수:', len(rows))
            pass
        elif menu == 2:
            code = int(input('코드 입력: '))
            name = input('상품명 입력: ')
            su = int(input('수량 입력: '))
            dan = int(input('단가 입력: '))

            sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
            cursor.execute(sql)
            conn.commit()
            pass
        elif menu == 3:
            code = int(input('수정할 코드 입력 :'))
            name = input('수정할 상품명 입력: ')
            su = int(input('수정할 수량 입력: '))
            dan = int(input('수정할 단가 입력: '))

            sql = f"update goods set name = '{name}', su = {su}, dan = {dan} where code = {code}"
            cursor.execute(sql)
            conn.commit()
            pass
        elif menu == 4:
            code = int(input('삭제할 코드 입력 :'))
            sql = f"select * from goods where code = {code}"
            cursor.execute(sql)
            rows = cursor.fetchall()

            if rows:
                # 레코드 1개 출력 : index 이용
                print('레코드 삭제')

                sql = f"delete from goods where code = {code}"
                cursor.execute(sql)
                conn.commit()
            else:
                print('해당 code 없음')
            pass
        elif menu == 5:
            print('프로그램 종료')
            break
        else :
            print('해당 메뉴는 없습니다.')
# DB 연결 예외 처리
except Exception as e:
    print('db 연동 오류:', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()