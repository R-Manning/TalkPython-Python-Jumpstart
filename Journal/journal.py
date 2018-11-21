"""
Journal module: file I/O, add/remove text from .jrl files
"""


import os


def load(name):
    """

    :param name: This is the name of the journal to load.
    :return: A new journal structure populated with the file data in the form of a list.
    """
    data = []
    filename = get_full_file_path(name)

    if os.path.exists(filename):
        with open(filename) as f_in:
            for entry in f_in.readlines():
                data.append(entry.rstrip())

    return data


def save(data, name):
    """

    :param data: This is the journal to be saved. List()
    :param name: This is the file name to save the journal to
    """
    filename = get_full_file_path(name)
    print('.... saving to: {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in data:
            fout.write(entry + '\n')


def get_full_file_path(name):
    """

    :param name: file name to be saved as .jrl file
    :return: full file-path OS independent
    """
    filename = os.path.abspath(os.path.join('.', 'Journals', name + '.jrl'))
    return filename


def add_entry(data, entry):
    """

    :param data: This is the journal to be added to
    :param entry: This is the entry that is to be added to the journal
    """
    data.append(entry)


def remove_entry(data, index):
    """

    :param data: This is the journal to remove the entry from
    :param index:  This is the index of the entry that you want to remove
    """
    data.pop(index)
