import sys
import multiprocessing

class Recon_Bear:
    def __init__(self, ip, type, speed):
        self.ip = ip
        self.type = type
        self.speed = speed


    def dirsearch(self):
        print('TO DO')


    def smb_scan(self):
        print('TO DO')


    def nikto_scan(self):
        print('TO DO')


    def nmap_scan(self):
        print('TO DO')


# check python version
def check_version():
    if sys.version_info[0] < 3:
        raise Exception("You will need Python 3 for this tool")

def show_options(option):
    if (option == 'ip'):
        print('IP address: ')
    if (option == 'type'):
        print('Indicate the scan type: ')
        print('\t1 - Normal')
        print('\t2 - Full')
        print('\t3 - Specific (you will need to choose which ports to scan)')
    if (option == 'speed'):
        print('Speed option: ')
        print('\t1- Slow')
        print('\t2 - Fast')

# get scan options
def get_options():
    ip = ''
    type = ''
    speed = ''

    show_options('ip')
    ip = input()
    show_options('type')
    type = input()
    show_options('speed')
    speed = input()

# main function
def main():
    check_version()


if __name__ == '__main__':
    main()
