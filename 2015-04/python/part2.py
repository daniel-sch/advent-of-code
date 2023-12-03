from hashlib import md5


def run(data):
    i = 0
    while True:
        if md5((data + str(i)).encode('ascii'), usedforsecurity=False).hexdigest().startswith("000000"):
            return i
        i += 1


if __name__ == "__main__":
    print(run("yzbqklnj"))
