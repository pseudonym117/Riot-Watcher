from functools import wraps


def remap_region_to_platform(argument_pos: int, argument_name="region"):
    def _remap_region_to_platform(api_call):
        remap = {
            "br1": "americas",
            "la1": "americas",
            "la2": "americas",
            "na1": "americas",
            "oc1": "sea",
            "ph2": "sea",
            "sg2": "sea",
            "th2": "sea",
            "tw2": "sea",
            "vn2": "sea",
            "eun1": "europe",
            "euw1": "europe",
            "ru": "europe",
            "tr1": "europe",
            "jp1": "asia",
            "kr": "asia",
        }

        @wraps(api_call)
        def remapper(*args, **kwargs):
            nargs = args
            if argument_name in kwargs:
                lower_region = kwargs[argument_name].lower()
                if lower_region in remap:
                    kwargs[argument_name] = remap[lower_region]
            if len(args) > argument_pos and isinstance(args[argument_pos], str):
                region = args[1].lower()
                if region in remap:
                    nargs = list(args)
                    nargs[1] = remap[region]
            return api_call(*nargs, **kwargs)

        return remapper

    return _remap_region_to_platform
