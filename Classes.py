try:
    class Point:
        def move(self):
            print("move")

        def drop(self):
            print('drop')


    point1 = Point()
    point1.x = 10
    point1.y = 20
    print(point1.x)
    point1.drop()

    point2 = Point()
    print(point2.x)
except AttributeError:
    print("It is okay")
