def Area(Radius,pi):
    Ans= pi*Radius*Radius
    return Ans


def main():
    Ret=Area(10.5,3.14)
    print("Area of circle", Ret)

    Ret=Area(13.6,7.12)
    print("Area of circle", Ret)

if __name__ =="__main__":
    main()
