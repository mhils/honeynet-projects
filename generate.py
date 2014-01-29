from markdown import Markdown
from jinja2 import Template
from cStringIO import StringIO

def get_projects(listfile):
    with open(listfile,"r") as f:
        project_files = f.read().splitlines()
    global md
    projects = []
    for pf in project_files:
        contents = StringIO()
        md = Markdown(extensions=["extra", "meta"])
        md.convertFile(pf, contents)
        md.Meta["content"] = contents.getvalue()
        projects.append(md.Meta)
    return projects


with open("template.html","r") as f:
    template = Template(f.read())

projects = get_projects("project_list")

with open("out.html","w") as f:
    out = template.render(projects=projects)
    f.write(out)
    print out

