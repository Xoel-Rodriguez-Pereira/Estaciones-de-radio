def greedy_search_global ():

    stations = {}

    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])
    stations["ksix"] = set(["nm", "tx", "ok"])
    stations["kseven"] = set(["ok", "ks", "co"])
    stations["keight"] = set(["ks", "co", "ne"])
    stations["knine"] = set(["ne", "sd", "wy"])
    stations["kten"] = set(["nd", "ia"])
    stations["keleven"] = set(["mn", "mo", "ar"])
    stations["ktwelve"] = set(["la"])
    stations["kthirteen"] = set(["mo", "ar"])


    stations_remaning = stations.copy()
    covered_states = set()
    stations_needed = []

    gradients = []
    num_states_covered = []

    while covered_states < needed_states:
        best_station, best_gradient = find_best_station(stations_remaining, covered_states)

        if best_station:
            gradients.append(best_gradient)
            covered_states |= stations_remaining[best_station]
            num_states_covered.append(len(covered_states))
            stations_needed.append(best_station)
            del stations_remaining[best_station]

    return (stations_needed, num_states_covered, gradients, covered_states)

