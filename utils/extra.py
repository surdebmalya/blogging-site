def shorten_text(data):
    for each in data:
        if len(each['body']) > 200:
            each['body'] = each['body'][:200] + "..."
    return data