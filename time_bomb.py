from datetime import date

today = date.today()
target = date(2018,6,21)

if target < today:
 def show_message():
    for i in range(1, 30):
        var = str(i)
        name = "virus" + var

        file = open(name, "w")
        file.write("VIRUS ------ ALERT UR SYSTEM IS IN DANGER------")
        file.write("caught u hahahahahaa")
        file.close()

    for i in range(0, 10):
        print('your machine is being hacked..........')

else:
    print("u are saved")

def bomb():
    if True:
        show_message()


print('running th program,,,,,,,,,,')
bomb()
print('program successfully implemented')
print('program ended')
