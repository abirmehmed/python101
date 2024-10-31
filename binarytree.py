import matplotlib.pyplot as plt
import networkx as nx

def draw_binary_tree():
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges to represent the binary tree
    edges = [
        ('Ro', 'L'),
        ('Ro', 'R'),
    ]
    G.add_edges_from(edges)

    # Define node colors
    color_map = {
        'Ro': '#FF9999',  # Color for A
        'L': '#99CCFF',  # Color for B
        'R': '#99CCFF',  # Color for C
    }
    
    node_colors = [color_map[node] for node in G.nodes()]

    # Define positions for a binary tree layout
    pos = {
        'Ro': (0, 2),   # Top node (A)
        'L': (-1, 1),  # Left child (B)
        'R': (1, 1),   # Right child (C)
    }

    # Draw the nodes with rounded edges
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=node_colors, edgecolors='black', linewidths=1)
    
    # Draw the edges
    nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif')

    # Set aspect ratio to be equal and turn off the axis
    plt.axis('off')
    
    # Show the plot
    plt.show()

# Call the function to draw the binary tree
draw_binary_tree()
