from models import Note_item

def create_note_item(title, description, new_summary):
    Note_item.create(title, description, new_summary)
