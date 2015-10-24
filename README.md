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
