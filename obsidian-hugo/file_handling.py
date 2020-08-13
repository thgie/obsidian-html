import os

def format_file(file_name, vault_root):
    with open(vault_root + "/" + file_name) as f:
        doc = f.read()

    new_doc = format_internal_links(
        format_internal_aliased_links(
            format_internal_header_links(doc)))

    new_doc = f"+++\ntitle = \"{file_name.replace('.md', '')}\"\n+++\n\n" + new_doc

    with open(os.path.dirname(vault_root) + "/hugo/content/" + file_name, "w") as f:
        f.write(new_doc)

def find_files(vault_root, extra_folders):
    md_files = [f for f in os.listdir(vault_root) if f.endswith(".md")]
    for folder in extra_folders:
        md_files += [folder + "/" + f for f in os.listdir(vault_root + "/" + folder) if f.endswith(".md")]

    return md_files