import unicodedata, re, os

def has_selected_yes(user_input):
    """
    Returns True if the user has selected yes.
    """
    return user_input == "y" or user_input == "Y" or user_input == "yes" or user_input == "Yes" or user_input == "YES"

def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters, and converts spaces to hyphens.
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)

def make_dir_if_not_exists(current_working_dir):
    """
    Creates a directory for the content if it doesn't already exist.
    """ 
    # Create the directory if it doesn't exist
    if not os.path.exists(current_working_dir):
        print("Creating directory: " + current_working_dir)
        os.makedirs(current_working_dir)
        os.makedirs(current_working_dir + "/images")
        os.makedirs(current_working_dir + "/script")
        os.makedirs(current_working_dir + "/audio")
        os.makedirs(current_working_dir + "/video")

