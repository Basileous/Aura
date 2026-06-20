import os
import glob

replacements = {
    '&#2547;': 'Rs.',
    '৳': 'Rs.'
}

# include all files in templates and static/js
search_path = r'c:\Users\Qadri Laptop\Downloads\Archive'
os.chdir(search_path)

files = glob.glob('templates/**/*.html', recursive=True) + glob.glob('static/**/*.js', recursive=True)

count = 0
for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
            
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
            count += 1
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Total files updated: {count}")
