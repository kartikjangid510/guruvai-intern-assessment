def can_attend_all(events):
    events.sort(key=lambda x: x[1])  # Sort by end times
    last_end_time = events[0][1]
    for start, end in events[1:]:
        if start < last_end_time:
            return False
        last_end_time = end
    return True


def min_rooms_required(events):
    if not events:
        return 0

    start_times = sorted([event[0] for event in events])
    end_times = sorted([event[1] for event in events])

    room_count = 0
    end_ptr = 0

    for start_ptr in range(len(start_times)):
        if start_times[start_ptr] < end_times[end_ptr]:
            room_count += 1
        else:
            end_ptr += 1

    return room_count


# Test Cases
if __name__ == '__main__':
    events1 = [(0, 30), (5, 10), (15, 20)]
    events2 = [(7, 10), (2, 4)]
    events3 = [(1, 3), (2, 4), (3, 5)]

    print("Can attend all (events1):", can_attend_all(events1))  # False
    print("Can attend all (events2):", can_attend_all(events2))  # True

    print("Minimum rooms required (events1):", min_rooms_required(events1))  # 2
    print("Minimum rooms required (events2):", min_rooms_required(events2))  # 1
    print("Minimum rooms required (events3):", min_rooms_required(events3))  # 2