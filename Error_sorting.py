LOG_FILE = input('Enter your file')

log_type_count = {}
daily_log_count = {}
message_count = {}

with open(LOG_FILE, "r") as file:
    for line in file:
        parts = line.strip().split()
        if not parts:
            continue

        if len(parts) == 1:
            date = parts[0]
            log_type = 'UNKNOWN'
            message = ''
        elif len(parts) == 2:
            date, log_type = parts
            message = ''
        else:
            date, log_type, message = parts

        if log_type not in log_type_count:
            log_type_count[log_type] = 0
        log_type_count[log_type] += 1

        if date not in daily_log_count:
            daily_log_count[date] = 0
        daily_log_count[date] += 1

        if message not in message_count:
            message_count[message] = 0
        message_count[message] += 1

print("\t Error file report \t")

print("Number of Errors")
for log_type, count in log_type_count.items():
    print(f"{log_type}: {count}")

print("Most used words")
sorted_messages = sorted(message_count.items(), key=lambda x: x[1], reverse=True)
for message, count in sorted_messages[:5]:
    print(f"{count} - {message}")

print("Number of errors per day")
for date, count in daily_log_count.items():
    print(f"{date}: {count}")