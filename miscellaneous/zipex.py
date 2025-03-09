def update(keys, values):
    # provides new signature for update()
    # but does not break __init__()
    items_list = []
    for item in zip(keys, values):
        items_list.append(item)
        print(item)


update([12, 45, 78], [78, 85, 96])
