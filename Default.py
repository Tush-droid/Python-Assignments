def Area(Radius,pi=3.14):
    Ans= pi*Radius*Radius
    return Ans


def main():
    Ret=Area(10.5)
    print("Area of circle", Ret)

    Ret=Area(10.5,7.12)
    print("Area of circle", Ret)


if __name__ =="__main__":
    main()
