import argparse
import csv
import os
from datetime import datetime, date, timedelta
from gooey import Gooey, GooeyParser


now = date.today()
yesterday = now - timedelta(days=1)


@Gooey(
    program_name='My Supermarkt APP',
    image_dir="C:/Users/Bernard/Desktop/Gooey/images",
    show_preview_warning=False,
    advanced=True,
    navigation='TABBED',
    header_bg_color="#f69c00",

    menu=[{'name': 'Help', 'items': [{'type': 'AboutDialog',
                                      'menuTitle': 'About',
                                      'name': 'My Supermarket APP',
                                      'description': 'This is a little summary on how to use this app, you have three main options: 1 Buy is where you can purchase items to add to your store, 2 Sell is where you can sell the same items to your costumers, 3 Reports is where you can get your reports on how your store is going',
                                      'version': '1.2.1',
                                      'copyright': '2022', }]}]
)
def main():

    parser = GooeyParser(
        description="Welcome to the My Supermarket, the tool to help you run your store")
    subparser = parser.add_subparsers(
        dest='command', description="Choose from the diferent departments")

    buy_parser = subparser.add_parser('Buy')
    sell_parser = subparser.add_parser('Sell')
    stock_parser = subparser.add_parser("Stock")
    search_parser = subparser.add_parser("Search_Report")


#############################################################################
    buy_parser.add_argument('-p', '--Product', required=True, type=str,
                            help="Product that you would like to ADD to your store")
    buy_parser.add_argument('-b', '--Bought', required=True, type=float,
                            help="The price you BOUGHT the product for")
    buy_parser.add_argument(
        '-e', '--Expiration',  required=True, help="Exiration date on the Product", widget="DateChooser")
##############################################################################
    sell_parser.add_argument('-p', '--Product',  required=True, type=str,
                             help="Product you wish to SEll in your store")
    sell_parser.add_argument(
        '-s', '--SELL', required=True, type=int, help="Price you wish to SELL the product for")


#############################################################################
    stock_group = stock_parser.add_argument_group(
        "Stock", "Check the products you currently have in your store")
    stock_group.add_argument(
        '-p', '--print', action="store_true", default=False)


#########################################################################
    search_group = search_parser.add_argument_group(
        "Search_Report", "Search though inventory history ")

    search_group.add_argument('-from', '--Start',
                              help="Type in the dates you would like to see your inventory report", widget="DateChooser")
    search_group.add_argument('-till', '--End',
                              help="Type in the dates you would like to see your inventory report", widget="DateChooser")
    search_group.add_argument('Department', choices=(
        "Inventory", "Revenue", "Profit", "Waste"))

