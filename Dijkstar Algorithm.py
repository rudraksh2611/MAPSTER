import cv2
from pyzbar.pyzbar import decode
import heapq
import time

# Function to scan QR code using the camera
def scan_qr_code():
    cap = cv2.VideoCapture(0)
    
    current_location = None
    while True:
        _, frame = cap.read()
        decoded_objects = decode(frame)
        
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            print(f"QR Code detected: {qr_data}")
            current_location = qr_data
            break
        
        cv2.imshow("QR Code Scanner", frame)
        
        if current_location is not None:
            break
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    return current_location

# Function to get the user's destination input
def get_target_location(floor_graph):
    print("Available destinations: ")
    for location in floor_graph:
        print(location)
    target_location = input("Please enter your destination: ")
    return target_location

# Dijkstra's algorithm with performance tracking
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # Initialize distances to infinity
    distances[start] = 0  # Distance to the start node is 0
    priority_queue = [(0, start)]  # Priority queue to store nodes and distances
    previous_nodes = {node: None for node in graph}  # To store the shortest path
    directions = {node: [] for node in graph}  # To store directions (left, right, etc.)
    nodes_expanded = 0  # To track number of nodes expanded

    start_time = time.time()  # Start timing

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        nodes_expanded += 1  # Increment nodes expanded

        if current_distance > distances[current_node]:
            continue

        for neighbor, (weight, direction) in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node  # Track the path
                directions[neighbor] = directions[current_node] + [(neighbor, direction, weight)]
                heapq.heappush(priority_queue, (distance, neighbor))

    end_time = time.time()  # End timing
    dijkstra_time = end_time - start_time  # Total time taken

    # Results
    return {
        "distances": distances,
        "previous_nodes": previous_nodes,
        "directions": directions,
        "performance": {
            "time": dijkstra_time,
            "nodes_expanded": nodes_expanded
        }
    }

# Function to reconstruct the shortest path with directions and distances in meters
def reconstruct_path_with_directions(directions, start, target):
    if target not in directions:
        return None

    path_directions = directions[target]
    steps = []
    total_distance = 0
    for i, (location, direction, distance) in enumerate(path_directions):
        total_distance += distance
        step = f"Step {i+1}: Go {direction} to {location} (Distance: {distance} meters)"
        steps.append(step)

    steps.append(f"Total distance to {target}: {total_distance} meters")
    return steps

# Function to map the QR code location to the graph's node name
def map_location(qr_location):
    location_mapping = {
        'IPDC Lab': '306 IPDC Lab',
        'Control/Comm Lab': '307B Control/Comm Lab',
        'Classroom 307A': '307A Classroom',
        'Classroom 308A': '308A Classroom',
        'Classroom 309A': '309A Classroom',
        'Analog Circuit Lab': '309B Analog Circuit Lab',
        'Classroom 310': '310 Classroom',
        'Faculty Room 311': '311 Faculty Room',
        'Classroom 312A': '312A Classroom',
        'Classroom 313A': '313A Classroom',
        'Classroom 313B': '313B Classroom',
        'Food Science Lab': '314A Food Science Lab',
        'Cyber Security Lab': '315 Cyber Security Lab',
        'CAD Simulation Lab': '316 CAD Simulation Lab',
        'Male Washroom': 'WR016 Male Washroom',
        'Female Washroom': 'WR013 Female Washroom',
        'Faculty Room 317': '317 Faculty Room',
        'Dept of CS & App': '301 Dept of CS & App',
        'Board Room': '302 Board Room',
        'HOD Room': '303 CS HOD Room',
        'Molecular Biology Lab': '304/305 Molecular Biology',
        'Library': 'Library',
        'CSE Office': '302D CSE Office',
        # Add other QR location mappings as needed
    }
    return location_mapping.get(qr_location, qr_location)  # Returns mapped location or the same location if not found

