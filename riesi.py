riesi_ = "riesi"
not_riesi_ = "not " + riesi_ + "!!"


def riesi(riesi):
    if riesi_ in riesi:
        return riesi_
    else:
        return not_riesi_

if __name__ == "__main__":
    frog_input = input("> ").lower()
    print(riesi(frog_input))
