import json, webbrowser, time, sys

data = 0


def load_data():
    global data
    with open("sites.json") as f:
        data = json.load(f)


def get_avalible_sites():
    sites = []
    for site in data:
        sites.append(site["site"])
    return sites


def show_avalible_sites():
    sites = get_avalible_sites()
    for index, site in enumerate(sites):
        print("Type %s to search in %s" % (index + 1, site))


def make_decision():
    try:
        decision = int(raw_input("Chose: "))
        if decision < 1 or decision > len(data):
            return make_decision()
        else:
            return decision
    except ValueError:
        print("Not a number")
        return make_decision()

def data_has(data, key):
    try:
      data[str(key)]
      return True
    except KeyError, TypeError:
      return False

def main():
    global data
    load_data()
    if len(sys.argv) > 1:
        decision = int(sys.argv[1])
    else:
        show_avalible_sites()
        decision = make_decision()
        data_decision = data[decision - 1]
    for query in data_decision["queries"]:
        if data_has(data_decision, "url"):
            webbrowser.open(data_decision["url"] + query, new = 2)
        else:    
            webbrowser.open(data_decision["url_start"] + query + data_decision["url_end"], new = 2)
            time.sleep(0.6)
    exit(0)


main()

