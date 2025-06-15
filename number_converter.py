def format_time(seconds):
    if not (0 <= seconds < 8640000):
        return "The number may be 0 to 8640000"

    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days == 1:
        day_word = "day"
    elif 2 <= days % 10 <= 4 and not 12 <= days % 100 <= 14:
        day_word = "day"
    else:
        day_word = "days"

    time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    return f"{days} {day_word}, {time_str}"

user_input = input("Enter number of seconds (0 to 8640000): ")
if user_input.isdigit():
    user_seconds = int(user_input)
    print(format_time(user_seconds))
else:
    print("Only for whole and additional numbers")