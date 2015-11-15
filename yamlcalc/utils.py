import yaml
from collections import OrderedDict
from datetime import date



# http://stackoverflow.com/questions/5121931/in-python-how-can-you-load-yaml-mappings-as-ordereddicts
def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)

# usage example:
# with open('tmp.yaml', 'r') as stream:
# 	d = ordered_load(stream, yaml.SafeLoader)

def ordered_dump(data, stream=None, Dumper=yaml.Dumper, **kwds):
    class OrderedDumper(Dumper):
        pass
    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            data.items())
    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)

# usage:
# with open(arguments['<outfile>'], 'w+') as outfile:
    # ordered_dump(d, Dumper=yaml.SafeDumper, stream=outfile,
    #   default_flow_style=False, allow_unicode=True)



# http://stackoverflow.com/questions/2217488/age-from-birthdate-in-python
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < 
        (born.month, born.day))