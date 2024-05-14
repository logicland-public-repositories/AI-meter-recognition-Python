import argparse
import sys
from record_recognition import record_recognition



def main():
    if len(sys.argv) != 9:
        print("incorrect number of arguments")
        return
    
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--url", help="Target URL")
    parser.add_argument("-l", "--login", help="User name (login)")
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument("-i", "--image_path", help="Path to the image")

    args = parser.parse_args()
    url = args.url
    login = args.login
    password = args.password
    image_path = args.image_path
    try:
    	response = record_recognition(url=url, username=login, password=password, image_path=image_path)
    	print("reading:", response.json()["reading"])
    	print("reliability:", response.json()["reliability"])
    except Exception as error:
         print(error)


if __name__ == "__main__":
    main()