#########################################################################
    args = parser.parse_args()

    #######################################################################
    csv_path = os.path.join(os.getcwd(), os.path.basename('bought.csv'))
    file_exists = os.path.isfile(csv_path)

    csv_sell_path = os.path.join(os.getcwd(), os.path.basename("sold.csv"))
    sell_file_exists = os.path.isfile(csv_sell_path)

    class SuperPy:

        sold_field_names = ["ID", "Product", "Price", "Sold_date",
                            "Expiration"]
        bought_field_names = ["ID", "Product", "Bought_price", "Bought_date",
                              "Expiration", "InStock"]

        def incre(count):
            count += 1
            return count

        def open_read_bought():
            with open('bought.csv', 'r', newline="") as output:
                csv_reader = csv.DictReader(output)
                copy_bought_reader = [line for line in csv_reader]

                return copy_bought_reader

        def open_read_sold():
            with open('sold.csv', 'r', newline="") as sold_read:
                csv_sell_reader = csv.DictReader(sold_read)
                copy_sold_reader = [line for line in csv_sell_reader]
                return copy_sold_reader

        def check_lowest_ex(product, reader):
            day_list = list()

            expiration_list = [line["Expiration"]
                               for line in reader if product == line["Product"] and line['InStock'] == "True"]

            if len(expiration_list) == 0:
                return print(f"Sorry! but you dont have anymore: {product}s in your inventory")

            for date in expiration_list:  # function to determine lowest expiration date

                ExpirationDate = datetime.strptime(
                    date, "%Y-%m-%d").date()
                amount_days = ExpirationDate - now

                if int(amount_days.days) > 0:
                    day_list.append(int(amount_days.days))
                lowest = min(day_list)

            return lowest

        def check_time(self, time):
            if time == "now":
                the_date = now
            elif time == "yesterday":
                the_date = yesterday
            elif time[0] in "1234567890" and time[-1:] in "wekdaymonths":
                time_arr = list(time)
                num = int(time_arr.pop(0))
                str_time = "".join(time_arr)
                if str_time == "weeks" or str_time == "week":
                    the_date = now - timedelta(days=7 * num)
                elif str_time == "month" or str_time == "months":
                    the_date = now - timedelta(days=30 * num)
                elif str_time == "day" or str_time == "days":
                    the_date = now - timedelta(days=1 * num)
            elif time[:2] == "20":

                the_date = datetime.strptime(
                    time, "%Y-%m-%d").date()

            return the_date

        def check_expired_products(self, reader):
            for line in reader:
                expiration_date = datetime.strptime(
                    line["Expiration"], "%Y-%m-%d").date()

                if expiration_date < now:
                    line["InStock"] = "Expired"

            writer = csv.DictWriter(
                open('bought.csv', 'w', newline=''), fieldnames=self.bought_field_names)
            writer.writeheader()
            for line in reader:
                writer.writerow(line)

        def print_stock_or_waste(variable):

            print("===================================")
            print("|  ID  |  Item  |  Bought  |  Bought_date  |  Expiration |  InStock")
            print("===================================")
            copy_reader = SuperPy.open_read_bought()
            for line in copy_reader:
                if line["InStock"] == variable:

                    print(
                        "|  {ID}  |  {Item}  |  {Bought}  |  {Bought_date}  |  {Expiration} |  {InStock}".format(**line))

            print("===================================")
# ####################################################################################################################################

    class Buy(SuperPy):
        def __init__(self, product, bought, expiration):
            self.product = product
            self.bought = bought
            self.expiration = expiration

        def add_inventory(self):
            try:

                with open('bought.csv', 'a', newline="") as input:
                    csv_writer = csv.DictWriter(
                        input, fieldnames=SuperPy.bought_field_names)
                    csv_reader = SuperPy.open_read_bought()

                    if not file_exists:
                        id = 1
                        csv_writer.writeheader()
                        csv_writer.writerow(
                            {"ID": id, 'Product': self.product, 'Bought_price': self.bought, "Bought_date": now, 'Expiration': self.expiration, 'InStock': True})

                    elif file_exists:

                        for line in csv_reader:
                            c = line["ID"]
                            id = int(c)
                            print(id)

                        csv_writer.writerow(
                            {"ID": SuperPy.incre(id), 'Product': self.product, 'Bought_price': self.bought, "Bought_date": now, 'Expiration': self.expiration, 'InStock': True})
            except Exception as e:
                print(e)

################################################################################################################################

    class Sell(SuperPy):
        def __init__(self, product, sold):
            self.product = product
            self.sold = sold

        def sell_products(self):
            try:
                with open('sold.csv', 'a', newline="") as sold_input:
                    csv_sell_writer = csv.DictWriter(
                        sold_input, fieldnames=SuperPy.sold_field_names)

                    if csv_sell_path:
                        csv_sell_reader = SuperPy.open_read_sold()
                        for line in csv_sell_reader:     # to get the ID number
                            c = line["ID"]
                            id = int(c)
                    else:
                        id = 1
                    if file_exists:      # check bought file exists
                        copy_reader = SuperPy.open_read_bought()
                        low = SuperPy.check_lowest_ex(
                            self.product, copy_reader)
                        for line in copy_reader:
                            expiration = line["Expiration"]
                            current_ex = datetime.strptime(
                                expiration, "%Y-%m-%d").date()
                            current_num = current_ex - now
                            if int(current_num.days) > 0:  # check if the item is expired
                                correct_num = int(current_num.days)
                            elif int(current_num.days) <= 0 and self.product == line['Product']:
                                line["InStock"] = "Expired"
                            if low == correct_num and self.product == line['Product'] and line["InStock"] == "True":
                                if not sell_file_exists:  # if sold file is not created yet
                                    id = 1
                                    line["InStock"] = False
                                    csv_sell_writer.writeheader()
                                    csv_sell_writer.writerow(
                                        {"ID": id, 'Product': self.product,
                                            'Price': self.sold, "Sold_date": now, 'Expiration': expiration}
                                    )
                                    print("Item sold")
                                    break
                                if sell_file_exists:
                                    line["InStock"] = False
                                    csv_sell_writer.writerow(
                                        {"ID": SuperPy.incre(id), 'Product': self.product,
                                         'Price': self.sold, "Sold_date": now, 'Expiration': expiration}
                                    )
                                    print("Item sold")
                                    break

                    else:
                        print(
                            "ID  Item  Bought_price  Bought_date  Expiration  InStock")
                        print("Your inventory is empty")

                writer = csv.DictWriter(
                    open('bought.csv', 'w', newline=''), fieldnames=SuperPy.bought_field_names)

                writer.writeheader()
                for line in copy_reader:
                    writer.writerow(line)

            except Exception as e:
                print(e)


