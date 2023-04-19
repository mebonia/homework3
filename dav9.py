import sqlite3

conn = sqlite3.connect('customers.sqlite')
cursor = conn.cursor()
select_res = cursor.execute('SELECT * FROM users')

two_rows = cursor.fetchmany(7)
for row in two_rows:
    print(row[1], ' ', row[5])

select_res = cursor.execute('SELECT * FROM users WHERE age > 25')
for row in select_res:
    print(row[2], row[3], row[4])

age = 25
select_res = cursor.execute('SELECT * FROM users WHERE age > :age_condition', {'age_condition': age})
print('\nმეორე ვარიანტი ცვლადის გამოყენებით:')
for row in select_res:
    print(row[2], row[3], row[4])

select_res = cursor.execute('SELECT * FROM users WHERE age BETWEEN 10 AND 25')
for row in select_res:
    print('\n', row)

select_res = cursor.execute('SELECT * FROM users WHERE age <>20')
for row in select_res:
    print(row[2], row[3])

cursor.execute("SELECT COUNT(*) FROM Users")
row = cursor.fetchone()
count = row[0]
print('\nჩანაწერების რაოდენობა:',count)

cursor.execute("SELECT * FROM Users ORDER BY age desc")
rows = cursor.fetchall()

for i in rows:
    print(i)

cursor.execute("SELECT DISTINCT firstname FROM Users ORDER BY firstname asc ")
rows = cursor.fetchall()

for row in rows:
    print(row[0])

cursor.execute('UPDATE users SET username = "gocha" WHERE age = 20')
conn.commit()


cursor.execute('UPDATE users SET age = 15 WHERE age > 30')
conn.commit()

cursor.execute('DElETE FROM users where user_id = 5')
conn.commit()


cursor.execute("DELETE FROM Users WHERE firstname LIKE 'ა%'")
conn.commit()


conn.close()



