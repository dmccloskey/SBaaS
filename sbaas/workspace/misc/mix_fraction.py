def mix_fraction(sample1, sample2, **kwargs):
    """ Compares two sets of sampled points and determines how mixed
    they are.

    Arguments
     sample1, sample2   Ordered set of points, numpy arrays.  The points must be in
                       the same order otherwise it does not make sense.
    kwargs
     fixed (optional)   The directions which are fixed and are not expected (indices)

    Returns
     mix                the mix fraction.  Goes from 0 to 1 with 1 being
                        completely unmixed and .5 being essentially 
                        perfectly mixed.  


    """
    from numpy import min, isnan, median, outer
    
    if 'fixed' not in kwargs:
        fixed = []
    else:
        fixed = kwargs['fixed']
        

    # ignore NAN rows
    ignore_rows = isnan(min(sample1,1)) | isnan(min(sample2,1))
    if len(fixed) > 0:
        ignore_rows[fixed] = True
    keep_rows = ~ ignore_rows

    sample1_reduced = sample1[keep_rows,:]
    sample2_reduced = sample2[keep_rows,:]

    m1 = median(sample1_reduced, 1)
    LPproblem = median(sample2_reduced, 1)
    n_rxn_reduced, n_points = sample1_reduced.shape

    l1 = (sample1_reduced > (outer(m1, ones([1, n_points]))))
    eq1 = (sample1_reduced == outer(m1, ones([1, n_points])))
    l2 = (sample2_reduced > outer(LPproblem, ones([1, n_points])))
    eq2 = (sample2_reduced == outer(LPproblem, ones([1, n_points])))

    eqtotal = eq1 | eq2

    fr_mix = float(sum(sum((l1 == l2) & (~ eqtotal))))/float(l1.size-sum(sum(eqtotal)))

    return fr_mix