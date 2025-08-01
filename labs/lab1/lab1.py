import random
import time
import matplotlib.pyplot as plt


myList = [1, 2, 3, 4, 5]

# #Original LinearSearch function
# def LinearSearch(list,key):
#     for i in range(0,len(list)):
#         if (list[i]==key):
#             return i
#     return -1

def LinearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# #Original GenArray function
# def GenArray(n):
#     arr = []
#     while len(arr)!=n:
#         num = random.randint(0,n)
#         if LinearSearch(arr,num)==-1:
#             arr.append(num)
#     return arr

def GenArray(n):
    arr = []
    while len(arr) != n:
        num = random.randint(0, n)
        if num not in arr:
            arr.append(num)
    return arr
best_times = []
worst_times = []
avg_times = []
def experiment_linear_search():
    sizes = [10, 100, 1000, 5000, 10000]
    print("Best Case Performance:")
    for n in sizes:
        arr = GenArray(n)
        key = arr[0]  # Best case: key at start
        start = time.time()
        LinearSearch(arr, key)
        end = time.time()
        elapsed = end - start
        best_times.append(elapsed)
        print(f"n={n}, time={elapsed:.8f} seconds (best case)")

    print("\nWorst Case Performance:")
    for n in sizes:
        arr = GenArray(n)
        key = arr[-1]  # Worst case: key at end
        start = time.time()
        LinearSearch(arr, key)
        end = time.time()
        elapsed = end - start
        worst_times.append(elapsed)
        print(f"n={n}, time={elapsed:.8f} seconds (worst case)")

    print("\nAverage Case Performance:")
    for n in sizes:
        arr = GenArray(n)
        key = arr[random.randint(0, n-1)]  # Average case: random position
        start = time.time()
        LinearSearch(arr, key)
        end = time.time()
        elapsed = end - start
        avg_times.append(elapsed)
        print(f"n={n}, time={elapsed:.8f} seconds (average case)")

   
experiment_linear_search()

# #Original experiment code
# lenn = 10000
# #BEST CASE
# print("BEST CASE")
# best_case  = GenArray(lenn);
# key = best_case[0];
# print("array ", best_case, "key: ", key)
# print(LinearSearch(best_case,key))
# print("")
# #worst CASE
# worst_case  = GenArray(lenn);
# key = worst_case[len(worst_case)-1];
# print("WORST CASE:")
# print("array ", worst_case, "key: ", key)
# print(LinearSearch(worst_case,key))

plt.plot(worst_times,marker='o')
plt.plot(best_times,marker='o')
plt.plot(avg_times,marker='o')
plt.grid(True)
plt.show()