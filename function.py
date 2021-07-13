import shelve
from batch import Batch

db = shelve.open("batches")
current_batch = ""


def create_new_instance():
    style = input('Enter the style: ')
    date = input("Enter Date: ")
    og = float(input('Enter original gravity: '))
    vol = float(input('Enter volume (L): '))
    batch = Batch(style, date, og, vol)  # Start a new instance of batch
    name = '{}_{}'.format(style, date)

    return [name, batch]


def open_batch(dbs):
    """

    :return: Index number of the batch
    """
    batch_list = load_batches(dbs)
    if len(batch_list) == 0:
        print('No saved Batches, please start a new batch')
        return ''
    i = 0
    for batch in dbs:
        print(i + 1, batch)
        i += 1
    selection = int(input('Select Batch to open: '))
    return batch_list[selection - 1]


def load_batches(dbs):
    """
    Create a list of batch names
    :return:
    """

    batch_list = []
    for batch in dbs:
        batch_list.append(batch)
    return batch_list


def is_current_batch(current_batch: str, dbs):
    """

    :param current_batch:
    :param dbs:
    :return:
    """
    if current_batch == '':
        print('No open batch, please open a batch')
        current_batch = open_batch(dbs)
        return current_batch
    else:
        return current_batch


def edit_batch_info(current_batch: str, dbs):
    current_batch = is_current_batch(current_batch, dbs)
    temp = dbs[current_batch]
    temp.update_final_gravity()
    dbs[current_batch] = temp
    print(dbs[current_batch].final_gravity)
