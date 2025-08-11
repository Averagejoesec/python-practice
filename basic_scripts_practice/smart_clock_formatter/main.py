from datetime import datetime

def time_output(time_format):
    present_time = datetime.now()
    time_frame = ''
    if time_format == 12:
        hour_clock = '%I'
        time_frame = '%p'
    else:
        hour_clock = '%H'
    verbose_date = datetime.strftime(present_time, f'%A, %B %d, %Y - {hour_clock}:%M {time_frame}')
    print(f"Current Local Time (Verbose): {verbose_date}")

    # ISO Time
    iso_date = datetime.strftime(present_time, f'%Y-%m-%d {hour_clock}:%M:%S {time_frame}')
    print(f"Current Local Time (ISO): {iso_date}")
    
    week_number = datetime.strftime(present_time, '%U')
    print(f"ISO Week Number: {week_number}")
    
    day_of_year = datetime.strftime(present_time, '%j')
    print(f"Day of Year: {day_of_year}")
    
    day = present_time.day
    if 10 <= day % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
    ordinal_day = f"{day}{suffix}"
    ordinal_date = datetime.strftime(present_time,  f'%B {ordinal_day}, %Y')
    print(f"Date with Ordinal: {ordinal_date}")

if __name__ == "__main__":
    time_format = int(input("Choose time format (12/24): "))
    time_output(time_format)

