import pprint

import toornament
import riot


def main():

    team = toornament.getTeamByTournamentIdAndName("1216503415138074624", "eSUKA Clownfiesta")

    print(team)

    matches = toornament.getMatchesByIdAndTeamId("1216503415138074624", team.teamId)

    #accId = riot.getAccountIdByName("Yakaryo")
    #matchList = riot.getMatchList(accId)

    pp = pprint.PrettyPrinter(indent=2)

    pp.pprint(matches)


if __name__ == "__main__":
    # execute only if run as a script
    main()

