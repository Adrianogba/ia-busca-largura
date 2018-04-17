import heapq

class State(object):

    def __init__(self, name,estimate):
        self.name = name
        self.estimate = estimate

    def add_actions(self, actions):
        self.actions = actions

    def __repr__(self):
        return self.name


class NodeSearch(object):

    def __init__(self, state, cost):
        self.state = state
        self.cost = cost

    def set_parent(self, parent):
        self.parent = parent

    def __repr__(self):
        return self.state.name


class Search(object):

    def __init__(self, start, goal):
        self.start = NodeSearch(start, 0)
        self.start.parent = None
        self.goal = goal

    def search(self):
        frontier = PriorityQueue()
        frontier.push(self.start, self.start.state.estimate + 0 )
        explored = set()
        passo = 1
    
        while True:

            if len(frontier) == 0:
                return False
            
            ft = self.view_frontier(frontier)
           
            new_state_info = self.choose_state(frontier)
            new_state = new_state_info[1]
            new_state_cost = new_state_info[0] - new_state.state.estimate
           
            print  ("Passo " +str(passo)+".")
            print  ("Fronteira: "+ ft)
            print  ("Explorado: "+str(new_state.state))
            print  (" ")

            explored.add(new_state.state)

            if new_state.state == self.goal:
                return new_state
            
            
            for state_info in new_state.state.actions:
                state = state_info[0]
                state_cost = state_info[1] + state_info[0].estimate
                
                if state not in explored:
                    aux_state = NodeSearch(state, state_cost + new_state_cost)
                    self.set_frontier(frontier, aux_state)
                    aux_state.set_parent(new_state)

            passo+=1
            
    def view_frontier(self,frontier):
        fronteiras = ""
        for state in frontier:
            if state==frontier[len(frontier)-1]:
                fronteiras = fronteiras + str(state[1])+": "+ str(state[0]) 
            else:
                fronteiras = fronteiras + str(state[1])+": "+ str(state[0]) +", "
        fronteiras = fronteiras[:len(fronteiras)-1]
        return fronteiras
    def set_frontier(self, frontier, node_search):
        for node_info in frontier:
            node_cost = node_info[0]
            node = node_info[1]

            if node.state.name == node_search.state.name:
                if node_search.cost < node_cost:
                    frontier.remove(node_info)
                    frontier.push(node_search, node_search.cost)
                    return frontier
                else:
                    return frontier

        frontier.push(node_search, node_search.cost)

    def choose_state(self, frontier):
        'print frontier'
        return frontier.pop()


class PriorityQueue(list):
    def push(self, element, priority):
        heapq.heappush(self, (priority, element))

    def pop(self):
        return heapq.heappop(self)


def print_path(state):
    state_parent = state.parent
    print (state)

    while state_parent:
        print (state_parent)
        state_parent = state_parent.parent

joao_pessoa = State("Joao pessoa",460)
itabaiana = State("Itabaiana",360)
campina_grande = State("Campina grande",300)
santa_rita = State("Santa rita",451)
mamanguape = State("Mamanguape",380)
guarabira = State("Guarabira",340)
areia = State("Areia",316)
coxixola = State("Coxixola",232)
soledade = State("Soledade",243)
picui = State("Picui",250)
monteiro = State("Monteiro",195)
patos = State("Patos",122)
pombal = State("Pombal",55)
itaporanga = State("Itaporanga",65)
catole_do_rocha = State("Catole do rocha",110)
sousa = State("Sousa",20)
cajazeiras = State("Cajazeiras",0)

joao_pessoa.add_actions([(itabaiana, 68), (campina_grande, 125), (santa_rita, 26)])
itabaiana.add_actions([(joao_pessoa, 68), (campina_grande, 65)])
santa_rita.add_actions([(joao_pessoa, 26), (mamanguape, 64)])
mamanguape.add_actions([(santa_rita, 64), (guarabira, 42)])
guarabira.add_actions([(mamanguape, 42), (areia, 41)])
areia.add_actions([(guarabira, 41), (campina_grande, 40)])
campina_grande.add_actions([(itabaiana, 65), (areia, 40), (soledade, 58), (coxixola, 128), (joao_pessoa, 125)])
soledade.add_actions([(campina_grande, 58), (patos, 117), (picui, 69)])
picui.add_actions([(soledade, 68)])
coxixola.add_actions([(campina_grande, 128), (monteiro, 83)])
patos.add_actions([(soledade, 117), (itaporanga, 108), (pombal, 71)])
monteiro.add_actions([(coxixola, 83), (itaporanga, 224)])
catole_do_rocha.add_actions([(pombal, 57)])
pombal.add_actions([(patos, 71), (catole_do_rocha, 57), (sousa, 56)])
itaporanga.add_actions([(patos, 108), (cajazeiras, 121), (monteiro, 224)])
sousa.add_actions([(pombal, 56), (cajazeiras, 43)])
cajazeiras.add_actions([(sousa, 43), (itaporanga, 121)])

search = Search(joao_pessoa, cajazeiras)
final_state = search.search()


print_path(final_state)
