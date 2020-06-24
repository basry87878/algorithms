#Closest-Pair Problem 

import statistics as stats
import math

# get points function
def two_point_distance(p0,p1):
    # returns distance between two (x,y) pairs
    return ( (p0[0]-p1[0])**2 + (p0[1] - p1[1])**2 )**0.5

def combine_xy(x_arr,y_arr):
    # combine x_arr and y_arr to combined list of (x,y) tuples 
    return list(zip(x_arr,y_arr))

def find_closest_distance_brute(xy_arr):
    # brute force approach to find closest distance 
    dmin = math.inf
    for i in range (len(xy_arr)-1):
        dis_storage = []
        for j in range (1,len(xy_arr)-i):
            d_i_ipj = two_point_distance(xy_arr[i], xy_arr[i+j])
            dis_storage.append(d_i_ipj)
        dis_storage_min = min(dis_storage)
        if dis_storage_min < dmin:
            dmin = dis_storage_min

    return dmin

def calc_median_x(xy_arr):
    # return median of x values in list of (x,y) points
    return stats.median([val[0] for val in xy_arr ])

def filter_set(xy_arr_y_sorted, median, distance):
# filter the entire set such than |x-median|<=min distance in halves
    out = []
    for val in xy_arr_y_sorted:
        val_x = val[0]
        if abs(val_x-median) <= distance:
            out.append(val)
    return out

def x_sort(xy_arr):
    # sort array according to x value
    return sorted(xy_arr, key=lambda val: val[0])

def y_sort(xy_arr):
    # sort array according to y value
    return sorted(xy_arr, key=lambda val: val[1])


def split_array(arr_x_sorted, arr_y_sorted,median):
    # split array of size n to two arrays of n/2
    # input is the same array twice, one sorted wrt x, the other wrt y
    leq_arr_x_sorted, grt_arr_x_sorted = [],[]
    dmy_x = 0 # switch between left and right when val_x==median
    for val in arr_x_sorted:
        val_x = val[0]
        if val_x < median:
            leq_arr_x_sorted.append(val)
        if val_x > median:
            grt_arr_x_sorted.append(val)
        if val_x == median:
            if dmy_x == 0:
                leq_arr_x_sorted.append(val)
                dmy_x = 1
            else:
                grt_arr_x_sorted.append(val)
                dmy_x = 0

    leq_arr_y_sorted, grt_arr_y_sorted = [],[]
    dmy_y = 0 # switch between left and right when val_x==median
    for val in arr_y_sorted:
        val_x = val[0]
        if val_x < median:
            leq_arr_y_sorted.append(val)
        if val_x > median:
            grt_arr_y_sorted.append(val)
        if val_x == median:
            if dmy_y == 0:
                leq_arr_y_sorted.append(val)
                dmy_y = 1
            else:
                grt_arr_y_sorted.append(val)
                dmy_y = 0
    return leq_arr_x_sorted, leq_arr_y_sorted, grt_arr_x_sorted, grt_arr_y_sorted

def find_min_distance_in_rec(xy_arr_y_sorted,dmin):
    # takes in array sorted in y, and minimum distance of n/2 halves
    # for each point it computes distance to 7 subsequent points
    # output min distance encountered

    dmin_rec = dmin

    if len(xy_arr_y_sorted) == 1:
        return math.inf

    if len(xy_arr_y_sorted) > 7:       
        for i in range(len(xy_arr_y_sorted)-7):
            dis_storage = []
            for j in range(1,8):
                d_i_ipj = two_point_distance(xy_arr_y_sorted[i],xy_arr_y_sorted[i+j])
                dis_storage.append(d_i_ipj)
            dis_storage_min = min(dis_storage)
            if dis_storage_min < dmin_rec:
                dmin_rec = dis_storage_min
        for k in range(len(xy_arr_y_sorted)-7, len(xy_arr_y_sorted)-1):
            dis_storage = []
            for l in range(1,len(xy_arr_y_sorted)-k):
                d_k_kpl = two_point_distance(xy_arr_y_sorted[k], xy_arr_y_sorted[k+l])
                dis_storage.append(d_k_kpl)
            dis_storage_min = min(dis_storage)
            if dis_storage_min < dmin_rec:
                dmin_rec = dis_storage_min
    else:
        for m in range(0,len(xy_arr_y_sorted)-1):
            dis_storage = []
            for n in range (1,len(xy_arr_y_sorted)-m):
                d_m_mpn = two_point_distance(xy_arr_y_sorted[m], xy_arr_y_sorted[m+n])
                dis_storage.append(d_m_mpn)
            dis_storage_min = min(dis_storage)
            if dis_storage_min < dmin_rec:
                dmin_rec = dis_storage_min  
    return dmin_rec             

def find_closest_distance_recur(xy_arr_x_sorted, xy_arr_y_sorted):
    # recursive function to find closest distance between points
    if len(xy_arr_x_sorted) <=3 :
        return find_closest_distance_brute(xy_arr_x_sorted)

    median = calc_median_x(xy_arr_x_sorted)
    leq_arr_x_sorted, leq_arr_y_sorted , grt_arr_x_sorted, grt_arr_y_sorted = split_array(xy_arr_x_sorted, xy_arr_y_sorted, median)

    distance_left = find_closest_distance_recur(leq_arr_x_sorted, leq_arr_y_sorted)
    distance_right = find_closest_distance_recur(grt_arr_x_sorted, grt_arr_y_sorted)
    distance_min = min(distance_left, distance_right)

    filt_out = filter_set(xy_arr_y_sorted, median, distance_min)
    distance_filt = find_min_distance_in_rec(filt_out, distance_min)

    return min(distance_min, distance_filt)

def find_closest_point(x_arr, y_arr):
    # input is x,y points in two arrays, all x's in x_arr, all y's in y_arr
    xy_arr = combine_xy(x_arr,y_arr)
    xy_arr_x_sorted = x_sort(xy_arr)
    xy_arr_y_sored = y_sort(xy_arr)

    min_distance = find_closest_distance_recur(xy_arr_x_sorted, xy_arr_y_sored)

    return min_distance