# network_mapper.py

import networkx as nx
import matplotlib.pyplot as plt
from enum import Enum, auto


class Action(Enum):
    ADD_NODE = auto()
    CONNECT_NODES = auto()
    DISPLAY_TEXT = auto()
    VISUALIZE = auto()
    EXIT = auto()


class NetworkNode:
    def __init__(self, name):
        self.name = name
        self.connections = set()

    def connect(self, other):
        self.connections.add(other)
        other.connections.add(self)


class NetworkTopologyMapper:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        self.nodes.setdefault(name, NetworkNode(name))

    def connect_nodes(self, name1, name2):
        self.add_node(name1)
        self.add_node(name2)
        self.nodes[name1].connect(self.nodes[name2])

    def display_network_text(self):
        print("\n[ Network Structure ]")
        for node in self.nodes.values():
            conns = ', '.join(sorted(n.name for n in node.connections))
            print(f"{node.name} -> {conns}")

    def visualize_network(self):
        G = nx.Graph()
        for node in self.nodes.values():
            for conn in node.connections:
                G.add_edge(node.name, conn.name)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue',
                font_weight='bold', node_size=1500)
        plt.title("Network Topology Visualization")
        plt.show()

    def run_menu(self):
        def add_node_action():
            name = input("Enter node name to add: ")
            self.add_node(name)

        def connect_nodes_action():
            n1 = input("Enter first node name: ")
            n2 = input("Enter second node name: ")
            self.connect_nodes(n1, n2)

        def display_action():
            self.display_network_text()

        def visualize_action():
            self.visualize_network()

        actions = {
            Action.ADD_NODE: add_node_action,
            Action.CONNECT_NODES: connect_nodes_action,
            Action.DISPLAY_TEXT: display_action,
            Action.VISUALIZE: visualize_action,
        }

        menu = {
            "1": Action.ADD_NODE,
            "2": Action.CONNECT_NODES,
            "3": Action.DISPLAY_TEXT,
            "4": Action.VISUALIZE,
            "5": Action.EXIT,
        }

        while True:
            print("\n[ Network Mapper Menu ]")
            print("1. Add Node")
            print("2. Connect Nodes")
            print("3. Display Network (Text)")
            print("4. Visualize Network")
            print("5. Exit")

            choice = input("Choose an option: ").strip()
            action = menu.get(choice)

            if action == Action.EXIT:
                break
            elif action in actions:
                actions[action]()
            else:
                print("Invalid choice. Please try again.")


# Run interactively if executed directly or explicitly invoked
if __name__ == "__main__":
    try:
        ntm = NetworkTopologyMapper()
        ntm.run_menu()
    except EOFError:
        print("Interactive mode is not supported in this environment.")