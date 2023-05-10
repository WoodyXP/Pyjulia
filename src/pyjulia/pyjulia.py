from subprocess import check_output

class Pyjulia:
    """
    Used to call Julia functions from python
    """
    def __init__(self, path: str, julia_interpreter: str = "julia"):
        self.path = path
        self.julia_interpreter = julia_interpreter
        self.functions = []
        self.get_funcs()
        self.declare_funcs()

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

    def call_func(self, func: str, args: list):
        """
        Used to call julia functions from python
        """
        args_list = [str(num) for num in args]

        cmd = ([self.julia_interpreter, self.path, func] + args_list)
        output_str = check_output(cmd)

        output = output_str.strip().decode("utf-8")
        return output

    def declare_funcs(self):
        """
        automatically declares functions according to self.functions
        """
        for function_name in self.functions:
            def func(self, args: list, fname=function_name):
                args_list = [str(num) for num in args]

                cmd = ([self.julia_interpreter, self.path, fname] + args_list)
                output_str = check_output(cmd)

                output = output_str.strip().decode("utf-8")
                return output

            setattr(Pyjulia, function_name.replace('-', '_'), func)

if __name__ == '__main__':
    print('This is a module! Please import using:\nimport Pyjulia')