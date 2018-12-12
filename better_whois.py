import subprocess
import sys
import re

def fang_url(url):
    return '.'.join(url.split('[.]'))

def clean_url(url):
    protocol_regex = re.compile('^.*://')
    match = protocol_regex.search(url)
    if match is None:
        return fang_url(url)
    else:
        url_without_protocol = url[match.end(0):]
        return fang_url(url_without_protocol)
    
def main():
    url = sys.argv[1]
    extra_params = []
    
    if len(sys.argv) < 1:
        print ('Missing URL')
        return

    if len(sys.argv) > 1:
        extra_params = sys.argv[2:]

    subprocess.Popen(['whois'] + [clean_url(url)] + extra_params)

if __name__ == '__main__':
    main()
