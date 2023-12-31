import xml.etree.ElementTree as ET
import os

def is_latin_char(character):
    return character.isalpha() and ord(character) < 128

def is_latin_numeral(character):
    return character.isdigit() and ord(character) < 128

dataclass = ['test']
dictionary = {
        'B': 'ب',
        'P': 'پ',
        'T': 'ت',
        'Y': 'ث',
        'Z': 'ز',
        'X': 'ش',
        'E': 'ع',
        'F': 'ف',
        'K': 'ک',
        'G': 'گ',
        'D': 'D',
        'S': 'S',
        'J': 'ج',
        'W': 'د',
        'C': 'س',
        'U': 'ص',
        'R': 'ط',
        'Q': 'ق',
        'L': 'ل',
        'M': 'م',
        'N': 'ن',
        'V': 'و',
        'H': 'ه',
        'I': 'ی',
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹',

}
Move = {
        'A': 'الف',
        '@': 'ویلچر',
    }
for i in dataclass:
    output_file_path = f'gt_{i}.txt'
    f = open(output_file_path, 'w')
    for file in os.listdir(f'{i}/'):
        # print(files)
        # for file in files:
        error_file = ''
        if file.endswith('.xml'):
            error_file = file
            # Parse the XML file
            tree = ET.parse(f'{i}/{file}')
            root = tree.getroot()
            # Access elements in the XML tree
            filename = root.find('filename').text
            print(f'Filename: {file}')
            name = ''
            new_name=''
            # Iterate through object elements
            for obj in root.findall('object'):
                name += obj.find('name').text
            # print(name)
            for key in Move:
                if name.find(Move[key]) != -1:
                    new_name=name.replace(Move[key], key)
                    name = ''
                    name = new_name
            new_name=''
            for index, v in enumerate(name):
                if is_latin_char(v)==False and is_latin_numeral(v) == False:
                    for key in dictionary:
                        if dictionary[key] == v:
                            new_name=name.replace(name[index], key)
                            name = ''
                            name = new_name
            # try:
            for g in name:
                if is_latin_char(g)==False and is_latin_numeral(g) == False and g != '@':
                    name = name.replace(g, "")
                # print(is_latin_char(g), is_latin_numeral(g))
            filejpg = file.split('.')
            filesave = filejpg[0] + ".jpg"
            f.write(f'{filesave}	{name}\n')