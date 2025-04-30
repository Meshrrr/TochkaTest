from datetime import datetime
import json


def check_capacity(max_capacity: int, guests: list) -> bool:
    # Реализация алгоритма
    events = []

    for guest in guests:

        check_in = datetime.strptime(guest['check_in'], '%Y-%m-%d').date()
        check_out = datetime.strptime(guest['check_out'], '%Y-%m-%d').date()

        events.append((check_in, 1))
        events.append((check_out, -1))

    events.sort()

    current_guests = 0
    max_guests = 0

    for event in events:
        current_guests += event[1]
        if current_guests > max_guests:
            max_guests = current_guests
            if max_guests > max_capacity:
                return False

    return True

if __name__ == "__main__":
    # Чтение входных данных
    max_capacity = int(input())
    n = int(input())


    guests = []
    for _ in range(n):
        guest_json = input()
        guest_data = json.loads(guest_json)
        guests.append(guest_data)


    result = check_capacity(max_capacity, guests)
    print(result)