from datetime import datetime

def verbose_time(time_format):
    present_time = datetime.now()
    if time_format == 12:
        hour_clock = '%I'
    else:
        hour_clock = '%H'
    verbose_date = datetime.strftime(present_time, f'%A, %B %d, %Y - {hour_clock}:%M')
    print(f"Current Local Time (Verbose): {verbose_date}")


def iso_time():
    pass


if __name__ == "__main__":
    time_format = int(input("Choose time format (12/24): "))
    verbose_time(time_format)

