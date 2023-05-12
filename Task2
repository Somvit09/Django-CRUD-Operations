API Documentation for Nudge Creation Page

Description
The Nudge Creation Page API allows users to create nudges for events. A nudge is a promotional message that can be attached to an event or article. Users can provide details such as title, image, schedule, description, icon, and one-line invitation for the nudge. The API supports CRUD (Create, Read, Update, Delete) operations for managing nudges.

Base URL
The base URL for the Nudge Creation Page API is: https://api.example.com

API Endpoints
The following API endpoints are available for the Nudge Creation Page:

1. Create a Nudge

  Endpoint: /api/nudge/create
  Method: POST
  Description: Create a new nudge for an event.
  Payload:
          {
          "event_id": "string",
          "title": "string (max 60 characters)",
          "image": "file",
          "schedule": "string (formatted as dd/mm/yy)",
          "start_time": "string (formatted as hh:mm)",
          "end_time": "string (formatted as hh:mm)",
          "description": "string",
          "icon": "file",
          "invitation": "string"
        }
  Response: Returns the created nudge object.
2. Retrieve a Nudge

  Endpoint: /api/nudge/{nudge_id}
  Method: GET
  Description: Retrieve details of a specific nudge.
  Response: Returns the nudge object.

3. Update a Nudge

  Endpoint: /api/nudge/{nudge_id}
  Method: PUT
  Description: Update an existing nudge.
  Payload:
          {
          "title": "string (max 60 characters)",
          "image": "file",
          "schedule": "string (formatted as dd/mm/yy)",
          "start_time": "string (formatted as hh:mm)",
          "end_time": "string (formatted as hh:mm)",
          "description": "string",
          "icon": "file",
          "invitation": "string"
          }
  Response: Returns the updated nudge object.
  
4. Delete a Nudge

    Endpoint: /api/nudge/{nudge_id}
    Method: DELETE
    Description: Delete a nudge.
    Response: Returns a success message indicating the deletion.
    
    
CRUD Functionality
The API provides the following CRUD functionality for managing nudges:

1. Create:

  Endpoint: /api/nudge/create
  Method: POST
  Description: Create a new nudge by providing the necessary details in the payload.
  
  
2. Read:

  Endpoint: /api/nudge/{nudge_id}
  Method: GET
  Description: Retrieve details of a specific nudge by providing the nudge ID.
  
3. Update:

  Endpoint: /api/nudge/{nudge_id}
  Method: PUT
  Description: Update an existing nudge by providing the nudge ID and the updated details in the payload.
  
4. Delete:

  Endpoint: /api/nudge/{nudge_id}
  Method: DELETE
  Description: Delete a nudge by providing the nudge ID.
Please note that the {nudge_id} in the endpoints should be replaced with the actual ID of the nudge you want to interact with.
Ensure that the necessary authentication and authorization mechanisms are implemented to secure the API endpoints and restrict access to authorized users only.



























