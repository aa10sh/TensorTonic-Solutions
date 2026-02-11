def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    values.sort()
    ans=[]
    if values[0]==values[-1]:
        return [0]*len(values)
    w=(values[-1]-values[0])/num_bins
    for i in values:
        ans.append(int(min((i-values[0])/w, num_bins-1)))

    return ans    
