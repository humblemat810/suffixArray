# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:09:46 2020

@author: pchan
"""
in_str = 'suffixarray'
def string_to_list_ord(in_str):
    return [ord(i) for i in in_str]
def list_ord_to_string(in_list_ord):
    return ''.join(chr(i) for i in in_list_ord)

str_len = len(in_str)
i = 1
char_size = 256
def radix_sort_chr_ord(list_like_to_sort, input_is_int = True, get_index_only = False):
    if input_is_int:
        converted = list_like_to_sort
    else:
        converted = string_to_list_ord(list_like_to_sort)
    output = radix_sort_single_digit(converted, get_index_only = get_index_only)
    if get_index_only :
        return output
    else:
        if input_is_int:
            return output
            pass
        else:
            ch_output = list_ord_to_string(output)
            return ch_output
def radix_sort_single_digit(converted, get_index_only = False, char_size = char_size, **kwarg):
    
    char_cnt = [0] * (char_size +1 )
    char_starting_lookup = [0] * (char_size +1 )
    new_index = [0] * len(converted)
    for i, ord_ch in enumerate(converted):
        char_cnt[ord_ch+1] += 1
        pass
    import numpy as np
    for i in range(1, len(char_starting_lookup)):
        char_starting_lookup[i] = char_starting_lookup[i-1] +  char_cnt[i]
    
    
    for i, ord_ch in enumerate(converted):
        char_starting = char_starting_lookup[ord_ch]
        char_starting_lookup[ord_ch] = char_starting_lookup[ord_ch] + 1
        new_index[i] = char_starting
    if get_index_only:
        return new_index
    output = np.array(converted)
    for i, idx in enumerate(new_index):
        output[idx] = converted[i]
        pass
    
    return output
ind = radix_sort_chr_ord(in_str, input_is_int = False)
def get_char_at(single_str, i):
    if i >= len(single_str):
        return chr(0)
    else:
        return single_str[i]
    
    pass
def radix_sort_least_significant_digit(list_of_str, num_of_digit_to_sort, input_is_int=False, get_rank_only=False):
    if input_is_int:
        sort_func = radix_sort_single_digit
    else:
        sort_func = radix_sort_chr_ord
    import numpy as np
    sort_index_list_out = np.arange(len(list_of_str))
    index_after_sorting = np.arange(len(list_of_str))
    for i in reversed(range(num_of_digit_to_sort)):
        list_to_sort = [ get_char_at(mystr, i)  for mystr in list_of_str]
        sort_index_list = sort_func(list_to_sort, input_is_int=input_is_int, get_index_only=True)
        rank = sort_index_list
        
        if get_rank_only:
            sort_index_list2 = np.arange(len(list_of_str))
            sort_index_list_out2=  sort_index_list_out.copy()
            for i in range(len(sort_index_list)):
                sort_index_list_out2[sort_index_list[i]] = sort_index_list_out[i]
                pass
            sort_index_list = sort_index_list_out2
            
            # so, sorted array will be (matlab terms)  list_of_str[sort_index_list]
            # rank = 
        else:
            src = np.arange(len(sort_index_list))  [np.array(sort_index_list)]
            src[np.array(sort_index_list)] = np.arange(len(sort_index_list))
            list_of_str = [list_of_str[sort_i] for sort_i in src]
        index_after_sorting2 = index_after_sorting.copy()
        for original_index, move_to_index in enumerate(np.array(sort_index_list)):
            index_after_sorting[move_to_index] = index_after_sorting2[original_index]
        # for i in range()
        pass
    if get_rank_only:
        return rank
    else:
        return list_of_str, index_after_sorting
def get_rank_using_digit(digit_index, ls_str):
    ls_char = [get_char_at(single_str, digit_index) for single_str in ls_str]
    rank = radix_sort_least_significant_digit(ls_char, num_of_digit_to_sort = 1, input_is_int = False,
                                              get_rank_only = True)
    return rank

def suffixarray(instr):
    instr = 'suffixarray'
    ref_pos = 0
    covered_inclusive_index = 1
    ls_char = [i for i in instr]
    ls_str = [ls_char[i:] for i in range(len(ls_char))]
    last_rank = radix_sort_least_significant_digit(ls_str, num_of_digit_to_sort = 1,
                                                   input_is_int=False, get_rank_only=True )
    import numpy as np
    while covered_inclusive_index < len(instr): 
        cur_rank = get_rank_using_digit(digit_index=covered_inclusive_index, ls_str=ls_str)
        combined_rank = np.concatenate([np.array(last_rank).reshape([-1,1]), 
                                  np.array(cur_rank).reshape([-1,1])],
                                  axis=1)
        last_rank = radix_sort_least_significant_digit(list_of_str=combined_rank,
                                                       num_of_digit_to_sort = 2,
                                                       input_is_int = True,
                                                       get_rank_only= True
                                                       )
        covered_inclusive_index = covered_inclusive_index * 2 + 1
    pass
    output = [''] * len(last_rank)
    for i_original, i_new in enumerate(last_rank):
        output[i_new] = ls_str[i_original]
    print(np.array(np.arange(len(ls_str)))[np.array(last_rank)] )
# suffixarray('suffixarray')
ls_ints = [[1,2], [3,1], [2,3]]
radix_sort_least_significant_digit(ls_ints, num_of_digit_to_sort = 2, input_is_int=True)
test_string_list = ['banana', 'apple', 'april', 'abcde']
radix_sort_least_significant_digit(test_string_list, 3)


