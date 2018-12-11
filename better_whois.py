import subprocess
import sys
import re

def defang_url(url):
    return '.'.join(url.split('[.]'))

def clean_url(url):
    protocol_regex = re.compile('^.*://')
    match = protocol_regex.search(url)

    url_without_protocol = url[match.end(0):]
    return defang_url(url_without_protocol)
    
def main():
    url = sys.argv[1]
    extra_params = []
    
    if len(sys.argv) != 1:
        print ('Missing URL')

    if len(sys.argv) > 1:
        extra_params = sys.argv[2:]

    subprocess.Popen(['whois'] + [clean_url(url)] + extra_params)

if __name__ == '__main__':
    main()
