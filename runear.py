
def return_eval(code):
    try:
        return f"{eval(code)}"
    except Exception as e:
        return e