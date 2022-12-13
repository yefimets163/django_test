from multiprocessing import Process

result = 0

def countTicket (start, end):
    count = 0
    for i in range(start, end):
        num = str(i).rjust(6, '0')
        if int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5]):
            count += 1
    print(f' from {start} to {end}: {count}')

if __name__ == '__main__':

    p1 = Process(target = countTicket, args = [0, 250000])
    p2 = Process(target = countTicket, args = [250000, 500000])
    p3 = Process(target = countTicket, args = [500000, 750000])
    p4 = Process(target = countTicket, args = [750000, 1000000])

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()



