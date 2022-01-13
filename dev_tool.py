import re
import time

DAT_FILE = 'fh5.dat'
dat_file_content = ''
fmt_table = {'s32': 'i', 'u32': 'I', 'f32': 'f',
             'u16': 'H', 'u8': 'B', 's8': 'b'}
py_type_table = {
    's32': 'c_int32', 'u32': 'c_uint32', 'f32': 'c_float', 'u16': 'c_uint16',
    'u8': 'c_uint8', 's8': 'c_int8'
}


def read_dat_file():
    global dat_file_content
    if not dat_file_content:
        with open(DAT_FILE, 'r', encoding='utf-8') as f:
            dat_file_content = f.read()
    return dat_file_content


def read_dat_fields_types():
    data = read_dat_file()
    types = re.findall('([ufs]\d+)', data, flags=re.M)
    return types


def read_dat_fields_names():
    data = read_dat_file()
    names = re.findall('[ufs]\d+\s(\w+);', data, flags=re.M)
    return names


def generate_struct_fmt():
    fmt = '<'
    for t in read_dat_fields_types():
        fmt += fmt_table[t]
    return fmt


def refresh_FH5_py():
    names = read_dat_fields_names()
    types = read_dat_fields_types()
    lines = []
    for name, dtype in zip(names, types):
        lines.append("\t\t('{name}', {py_type})".format(
            name=name, py_type=py_type_table[dtype]))
    content_to_fill = ',\n'.join(lines)
    with open('template/FH5.template.py', 'r') as f:
        template = f.read()
    content = template.format(struct_fmt=generate_struct_fmt(),
                              fields=content_to_fill,
                              creator=__name__,
                              date = time.strftime('%Y-%m-%d %H:%M:%S'))
    with open('utils/FH5api.py', 'w') as f:
        f.write(content)


if __name__ == '__main__':
    refresh_FH5_py()
