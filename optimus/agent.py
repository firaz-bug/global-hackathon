from servicenow import fetch_unassigned_incidents, get_assignment_group
from mongo import get_agent_details
import requests



from servicenow import assign_incident


def markAssignment(incident_number,platformOwner):


def send_to_agent(assignment_group, incident_number, priority, short_description, long_description, comments):
    """
    Send incident details to the assigned agent.
    """
    agent_details = get_agent_details(assignment_group)
    agent_url = agent_details.get("restURL")
    agent_mail = agent_details.get("mailId")
<<<<<<< Updated upstream
    platformOwner=agent_details.get("platformOwner")
    assign_incident(incident_number,platformOwner)
=======

    # Prepare the payload
    payload = {
        "incident_number": incident_number,
        "priority": priority,
        "short_description": short_description,
        "long_description": long_description,
        "comments": comments,
    }

    # Send the POST request
    response = requests.post("http://127.0.0.1:8000/api/incidents/", json=payload)

    # Check the response status
    if response.status_code == 200 or response.status_code == 201:
        print("Incident successfully sent to the API.")
    else:
        print(f"Failed to send incident. Status code: {response.status_code}, Response: {response.text}")
    
>>>>>>> Stashed changes
    # Log the details (replace with actual logic to send data)
    print(f"Agent URL: {agent_url}")
    print(f"Agent Email: {agent_mail}")
    print(f"Incident Number: {incident_number}")
    print(f"Priority: {priority}")
    print(f"Short Description: {short_description}")
    print(f"Long Description: {long_description}")
    print(f"Comments: {comments}")

def process_incidents():
    """
    Process unassigned incidents and send them to the appropriate agents.
    """
    incidents = fetch_unassigned_incidents()
    for incident in incidents:
        assignment_group_detail = incident.get("assignment_group", {})
        incident_number = incident.get("number", "")
        priority = incident.get("priority", "")
        short_description = incident.get("short_description", "")
        long_description = incident.get("description", "")
        comments = incident.get("comments", "")


        
        if isinstance(assignment_group_detail, dict):
            assignment_group_link = assignment_group_detail.get("link")
            assignment_group = get_assignment_group(assignment_group_link)
            send_to_agent(assignment_group, incident_number, priority, short_description, long_description, comments)