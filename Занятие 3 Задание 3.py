def add (n):
     n = n % 1440
     h = n // 60
     n = n - (h*60)
     print(h,n)
