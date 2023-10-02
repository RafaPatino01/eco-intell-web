import re

# Define a function to update font sizes by multiplying by 1.2
def update_font_sizes(match):
    size = match.group(1)
    unit = match.group(2)
    updated_size = str(float(size) * 1.2)
    return f'font-size: {updated_size}{unit};'

# Read the CSS file
with open('old_webflow.css', 'r') as css_file:
    css_content = css_file.read()

# Define a regular expression pattern to match font-size rules with different units
pattern = r'font-size:\s*([\d.]+)(\D+);'

# Use re.sub() to find and replace font-size rules
updated_css = re.sub(pattern, update_font_sizes, css_content)

# Write the updated CSS back to the file
with open('webflow.css', 'w') as updated_file:
    updated_file.write(updated_css)

print("CSS font sizes updated and saved.")
