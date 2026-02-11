
def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here
    answer=[]  
    for v in values:  
      angle=2*math.pi*v/period
      answer.append([math.sin(angle),math.cos(angle)])

    return answer        


