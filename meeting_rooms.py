#!/usr/bin/env python3

import heapq


def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    free_rooms = []  # place the end time of the meetings here
    intervals.sort(key=lambda x: x[0])
    heapq.heappush(free_rooms, intervals[0][1])
    for meeting in intervals[1:]:
        start_time, end_time = meeting
        if (
            free_rooms[0] <= start_time
        ):  # then the room would be free for the meeting
            heapq.heappop(free_rooms)
        heapq.heappush(free_rooms, end_time)
    return len(free_rooms)


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(min_meeting_rooms(intervals))
