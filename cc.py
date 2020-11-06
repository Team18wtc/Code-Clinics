import datetime
from prettytable import PrettyTable
from simple_term_menu import TerminalMenu

time_slots = [
    "07:00",
    "07:30",
    "08:00",
    "08:30",
    "09:00",
    "09:30",
    "10:00",
    "10:30",
    "11:00",
    "11:30",
    "12:00",
    "12:30",
    "13:00",
    "13:30",
    "14:00",
    "14:30",
    "15:00",
    "15:30",
    "16:00",
    "16:30",
    "17:00",
    "17:30",
]


def show_slots(today, time, day):
    slots = []
    for slot in time_slots:
        hour, mins = slot.split(":", 2)

        slot_hour = datetime.timedelta(hours=int(hour))
        current_hour = datetime.timedelta(hours=int(time.hour))
        slot_minute = datetime.timedelta(minutes=int(mins))
        current_minute = datetime.timedelta(minutes=int(time.minute))
        thirty_minutes = datetime.timedelta(minutes=30)

        if today.date() == day:
            if slot_hour < current_hour:
                slots.append("-")
                continue
            elif slot_hour == current_hour and mins == "00" and slot_minute < current_minute:
                slots.append("-")
                continue
            elif slot_hour == current_hour and mins == "30" and slot_minute < current_minute - thirty_minutes:
                slots.append("-")
                continue
        slots.append(slot)
        # print(slots)
    
    return slots


def get_available_slots():

    available_slots = []
    today = datetime.datetime.now()
    time = today.time()
    number_of_days = 7
    days = [
        (today + datetime.timedelta(days=i)).date()
        for i in range(number_of_days)
    ]

    x = PrettyTable()

    for day in days:
        slots = show_slots(today, time, day)
        x.add_column(str(day), slots)
        available_slots.append(slots)
        
    print(x)

    date_menu = TerminalMenu([str(day) for day in days])
    print("Choose date:")
    selected_date = date_menu.show()
    print(str(days[selected_date]))
    available_slots[selected_date] = [slot for slot in available_slots[selected_date] if slot != "-"]
    # print(available_slots[selected_date])
    slot_menu = TerminalMenu(available_slots[selected_date])
    print("Choose slot:")
    selected_slot = slot_menu.show()
    print(available_slots[selected_date][selected_slot])

    return


def get_command():

    return input("What do you want to do.?: ")


def init_cc():

    print("Welcome to Code Clinics")

    print("please wait while we load your calendar...")
    print()
    print("<Shows user events or Code Clinics Events>")

    print("""
mkslot - create a slot
bkslot - book a slot
""")

    command = get_command()

    if command == "mkslot":
        get_available_slots()


if __name__ == "__main__":
    init_cc()