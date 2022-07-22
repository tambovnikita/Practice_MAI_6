
import sqlite3


def count_all_users():
    cursor_info.execute("SELECT id FROM users_info ORDER BY id DESC")
    return int(cursor_info.fetchone()[0]) + 1


def count_all_airports():
    cursor_info.execute("SELECT id FROM airports_info ORDER BY id DESC")
    return int(cursor_info.fetchone()[0]) + 1


def count_all_flights(airport_id):
    cursor_flights.execute("SELECT id FROM airport{} ORDER BY id DESC".format(airport_id))
    return int(cursor_flights.fetchone()[0]) + 1


def getUserInfo(id, parameter):
    cursor_info.execute("SELECT {0} FROM users_info WHERE id={1}".format(parameter, id))
    return cursor_info.fetchone()[0]


def getAirportInfo(id, parameter):
    cursor_info.execute("SELECT {0} FROM airports_info WHERE id={1}".format(parameter, id))
    return cursor_info.fetchone()[0]


def getFlightInfo(id, airport_id, parameter):
    cursor_flights.execute("SELECT {0} FROM airport{1} WHERE id={2}".format(parameter, airport_id, id))
    return cursor_flights.fetchone()[0]


conn_info = sqlite3.connect("./db/info.db", check_same_thread=False)
cursor_info = conn_info.cursor()

conn_flights = sqlite3.connect("./db/flights.db", check_same_thread=False)
cursor_flights = conn_flights.cursor()
