riesi_ = "riesi"
not_riesi_ = "not " + riesi_ + "!!"


def riesi(riesi):
    if riesi_ in riesi:
        return CBLUE + riesi_ + CEND
    else:
        return CRED + not_riesi_ + CEND

if __name__ == "__main__":
    print(CGREEN, frog, CEND)
    frog_input = input("> ").lower()
    print(riesi(frog_input))
