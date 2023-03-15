def add():
    cid = input("Customer ID : ")
    nm = input("Customer Name : ")
    ad = input("Customer Address: ")
    cn = input("Contact No : ")

    f = open("D:\Python\File handling - Customer Management System\customer.txt","a")
    f.write(cid+"\t")
    f.write(nm+"\t")
    f.write(ad+"\t")
    f.write(cn+"\n")
    print("Record added")
    f.close()
    print()

def delete():
    i = input("Enter the ID to remove from file : ")
    with open("D:\Python\File handling - Customer Management System\customer.txt","r") as f:
        all = f.readlines()
        # print(data)
    with open("D:\Python\File handling - Customer Management System\customer.txt", "w") as f:
        for data in all:
            d = data.split('\t',1)
            if(d[0] != i):
                f.writelines(data)
    print("Record deleted")


def update():
    i = input("Enter the ID to updated from file : ")
    with open("D:\Python\File handling - Customer Management System\customer.txt","r") as f:
        all = f.readlines()
    with open("D:\Python\File handling - Customer Management System\customer.txt", "w") as f:
        for data in all:
            d = data.split('\t',1)
            if (d[0] == i):
                nn = input("New Name : ")
                na = input("New Address : ")
                nc = input("New Contact No. : ")
                f.writelines(d[0] + "\t" + nn + "\t" + na + "\t" + nc + "\n")
            else:
                f.writelines(data)
        print(("Record Updated"))

def search():
    i = input("Enter the ID to updated from file : ")
    with open("D:\Python\File handling - Customer Management System\customer.txt","r") as f:
        all = f.readlines()
        for data in all:
            d = data.split('\t',1)
            if (d[0] == i):
                print("ID \t Name \t Address \t Contact No.")
                print(data)
        print()

def show():
    f = open("D:\Python\File handling - Customer Management System\customer.txt","r")
    print("ID \t Name \t Address \t Contact No.")
    print(f.read())
    f.close()

while (True):
    print("Welcome to Customer Portal")
    print("1. Add new customer")
    print("2. Delete customer")
    print("3. Update customer")
    print("4. Search customer")
    print("5. Show all customer")
    print("6. Exit")
    ch = int(input("Enter your choice : "))
    print()
    if ch == 1:
        add()
    elif ch == 2:
        delete()
    elif ch == 3:
        update()
    elif ch == 4:
        search()
    elif ch == 5:
        show()
    elif ch == 6:
        break