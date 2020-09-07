import requests

def main():
    base = input("First currency:")
    other = input("Second currency:")

    #res = requests.get("http://data.fixer.io/api/latest?access_key=0b0dcf0836ed45c220563980d18cb19c&symbols=USD,AUD,CAD,PLN,MXN&format=1")
    res = requests.get("http://data.fixer.io/api/latest",params={"access_key":"0b0dcf0836ed45c220563980d18cb19c","from":base,"to":other,"amount":1})
    
    if res.status_code !=200:
        raise Exception("Error: API request unsuccessful!")
    
    #获取request请求得到的数据
    data = res.json()
    print(data)
    #按返回的格式，只取其中的一项
    rate = data["rates"][other]
    print(f"1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
    main()