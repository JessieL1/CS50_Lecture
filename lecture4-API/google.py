import requests

def main():
    res = requests.get("https://www.baidu.com/")
    print(res.text.decode('utf-8'))

if __name__ == "__main__":
    main()