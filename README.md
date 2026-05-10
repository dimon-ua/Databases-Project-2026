# Databases-Project-2026

A conference management system built with Python, utilizing MySQL for relational data storage and Neo4j for graph-based relationships between attendees.

## Features

- **View Speakers & Sessions**: Search for speakers and view their associated sessions and room assignments.
- **View Attendees by Company**: Display attendees grouped by their company.
- **Add New Attendee**: Register new attendees with their details.
- **View Connected Attendees**: Explore attendee connections using graph database capabilities.
- **Add Attendee Connection**: Create relationships between attendees.
- **View Rooms**: List available conference rooms.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.8 or higher
- MySQL Server
- Neo4j Desktop or Server
- Required Python packages:
  - `mysql-connector-python`
  - `neo4j`

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dimon-ua/Databases-Project-2026.git
   cd Databases-Project-2026
   ```

2. **Install Python dependencies**:
   ```bash
   pip install mysql-connector-python neo4j
   ```

3. **Set up MySQL Database**:
   - Create a MySQL database named `conference_db` (or update the connection details in `mysql_connection.py`).
   - Import the necessary tables and data. (Ensure you have the schema for tables: attendee, company, session, room, etc.)

4. **Set up Neo4j Database**:
   - Start Neo4j server on `neo4j://127.0.0.1:7687` with user `neo4j` and password `rootroot` (or update `config_neo4j.py`).
   - Create nodes and relationships for attendees and their connections.

## Usage

Run the main application:

```bash
python main.py
```

Follow the on-screen menu to perform various operations:

1. View Speakers & Sessions
2. View Attendees by Company
3. Add New Attendee
4. View Connected Attendees
5. Add Attendee Connection
6. View Rooms
x. Exit

## Database Schema

### MySQL Tables
- `attendee`: Stores attendee information (ID, name, DOB, gender, company ID)
- `company`: Company details
- `session`: Session information with speaker and room
- `room`: Conference rooms

### Neo4j Graph
- Nodes: Attendees
- Relationships: Connections between attendees

## Configuration

- Update database credentials in `mysql_connection.py` for MySQL.
- Update Neo4j connection details in `config_neo4j.py`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.