# Main function
def main():
    # Step 1: Use the camera to scan the QR code and get the current location
    print("Scanning for QR code... Please hold your QR code up to the camera.")
    current_location = scan_qr_code()

    if current_location:
        print(f"Current location from QR code: {current_location}")
    else:
        print("No QR code detected.")
        return

    # Step 2: Map the QR code location to the graph node name
    current_location = map_location(current_location)
    print(f"Mapped current location: {current_location}")

    # Step 3: Define the node graph (pre-defined for the building)
    floor_graph = {
        '306 IPDC Lab': [('307A Classroom', (1.5, 'LEFT then take RIGHT')), ('Elevator', (1, 'RIGHT'))],
        '307A Classroom': [('306 IPDC Lab', (1.5, 'LEFT then again take LEFT ')), ('307B Control Lab', (2, 'STRAIGHT'))],
        '307B Control Lab': [('307A Classroom', (2, 'STRAIGHT')), ('308A Classroom', (0.5, 'STRAIGHT'))],
        '308A Classroom': [('307B Control Lab', (0.5, 'STRAIGHT')), ('309A Classroom', (2, 'STRAIGHT'))],
        '309A Classroom': [('308A Classroom', (2, 'STRAIGHT')), ('309B Analog Lab', (2.5, 'RIGHT then take LEFT')), ('Washroom', (4.5, 'STRAIGHT'))],
        '309B Analog Lab': [('309A Classroom', (2.5, 'RIGHT then again take RIGHT')), ('310 Classroom', (2.5, 'STRAIGHT'))],
        'Washroom': [('309A Classroom', (4.5, 'STRAIGHT')), ('313B Classroom', (1.5, 'RIGHT')), ('314A Food Science Lab', (4, 'STRAIGHT towards balcony then take RIGHT'))],
        '310 Classroom': [('309B Analog Lab', (2.5, 'STRAIGHT')), ('311 Faculty Room', (1.5, 'RIGHT'))],
        '311 Faculty Room': [('310 Classroom', (1.5, 'LEFT')), ('312A Classroom', (2.5, 'STRAIGHT'))],
        '312A Classroom': [('311 Faculty Room', (2.5, 'STRAIGHT')), ('313A Classroom', (1.5, 'RIGHT'))],
        '313A Classroom': [('312A Classroom', (1.5, 'LEFT')), ('313B Classroom', (2.5, 'STRAIGHT'))],
        '313B Classroom': [('313A Classroom', (2.5, 'STRAIGHT')), ('Washroom', (1.5, 'LEFT'))],
        '314A Food Science Lab': [('Washroom', (4, 'towards Balcony then take LEFT')), ('314B Biology Lab', (2, 'STRAIGHT'))],
        '314B Biology Lab': [('314A Food Science Lab', (2, 'STRAIGHT')), ('Elevator', (3, 'STRAIGHT towards Junction then take RIGHT'))],
        'Elevator': [('314B Biology Lab', (3, 'After Exiting from lift take RIGHT then LEFT')), ('306 IPDC Lab', (1, 'After exiting from Lift take LEFT'))]
    }

    # Step 4: Ask user for their destination from the available locations
    target_location = get_target_location(floor_graph)

    # Step 5: Check if the target location exists in the graph
    if target_location not in floor_graph:
        print("Invalid destination.")
        return

    # Step 6: Use Dijkstra's algorithm to find the shortest path, directions, and performance metrics
    result = dijkstra(floor_graph, current_location)
    distances, previous_nodes, directions = result['distances'], result['previous_nodes'], result['directions']
    performance = result['performance']
    
    # Step 7: Reconstruct the path and display directions with distances in meters
    path_directions = reconstruct_path_with_directions(directions, current_location, target_location)
    
    if path_directions:
        print(f"Directions from {current_location} to {target_location}:")
        for step in path_directions:
            print(step)
        print("\nPerformance Metrics:")
        print(f"Time Taken: {performance['time']:.20f} seconds")
        print(f"Nodes Expanded: {performance['nodes_expanded']}")
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
