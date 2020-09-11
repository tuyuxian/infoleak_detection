"""
Author: Yu-Hsien,Tu
Date: 2020/09/12
Connect to Database
Version 1.1
"""
import mysql.connector


def update(tag, text):
    """ update """

    sql = 'INSERT INTO contract_table (tag, text) VALUES (%s, %s)'
    val = [
        (tag, text)
    ]

    cursor.executemany(sql, val)
    mydb.commit()
    #print('Insert Done!')


def lookup(text):
    """ lookup """

    global mydb
    global cursor
    mydb = mysql.connector.connect(user='your username', password='your password',
                                   host='xxx.xxx.xxx.xxx', database='your database')

    cursor = mydb.cursor()
    sql = "SELECT tag, text FROM contract_table WHERE text = %s"
    val = [
        (text)
    ]
    cursor.execute(sql, val)
    result = cursor.fetchall()
    #print('Lookup Done!')
    if result == []:
        return -1
    else:
        return str(result[0][0])  # tag


def delete(text):
    """ delete """

    sql = "DELETE FROM contract_table WHERE text = %s"
    val = [
        (text)
    ]
    cursor.execute(sql, val)
    #print('Delete Done!')


def feedback(uuid, risk, contract):
    """ update feedback """

    sql = 'INSERT INTO feedback_table (id, risk, contract) VALUES (%s, %s, %s)'
    val = [
        (uuid, risk, contract)
    ]

    cursor.executemany(sql, val)
    mydb.commit()
    mydb.close()
