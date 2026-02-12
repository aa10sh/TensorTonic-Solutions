def median(nums):
    n=len(nums)
    mid=n//2

    if(n%2==0):
        return (nums[mid-1]+nums[mid])/2
    else:
        return (nums[mid])    

def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here
    if len(values) == 1:
      return [0]

    values2=sorted(values)
    q2=median(values2)

    n=len(values2)
    mid=n//2

    if(n%2==0):
        l_half=values2[:mid]
        u_half=values2[mid:]
    else:
        l_half=values2[:mid]
        u_half=values2[mid+1:]  

    q1=median(l_half)
    q3=median(u_half)

    scaled=[]
    iqr=q3-q1
    for x in values:
        if (iqr==0):
            scaled.append(x-q2)
        else:
            scaled.append((x-q2)/iqr)

    return scaled                  