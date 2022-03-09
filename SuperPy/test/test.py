import argparse
import csv
import os
import datetime


# parser = argparse.ArgumentParser(description="==Welcome to Kwik-E-Mart==")
# parser.add_argument('-item', '--item', type=str,
#                     help="Item to ADD to your store")
# parser.add_argument('-bought', '--bought', type=float,
#                     help="Item to ADD to your store")
# parser.add_argument('-amount', '--amount', type=int,
#                     help="The quantity of that item")
# parser.add_argument('-expiration', '--expiration', help="was the item sold")

# # parser.add_argument('-sold', '--sold', help="Price item was sold at")
# # parser.add_argument(
# #     'task', help="what would you like to see [revenue, inventory, profit]")
# # parser.add_argument('-time', '--time', help="what date would you like to see")

# # problem: make argparse argument only requierd if previous argument was called

# group = parser.add_mutually_exclusive_group()
# group.add_argument('-buy', '--buy', action='store_true',
#                    help='type -buy to add items to your store')
# group.add_argument('-sell', '--sell', action='store_true',
#                    help='type -sell to sell items from your store')
# group.add_argument('-report', '--report', action='store_true',
#                    help='type -report to see your report')

# args = parser.parse_args()


csv_path = os.path.join(os.getcwd(), os.path.basename("info.csv"))
file_exists = os.path.isfile(csv_path)


# the_time = datetime.datetime.now()

# the_time.strftime("%Y-%m-%d")


def incre(count):
    count += 1
    return count


# def sell():
#     print("you are in the sell function")


# def report(task):
#     if task == "inventory":
#         if file_exists:
#             with open("info.csv", "r", newline="") as read_file:
#                 csv_reader = csv.DictReader(read_file)

#                 for line in csv_reader:
#                     print(line)
#         else:
#             print(["ID", "Item", "Bought", "Amount", "Expiration"])
#             print("Your inventory is empty")

#     elif task == "revenue":
#         print("here is the revenue")
#     elif task == "profit":
#         print("here is the profit")
#     print("you are in the report function")


id = 0


def buy(item, bought, amount, expiration):
    print("you are in the buy function")

    if file_exists:
        with open('info.csv', 'r', newline="") as file_2:
            csv_reader = csv.DictReader(file_2)

            next(csv_reader)
            for line in csv_reader:
                c = line["ID"]
                id = int(c)

    with open('info.csv', 'a', newline="") as file:
        field_names = ["ID", "Item", "Bought", "Amount", "Expiration"]
        csv_writer = csv.DictWriter(file, fieldnames=field_names)

        if not file_exists:
            csv_writer.writeheader()
            csv_writer.writerow(
                {"ID": 0, 'Item': item, 'Bought': bought, 'Amount': amount, 'Expiration': expiration})

        csv_writer.writerow(
            {"ID": incre(id), 'Item': item, 'Bought': bought, 'Amount': amount, 'Expiration': expiration})


buy("tomatoe", 0.5, 2, "22/03/2022")

# if __name__ == '__main__':

#     if args.buy:
#         buy(args.item, args.bought, args.amount, args.expiration)
# elif args.sell:
#     sell(args.item, args.sold)
# elif args.report:
#     report(args.task)
