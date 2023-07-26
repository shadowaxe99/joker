def read_shipping_order(file):
    with open(file, 'r') as f:
        print(f.read())


if __name__ == '__main__':
    read_shipping_order('shipping_order.txt')