import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------')
    print('    Journal App    ')
    print('-------------------')


def run_event_loop():
    print('What would you like to do with your journal?')
    cmd = 'Nothing yet!'
    journal_name = 'Default'  # Todo: add the ability to save/load to user defined file-names
    journal_data = journal.load(journal_name)  # list

    while cmd.upper() != 'X' and cmd:
        # turning input to all UPPER case and stripping white space
        cmd = input('[L]ist entries, [A]dd an entry, [R]emove an entry, E[X}it: ').upper().strip()
        print()  # new line to make the flow better
        if cmd == 'L':
            print(list_entries(journal_data))
        elif cmd == 'A':
            add_entry(journal_data)
        elif cmd == 'R':
            remove_entry(journal_data)
        elif cmd != 'X' and cmd:
            print('Invalid command. Please choose from the following list')

    print('Exiting app')
    journal.save(journal_data, journal_name)


def list_entries(data):
    text = ''
    if len(data) == 0:
        text = 'The journal is empty.\n'
    else:
        data = reversed(data)  # show most recent entries first
        for idx, entry in enumerate(data):
            text += '[{}] : {}\n'.format(idx + 1, entry)
    return text


def add_entry(data):
    entry = input('Type your entry, then hit <enter> to exit:\n')
    print()  # new line to flow better
    journal.add_entry(data, entry)
    # data.append(entry) to be deleted


def remove_entry(data):
    if len(data) == 0:
        print('The length of the journal is zero, cannot remove any entries.')
    else:
        print("Choose the index of the entry that you'd like to remove:\n")
        print("{}".format(list_entries(data)))
        # TODO: need to add in user input verification here so it doesn't crash
        index = int(input())
        journal.remove_entry(data, index)
        # data.pop(index * (-1)) to be deleted
        print()  # new line to flow better

# if we're trying to run this program, then run main
# otherwise, if the methods are just being accessed then don't run main
if __name__ == '__main__':
    main()
