seconds = int(input())
if seconds > 86400:
    print(seconds // 86400,"days")
else:
    if seconds > 3600 and seconds < 86400:
        print(seconds // 3600,"hours")
    else:
        if seconds > 60 and seconds < 3600:
            print(seconds // 60,"minutes")
            
