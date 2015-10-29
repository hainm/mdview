# mdview

Trajectory viewer on Jupyter notebook

A fork from [mdtraj](https://github.com/mdtraj/mdtraj/tree/master/mdtraj/html) sub-package.

This is my experiment. Not guarantee to make it work, but the overall aim is to build a package that can be integrated with `mdtraj`,
`pytraj`, `mdanalysis`, `chemlab`, ...

## License

Currently mdview license follows [`mdtraj` license] (https://github.com/mdtraj/mdtraj/blob/master/LICENSE) (LGPLv2+)

## Proposal 

(copied and lightly change from [mdtraj's website](http://mdtraj.org/latest/viewer.html))

```python
from mdview import TrajectoryView, enable_notebook
enable_notebook()

# use mdtraj as backend
import mdtraj as md
traj = md.load(fname, topology_name)
TrajectoryView(traj, backend='mdtraj')

# use pytraj as backend
import pytraj as pt
traj = pt.load(fname, topology_name)
TrajectoryView(traj, backend='pytraj')
# 
```

## Demo from other packages:

- http://istar.cse.cuhk.edu.hk/iview/
- http://biasmv.github.io/pv/demo.html

## Why bother creating this?

- Developing a good GUI is very difficult. We should focus on a single package rather making different ones (mdtraj's view, chemview, pymol, ...). And it's fun to collaborate.

- try to have BSD license?
- integrate with [jupyter notebook] (https://jupyter.org/)
- why not using VMD? VMD is a beast and I really like it. But I love Python, it's hard to bring python to VMD...
- why not developing based on pymol? its license, not sure how to combine to jupyter notebook, many other things.
- make a light package. For example, if `pytraj` users want to use the trajectory view with jupyter notebook, they need to install `mdtraj` too, which instroduce additional level of complexity in installation.

## Current limitations of trajectove view in `mdtraj`:

- mouse sensitivity, molecule rotation are not that great compareted to VMD (actually I don't see any program (even chimera, pymol) has that kind of mouse sensitivy like the one in VMD).
- don't have reprsentation for nucleic acid.
- ...


## Why naming `mdview`?

- it's just temp name
- I myself prefer short typing

## Install

- from conda::

    $ conda install mdview -c ambermd

- from github

    $ git clone https://github.com/mdview/mdview
    $ cd mview
    $ python setup.py install

## Credits

(For more details, please the license in each file)

- Hai Nguyen, patch for [pytraj] (https://github.com/Amber-MD/pytraj)
- [mdtraj's developers] (https://github.com/mdtraj/mdtraj): original python implementation
- Jacob Kelley, [Context.js] (https://github.com/jakiestfu/Context.js)
- Eli Grey, [FileSaver.js] (https://github.com/eligrey/FileSaver.js)
- [iview developers] (https://github.com/HongjianLi/iview)
- [GLmol developers] (https://github.com/biochem-fan/GLmol)
- mrdoob, [three.js] (https://github.com/mrdoob/three.js)
- John Resig [jQuery] (http://jquery.org)
