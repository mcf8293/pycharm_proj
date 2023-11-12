# 冒泡排序算法
# 冒泡排序
def bubble_sort(arr):
    # 获取数组的长度
    n = len(arr)
    # 遍历数组
    for i in range(n):
        # 内层循环，从第一个元素开始，到最后一个元素结束
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 示例
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("排序后的数组：")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
