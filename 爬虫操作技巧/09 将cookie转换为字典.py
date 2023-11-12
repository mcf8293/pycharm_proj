def cookie_convert_dict(cookie_string):
    mydic={}
    for item in cookie_string.split('; '):
        key, value = item.split('=')
        mydic[key.strip()]=value.strip()
    return mydic

if __name__ == '__main__':
    cookie_str = """        
            t=c45d2f297e2c388e92278cfaacc3c7cf; r=346; Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273=1699067809,1699073758; Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273=1699073758
            """

    print(cookie_convert_dict(cookie_str))
