import requests

url = "https://www.samsung.com/in/api/v4/configurator/syndicated-product-linear?skus=SM-F936BZAD,SM-F936BZKD&component=offers,promotion,promotion_price,delivery_modes&count=0"

payload={}
headers = {
  'Cookie': 'ak_bmsc=15AE2B7B3E773DE899AD7172905F9B32~000000000000000000000000000000~YAAQX2f2SMCgieKEAQAAEFlZ5xLUKVr6630OYEAC2xGL70v/v7ws8JCsYcxF0CWptH/syql2xJ03GTEuBs74oziPcZyi+BedjRzyqL9+iYLouALqIIKr6xMFtoZBgVMeCUENRcBa/QqU5rR11TV2mzfEHeSpauCfr2y0B5JC4BkY+VyTXBKwGluBRsNkhCJV9d9A9Twuur6NpclLTwsCS83glvkEbIYVNqOcWPEb+e/E/0QRyKWuApYr13b3+dXlg4YO69kNG3iEUYWcjabww6cjKgj5g3/FdA4MJLZCor8UNGRiOqSdYb5UOQJEeDoSLAXnzu3EviwjD7Yi2Qbk+/oX7zTqZiWjrlOxp3S9Iv2cL7xSZRHx2Aah1OBJmw==; bm_sv=D765DDF1F9F97B3DDBC977268447F6A5~YAAQX2f2SCA9i+KEAQAAPvxi5xLd4OwERrj89H/iTa/IUsfke9RBIlJ5g5XVamC5H93d/F51Rc8GpnPvQg7teoz8vUIK1rFQOf2SeTyGjIpLXKekyZz1J/fPevj+0w3AbRGkzg8Fx+tlZROMCGqwf/Xiu8r0AgHUWQEODZ8yQx0PhLMvYAODNmpPy7nrhuEKxo5V08doicSvQvwV+QB/VTWBhsJqk97jutY4kSlyHu10OqmntQs+TdXYpVc6qunDow==~1; country_codes=in; device_type=pc; country_region=CA-ON'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
