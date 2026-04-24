grep -m1 "Linux version" dmesg | sed -n 's/.*(Ubuntu \(.*\)).*/\1/p'
