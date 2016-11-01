import re

def change_numbers():
    o_file = open('test1.txt', 'r')
    regex_pattern = re.compile('\d\d\d') # change the pattern
    list_elements = []
    number = 100
    for line in o_file:
        number = int(regex_pattern.search(line).group())
        m = re.sub(regex_pattern, str(number),str(line))
        number+= 1
        list_elements.append(m)
    o_file.close()

    m_file = open('test1.txt', 'w')
    for element in list_elements:
        m_file.write(element)

    m_file.close()

def change_folder():
    o_file = open('test1.txt', 'r')
    regex_pattern = re.compile('x') # change the pattern
    list_elements = []
    for line in o_file:
        # number = int(regex_pattern.search(line).group())
        # first argument the pattern, the second the new value, third the line or string 
        m = re.sub(regex_pattern, '500', str(line))
        list_elements.append(m)
    o_file.close()

    m_file = open('test1.txt', 'w')
    for element in list_elements:
        m_file.write(element)

    m_file.close()

