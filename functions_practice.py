def hello():
    print("hello user"),


def pack(deku,leon,zoro):
    return[deku,leon,zoro],

def eat_lunch(luffy):
    if len(luffy) == 0:
        print("My lunchbox is empty"),
    else:
        for i in range(len(luffy)):
            if i == 0:
                print(f"first i eat{luffy[0]}")
            else:
                print(f"next i eat {luffy[i]}")


hello()
print(pack("deku","leon","zoro"))
eat_lunch([])
eat_lunch(["gomu gomu"])
eat_lunch(["sing sing","wax wax"])




