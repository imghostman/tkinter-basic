import sqlite3


def connect():
    conn = sqlite3.connect("hotel.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs hotel (id INTEGER PRIMARY KEY, name TEXT, "
                "address TEXT, contact INTEGER, no_of_days INTEGER, room_type TEXT,"
                "total INTEGER)")
    conn.commit()
    conn.close()


def insert(name, address, contact, no_of_days, room_type, total):
    from back import calculation
    con = sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("INSERT INTO hotel VALUE(NULL,?,?,?,?,?,?)",
                (name, address, contact, no_of_days, calculation(no_of_days, room_type)))

    # cur.execute("INSERT INTO hotel VALUE(NULL,?,?,?,?,?,?")
    con.commit()
    con.close()
    view()


def view():
    con = sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM hotel")
    row = cur.fetchall()
    con.close()
    return row


def search(name, address, contact, room_type, no_of_days, total):
    con = sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM hotel WHERE name=? OR address=? OR contact=? OR room_type=? OR no_of_days=? total = ?",
                (name, address, contact, no_of_days, room_type, total))
    row = cur.fetchall()
    con.close()
    return row


def delete(id):
    con = sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("DELETE FROM hotel where id=?", (id,))
    con.commit()
    con.close()


def update(id, name, address, contact, room_type, no_of_days, total):
    from back import calculation
    con = sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("UPDATE hotel SET name=? , address=? , contact=? , room_type=? , total = ? WHERE id=?",
                (name, address, contact, room_type, no_of_days, calculation(no_of_days, room_type), id))
    con.commit()
    con.close()


def calculation(no_of_days, room_type):
    if room_type == ("normal" or "NORMAL"):
        total = int(no_of_days) * 1500
        return total
    elif room_type == ("KING" or "king"):
        total = int(no_of_days) * 1800
        return total
    elif room_type == ("DELUXE" or "deluxe"):
        total = int(no_of_days) * 2000
        return total


connect()

# import sqlite3
#
#
# def connect():
#     conn = sqlite3.connect("hotel.db")
#     cur = conn.cursor()
#     cur.execute(
#         "CREATE TABLE IF NOT EXISTs hotel (id INTEGER PRIMARY KEY , name TEXT , address TEXT , phone_number INTEGER, "
#         "no_of_days INTEGER , room_type TEXT , total INTEGER)")
#     conn.commit()
#     conn.close()
#
#
# def insert(name, address, phone_number, no_of_days, room_type, total):
#     from back import calculation
#     conn = sqlite3.connect("hotel.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO hotel VALUES (NULL, ?,?,?,?,?,?)",
#                 (name, address, phone_number, no_of_days, room_type, calculation(no_of_days, room_type)))
#     conn.commit()
#     conn.close()
#     view()
#
#
# def view():
#     conn = sqlite3.connect("hotel.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM hotel")
#     row = cur.fetchall()
#     conn.close()
#     return row
#
#
# def search(name="", address="", phone_number="", room_type="", no_of_days="", total=""):
#     conn = sqlite3.connect("hotel.db")
#     cur = conn.cursor()
#     cur.execute(
#         "SELECT * FROM hotel WHERE name=? OR address=? OR phone_number=?  OR  room_type=?  OR  no_of_days=?  OR  "
#         "total=?",
#         (name, address, phone_number, room_type, no_of_days, total))
#     row = cur.fetchall()
#     conn.close()
#     return row
#
#
# def delete(id):
#     conn = sqlite3.connect("hotel.db")
#     cur = conn.cursor()
#     cur.execute("DELETE FROM hotel  where id=?", (id,))
#     conn.commit()
#     conn.close()
#
#
# def update(id, name, address, phone_number, room_type, no_of_days, total):
#     from back import calculation
#     conn = sqlite3.connect("hotel.db")
#     cur = conn.cursor()
#     cur.execute(
#         "UPDATE hotel SET name=? ,address=? , phone_number=? ,  room_type=? , no_of_days=? , total=? where id=?",
#         (name, address, phone_number, room_type, no_of_days, calculation(no_of_days, room_type), id))
#     conn.commit()
#     conn.close()
#
#
# def calculation(no_of_days, room_type):
#     if room_type == ("normal" or "NORMAL"):
#         total = int(no_of_days) * 1500
#         return total
#     elif room_type == ("KING" or "king"):
#         total = int(no_of_days) * 1800
#         return total
#     elif room_type == ("delux" or "DELUX"):
#         total = int(no_of_days) * 2000
#         return total
#
#
# connect()
