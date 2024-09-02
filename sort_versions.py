versions = ["1.0", "0.9", "0.9.9", "0.9.10"]

sorted_versions = sorted(versions, key=lambda v: [int(part) for part in v.split('.')])

print(sorted_versions)

# This approach works by converting each part of the version string into an integer and sorting based on these integer lists. 
# The split('.') breaks the version string into its components, and the list comprehension converts these components into integers.