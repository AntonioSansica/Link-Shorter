import pyshorteners


def short(link):
    s_link = pyshorteners.Shortener()
    n_link = s_link.tinyurl.short(link)
    print("> " + n_link)


def main():
    link = input("fornire link> ")
    short(link)


if __name__ == '__main__':
    main()
