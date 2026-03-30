#!/usr/bin/python3
"""Templating program for generating invitation files."""


def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and a list of attendees.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): A list of dictionaries containing attendee data.

    Returns:
        None
    """
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if attendees == []:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(index)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
