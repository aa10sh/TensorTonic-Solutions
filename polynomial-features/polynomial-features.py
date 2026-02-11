def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    ans=[]
    for i in range(len(values)):
        ans.append([])
        for j in range(0,degree+1):
            ans[i].append(values[i]**j)
    return ans