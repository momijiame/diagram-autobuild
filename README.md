# diagram-autobuild

![diagram-autobuild-demo](https://raw.githubusercontent.com/wiki/momijiame/diagram-autobuild/images/diagram-autobuild.gif)

## What is this?

diagram-autobuild improves the efficiency of the making diagrams.
diagram-autobuild is supporting the following tools.

- graphviz (http://www.graphviz.org/)
- blockdiag (https://pypi.python.org/pypi/blockdiag)
- nwdiag (https://pypi.python.org/pypi/nwdiag)
- actdiag (https://pypi.python.org/pypi/actdiag)
- seqdiag (https://pypi.python.org/pypi/seqdiag)
- ERAlchemy (https://pypi.python.org/pypi/ERAlchemy)

### Background

If you make a diagram, you usually do the following cycle.

1. Edit the source (e.g. \*.dot)
2. Build the diagram (e.g. execute 'dot' command)
3. Open the diagram
4. Make sure whether the diagram is your intended (If it isn't so, retry from the first)

This procedure is inefficient and bother you.

### Solution

Automation: the above procedure between 2 and 3

diagram-autobuild observes the source file.
If the source file is modified, rebuild the diagram, and the browser which indicates the diagram is reloaded.

## How to install

diagram-autobuild is installed by using pip of Python's package manager.

```
$ pip install diagram-autobuild
```

or

```
$ pip install git+https://github.com/momijiame/diagram-autobuild.git
```

## How to use

You will be able to use 'diagram-autobuild' command.
```
$ diagram-autobuild --help
Usage: diagram-autobuild [OPTIONS] TOOL SOURCE

Options:
  --tool-opts TEXT                Options that are passed to the tool
  --open-browser / --no-open-browser
                                  Open your default browser when the command
                                  is executed
  --help                          Show this message and exit.
```

Execute 'diagram-autobuild' command with the tool name and the path of source file.
(The tool must to be installed already)

Example (graphviz):
```
$ ls
sample.dot
$ diagram-autobuild graphviz sample.dot
```

Example (blockdiag):
```
$ ls
sample.diag
$ diagram-autobuild blockdiag sample.diag
```

Example (ERAlchemy):
```
$ ls
sample.er
$ diagram-autobuild eralchemy sample.er
```

If it succeed, open your default browser and you can see the diagram.
