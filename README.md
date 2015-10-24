# mdview
Trajectory viewer on Jupyter notebook

A fork from [mdtraj](https://github.com/mdtraj/mdtraj/tree/master/mdtraj/html) sub-package.

This is my experiment. Not guarantee to make it work, but the overall aim is to build a package that can be integrated with `mdtraj`,
`pytraj`, `mdanalysis`, `chemlab`, ...

Currently mdview license follows https://github.com/mdtraj/mdtraj/blob/master/LICENSE

Proposal (copied and lightly change from [mdtraj's website](http://mdtraj.org/latest/viewer.html))

```python
from mdview import TrajectoryView, enable_notebook
enable_notebook()
TrajectoryView(traj)
```

Why bother creating this?

- Developing a good GUI is very difficult. We should focus on a single package rather making different ones (mdtraj's view, chemview, pymol, ...). And it's fun to collaborate.

- try to have BSD license?
- ...


Current limitations of trajectove view in `mdtraj`:

- mouse sensitivity (?) is not that great compareted to VMD (actually I don't see any program (even chimera, pymol) has that kind of mouse sensitivy like the one in VMD).
- don't have reprsentation for nucleic acid.
