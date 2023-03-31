'''
Amazon has a string of categories of items purchased by a particular customer, each represented as a lowercase English letter. To analyze customer behavior, 
we define a metric called the MaximaCount of a category. It is the number of indices where the frequency of some category e is maximum among all
categories present in the prefix of i.
More elaboratively, MaximaCount of character, char, representing a category is defined as the number of indices i, 
such that the frequency of char is maximum in the prefic of the string up to the index i
Given the string categories, find the maximum Maxima Count among al the categories.
'''




def maxima_count1(categories):
    uniq = list(set(categories))
    print(uniq)
    m = len(uniq)
    n = len(categories)
    arr = [[0]*n for _ in range(m)]
    count = [0]*m

    for i in range(0,n):
        idx = uniq.index(categories[i])
        count[idx] += 1
        for j in range(i,n):
            arr[idx][j] = count[idx]

    
    count = [0] * m
    max_count = 0
    max_idx = -1

    for i in range(n):
        for j in range(m):
            if arr[j][i] > max_count:
                max_count = arr[j][i]
                print(j)
                print(max_count)
                max_idx = j

                count[max_idx] += 1

        # Reset max_count and max_idx for the next column
        max_count = 0
        max_idx = -1

    max_count = max(count)

    return max_count
  
  
  
  
  
  '''
max_count1 = maxima_count1("bcc")
print(max_count1)  # output: 2
'''
  
  
  
  
  
