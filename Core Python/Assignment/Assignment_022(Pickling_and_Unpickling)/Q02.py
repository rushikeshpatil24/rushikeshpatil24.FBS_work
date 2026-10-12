# Menu driven program using file and pickle

import pickle
from Q01 import Emp

filename = "emp.dat"


def add_record():
    eid = int(input("Enter employee id: "))
    ename = input("Enter employee name: ")
    basic = float(input("Enter basic salary: "))

    f = open(filename, "ab")
    pickle.dump(Emp(eid, ename, basic), f)
    f.close()

    print("Record added")


def show_record(eid):
    try:
        f = open(filename, "rb")

        while True:
            e = pickle.load(f)

            if e.eid == eid:
                print(e)
                f.close()
                return

    except EOFError:
        f.close()
        print("Record not found")


def read_all():
    records = []

    try:
        f = open(filename, "rb")

        while True:
            records.append(pickle.load(f))

    except EOFError:
        f.close()

    return records


def delete_record(eid):
    records = read_all()
    records = [e for e in records if e.eid != eid]

    f = open(filename, "wb")

    for e in records:
        pickle.dump(e, f)

    f.close()
    print("Record deleted")


def edit_record(eid):
    records = read_all()

    for e in records:
        if e.eid == eid:
            e.ename = input("Enter new name: ")
            e.basic = float(input("Enter new basic salary: "))

    f = open(filename, "wb")

    for e in records:
        pickle.dump(e, f)

    f.close()
    print("Record updated")


def display_all():
    records = read_all()

    for e in records:
        print(e)


while True:
    print("\n1. Add")
    print("2. Search")
    print("3. Delete")
    print("4. Edit")
    print("5. Display All")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_record()
    elif ch == 2:
        eid = int(input("Enter id: "))
        show_record(eid)
    elif ch == 3:
        eid = int(input("Enter id: "))
        delete_record(eid)
    elif ch == 4:
        eid = int(input("Enter id: "))
        edit_record(eid)
    elif ch == 5:
        display_all()
    elif ch == 6:
        break
    else:
        print("Invalid choice")
