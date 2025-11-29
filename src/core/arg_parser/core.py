import argparse
from .model import Args, Mode, Override


def parse_key_value(x):
    key, value = x.split("=")
    return key, value


def no_parse(x):
    return x


def parse_args() -> Args:
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", action="append", type=parse_key_value)
    parser.add_argument("-m", required=True, type=no_parse)
    
    args = parser.parse_args()
    mode: Mode = Mode(args.m)

    if args.o is not None:
        overrides = [Override(keyword=i[0], value=i[1]) for i in args.o]
    else:
        overrides = []
        
    return Args(mode=mode, overrides=overrides)


args:Args = parse_args()        
