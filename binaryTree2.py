import matplotlib.pyplot as plt
import networkx as nx

def draw_binary_tree():
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges to represent the binary tree
    edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('C', 'E'),
        ('C', 'F')
    ]
    G.add_edges_from(edges)

    # Define node colors
    color_map = {
        'A': '#FF9999',  # Color for A
        'B': '#99CCFF',  # Color for B
        'C': '#99CCFF',  # Color for C
        'E': '#66FF66',  # Color for E
        'F': '#66FF66'   # Color for F
    }
    
    node_colors = [color_map[node] for node in G.nodes()]

    # Define positions for a binary tree layout
    pos = {
        'A': (0, 2),   # Top node (A)
        'B': (-1, 1),  # Left child (B)
        'C': (1, 1),   # Right child (C)
        'E': (0.5, 0), # Left child of C (E)
        'F': (1.5, 0)  # Right child of C (F)
    }

    # Draw the nodes with rounded edges
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=node_colors, edgecolors='black', linewidths=1)
    
    # Draw the edges
    nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif')

    # Set aspect ratio to be equal and turn off the axis
    plt.axis('off')
    plt.title("Binary Tree Structure", fontsize=20)
    
    # Show the plot
    plt.show()

# Call the function to draw the binary tree
draw_binary_tree()
