from multiprocessing import Pool, cpu_count


def calculate_range(start, end):
    ranges = []
    cpu_range = end - start +1
    partial = cpu_range//cpu_count()
    remainder = cpu_range % cpu_count()
    for cpu_num in range(cpu_count()):
        start_partial = cpu_num*partial
        end_partial = (cpu_num+1)*partial
        ranges.append([start_partial-end, end_partial-end])
    if remainder > 0:
        ranges[-1][1] += remainder
        
    return ranges

def two_sum(arr, start, end):
    count = 0
    for i in range(start, end):
        for j in arr:
            c = i - j
            if c in arr and c != j: #if complement is in the hashMap and complement is not the target it self
                count +=1
                break
    return count


def main():
    with open("2SUM.txt","r", encoding="utf-8") as file:
        arr = set(int(i) for i in file.read().splitlines())
        
        start = -10000
        end = 10000
        
        # implementation 1:
        # count = sum(any(n-x in arr and 2*x != n for x in arr) for n in range(start, end+1))
        # print(count)

        #implementation 2:
        with Pool(processes=cpu_count()) as p:
            ranges = calculate_range(start, end)
            results = p.starmap(two_sum, [(arr, ranges[i][0], ranges[i][1]) for i in range(cpu_count())])
            p.close()
            p.join()
            total = sum(results)
            
        print(total)
            
if __name__ == "__main__":
    main()