def solution(lines):
    def time_to_milliseconds(time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split('.')
        return (int(h) * 3600 + int(m) * 60 + int(s)) * 1000 + int(ms)

    logs = []

    for line in lines:
        _, time_str, duration_str = line.split()
        duration = float(duration_str[:-1]) * 1000
        end_time = time_to_milliseconds(time_str)
        start_time = end_time - duration + 1
        logs.append((start_time, end_time))

    max_traffic = 0

    for _, end_time in logs:
        window_start_time = end_time
        window_end_time = end_time + 1000

        traffic = 0
        for start_time, end_time in logs:
            if start_time < window_end_time and end_time >= window_start_time:
                traffic += 1

        max_traffic = max(max_traffic, traffic)

    return max_traffic
