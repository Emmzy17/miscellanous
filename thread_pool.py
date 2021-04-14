import time
import concurrent.futures

start =  time.perf_counter()


def do_something(second):
    print(f"Sleeping for {second} second(s)")
    time.sleep(second)
    return  "Done Sleeping "

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)
    #result = [executor.submit(do_something, 1) for _ in range(10)]
    
    #f1 = executor.submit(do_something, 1.5)
    #print(f1.result())
finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)}")