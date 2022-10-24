for i in range(2, 101):
    def primo(i):
        for a in range(2, i - 1):
            if i == 2:
                return True

            if i > 2:
                if i % a == 0:
                    return False

                elif i % a != 0:
                    return True

    if primo(i) == True:
        print(i)