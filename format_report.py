

class HeuristicEntry():
    def __init__(self, name, time, expanded, frontier):
        self.name = name
        self.time = float(time)
        self.expanded = int(expanded)
        self.frontier = int(frontier)

class Entry():
    def __init__(self, initial, heuristic_entrys):
        self.initial = initial
        self.heuristic_entrys = heuristic_entrys
        pass



def read_file(filepath):
    file = open(filepath, 'r')
    data = file.read()
    file.close()
    return data

def write_file(filepath, data):
    file = open(filepath, 'w')
    file.write(data)
    file.close()

def extract_data(data):
    data = data.split('\n\n')
    data.pop()
    formatted = [entry.split('\n') for entry in data]

    entrys = []
    for strings in formatted:
        heuristic_entrys = [
            # add name ot heuristic entrys
            HeuristicEntry(
                strings[1].split(' ')[0],
                strings[1].split(' ')[2],
                strings[2].split(' ')[0].strip("'["),
                strings[2].split(' ')[6]
            ),
            HeuristicEntry(
                strings[3].split(' ')[0],
                strings[3].split(' ')[2],
                strings[4].split(' ')[0].strip("'["),
                strings[4].split(' ')[6]
            ),
            HeuristicEntry(
                strings[5].split(' ')[0],
                strings[5].split(' ')[2],
                strings[6].split(' ')[0].strip("'["),
                strings[6].split(' ')[6]
            ),
        ]
        initial = strings[0].strip('(').strip(')').split(',')
        initial = tuple([int(num.strip()) for num in initial])
        entrys.append(Entry(initial, heuristic_entrys))
    return entrys

def format_data(entrys, val='time'):
    heuristics = [h.name for h in entrys[0].heuristic_entrys]

    formatted_data = 'initial,'
    for h in heuristics:
        formatted_data += h + ','
    formatted_data = formatted_data.strip(',') + '\n'

    for entry in entrys: 
        formatted_data += str(entry.initial).replace(',', '') + ','
        for h in entry.heuristic_entrys:
            if val == 'time': target = h.time
            elif val == 'expandedpaths': target = h.expanded
            formatted_data += str(target) + ','
        formatted_data = formatted_data.strip(',') + '\n'

    return formatted_data

def format_reports():
    raw = read_file('report_1648526706.9344606.txt')
    entrys = extract_data(raw)
    time_data = format_data(entrys, val='time')
    expandedpaths_data = format_data(entrys, val='expandedpaths')
    write_file('heuristic_time_data.csv', time_data)
    write_file('heuristic_expandedpaths_data.csv', expandedpaths_data)

def main():
    format_reports()



main()