#################################################################################################################

    class Report(SuperPy):
        def __int__(self, sector, sta_dat, end_dat):
            self.sector = sector
            self.sta_dat = sta_dat
            self.end_dat = end_dat

        def records(self):
            try:
                copy_bought_reader = SuperPy.open_read_bought()
                copy_sold_reader = SuperPy.open_read_sold()

                if self.sector == "Inventory":
                    for line in copy_bought_reader:
                        keys = list(line.keys())
                        keys
                        print(
                            "========================================")
                        print("", "  |  ".join(keys))
                        print(
                            "========================================")

                        break
                    SuperPy.check_expired_products(copy_bought_reader)

                    for line in copy_bought_reader:
                        current_date = datetime.strptime(
                            line["Bought_date"], "%Y-%m-%d").date()

                        if self.end_dat == None:
                            the_date = SuperPy.check_time(self.sta_dat)
                            if the_date == current_date:

                                print(
                                    "{ID}  |  {Item}  |  {Bought}  |  {Bought_date}  |  {Expiration}  |  {InStock}".format(**line))

                        if self.end_dat is not None:

                            stadate = self.sta_dat
                            endate = self.end_dat

                            start_date = datetime.strptime(
                                stadate, "%Y-%m-%d").date()

                            end_date = datetime.strptime(
                                endate, "%Y-%m-%d").date()

                            if start_date <= current_date and end_date >= current_date:
                                print(
                                    "{ID}  |  {Item}  |  {Bought}  |  {Bought_date}  |  {Expiration}  |  {InStock}".format(**line))

                            # print(
                            #     f"This is your report from {start_date} till {end_date}")

                elif self.sector == "Revenue":
                    total_rev = 0
                    for line in copy_sold_reader:
                        current_date = datetime.strptime(
                            line["Sold_date"], "%Y-%m-%d").date()

                        if self.end_dat == None:
                            the_date = self.check_time(self.sta_dat)
                            if the_date == current_date:
                                rev = line["Price"]
                                total_rev += int(rev)
                        elif self.end_dat is not None:

                            stadate = self.sta_dat
                            endate = self.end_dat

                            start_date = datetime.strptime(
                                stadate, "%Y-%m-%d").date()

                            end_date = datetime.strptime(
                                endate, "%Y-%m-%d").date()

                            if start_date <= current_date and end_date >= current_date:
                                rev = line["Price"]
                                total_rev += int(rev)
                    print(f"Your revenue was {total_rev}")

                elif self.sector == "Profit":
                    print(
                        f"you are in the profit and its this :{self.when} time")

            except FileNotFoundError:
                print("You havent created your inventory file yet")
                print("Your inventory is empty")


#################################################################################################################

    if args.command == "Buy":
        product = Buy(args.Product, args.Bought, args.Expiration)
        product.add_inventory()
        print(f"OK, 1 {args.Product} added to your inventory")
    elif args.command == "Sell":
        sold_product = Sell(args.Product, args.SELL)
        sold_product.sell_products()

    elif args.command == "Stock":
        if args.print:
            SuperPy.print_stock_or_waste("True")
    elif args.command == "Search_Report":
        if args.Department == "Waste":
            SuperPy.print_stock_or_waste("Expired")

        else:
            report = Report(args.Department, args.Start, args.End)
            report.records()


if __name__ == '__main__':
    main()
