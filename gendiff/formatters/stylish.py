def create_stylish(d_list, lvl=0):
    res = []
    res.append('{\n')
    ind = ' ' * 2
    ind = ind + ind * 2 * lvl
    d_list.sort(key=lambda x: x['name'])
    for node in d_list:
        op = ' '
        if node['status'] != 'nested' and \
           node['status'] != 'changed' and \
           node['status'] != 'not changed' and \
           node['status'] != 'added' and \
           node['status'] != 'deleted':
            raise ValueError('Invalid type!')
        elif node['status'] == 'nested':
            data = create_stylish(node['children'], lvl + 1)
        elif node['status'] == 'changed':
            data = сonvert_to_string(node['data before'], ind)
            res.append(f"{ind}- {node['name']}: {data}\n")
            data = сonvert_to_string(node['data after'], ind)
            op = '+'
        else:
            data = сonvert_to_string(node['data'], ind)
            match node['status']:
                case 'added':
                    op = '+'
                case 'deleted':
                    op = '-'
        res.append(f"{ind}{op} {node['name']}: {data}\n")
    res.append(ind[:-2] + '}')
    return ''.join(res)


def сonvert_to_string(data, ind):
    if type(data) is dict:
        ind = ind + '    '
        res = '{\n'
        for key in data.keys():
            value = сonvert_to_string(data[key], ind)
            res = res + ind + '  ' + key + ': ' + value + '\n'
        res = res + ind[:-2] + '}'
    elif data is False or data is True:
        res = str(data).lower()
    elif data is None:
        res = 'null'
    else:
        res = str(data)
    return res
