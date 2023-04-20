from datetime import datetime, timedelta, date

USERS = [{"name": "Bob", "birthday": datetime(1995, 4, 25)},
         {"name": "Frank", "birthday": datetime(1997, 4, 23)},
         {"name": "Heidi", "birthday": datetime(1978, 4, 22)},
         {"name": "Victoria", "birthday": datetime(1963, 4, 26)},
         {"name": "Max", "birthday": datetime(2000, 4, 24)},
         {"name": "Julia", "birthday": datetime(2004, 2, 29)},
         {"name": "Mario", "birthday": datetime(1985, 4, 30)},
         {"name": "Mark", "birthday": datetime(1987, 5, 2)},
         {"name": "Mary", "birthday": datetime(2004, 4, 26)}]

TODAY = date.today()
ONE_WEEK = timedelta(weeks=1)
ONE_DAY = timedelta(days=1)


def get_birthdays_per_week(colleagues):
    colleagues_birthdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    date_ = TODAY

    while date_ != TODAY + ONE_WEEK:
        for colleague in colleagues:
            coming_birthday = colleague["birthday"].strftime("%d %B")  # colleague's birthday in format "day month"

            if date_.strftime("%d %B") == coming_birthday:
                week_day = date_.strftime("%A")  # getting a day of week (Monday, Tuesday etc.)

                # add information to "colleagues_birthdays" dictionary
                if week_day in colleagues_birthdays.keys():
                    colleagues_birthdays[week_day].append(colleague["name"])
                else:
                    colleagues_birthdays["Monday"].append(colleague["name"])

        date_ += ONE_DAY

    # === Output the result to the user ===
    for day in colleagues_birthdays:
        if len(colleagues_birthdays[day]) != 0:
            print(day + ":", ", ".join(colleagues_birthdays[day]))


def main():
    get_birthdays_per_week(USERS)


if __name__ == "__main__":
    main()
