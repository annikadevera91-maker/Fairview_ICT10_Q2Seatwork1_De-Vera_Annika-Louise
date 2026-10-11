from pyscript import document

# Python list containing g10 ict club members
club_members = [
"Francis Fernandez", "Gavin Ruiz", "Edrian Correa", "Philip Ponce", "Julian Anaque", "Andrik David", "Annika De Vera", "Eliana Daet"]

def check_membership(event):
    # First and last name entered by the user and combine them into one full name
    fname = document.querySelector("#first-name").value.strip()
    lname = document.querySelector("#last-name").value.strip()
    full_name = f"{fname} {lname}"

    # Check whether the full name is in the club members list. 
    is_member = full_name in club_members

    # boolean indexing (True -> 1, False -> 0)
    messages = [
        f"Sorry {full_name}, your name is not on the list.",
        f"Welcome {full_name}, you are a member of the G10 ICT Club!"]
    
    bg_colors = ["#f8d7da", "#d1e7dd"]
    text_colors = ["#842029", "#0f5132"]

    index = int(is_member)
    message = messages[index]

    # Update result area UI
    result_div = document.querySelector("#result")
    result_div.innerText = message
    result_div.style.backgroundColor = bg_colors[index]
    result_div.style.color = text_colors[index]