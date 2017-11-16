import time
from yto_query import Yto
from stops import StopNode

def main():
    bills = []
    with open("BillList.txt") as f:
        bills = f.readlines()
    print(bills)
    y = Yto()
    for bills_v in bills:
        bill_info = bills_v.split(' ')
        if bill_info[0] == "yto":
            bill = bill_info[1].strip()
            print("Querying {}".format(bill))
            info = y.query(bill)
            for i in info:
                print(i)
            print("")


if __name__ == '__main__':
    main()
