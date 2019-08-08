import time

tt1 = time.time()


with open('test1.txt', 'w') as fout:

    for i in xrange(1000000):
        # i % 4
        print >> fout, 1

tt2 = time.time()
print(tt2 - tt1)


from threading import Thread

def writer(filename, n):

    with open(filename, 'w') as fout:

        for i in xrange(n):
            # i % 4
            print >> fout, 1
#
t1 = Thread(target=writer, args=('test2.txt', 1000000,))

t2 = Thread(target=writer, args=('test3.txt', 1000000,))

t1.start()

t2.start()

t1.join()

t2.join()

print (time.time()-tt2)


from multiprocessing import Pool, cpu_count
pool = Pool()
start = time.time()
for i in range(4):
    pool.apply_async(writer, args=('test_b_'+str(i+1)+'.txt', 1000000))
pool.close()
pool.join()
print(time.time()-start)
