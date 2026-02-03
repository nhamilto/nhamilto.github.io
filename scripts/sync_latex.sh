#!/bin/bash

echo "=== Syncing LaTeX CV to GitHub Pages ==="

# Check if LaTeX source exists
if [ ! -f "latex_source/portfolio.20251230.bib" ]; then
    echo "Error: portfolio.20251230.bib not found in latex_source/"
    exit 1
fi

# Copy and clean bibliography file
echo "1. Copying and cleaning bibliography file..."
python3 scripts/clean_bib.py

# Backup existing publications
echo "2. Backing up existing publications..."
if [ -d "_publications" ]; then
    mkdir -p _publications_backup
    cp -r _publications/* _publications_backup/
fi

# Convert BibTeX to markdown
echo "3. Converting BibTeX to markdown..."
cd markdown_generator
python pubsFromBib.py

if [ $? -ne 0 ]; then
    echo "Error: BibTeX conversion failed"
    exit 1
fi

cd ..

# Copy PDF CV if it exists
echo "4. Copying PDF CV..."
if [ -f "latex_source/Hamilton_CV.pdf" ]; then
    cp latex_source/Hamilton_CV.pdf files/Hamilton_CV.pdf
    echo "   ✓ PDF CV copied to files/"
else
    echo "   ⚠ Warning: Hamilton_CV.pdf not found in latex_source/"
fi

# Show statistics
echo ""
echo "=== Conversion Summary ==="
echo "Publications generated: $(ls -1 _publications/*.md 2>/dev/null | wc -l)"
echo ""
echo "Next steps:"
echo "  1. Review changes: git diff _publications/"
echo "  2. Test locally: bundle exec jekyll serve"
echo "  3. Commit changes: git add . && git commit -m 'Update CV and publications'"
