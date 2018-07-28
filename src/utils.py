from decimal import Decimal


def checkPositive(var):
    try:
        tmp = float(var)
        if tmp >= 0:
            return Decimal(var)
    except ValueError:
        return False
    except TypeError:
        return False
    return False

def check_element(element):

    if element is None:
        return False
    if not len(element) == 5:
        return False
    var0 = checkPositive(element[0])
    var4 = checkPositive(element[4])
    if var0 is not False and var4 is not False:
        element[0] = var0
        element[4] = var4
        try:
            element[3] = element[3].replace('-', ' ')
        except AttributeError:
            return False
    else:
        return False
    return element

def add_element(element, dict):
    if check_element(element):
        element_dict = {}
        if element[3] in dict:
            element_dict = dict[element[3]]
            if element[0] not in element_dict:
                element_dict[element[0]] = True
            element_dict['cost'] = element_dict['cost'] + element[4]
        else:
            dict[element[3]] = element_dict
            element_dict[element[0]] = True
            element_dict['cost'] = element[4]
    else:
        print 'Element not valid %s' % element
        return False
    return True