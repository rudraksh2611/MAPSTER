# Mapster 
An Offline Indoor Navigation App for Large Buildings

Hello! I'm Rudraksh Singh Bhadauria, a B.Tech student at Sharda University, and I'm thrilled to introduce my latest project, **Mapster**. This innovative app aims to simplify indoor navigation within large, complex buildings by allowing users to navigate effortlessly without relying on an internet or GPS connection. By scanning strategically placed QR codes, Mapster provides users with precise, step-by-step directions to their desired destination.

### Introdution Audio

[Audio](
https://github.com/user-attachments/assets/55cab040-d78c-4b23-a2fb-c5e45dd20487)

NOTE - Since GitHub’s README files don’t support direct MP3 uploads, I’ve uploaded an MP4 version instead. I hope you enjoy the introduction provided in the video. 

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Getting Started](#getting-started)
* [Installation](#installation)
* [Usage](#usage)
* [Code Explanation](#code-explanation)
* [Performance](#performance)
* [Future Enhancements](#future-enhancements)
* [License](#license)

## Project Overview

Mapster is designed to assist users navigating large buildings, such as campuses, hospitals, museums, and office complexes, where conventional GPS and internet connectivity might not be accessible. Using Dijkstra's algorithm, Mapster calculates the shortest route to any destination within a building and provides optimized directions.

**How it Works**: By scanning a QR code at their current location, users can get their position and navigate to various destinations simply by entering the destination. Mapster will handle the rest, ensuring an intuitive and seamless user experience.

### Demo Images

Here are a few images to showcase the app’s functionality and user interface:

#### Main Interface
![Main Interface](https://github.com/rudraksh2611/MAPSTER/blob/4788dfddbea81c8bbcdb2848123ecf7e3f22a680/Main%20Interface)

#### Search Your Destiny
![QR Code Scanning](https://github.com/rudraksh2611/MAPSTER/blob/4788dfddbea81c8bbcdb2848123ecf7e3f22a680/Search%20Your%20Destiny)

#### Navigation Directions
![Navigation Directions](https://github.com/rudraksh2611/MAPSTER/blob/4788dfddbea81c8bbcdb2848123ecf7e3f22a680/Navigation%20Directions)

## Features

* **Offline Navigation**: Operates without internet or GPS, providing reliable access in areas with limited connectivity.
* **QR Code Scanning**: Use the device’s camera to scan QR codes that identify the current location.
* **Efficient Route Calculation**: Utilizes Dijkstra’s algorithm to find the shortest route to a specified destination.
* **Easy-to-Follow Directions**: Step-by-step directions with distances and clear instructions.
* **Customizable for Any Building Layout**: Easily adaptable to different indoor environments with pre-defined maps and QR code placements.

## Getting Started

### Prerequisites

To run Mapster, ensure you have the following:

* Python (3.x recommended)
* OpenCV library for QR code scanning
* pyzbar library for decoding QR codes

```Bash
pip install opencv-python pyzbar
```
## Additional Libraries
You may also need:

1. time for performance measurement
2. heapq for efficient priority queue management (used in Dijkstra’s algorithm)

## Installation
Clone this repository to your local machine:

```Bash
git clone [https://github.com/yourusername/Mapster.git](https://github.com/yourusername/Mapster.git)
cd Mapster
```
Install dependencies:

```Bash
pip install -r requirements.txt
```
## Usage
To run the app, simply execute the main.py script:

```Bash
python main.py
```
## Steps to Use Mapster

1. Open the App: The app will open your device's camera to scan the QR code of your current location.
2. Scan QR Code: Hold the QR code in front of the camera until the location is detected.
3. Set Destination: From the list of available destinations, select your target location.
4. Get Directions: Mapster calculates the shortest route and provides step-by-step directions.

### Example:
Start at the "IPDC Lab" and navigate to "Analog Circuit Lab" using the Let’s Go button.

## Code Explanation
### Key Components

- QR Code Scanning: Uses OpenCV and Pyzbar libraries to read QR codes and decode the user's current location.
- Mapping: The map_location() function maps QR code data to a pre-defined node in the building graph.
- Dijkstra’s Algorithm: This is the core of Mapster’s route calculation, implemented with performance tracking.
    - Calculates the shortest path based on distances (weights) between nodes.
    - Tracks expanded nodes and elapsed time for efficiency evaluation.
- Path Reconstruction: Provides clear, directional instructions to guide the user through the building.

## Functions
- scan_qr_code(): Scans the QR code and retrieves the current location.
get_target_location(): Prompts the user to select a destination.
- dijkstra(): Implements Dijkstra's algorithm with performance monitoring.
- reconstruct_path_with_directions(): Reconstructs the shortest path with clear, step-by-step instructions.

## Graph Example
A sample building floor plan structured in Mapster:

```python
floor_graph = {
    '306 IPDC Lab': [('307A Classroom', (1.5, 'LEFT then RIGHT')), ('Elevator', (1, 'RIGHT'))],
    '307A Classroom': [('306 IPDC Lab', (1.5, 'LEFT then LEFT')), ('307B Control Lab', (2, 'STRAIGHT'))],
    # More nodes and paths...
}
```
## Performance
Mapster optimizes pathfinding with Dijkstra’s algorithm, tracking both time taken and nodes expanded:

- Time Taken: Typically under a second for moderately sized graphs.
- Nodes Expanded: Provides an efficient route with minimal node expansions.

### Sample Output
```text
Directions from IPDC Lab to Analog Circuit Lab:
Step 1: Go LEFT to 307A Classroom (Distance: 1.5 meters)
Step 2: Go STRAIGHT to 307B Control Lab (Distance: 2 meters)
...
Total distance to Analog Circuit Lab: 10 meters

Performance Metrics:
Time Taken: 0.0002350807 seconds
Nodes Expanded: 5
```
## Future Enhancements
- Voice Navigation: Add voice-guided navigation for accessibility.
- Dynamic Floor Mapping: Allow admins to dynamically update and add new nodes or paths.
- Multi-Floor Support: Extend navigation to multi-floor buildings with additional layers.
- Augmented Reality (AR) Directions: Integrate AR for a more immersive navigation experience.

## License
This project is licensed under the MIT License - see the LICENSE file for details.



