#!/usr/bin/env python3
"""Clean BibTeX file by removing comments, fixing trailing commas, and removing duplicates."""

import re

# Read the original source file
with open("latex_source/portfolio.20251230.bib", "r", encoding="utf-8") as f:
    content = f.read()

# Step 1: Remove commented lines and commented entries
lines = content.split("\n")
cleaned_lines = []
inside_entry = False
inside_commented_entry = False

for line in lines:
    stripped = line.strip()

    # Check if this is a commented entry start
    if stripped.startswith("% @"):
        inside_commented_entry = True
        continue

    # Check if we're exiting a commented entry
    if inside_commented_entry:
        if stripped.startswith("% }") or stripped == "}":
            inside_commented_entry = False
        continue

    # Track if we're inside a real entry
    if stripped.startswith("@"):
        inside_entry = True
    elif inside_entry and stripped == "}":
        inside_entry = False

    # Skip comment lines inside real entries
    if inside_entry and stripped.startswith("%"):
        continue

    # Skip standalone comment lines
    if stripped.startswith("%"):
        continue

    cleaned_lines.append(line)

content = "\n".join(cleaned_lines)

# Step 2: Fix trailing commas before closing braces
content = re.sub(r",(\s*)\}", r"\1}", content)

# Step 3: Remove duplicate entries (keep first occurrence)
entries = []
current_entry = []
seen_keys = set()
duplicates_removed = 0

lines = content.split("\n")
for line in lines:
    stripped = line.strip()

    # Check if this is the start of a new entry
    if stripped.startswith("@"):
        # If we have a previous entry, save it
        if current_entry:
            # Extract the key from the first line of the entry
            first_line = current_entry[0]
            match = re.match(r"@\w+\{([^,]+),", first_line)
            if match:
                key = match.group(1)
                if key not in seen_keys:
                    entries.append("\n".join(current_entry))
                    seen_keys.add(key)
                else:
                    duplicates_removed += 1

        # Start new entry
        current_entry = [line]
    else:
        if current_entry:  # Only add if we're in an entry
            current_entry.append(line)

# Don't forget the last entry
if current_entry:
    first_line = current_entry[0]
    match = re.match(r"@\w+\{([^,]+),", first_line)
    if match:
        key = match.group(1)
        if key not in seen_keys:
            entries.append("\n".join(current_entry))
            seen_keys.add(key)
        else:
            duplicates_removed += 1

# Write deduplicated content
with open("markdown_generator/pubs.bib", "w", encoding="utf-8") as f:
    f.write("\n\n".join(entries))

print(f"   ✓ Cleaned BibTeX file")
print(f"   - Removed comment lines and commented entries")
print(f"   - Fixed trailing commas")
print(f"   - Removed {duplicates_removed} duplicate entries")
print(f"   - {len(seen_keys)} unique entries remaining")
