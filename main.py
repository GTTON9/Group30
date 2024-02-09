# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from GrabData.GOLD_graber import GrabHttp

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://my.sa.ucsb.edu/gold'

    xpath_list = []
    IndexValue = GrabHttp(url, xpath_list).IndexValue


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
