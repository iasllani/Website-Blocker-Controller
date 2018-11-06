import time
from datetime import datetime as dt

hosts_temp = 'hosts'
# using the r allows us to escape 'escape' characters
hosts_path = r'C:\Windows\System32\drivers\etc'
# sites that we want to block
kill_sites = ['www.facebook.com', 'facebook.com', 'www.twitter.com', 'twitter.com']
redirect = '127.0.0.1'
# these 4 elements need their own respective lines on the host file and redirect IP
print(dt.now())
while True:
    # while our current time is within our schedule that we set below
    if dt(dt.now().year, dt.now().month, dt.now().day, 15) < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print('Working Hours: ')
        # if true, we will modify the hosts file, r+ allows us to modify the file
        with open(hosts_path, 'r+') as file:
            content = file.read()  # this will load our host file
            for site in kill_sites:
                if site in content:
                    pass
                else:
                    file.write(redirect+' '+site+'\n')
    else:
        with open(hosts_path, 'r+') as file:
            # the readlines method produces a list with each of the strings
            # as an element in the list. This helps us delete the adjustments we made prior
            content = file.readlines()
            file.seek(0)  # readlines moves our cursor to end of file, seek method resets it to beginning
            for line in content:
                if not any(site in line for site in kill_sites):
                    # this essentially copys and pastes lines that are NOT in our kill_sites
                    # we use this to preserve the original text in the file before we made changes
                    file.write(line)
            file.truncate()
        print('UNBLOCKED ENJOY :)')
    time.sleep(5)
