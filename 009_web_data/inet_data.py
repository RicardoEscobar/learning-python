# 
# Example file for retrieving data from the internet
#
import urllib.request

def main():
    # open a connection to a URL using urllib2
    web_url = urllib.request.urlopen("http://www.google.com")

    # get the result code and print it
    print ("result code: " + str(web_url.getcode()))

if __name__ == "__main__":
    main()