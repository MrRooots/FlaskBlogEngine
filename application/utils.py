# Function that will create a proper slug from the post title
def slugify(title: str, instance: str) -> str:
  cleaned_slug = 'tag-' if instance == 'Tag' else ''

  for char in title:
    if char.isalpha():
      cleaned_slug += char.lower()
    elif char.isspace():
      cleaned_slug += '-'

  while '--' in cleaned_slug:
    cleaned_slug = cleaned_slug.replace('--', '-')

  return cleaned_slug if cleaned_slug[-1] != '-' else cleaned_slug[:-1]