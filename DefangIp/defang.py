def defang(ip: str):
    result = ip.replace('.', '[.]')
    return result


print(defang('1.1.1.1'))
