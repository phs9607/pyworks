from libs.db.dbconn import getconn

def select_emp():
    conn = getconn()
    cur = conn.cursor()
    # sql - select
    sql = "select * from employee"
    cur.execute(sql)
    rs = cur.fetchall()  # 데이터 목록 리스트형 반환
    for i in rs:
        print(i)
    conn.close()

def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "select * from employee where emp_id=?"
    cur.execute(sql, ('e103',)) #1개 매핑인 경우(튜플 자료구조 콤머 넣을것)
    rs = cur.fetchone()
    print(rs)
    conn.close()

def insert_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "insert into employee(emp_id, name, age, salary) values (?, ?, ?, ?)"
    cur.execute(sql, ('e104', '김산', 22, 5000))
    conn.commit()
    conn.close()

def update_emp():
    conn = getconn()
    cur = conn.cursor()
    #박인비의 급여를 20000->25000으로 변경
    sql = "update employee set salary=? where emp_id=?"
    cur.execute(sql, (25000, 'e102'))
    conn.commit()
    conn.close()

def delete_emp():
    conn = getconn()
    cur = conn.cursor()
    #사원번호가 'e102' 삭제
    sql = "delete from employee where emp_id=?"
    cur.execute(sql, ('e102', ))
    conn.commit()
    conn.close()

if __name__=="__main__":
    #insert_emp()
    #update_emp()
    delete_emp()
    select_emp()
    #select_one()
