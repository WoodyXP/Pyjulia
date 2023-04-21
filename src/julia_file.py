from subprocess import check_output
from typing import Union, List


class JuliaFile(object):

    def __init__(self, path, function_names):
        self.path = path
        self.function_names = function_names

        for function_name in function_names:
            def func(self, args: Union[int, List[int], float, List[float]]):

                args_list = [str(num) for num in args]

                cmd = (["julia", self.path, func] + args_list)
                output_str = check_output(cmd)

                output = output_str.strip().decode("utf-8")

                return output

            setattr(JuliaFile, function_name, func)