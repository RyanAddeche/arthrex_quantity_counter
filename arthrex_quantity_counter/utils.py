


# Finds an unknown substring when given text in front and behind of the unknown substring
def find_string(text, start_marker, end_marker):
    start = text.find(start_marker) + len(start_marker)
    end = text.find(end_marker)

    if start_marker != -1 and end_marker != -1:
        unknown_substring = text[start:end]
        return unknown_substring
    else:
        print("Leading or trailing substring not found.")
