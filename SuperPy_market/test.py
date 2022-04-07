import argparse
import csv
import os
from datetime import datetime, date, timedelta


now = date.today()


def main():

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    buy_parser = subparser.add_parser('buy')
    sell_parser = subparser.add_parser('sell')

    report_parser = subparser.add_parser("report")

    child_report = report_parser.add_subparsers(dest="task")

    child_inventory_parser = child_report.add_parser("inventory")
    child_revenue_parser = child_report.add_parser("revenue")
    child_profit_parser = child_report.add_parser("profit")
#############################################################################
    buy_parser.add_argument('-item', '--item', required=True, type=str,
                            help="Item to ADD to your store")
    buy_parser.add_argument('-bought', '--bought', required=True, type=float,
                            help="Item to ADD to your store")
    buy_parser.add_argument(
        '-expiration', '--expiration', help="Exiration date on the item")
##############################################################################
    sell_parser.add_argument('-item', '--item', type=str,
                             help="Item to SEll in your store")
    sell_parser.add_argument(
        '-price', '--price', type=int, help="Price you sold the item for")

    for child_parser in [child_inventory_parser, child_revenue_parser, child_profit_parser]:
        child_parser.add_argument(
            '-time', '--time', required=True, help="Type in the date you would like to see the report")

#########################################################################
    args = parser.parse_args()

    #######################################################################
    csv_path = os.path.join(os.getcwd(), os.path.basename('bought.csv'))
    file_exists = os.path.isfile(csv_path)

    csv_sell_path = os.path.join(os.getcwd(), os.path.basename("sold.csv"))
    sell_file_exists = os.path.isfile(csv_sell_path)

    # the_time = datetime.datetime.now()

    # the_time.strftime("%Y-%m-%d")

    def incre(count):
        count += 1
        return count
# ####################################################################################################################################

    def buy(item, bought, expiration):

        with open('bought.csv', 'a', newline="") as input, open('bought.csv', 'r', newline="") as output:
            field_names = ["ID", "Item", "Bought", "Bought_date",
                           "Expiration", "InStock"]
            csv_writer = csv.DictWriter(
                input, fieldnames=field_names)
            csv_reader = csv.DictReader(output)

            if not file_exists:
                id = 1
                csv_writer.writeheader()
                csv_writer.writerow(
                    {"ID": id, 'Item': item, 'Bought': bought, "Bought_date": now, 'Expiration': expiration, 'InStock': True})

            elif file_exists:

                for line in csv_reader:
                    c = line["ID"]
                    id = int(c)

                csv_writer.writerow(
                    {"ID": incre(id), 'Item': item, 'Bought': bought, "Bought_date": now, 'Expiration': expiration, 'InStock': True})
