import yaml


class Utils:
    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            yaml_data = yaml.safe_load(f)
            params = yaml_data['params']
            keys = set()
            values = []
            if isinstance(params, list):
                # keys = [row.keys() for row in params]

                for row in params:
                    if isinstance(row, dict):
                        keys += row.keys()
                        values.append(list(row.values())[0])
            var_names = ','.join(keys)
            return {'keys': var_names, 'values': values}
