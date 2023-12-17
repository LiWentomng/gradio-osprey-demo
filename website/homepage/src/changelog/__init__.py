import os
import re

import markdown2

DIR = os.path.dirname(__file__)
INNER_TEMPLATE_FILE = os.path.join(DIR, "inner_template.html")
CHANGELOG_FILE = os.path.join(DIR, "..", "..", "..", "..", "CHANGELOG.md")

def render_md():
    with open(CHANGELOG_FILE, "r") as change_file:
        content = change_file.read()
    
    # replace code blocks correctly
    content = re.sub(
            r"```([a-z]+)\n",
            lambda x: f"<div class='codeblock'><pre><code class='lang-{x.group(1)}'>",
            content,
        )
    content = re.sub(r"```", "</code></pre></div>", content)
   
    # remove empty/unused sections
    content = re.sub(r"## [\w^:\n ]*No changes to highlight.", "", content)

    # get versions and their correct href
    versions = re.findall(r"# Version \d\.\d[^\n ]*", content)
    versions = [("Upcoming Release", "upcoming-release")] + [("v" + v.strip("# Version "), "version-" + v.strip("# Version ").replace('.','')) for v in versions]


    content_html = markdown2.markdown(
                content,
                extras=[
                    "target-blank-links",
                    "header-ids",
                    "tables",
                    "fenced-code-blocks",
                ],
            )

    with open(INNER_TEMPLATE_FILE, "w+") as temp_html:
        temp_html.write(content_html)

    return versions


def build(output_dir, jinja_env, latest_gradio_stable):
    versions = render_md()
    os.makedirs(output_dir, exist_ok=True)
    template = jinja_env.get_template("changelog/parent_template.html")
    output = template.render(versions=versions, latest_gradio_stable=latest_gradio_stable)
    output_folder = os.path.join(output_dir, "changelog")
    os.makedirs(output_folder)
    output_file = os.path.join(output_folder, "index.html")
    with open(output_file, "w") as index_html:
        index_html.write(output)
