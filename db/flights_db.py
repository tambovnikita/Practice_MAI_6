
import random, time
import sqlite3


def random_type():
    all_type = ["boarding_flight", "takeoff_flight"]
    return random.choice(all_type)


def random_firm():
    all_firm = ['"Аэрофлот"', '"Группа S7"', '"Уральские авиалинии"', '"NordWind"', '"Россия"', '"ЮТэйр"', '"Red Wings"',
                '"Победа"', '"AZUR Air"', '"Азимут"', '"Аврора"', '"РусЛайн"', '"ИрАэро"', '"Якутия"', '"Royal Flight"',
                '"Сибирская Легкая Авиация"', '"Smartavia"', '"Татарстан"', '"NordStar"', '"Pegas Fly"']
    return random.choice(all_firm)


def random_model():
    all_model = ["Airbus-A310", "Airbus-A319", "Airbus-A320", "Airbus-A330", "Airbus-A380", "Boeing-737", "Boeing-747",
                 "Boeing-757", "Boeing-767", "Boeing-777", "ИЛ-62", "ИЛ-86", "ИЛ-96", "ТУ-154", "ТУ-204"]
    return random.choice(all_model)


if __name__ == "__main__":

    # База данных (БД)
    conn = sqlite3.connect("airports.db", check_same_thread=False)
    cursor = conn.cursor()

    # airport1
    time.sleep(1)
    number = 0
    for i in range(100000):
        if number >= 86400:
            break
        time_show = time.strftime("%H:%M:%S", time.gmtime(number))
        time_on_runway = 120
        #print(i, random_type(), number, random_firm(), random_model(), time_show, time_on_runway)
        cursor.execute("INSERT INTO airport1 VALUES (?,?,?,?,?,?,?)",
                       tuple([i, random_type(), number, random_firm(), random_model(), time_show, time_on_runway]))
        conn.commit()  # Сохраняем изменения
        number += random.randint(15, 20)

    # airport2
    number = 0
    time.sleep(1)
    for i in range(100000):
        if number >= 86400:
            break
        time_show = time.strftime("%H:%M:%S", time.gmtime(number))
        time_on_runway = 120
        # print(i, random_type(), number, random_firm(), random_model(), time_show, time_on_runway)
        cursor.execute("INSERT INTO airport2 VALUES (?,?,?,?,?,?,?)",
                       tuple([i, random_type(), number, random_firm(), random_model(), time_show, time_on_runway]))
        conn.commit()  # Сохраняем изменения
        number += random.randint(10, 15)

    # airport3
    number = 0
    time.sleep(1)
    for i in range(100000):
        if number >= 86400:
            break
        time_show = time.strftime("%H:%M:%S", time.gmtime(number))
        time_on_runway = 120
        # print(i, random_type(), number, random_firm(), random_model(), time_show, time_on_runway)
        cursor.execute("INSERT INTO airport3 VALUES (?,?,?,?,?,?,?)",
                       tuple([i, random_type(), number, random_firm(), random_model(), time_show, time_on_runway]))
        conn.commit()  # Сохраняем изменения
        number += random.randint(5, 10)

    # airport4
    number = 0
    time.sleep(1)
    for i in range(100000):
        if number >= 86400:
            break
        time_show = time.strftime("%H:%M:%S", time.gmtime(number))
        time_on_runway = 120
        # print(i, random_type(), number, random_firm(), random_model(), time_show, time_on_runway)
        cursor.execute("INSERT INTO airport4 VALUES (?,?,?,?,?,?,?)",
                       tuple([i, random_type(), number, random_firm(), random_model(), time_show, time_on_runway]))
        conn.commit()  # Сохраняем изменения
        number += random.randint(1, 5)
