import shelve


def get_batch(location, selection):
    """

    :return: Index number of the batch
    """
    db = shelve.open(location)
    temp = db[selection]
    db.close()
    return temp


def load_batches(location):
    """
    Create a list of batch names
    :return:
    """
    dbs = shelve.open(location)
    batch_list = []
    for batch in dbs:
        batch_list.append(batch)
    dbs.close()

    return batch_list


def is_current_batch(current_batch: str, dbs):
    """

    :param current_batch:
    :param dbs:
    :return:
    """
    # if current_batch == '':
    #     print('No open batch, please open a batch')
    #     current_batch = open_batch(dbs)
    #     return current_batch
    # else:
    #     return current_batch


def edit_batch_info(current_batch: str, dbs):
    current_batch = is_current_batch(current_batch, dbs)
    temp = dbs[current_batch]
    temp.update_final_gravity()
    dbs[current_batch] = temp
    print(dbs[current_batch].final_gravity)



