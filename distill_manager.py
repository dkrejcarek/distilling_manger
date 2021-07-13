import shelve
import function as f
import window

options = {
    '0': 'Exit',
    '1': 'New Batch',
    '2': 'Open Batch',
    '3': 'Update Batch',
    '4': 'Print Batch',
    '5': 'Add Run info',
    '6': 'Delete Batch'
}

db = shelve.open("batches")
current_batch = ""

print('Welcome to Distilling Manager')
print()

window.mainWindow.mainloop()
while True:
    if not current_batch:
        for i in range(0, 3):
            print('{}: {}'.format(i, options[str(i)]))
    else:
        for option in options:
            print('{}: {}'.format(option, options[option]))

    selection = input("Please enter an option: ")

    if selection == '0':
        break
    elif selection == '2':
        current_batch = f.open_batch(db)

    elif selection == '3':
        current_batch = f.is_current_batch(current_batch, db)
        temp = db[current_batch]
        temp.update_final_gravity()
        db[current_batch] = temp
        print(db[current_batch].final_gravity)

    elif selection == '4':
        current_batch = f.is_current_batch(current_batch, db)
        print(db[current_batch])

    elif selection == '5':
        current_batch = f.is_current_batch(current_batch, db)
        temp = db[current_batch]
        temp.start_run()
        db[current_batch] = temp

    elif selection == '6':
        current_batch = f.is_current_batch(current_batch, db)
        confirm = input('Are you sure you want to delete {} (y/n): '.format(current_batch))
        if confirm.lower() == 'y':
            del db[current_batch]
            current_batch = ''
            print('Batch deleted')
        else:
            print("Deletion canceled")

    else:
        print('Please print a valid option')

print('Goodbye, Thank you for using Distilling Manager')
