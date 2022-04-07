# import argparse
# import csv
# import os
# import datetime


# def main():

#     parser = argparse.ArgumentParser()
#     subparser = parser.add_subparsers(dest='command')
#     buy_parser = subparser.add_parser('buy')
#     sell_parser = subparser.add_parser('sell')
#     # report_parser = subparser.add_parser('report')
# #############################################################################
#     buy_parser.add_argument('-item', '--item', required=True, type=str,
#                             help="Item to ADD to your store")
#     buy_parser.add_argument('-bought', '--bought', required=True, type=float,
#                             help="Item to ADD to your store")
#     buy_parser.add_argument(
#         '-expiration', '--expiration', help="Exiration date on the item")
# ##############################################################################
#     sell_parser.add_argument('-item', '--item', type=str,
#                              help="Item to SEll in your store")
#     sell_parser.add_argument(
#         '-price', '--price', type=float, help="Price you sold the item for")
# #########################################################################
#     args = parser.parse_args()
# #######################################################################
#     csv_path = os.path.join(os.getcwd(), os.path.basename('info.csv'))
#     file_exists = os.path.isfile(csv_path)

#     csv_sell_path = os.path.join(os.getcwd(), os.path.basename("sell.csv"))
#     sell_file_exists = os.path.isfile(csv_sell_path)

#     the_time = datetime.datetime.now()

#     the_time.strftime("%Y-%m-%d")

#     def incre(count):
#         count += 1
#         return count
# ####################################################################################################################################

#     def buy(item, bought, expiration):

#         with open('info.csv', 'a', newline="") as input, open('info.csv', 'r', newline="") as output:
#             field_names = ["ID", "Item", "Bought",
#                            "Expiration", "InStock"]
#             csv_writer = csv.DictWriter(
#                 input, fieldnames=field_names, delimiter='\t')
#             csv_reader = csv.DictReader(output)

#             if not file_exists:
#                 id = 1
#                 csv_writer.writeheader()
#                 csv_writer.writerow(
#                     {"ID": id, 'Item': item, 'Bought': bought, 'Expiration': expiration, 'InStock': True})

#             elif file_exists:
#                 # next(csv_reader)
#                 id = 1
#                 for line in csv_reader:
#                     c = line["ID"]
#                     id = int(c)

#                 csv_writer.writerow(
#                     {"ID": incre(id), 'Item': item, 'Bought': bought,  'Expiration': expiration, 'InStock': True})
# #################################################################################################################################

#     def sell(item, price):

#         with open('inventory.csv', 'r', newline="") as output, open('sell.csv', 'a', newline="") as sold_input:
#             field_names = ["ID", "Item", "Sold Price",
#                            "Expiration", "InStock"]
#             csv_reader = csv.DictReader(output)
#             csv_sell_writer = csv.DictWriter(
#                 sold_input, fieldnames=field_names, delimiter='\t')

#             if file_exists:

#                 next(csv_reader)
#                 for line in csv_reader:
#                     print(line['Item'])
#                     # if item == line['Item']:
#                     #     print("there i an item")
#                     #     if not sell_file_exists:
#                     #         id = 1
#                     #         csv_sell_writer.writeheader()
#                     #         csv_sell_writer.writerow(
#                     #             {"ID": id, 'Item': item,
#                     #                 'Price': price, 'InStock': True}
#                     #         )

#                     #     elif sell_file_exists:
#                     #         next(csv_reader)
#                     #         id = 1
#                     #         for line in csv_reader:
#                     #             c = line["ID"]
#                     #             id = int(c)
#                     #         csv_sell_writer.writerow(
#                     #             {"ID": incre(id), 'Item': item,
#                     #              'Price': price, 'InStock': True}
#                     #         )
#             else:
#                 print("ID  Item  Bought  Amount  Expiration  InStock")
#                 print("Your inventory is empty")


# #################################################################################################################


#     def report():
#         pass
#     #     print("you are in the report function")
#     #     if res == "inventory":
#     #         if file_exists:
#     #             with open("info.csv", "r", newline="") as read_file:
#     #                 csv_reader = csv.DictReader(read_file)

#     #                 for line in csv_reader:
#     #                     print(line)
#     #         else:
#     #             print(["ID", "Item", "Bought", "Amount", "Expiration"])
#     #             print("Your inventory is empty")

#     #     elif res == "revenue":
#     #         print("here is the revenue")
#     #     elif res == "profit":
#     #         print("here is the profit")
#     #     print("you are in the report function")

#     if args.command == "buy":
#         buy(args.item, args.bought, args.expiration)
#     elif args.command == "sell":
#         sell(args.item, args.price)
#     elif args.command == "report":
#         report()


# if __name__ == '__main__':
#     main()
# w = input("Put in your wheight  ")
# m = input("Is this pound, or kilos (P)pound - (K)kilo  ")


# def cal_w(some, thing):
#     if thing.upper() == "K":
#         pound = some * 2.20462
#         print("Your wheight in pounds is: {:.2f} ".format(pound))
#     elif thing.upper() == "P":
#         kilo = some / 2.20462
#         print(f"Your wheight in kilos is: {kilo}")


some_obj_list = [{"name": "popo",  "home": "norway", "age": 28, "over_30": False}, {"name": "momo",  "home": "ireland", "age": 31, "over_30": True}, {"name": "toto", "home": "ireland", "age": 29, "over_30": False}, {
    "name": "crocro",  "home": "usa", "age": 32, "over_30": True}, {"name": "fofo",  "home": "china", "age": 33, "over_30": True}]

for obj in some_obj_list:
    if obj["over_30"] is False and obj["home"] == "ireland":
        print(obj)
