# -*- coding: utf-8 -*-
import re
for test_string in ['954-888-888', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{3}-\d{3}$', test_string):
        print test_string, 'es un numero de telefono valido'
    else:
        print test_string, 'rechazado'