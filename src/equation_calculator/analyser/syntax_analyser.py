def syntax_analyser(token_list: list) -> tuple[bool, int] | bool:
    number_paren_open: int = 0
    is_previous_token_operator: bool = False

    for index, token in enumerate(token_list):
        if token == "LPAREN":
            is_previous_token_operator = False
            number_paren_open += 1
            continue
        if token == "RPAREN":
            is_previous_token_operator = False
            number_paren_open -= 1
            if number_paren_open < 0:
                return (False, index)
            continue
        if token == "INTEGER":
            is_previous_token_operator = False
            continue
        if token in ["ADDITION", "SUBTRACT", "MULTIPLY", "DIVISION", "POWER"]:
            if index == 0:
                return (False, index)
            if is_previous_token_operator == True:
                return (False, index)
            is_previous_token_operator = True

    if number_paren_open == 0:
        return (True, -1)
    else:
        return (False, 0)
