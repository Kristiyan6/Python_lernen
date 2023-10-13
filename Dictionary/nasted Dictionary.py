#travel_log = {
#    "frankreich": ["paris, straßburg"],
#    "amerika": ["new york", "las vegas"],
#    "spanien": ["barcelona", "madrid"]
#}

travel_log = {
    "frankreich": {
        "besuchte_staedte": ["paris", "straßburg"],
        "anzahl_besuche": 12
    },
    "amerika": {
        "besuchte_staedte": ["new york", "las vegas"],
        "anzahl_besuche": 5
    },
    "spanien": {
        "besuchte_staedte": ["barcelona", "madrid"],
        "anzahl_besuche": 20
    }
}
for key in travel_log:
    for key2 in travel_log[key]["besuchte_staedte"]:
        print(f"Stadt: {key2}")
