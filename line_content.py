def LateralContent(content, width):
    spaces = " " * (width - len(content))
    return content + spaces     
def CentralContent(content, width):
    new_content = content
    if len(content) < width:
        n_s = (width - len(content)) // 2
        new_content = " " * n_s + new_content
    spaces = " " * (width - len(new_content))    
    return new_content + spaces