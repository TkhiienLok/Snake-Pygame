from domain.interfaces import Result


def save_result(result: Result):
    try:
        f = open("results.txt", "r")
        n = f.read().count(result.player_name) + 1  # TODO: increment if the same name already exists
        f.close()
    except FileNotFoundError:
        f = open("results.txt", "w")
        f.close()
        n = 0

    f = open("results.txt", "a")
    f.write("{} : Apples - {} Points - {} \n".format(result.player_name + str(n), result.apples, result.points))
    f.close()
