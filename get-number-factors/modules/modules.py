import math # The use of this module is temporal

# Uncomment the 'print' statements to see textually in the console how the code works.


def get_factors(num):
    '''This function returns a list of the factors of the number passed'''

    max_factor = math.floor(num / 2)
    range_numbers = list(range(1, max_factor+1))
    factor_list = [1,num]

    i = 0
    while i < len(range_numbers):
        j = 0
        # print('Outer loop iteration: {}'.format(i))
        while j < len(range_numbers):
            # print('\tInner loop iteration: {}'.format(j))
            if range_numbers[j] * range_numbers[i] == num:
                # print('\t\tPass conditional: {} X {} = {}'.format(range_numbers[j], range_numbers[i], range_numbers[j] * range_numbers[i]))
                if range_numbers[j] not in factor_list:
                    factor_list.append(range_numbers[j])
                    # print('\t\t\tAdding '{}' to list'.format(range_numbers[j]))
                if range_numbers[i] not in factor_list:
                    factor_list.append(range_numbers[i])
                    # print('\t\t\tAdding '{}' to list'.format(range_numbers[i]))
                # print('\t\tFactor list status: {}'.format(factor_list))
            j += 1
        i += 1

    return sorted(factor_list)

