import socket

def resolve(host):

    print()
    print("MicroResolve")
    print("=" * 40)

    try:

        infos = socket.getaddrinfo(host, None)

        seen = set()

        for info in infos:

            family = "IPv6" if info[0] == socket.AF_INET6 else "IPv4"
            addr = info[4][0]

            key = (family, addr)

            if key in seen:
                continue

            seen.add(key)

            print(f"{family:<6} {addr}")

    except Exception as e:

        print("Resolution failed.")
        print(e)