################################################################################################################################

    def sell(item, price):

        def check_lowest_ex(product, reader):
            day_list = list()

            expiration_list = [line["Expiration"]
                               for line in reader if product == line["Item"] and line['InStock'] == "True"]

            if len(expiration_list) == 0:
                return print(f"Sorry! but you dont have anymore: {item}s in your inventory")

            for date in expiration_list:  # function to determine lowest expiration date

                ExpirationDate = datetime.strptime(
                    date, "%Y-%m-%d").date()
                amount_days = ExpirationDate - now

                if int(amount_days.days) > 0:
                    day_list.append(int(amount_days.days))
                lowest = min(day_list)

            return lowest

        with open('bought.csv', 'r', newline="") as output, open('sold.csv', 'a', newline="") as sold_input, open('sold.csv', 'r', newline="") as sold_read:
            field_names = ["ID", "Item", "Price", "Sold_date",
                           "Expiration"]

            csv_reader = csv.DictReader(output)
            csv_sell_reader = csv.DictReader(sold_read)
            csv_sell_writer = csv.DictWriter(
                sold_input, fieldnames=field_names)

            for line in csv_sell_reader:     # to get the ID number
                c = line["ID"]
                id = int(c)

            if file_exists:      # check bought file exists

                copy_reader = [line for line in csv_reader]

                low = check_lowest_ex(item, copy_reader)

                for line in copy_reader:
                    expiration = line["Expiration"]

                    current_ex = datetime.strptime(
                        expiration, "%Y-%m-%d").date()

                    current_num = current_ex - now

                    if int(current_num.days) > 0:  # check if the item is expired
                        correct_num = int(current_num.days)
                    elif int(current_num.days) <= 0 and item == line['Item']:
                        line["InStock"] = "Expired"

                    if low == correct_num and item == line['Item'] and line["InStock"] == "True":
                        if not sell_file_exists:  # if sold file is not created yet
                            id = 1
                            line["InStock"] = False
                            csv_sell_writer.writeheader()
                            csv_sell_writer.writerow(
                                {"ID": id, 'Item': item,
                                    'Price': price, "Sold_date": now, 'Expiration': expiration}
                            )
                            print("Item sold")
                            break
                        if sell_file_exists:
                            line["InStock"] = False
                            csv_sell_writer.writerow(
                                {"ID": incre(id), 'Item': item,
                                 'Price': price, "Sold_date": now, 'Expiration': expiration}
                            )
                            print("Item sold")
                            break

            else:
                print("ID  Item  Bought_price  Bought_date  Expiration  InStock")
                print("Your inventory is empty")

        copy_field_names = ["ID", "Item", "Bought", "Bought_date",
                            "Expiration", "InStock"]
        writer = csv.DictWriter(
            open('bought.csv', 'w', newline=''), fieldnames=copy_field_names)

        writer.writeheader()
        for line in copy_reader:
            writer.writerow(line)


#################################################################################################################


    def report(sector, time):

        yesterday = now - timedelta(days=1)
        try:
            with open("bought.csv", "r", newline="") as bought_rep, open("sold.csv", "r", newline="") as sold_rep:
                bought_rep_reader = csv.DictReader(bought_rep)
                sold_rep_reader = csv.DictReader(sold_rep)

                copy_bought_reader = [line for line in bought_rep_reader]
                copy_sold_reader = [line for line in sold_rep_reader]

            if sector == "inventory":
                for line in copy_bought_reader:
                    keys = list(line.keys())
                    keys.pop()
                    print(
                        "==================================================================")
                    print("", "  |  ".join(keys))
                    print(
                        "==================================================================")
                    break

                if time == "now":
                    the_date = now
                elif time == "yesterday":
                    the_date = yesterday
                elif time[0] in "1234567890":

                    time_arr = list(time)
                    num = int(time_arr.pop(0))
                    str_time = "".join(time_arr)

                    if str_time == "weeks" or str_time == "week":
                        the_date = now - timedelta(days=7 * num)

                        print(
                            f"you want to see report from {the_date} which was {num} {str_time} ago")

                    elif str_time == "month" or str_time == "months":
                        the_date = now - timedelta(days=30 * num)

                        print(
                            f"you want to see report from {the_date} which was {num} {str_time} ago")

                for line in copy_bought_reader:
                    current_date = datetime.strptime(
                        line["Bought_date"], "%Y-%m-%d").date()
                    if line["InStock"] == "True" and current_date <= the_date:
                        print(
                            " " + "{ID}  |  {Item}  |  {Bought}  |  {Bought_date}  |  {Expiration}  ".format(**line))

            elif sector == "revenue":
                total_rev = 0
                for line in copy_sold_reader:
                    rev = line["Price"]
                    total_rev += int(rev)
                print(f"Your revenue was {total_rev}")

            elif sector == "profit":
                print(f"you are in the profit and its this :{time} time")

        except FileNotFoundError:
            print("You havent created your inventory file yet")
            print("Your inventory is empty")


#################################################################################################################

    if args.command == "buy":
        buy(args.item, args.bought, args.expiration)
        print(f"OK, 1 {args.item} added to your inventory")
    elif args.command == "sell":
        sell(args.item, args.price)

    elif args.command == "report":
        report(args.task, args.time)


if __name__ == '__main__':
    main()
