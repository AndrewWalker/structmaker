import sys
import argparse
from jinja2 import StrictUndefined, DictLoader, Environment
from .builder import *

output = '''#ifndef STRUCTMAKER_AUTOGEN_H
#define STRUCTMAKER_AUTOGEN_H

#include <cstdint>

{% for s in structs %}
struct {{ s.typename }}
{
{% for field, name in s.fields %}
    {{ field.typename }} {{ name }};
{% endfor %}
};

{% endfor %}
#endif'''


def main():
    fundamental_types = [
        'uint8_t',
        'uint16_t',
        'uint32_t',
        'int8_t',
        'int16_t',
        'int32_t',
        'float',
        'double'
    ]

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=int, default=10)
    args = parser.parse_args(sys.argv[1:])

    d = {}
    d['output'] = output
    
    loader = DictLoader(d)
    env = Environment(trim_blocks = True, lstrip_blocks = True,
                      undefined = StrictUndefined, 
                      loader=loader)
    model = SimpleStructureGenerator(fundamental_types)
    structs = model.random_structs('S', args.number)
    tpl = env.get_template('output')
    print tpl.render(structs=structs)
