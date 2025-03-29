# for i in range(1,21):
#     print("1*i"+"=", 1*i)


def mul():
    # Loop through numbers from 1 to 20
    for i in range(1, 21):
        print(f"Multiplication Table for {i}:")
        # For each number, multiply it by values 1 to 10
        for x in range(1, 11):
            print(f"{i} * {x} = {i * x}")
        print("-" * 20)  # Line separator for each table

mul()
