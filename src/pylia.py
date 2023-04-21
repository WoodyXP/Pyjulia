from subprocess import check_output
from typing import List, Union

class Julia:
    """
    Used to call Julia functions from python
    """
    def __init__(self, path: str):
        self.path = path
        self.functions = []
        self.get_funcs()
        # self.declare_funcs()

    def get_funcs(self):
        """
        parses all functions from julia file into functions array
        """
        with open(f"{self.path}", "r", encoding="utf-8") as file:
            for line in file.readlines():
                if line.startswith("@main"):
                    linearr = line.split("(")
                    self.functions.append((linearr[0]).replace("@main function ", ""))

        return self.functions

    def call_func(self,
                        func: str,
                        args: Union[int, List[int], float, List[float]]):
        """
        Used to call julia functions from python
        """
        args_list = [str(num) for num in args]

        cmd = (["julia", self.path, func] + args_list)
        output_str = check_output(cmd)

        output = output_str.strip().decode("utf-8")
        return output

    # def declare_funcs(self):
    #     for function_name in self.functions:
    #         def func(self, args: Union[int, List[int], float, List[float]]):
    #             args_list = [str(num) for num in args]

    #             cmd = (["julia", self.path, function_name] + args_list)
    #             output_str = check_output(cmd)

    #             output = output_str.strip().decode("utf-8")
    #             return output

    #         print(func)
    #     setattr(Julia, function_name, func)
