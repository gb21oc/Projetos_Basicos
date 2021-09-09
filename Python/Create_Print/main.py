import os

newLine = False
params_keyword = False


def verify_keyword(text, **kwargs):
    global newLine, params_keyword
    params_keyword = False
    if kwargs.get("sep") is not None:
        params_keyword = True
        text = text.replace(" ", kwargs["sep"])
    if kwargs.get("end") is not None:
        if "\n" in kwargs.get("end"):
            text = text.strip() + kwargs.get("end")
            newLine = True
        else:
            text = text.strip() + kwargs.get("end")
        params_keyword = True
    if kwargs.get("file") is not None:
        os.system(f'echo {text} > {kwargs.get("file")}')
        return f"File is created: {kwargs.get('file')}"
    if len(kwargs.keys()) == 0:
        return
    elif not params_keyword:
        raise TypeError("Is an invalid keyword argument for print_f()")
    else:
        return text


def print_f(*args, **kwargs):
    return_itens = ""
    for help in args:
        if help == "-h":
            print_f("Unfortunately I wasn't able to perform all the functionality of print, but in fact it added to my "
                    "knowledge of how some functions work. If you use \n it will not return what you want sorry! :( "
                    "I accept tips, help, ideas, jobs, etc: "
                    "Gmail: gabrielsuporte2021@gmail.com Linkedin: https://www.linkedin.com/in/gabriel-jos%C3%A9/")
            return
    for value in args:
        if type(value) == int:
            return_itens += " " + str(value)
        else:
            return_itens += " " + value
    text_sep = verify_keyword(return_itens.strip(), **kwargs)
    if text_sep != "" and text_sep is not None:
        if newLine:
            os.system(f'echo {text_sep}')
        else:
            os.system(f'echo|set /p="{text_sep}"')
    else:
        os.system(f'echo {return_itens.strip()}')


print_f("Teste file", file="teste.txt")
