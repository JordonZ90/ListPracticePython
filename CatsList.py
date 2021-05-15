cats = []

while True:
    name = input(f"Enter the name of the cat {str(len(cats) + 1)} or nothing to stop ")
    if name == '':
        break
    cats += [name]
    print("The cat names are:")
    for name in cats:
        print(f"{name}")
    # for i in range(len(cats)):
    #     print(f"Index {i} in cats is {cats[i]}")
    for index, item in enumerate(cats):
        print(f"Index {index} in cats is {item}")


# supplies = ['pens', 'bags', 'binders']
# for index, item in enumerate(supplies):
#     print(f"Index {index} in supplies is {item}")