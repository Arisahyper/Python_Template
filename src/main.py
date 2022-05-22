from pkg import pkg1


def main():
    greet = pkg1.greet_handler("World")
    print(greet)


if __name__ == "__main__":
    main()
